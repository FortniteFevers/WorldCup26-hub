#!/usr/bin/env python3
"""
Preprocess FC26 CSV into two JSON files:
  1. football-data/fc26-players.json   — WC squad players enriched with FC26 data
  2. football-data/fc26-ratings.json   — name→overall lookup for 104-0 draft
"""
import csv, json, unicodedata, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH    = os.path.join(BASE, 'football-data', 'FC26_20250921.csv')
OUT_PLAYERS = os.path.join(BASE, 'football-data', 'fc26-players.json')
OUT_RATINGS = os.path.join(BASE, 'football-data', 'fc26-ratings.json')
OUR_PLAYERS = os.path.join(BASE, 'football-data', 'all-players.json')

NATION_MAP = {
    'South Korea':        'Korea Republic',
    'Turkey':             'Türkiye',
    'Bosnia-Herzegovina': 'Bosnia and Herzegovina',
    'Congo DR':           'DR Congo',
    'Ivory Coast':        "Côte d'Ivoire",
    'Cape Verde Islands': 'Cape Verde',
}

def normalize(s):
    s = s.lower()
    # Language-specific substitutions BEFORE stripping accents
    # (å→aa is Norwegian; ø→o; æ→ae; ß→ss German; etc.)
    s = s.replace('å', 'aa').replace('ø', 'o').replace('æ', 'ae')
    s = s.replace('ß', 'ss').replace('đ', 'd').replace('ð', 'd').replace('þ', 'th')
    # Strip Arabic / non-Latin script characters
    s = ''.join(c for c in s if c.isascii() or not unicodedata.category(c).startswith('L') or c.isalpha())
    # Strip remaining combining marks
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def to_int(v):
    try: return int(v)
    except: return None

print("Reading data...")
with open(CSV_PATH, encoding='utf-8') as f:
    fc26 = list(csv.DictReader(f))
with open(OUR_PLAYERS, encoding='utf-8') as f:
    our_players = json.load(f)
print(f"  FC26: {len(fc26)} players  |  Our squads: {len(our_players)} players")

# ── Name matching ────────────────────────────────────────────────────────────
def find_fc26_player(player):
    name = normalize(player['name'])
    nation = NATION_MAP.get(player.get('teamName',''), player.get('teamName',''))
    parts = name.split()

    # 1. Exact normalized long_name
    for r in fc26:
        if normalize(r['long_name']) == name:
            return r

    # 2. All name parts in long_name, same nation
    for r in fc26:
        if r['nationality_name'] == nation:
            ln = normalize(r['long_name'])
            if all(p in ln for p in parts):
                return r

    # 3. First + last word in long_name, same nation
    if len(parts) >= 2:
        first, last = parts[0], parts[-1]
        for r in fc26:
            if r['nationality_name'] == nation:
                ln = normalize(r['long_name'])
                lparts = ln.split()
                if first in lparts and last in lparts:
                    return r

    # 4. Last name only + nation (mononyms like Neymar, Pedri)
    if len(parts) == 1:
        for r in fc26:
            if r['nationality_name'] == nation:
                if normalize(r['short_name']) == name or normalize(r['long_name']) == name:
                    return r

    return None

# ── Build enriched player list ───────────────────────────────────────────────
INT_STATS = [
    'overall','potential','age','height_cm','weight_kg',
    'weak_foot','skill_moves','international_reputation','nation_jersey_number',
    'pace','shooting','passing','dribbling','defending','physic',
    'attacking_crossing','attacking_finishing','attacking_heading_accuracy',
    'attacking_short_passing','attacking_volleys',
    'skill_dribbling','skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control',
    'movement_acceleration','movement_sprint_speed','movement_agility',
    'movement_reactions','movement_balance',
    'power_shot_power','power_jumping','power_stamina','power_strength','power_long_shots',
    'mentality_aggression','mentality_interceptions','mentality_positioning',
    'mentality_vision','mentality_penalties','mentality_composure',
    'defending_marking_awareness','defending_standing_tackle','defending_sliding_tackle',
    'goalkeeping_diving','goalkeeping_handling','goalkeeping_kicking',
    'goalkeeping_positioning','goalkeeping_reflexes',
]

matched = 0
players_out = []
ratings_out = {}

for p in our_players:
    fc = find_fc26_player(p)

    obj = {
        # From all-players.json
        'id':         p['id'],
        'name':       p['name'],
        'team':       p['teamName'],
        'teamTla':    p.get('teamTla',''),
        'position':   p['position'],  # Goalkeeper/Defence/Midfield/Offence
        'dob':        p.get('dateOfBirth',''),
    }

    if fc:
        matched += 1
        # Core identity
        obj['shortName']  = fc['short_name']
        obj['faceUrl']    = fc['player_face_url']
        obj['positions']  = fc['player_positions']  # e.g. "CAM, CM"
        obj['foot']       = fc['preferred_foot']
        obj['workRate']   = fc['work_rate']
        obj['valueEur']   = to_int(fc['value_eur'])
        # All numeric stats
        for s in INT_STATS:
            obj[s] = to_int(fc.get(s,''))
        # Save to ratings lookup
        ratings_out[normalize(p['name'])] = to_int(fc['overall'])
    else:
        obj['faceUrl'] = None

    players_out.append(obj)

# Sort: by team, then by overall desc (unmatched go to bottom within team)
players_out.sort(key=lambda x: (x['team'], -(x.get('overall') or 0)))

print(f"\n  Matched: {matched}/{len(our_players)} ({matched/len(our_players)*100:.1f}%)")
print(f"  Unmatched: {len(our_players)-matched}")

with open(OUT_PLAYERS, 'w', encoding='utf-8') as f:
    json.dump(players_out, f, ensure_ascii=False, separators=(',',':'))

size_kb = os.path.getsize(OUT_PLAYERS)/1024
print(f"  Written {OUT_PLAYERS} ({size_kb:.0f} KB)")

with open(OUT_RATINGS, 'w', encoding='utf-8') as f:
    json.dump(ratings_out, f, ensure_ascii=False, separators=(',',':'))

size_kb2 = os.path.getsize(OUT_RATINGS)/1024
print(f"  Written {OUT_RATINGS} ({size_kb2:.1f} KB)")
print("\nDone!")

# ── Build fc26-team-stats.json ───────────────────────────────────────────────
# Per-team: avg overall, top 3 players (for index hero + groups + games + bracket)
OUT_TEAM_STATS = os.path.join(BASE, 'football-data', 'fc26-team-stats.json')
OUT_TOP_PLAYERS = os.path.join(BASE, 'football-data', 'fc26-top-players.json')

from collections import defaultdict

team_players = defaultdict(list)
for p in players_out:
    if p.get('overall') and p.get('faceUrl'):
        team_players[p['team']].append(p)

team_stats = {}
for team, plist in team_players.items():
    sorted_p = sorted(plist, key=lambda x: -(x['overall'] or 0))
    avg = round(sum(p['overall'] for p in plist) / len(plist))
    team_stats[team] = {
        'avg': avg,
        'top': [{'name': p.get('shortName') or p['name'],
                 'fullName': p['name'],
                 'overall': p['overall'],
                 'faceUrl': p['faceUrl'],
                 'position': p.get('positions', '').split(',')[0].strip() or p['position']}
                for p in sorted_p[:3]]
    }

with open(OUT_TEAM_STATS, 'w', encoding='utf-8') as f:
    json.dump(team_stats, f, ensure_ascii=False, separators=(',',':'))
print(f"  Written {OUT_TEAM_STATS} ({os.path.getsize(OUT_TEAM_STATS)/1024:.1f} KB)")

# Top 12 players across all nations for landing page
all_with_face = [p for p in players_out if p.get('overall') and p.get('faceUrl')]
all_with_face.sort(key=lambda x: -(x['overall'] or 0))
top_players = [{'name': p.get('shortName') or p['name'],
                'fullName': p['name'],
                'team': p['team'],
                'overall': p['overall'],
                'faceUrl': p['faceUrl'],
                'pace': p.get('pace'), 'shooting': p.get('shooting'),
                'passing': p.get('passing'), 'dribbling': p.get('dribbling'),
                'defending': p.get('defending'), 'physic': p.get('physic'),
                'position': p.get('positions','').split(',')[0].strip() or p['position']}
               for p in all_with_face[:12]]

with open(OUT_TOP_PLAYERS, 'w', encoding='utf-8') as f:
    json.dump(top_players, f, ensure_ascii=False, separators=(',',':'))
print(f"  Written {OUT_TOP_PLAYERS} ({os.path.getsize(OUT_TOP_PLAYERS)/1024:.1f} KB)")
