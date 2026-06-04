# 🌍⚽ World Cup 2026

Your interactive companion for the 2026 FIFA World Cup — track all 104 matches across 16 stadiums, explore live team rosters, and sync games to your calendar.

**Live Demo:** [world-cup-2026.github.io](https://your-username.github.io/world-cup-2026)

---

## ✨ Features

- **📅 Full Schedule** — All 104 group, knockout, and final matches with kickoff times (Eastern Time)
- **🗺️ Stadium Map** — Interactive Leaflet.js map with all 16 venues color-coded by country (USA, Mexico, Canada)
- **👥 Live Team Rosters** — Integrate with [football-data.org](https://www.football-data.org) API to fetch squad data for all 48 teams
  - Player names, positions (GK/DEF/MID/FWD), ages, nationality
  - Position breakdown badges (🧤🛡️⚙️⚡) on team cards
  - Data cached in localStorage for instant loading after first sync
- **📆 Calendar Export** — Select matches and download as `.ics` file or add individually to Google Calendar
- **🔍 Search & Filter** — Find games by team, date, stadium, or tournament stage
- **🌙 Dark/Light Mode** — Toggle theme with persistent storage
- **📱 Mobile-Responsive** — Optimized for all screen sizes
- **⏳ Live Countdown** — Hours/minutes/seconds until first match

---

## 🛠️ Tech Stack

- **Frontend:** Vanilla JavaScript (ES6+), HTML5, CSS3
- **Maps:** [Leaflet.js](https://leafletjs.com/) + CartoDB tiles
- **API:** [football-data.org](https://www.football-data.org) (free tier)
- **Backend Proxy:** Python CORS proxy for API requests
- **Storage:** localStorage for squad caching
- **Deployment:** GitHub Pages (static site)

---

## 📖 Usage

### 1. View the Schedule
- **Home** → See opening matches and tournament stats
- **Games** → Browse all 104 matches with search, filter by date/stadium/stage
- **Calendar** → Visual grid view of the full schedule

### 2. Explore Stadiums
- **Locations** → Interactive map of all 16 venues
- Click a marker to see games at that stadium
- Click a card below the map to zoom to that location

### 3. View Team Rosters (Requires API Key)
- **Teams** → All 48 teams in a grid
- Get a free API key at [football-data.org](https://www.football-data.org/register)
- Paste your key on the Teams page → Auto-fetches all rosters (~8 minutes, then cached)
- Click any team to see full player roster with stats

### 4. Export to Calendar
- **Calendar** → Visual month grid of all matches
- Select individual games or "Select All"
- Download as `.ics` file (works with Apple Calendar, Google Calendar, Outlook)
- Or add each game individually to Google Calendar

---

## 🚀 Local Development

### Prerequisites
- Python 3.7+ (for CORS proxy)
- A modern web browser

### Installation

```bash
git clone https://github.com/yourusername/world-cup-2026.git
cd world-cup-2026
```

### Running Locally

```bash
# Terminal 1: Start the web server (port 8002)
cd world-cup-2026
python3 -m http.server 8002 --directory .

# Terminal 2: Start the API proxy (port 8003)
python3 proxy.py
```

Then open **http://localhost:8002** in your browser.

### API Integration (Optional)

To fetch live team rosters:

1. Register for a free API key at [football-data.org](https://www.football-data.org/register)
2. Navigate to the **Teams** page
3. Paste your API key and click "Connect"
4. All 48 team rosters will auto-fetch and cache

**Note:** The CORS proxy (`proxy.py`) is required because the API doesn't allow direct browser requests from localhost. On GitHub Pages, you can replace this with a serverless function or use the proxy URL as-is.

---

## 📁 Project Structure

```
world-cup-2026/
├── index.html           # Home page with countdown & stats
├── games.html           # Full match schedule with filters
├── locations.html       # Interactive stadium map
├── calendar.html        # Visual calendar view & export
├── teams.html           # Team rosters & squad data
├── data.js              # All 104 matches & stadium data
├── styles.css           # Responsive dark/light mode styles
├── theme.js             # Theme toggle & mobile nav
├── proxy.py             # Python CORS proxy (local only)
└── README.md            # This file
```

---

## 🌐 Deployment to GitHub Pages

### 1. Create a GitHub Repository
```bash
git init
git add .
git commit -m "Initial commit: World Cup 2026 fan site"
git remote add origin https://github.com/yourusername/world-cup-2026.git
git branch -M main
git push -u origin main
```

### 2. Enable GitHub Pages
1. Go to **Settings** → **Pages**
2. Set **Source** to `main` branch, `/root` directory
3. GitHub will deploy to `https://yourusername.github.io/world-cup-2026`

### 3. Note on API Proxy
The local `proxy.py` won't run on GitHub Pages (static hosting only). For the Teams API feature to work on the live site, you have two options:

**Option A: Use a Public CORS Proxy**
```javascript
// In teams.html, change:
const API_BASE = 'https://cors-anywhere.herokuapp.com/https://api.football-data.org/v4';
```

**Option B: Deploy Proxy to Heroku/Railway**
```bash
heroku create your-app-name
git push heroku main
```
Then update `API_BASE` to point to your deployed proxy.

---

## 📝 Data

All 104 matches are hardcoded in `data.js` with:
- **Group Stage** (72 matches): June 11–27, 2026
- **Knockout Rounds** (32 matches): June 28–July 19, 2026
- Teams, times, stadiums, and group assignments

Stadium coordinates and capacities are included for the interactive map.

---

## 🔌 API Credits

- **Match Schedule & Stadium Data:** Manual compilation from official FIFA sources
- **Team Rosters & Player Data:** [football-data.org](https://www.football-data.org)
  - Free tier: 10 requests/minute
  - Requires free API key (no credit card)

---

## 🎨 Design Features

- **Dark Mode (Default):** Deep navy background with gold accents
- **Light Mode:** Clean white with amber gold, optimized for readability
- **Glassmorphism:** Frosted glass nav bar with blur effects
- **Responsive Grid:** Auto-adjusts from mobile (1 col) to desktop (3+ cols)
- **Accessible Colors:** High contrast, colorblind-friendly position badges

---

## 🤝 Contributing

Found a bug or want to add a feature? Pull requests welcome!

**Ideas for contributions:**
- Add more tournament stats (win probabilities, historical comparisons)
- Player highlight videos or bio links
- Betting odds integration
- Multi-language support
- Progressive Web App (offline support)

---

## 📄 License

MIT License — See [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Created by

[Zach Andelman](https://linktr.ee/zachspam06)

*Not affiliated with FIFA or any official organization.*

---

## 📚 Resources

- [Football Data API Docs](https://www.football-data.org/documentation/quickstart)
- [Leaflet.js Map Library](https://leafletjs.com/examples.html)
- [2026 World Cup Official Info](https://www.fifa.com/)

---

**Enjoy the tournament! ⚽🏆**
