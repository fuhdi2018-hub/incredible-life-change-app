# Ìyípadà Ìyanu Ìwàláàyè — Ìtòlẹ́sẹẹsẹ 1
### The Incredible Life Change, Yoruba Offline Reading PWA

Offline-capable Progressive Web App (PWA) presenting *The Incredible Life Change* by Kunle Bello in Yoruba (`BOOK_DATA_YO`) with matching English text (`BOOK_DATA_EN`), across 12 chapters, with reading-companion tools and a Yorùbá/English toggle.

> Yoruba Read Aloud (TTS) is planned — see `../incredible-life-change-yoruba-tts-PRD.md`. No audio/TTS exists in this build yet.

## Features

- **Bilingual book:** 12 chapters in Yoruba + matching English text from `book-data.js`, in-app Yorùbá/English toggle
- **Reader view:** chapter list, bookmarks, diacritic-friendly Yoruba typography
- **Home:** daily pick + streak tracker
- **Live the Chapter:** application / quiz per chapter
- **Journal, Prayer, Explore tabs**
- **Export:** PDF (jsPDF) + Word (.docx, with/without journal notes)
- **Offline-first PWA:** `sw.js` precache + runtime cache, installable via `manifest.json`
- **Assets:** `images/nail-diagram.png`, `images/triangle-diagram.png`, bundled `fonts/DejaVuSans.ttf` for PDF export

## Tech stack

- Single-file React 18 app in `index.html` (CDN: React, ReactDOM, jsPDF, docx), `lang="yo"`
- Content in `book-data.js` (`window.BOOK_DATA_YO` + `window.BOOK_DATA_EN`)
- No build step, no backend
- State in browser `localStorage`; offline via Service Worker Cache Storage
- PWA: `manifest.json` + `sw.js`

## Project structure

```
incredible-life-change-yoruba-app-1/
  index.html      # app UI (Reader, Home, Journal, Prayer, Explore, export)
  book-data.js    # BOOK_DATA_YO + BOOK_DATA_EN, 12 chapters each
  manifest.json   # PWA manifest (Yoruba name/description)
  sw.js           # service worker, offline cache
  icons/          # icon-192.png, icon-512.png
  images/         # nail-diagram.png, triangle-diagram.png
  fonts/          # DejaVuSans.ttf (PDF export)
  design.html     # theme preview (colors, type, buttons, inputs)
  serve.ps1       # local static server for browser testing
```

## Run locally

```powershell
# serve (required for service worker / PWA install test)
powershell -NoProfile -ExecutionPolicy Bypass -File ./serve.ps1
```

Then open `http://localhost:8000/index.html`. PWA install needs `http://localhost` or HTTPS.

## Roadmap — Yoruba Read Aloud TTS

Planned per PRD, not yet built:

- Read Aloud control in Reader reading from `BOOK_DATA_YO`
- Play / pause / resume, paragraph + chapter skip, speed control
- Resume last position, offline / cached audio

## Status

Yoruba reading app in place (Phase 0 done). TTS scoped, not yet implemented (Phase 1 next: Yoruba voice spike).
