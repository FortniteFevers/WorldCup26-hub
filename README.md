# World Cup Field Guide

An interactive public field guide for following the 2026 FIFA World Cup. It brings the schedule, groups, stadiums, teams, calendar tools, roster data, and bracket simulations into one place for both casual fans and people who already follow the sport closely.

**Live Site:** [worldcupfieldguide.com](https://worldcupfieldguide.com)

## Features

- **Full Match Schedule** - Browse all 104 matches from the group stage through the final, with kickoff times shown in Eastern Time.
- **Search & Filters** - Find matches by team, stadium, date, or tournament stage.
- **Groups View** - See all 12 groups, standings structure, matchday schedules, and advancement rules.
- **Stadium Map** - Explore all 16 host venues on an interactive Leaflet map with venue cards and match counts.
- **Calendar Export** - Select games and download an `.ics` file or add individual matches to Google Calendar.
- **Teams Hub** - Browse all 48 qualified teams and optionally connect a football-data.org API key for live squad data.
- **My Team** - Pick a country, build a starting XI on a tactical pitch, choose formations, and simulate a match.
- **Bracket Simulator** - Simulate the full tournament from groups through the final, including best third-place advancement.
- **World Cup Guide** - Beginner-friendly explanations for how the tournament format works.
- **Optional Accounts** - Clerk sign-in/sign-up is available for future saved data and paid features, but the site remains publicly browsable without an account.
- **Dark/Light Mode** - Persistent theme toggle across pages.
- **Mobile Responsive** - Compact navigation and responsive layouts for smaller screens.
- **Vercel Analytics** - Basic traffic analytics through Vercel.

## Tech Stack

- **Core App:** HTML5, CSS3, vanilla JavaScript
- **Deployment Wrapper:** Next.js App Router on Vercel
- **Auth:** Clerk
- **Analytics:** Vercel Analytics
- **Maps:** Leaflet.js with CartoDB tiles
- **Animations:** Lenis smooth scrolling
- **Image Export:** html2canvas for bracket sharing
- **API Data:** football-data.org for optional squad/player data
- **Storage:** localStorage for theme, API key state, cached squads, and simulator data

## Project Structure

```text
world-cup-2026/
├── app/
│   ├── layout.tsx        # ClerkProvider, Vercel Analytics, global app shell
│   └── page.tsx          # Redirects / to the static landing page
├── public/               # Static files served by the Next/Vercel app
├── index.html            # Landing page with countdown, stats, and feature links
├── games.html            # Full 104-match schedule with filters and modals
├── groups.html           # Group standings and matchday overview
├── locations.html        # Interactive stadium map
├── calendar.html         # Calendar grid, .ics export, Google Calendar links
├── teams.html            # Team cards and optional roster API integration
├── myteam.html           # Squad builder and match simulator
├── bracket.html          # Full World Cup bracket simulator
├── guide.html            # Beginner-friendly World Cup guide
├── data.js               # Matches, groups, stadiums, flags, helper data
├── script.js             # Shared landing/schedule behavior
├── auth.js               # Clerk JS integration for static pages
├── theme.js              # Theme toggle and mobile nav behavior
├── styles.css            # Global responsive styles and themes
├── proxy.ts              # Clerk middleware for Next/Vercel
├── proxy.py              # Optional local-only CORS helper for API testing
├── package.json          # Next, React, Clerk, and Vercel dependencies
└── README.md
```

When editing the static pages, keep the root files and matching files in `public/` in sync because Vercel serves the static experience from `public/`.

## Data

All tournament schedule and venue data lives in `data.js`.

- **Total matches:** 104
- **Group stage:** 72 matches from June 11-27, 2026
- **Knockout rounds:** 32 matches from June 28-July 19, 2026
- **Teams:** 48 teams across 12 groups
- **Stadiums:** 16 venues across the United States, Mexico, and Canada

The schedule, stadium coordinates, capacities, groups, flags, and helper mappings are currently stored client-side.

## Local Development

Install dependencies:

```bash
npm install
```

Create `.env.local` for Clerk if you want to test sign-in locally:

```bash
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=your_publishable_key_here
CLERK_SECRET_KEY=your_secret_key_here
```

Start the development server:

```bash
npm run dev
```

Then open:

```text
http://localhost:3000
```

The site should remain accessible without signing in. Sign-in is only for optional account-based features.

## Optional API Integration

Roster and player data use [football-data.org](https://www.football-data.org). Users can paste their own API key on the Teams or My Team pages to fetch squad data.

- The API key is stored locally in the browser.
- Squad data is cached in localStorage after it loads.
- The deployed site routes browser requests through a CORS proxy URL.
- `proxy.py` exists only as a local development helper if direct local API testing needs it.

Future monetization can use the existing account system to unlock an API connection as a one-time paid feature while keeping the rest of the guide free.

## Deployment

The project is set up for Vercel with GitHub integration.

Required Vercel environment variables:

```bash
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=your_publishable_key_here
CLERK_SECRET_KEY=your_secret_key_here
```

Do not commit secrets. Keep `.env.local`, `node_modules`, `.next`, and other generated files out of Git.

After changing Vercel environment variables, redeploy the project so the new values are included in the build.

## Design

- Dark mode is the default visual identity, with gold World Cup-inspired accents.
- Light mode is supported across the main pages.
- Navigation uses a compact mobile layout with auth controls, theme toggle, and menu access.
- Cards, tables, filters, and modals are designed for quick scanning during the tournament.

## Contributing Ideas

- Saved user picks and bracket history
- Account-based dashboard for saved teams and favorite matches
- Stripe one-time payment for premium API-powered features
- More tournament explainers for new fans
- Historical World Cup stats and comparisons
- Progressive Web App support for offline schedule access

## Credits

Created by [Zach Andelman](https://linktr.ee/zachspam06).

Schedule and venue information is manually compiled from public World Cup sources. Live squad/player data is provided through [football-data.org](https://www.football-data.org).

This project is not affiliated with FIFA or any official organization.

## License

MIT License

Copyright (c) 2026 Zach Andelman
