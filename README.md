# The Incredible Life Change — Series 1
### Ìyípadà Ìyanu Ìwàláàyè | Offline Yoruba + English Reading PWA

Offline-capable Progressive Web App (PWA) presenting the book *The Incredible Life Change* by Kunle Bello in parallel Yoruba (`BOOK_DATA_YO`) and English (`BOOK_DATA_EN`) editions, across 12 chapters, with reading-companion tools.

> Yoruba Read Aloud (TTS) is planned — see `../incredible-life-change-yoruba-tts-PRD.md`. No audio/TTS exists in this build yet.

## Features

- **Bilingual book:** 12 chapters in Yoruba + matching English text from `book-data.js`
- **Reader view:** chapter list, bookmarks, Yoruba/English toggle
- **Home:** daily pick + streak tracker
- **Live the Chapter:** application / quiz per chapter
- **Journal, Prayer, Explore tabs**
- **Export:** PDF (jsPDF) + Word (.docx, with/without journal notes)
- **Offline-first PWA:** `sw.js` precache + runtime cache, installable via `manifest.json`
- **Assets:** `images/nail-diagram.png`, `images/triangle-diagram.png`, bundled `fonts/DejaVuSans.ttf` for PDF export

## Chapters (Yoruba)

1. Ọ̀jọ̀ Àyẹ̀yẹ́
2. Ìgbàgbọ́ Lasan Tàbí Ọmọ Ẹ̀hìn?
3. Ọ̀tá Tó Búburú Jù
4-7. Àwọn Ìfarahàn Ẹran-ara 1–4
8. Owó Tí Ìjẹ́-ẹ̀yìn Ẹ̀yìn Jésù Ń Béèrè
9. Ojúṣe Ọmọ-ẹ̀yìn
10. Títẹ̀lé Jésù
11. Nípa Títẹ̀lé Àwọn Ìṣísẹ̀ Rẹ̀
12. Àkópọ̀ Kristẹni

## Tech stack

- Single-file React 18 app in `index.html` (CDN: React, ReactDOM, jsPDF, docx)
- Content in `book-data.js`
- No build step, no backend
- PWA: `manifest.json` + `sw.js` (`ilc-book-v1` cache)

## Project structure

```
incredible-life-change-app-1/
  index.html      # app UI (Reader, Home, Journal, Prayer, Explore, export)
  book-data.js    # BOOK_DATA_YO + BOOK_DATA_EN, 12 chapters each
  manifest.json   # PWA manifest
  sw.js           # service worker, offline cache
  icons/          # icon-192.png, icon-512.png
  images/         # nail-diagram.png, triangle-diagram.png
  fonts/          # DejaVuSans.ttf (PDF export)
```

## Run locally

No install needed. Either:

```powershell
# option 1 — open directly
start index.html

# option 2 — serve (required for service worker / PWA install test)
npx serve .
# or
python -m http.server 8000
```

Then open `http://localhost:8000` / `http://localhost:3000`.

PWA install needs `http://localhost` or HTTPS.

## Roadmap — Yoruba Read Aloud TTS

Planned per PRD, not yet built:

- Read Aloud control in Reader reading from `BOOK_DATA_YO`
- Play / pause / resume, paragraph + chapter skip, speed control
- Resume last position, offline / cached audio

## Status

Reading app complete. TTS scoped, not yet implemented.
