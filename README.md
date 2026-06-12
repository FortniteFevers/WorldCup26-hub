# World Cup Field Guide

An interactive field guide for following the 2026 FIFA World Cup.

World Cup Field Guide brings the tournament schedule, groups, stadiums, teams, calendar tools, bracket simulations, and beginner-friendly explainers into one public site for casual fans and serious followers.

**Live site:** [worldcupfieldguide.com](https://worldcupfieldguide.com)

## Features

- Full 104-match schedule for the 2026 FIFA World Cup
- Search and filters by team, stadium, date, and tournament stage
- Calendar export with `.ics` download and Google Calendar links
- Visual schedule view for June and July 2026
- Groups view with all 12 groups and advancement context
- Interactive stadium map for all 16 host venues
- Team hub with ratings and roster data
- My Team squad builder and match simulator
- Bracket simulator from groups through the final
- Beginner-friendly World Cup guide
- Dark and light theme support
- Responsive layouts for desktop and mobile

## Tech Stack

- HTML
- CSS
- Vanilla JavaScript
- Next.js wrapper for Vercel deployment
- Clerk for optional authentication
- Vercel Analytics
- Leaflet for maps
- Lenis for smooth scrolling
- Local JSON football data exports

## Project Structure

```text
world-cup-2026/
├── app/                    # Next.js wrapper
├── public/                 # Static files served in production
├── football-data/          # Local football data exports
├── scripts/                # Data export scripts
├── index.html              # Landing page
├── games.html              # Schedule, filters, calendar export, venues
├── groups.html             # Group stage overview
├── locations.html          # Stadium map
├── calendar.html           # Standalone calendar export page
├── teams.html              # Teams hub
├── myteam.html             # Squad builder
├── bracket.html            # Bracket simulator
├── guide.html              # World Cup guide
├── data.js                 # Core schedule, groups, stadiums, flags
├── styles.css              # Global styles
├── theme.js                # Theme and nav helpers
├── auth.js                 # Clerk integration
└── package.json
```

## Credits

Created by [Zach Andelman](https://fevers.dev/links).

This is an independent fan project and is not affiliated with FIFA, EA SPORTS, EA SPORTS FC, or any national federation.
