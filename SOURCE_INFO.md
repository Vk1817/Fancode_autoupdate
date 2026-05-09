# 📡 drmlive/fancode-live-events — Source Info

> This is the **original source** that powers `Vk1817/Fancode-New-Auto-Update`.
> All data is fetched from here and mirrored into `pranav.json` and `fancode.m3u`.

---

## 🔗 Original Source

| | |
|--|--|
| **Repo** | [https://github.com/drmlive/fancode-live-events](https://github.com/drmlive/fancode-live-events) |
| **Stars** | ⭐ 27 |
| **Forks** | 🍴 12 |
| **Commits** | 74,000+ (extremely active) |

---

## 📂 Original File URLs

| File | Raw URL |
|------|---------|
| `fancode.json` | `https://raw.githubusercontent.com/drmlive/fancode-live-events/main/fancode.json` |
| `fancode.m3u` | `https://raw.githubusercontent.com/drmlive/fancode-live-events/main/fancode.m3u` |

---

## 🧾 JSON Schema (drmlive format)

```json
{
  "live_events": [
    {
      "title": "Match Title",
      "tournament": "Tournament Name",
      "category": "Cricket",
      "language": "Hindi",
      "status": "LIVE",
      "streamingStatus": "STARTED",
      "image": "https://...",
      "dai_url": "https://...m3u8",
      "adfree_url": "https://...m3u8",
      "startTime": "2026-05-09T10:00:00Z",
      "teams": [
        { "logo": "https://..." },
        { "logo": "https://..." }
      ]
    }
  ],
  "upcoming_events": [ ... ],
  "headers": {
    "User-Agent": "...",
    "Referer": "..."
  }
}
```

---

## 💖 Credit

All live data credit goes to **[drmlive](https://github.com/drmlive)**.
Please ⭐ star their repo: [drmlive/fancode-live-events](https://github.com/drmlive/fancode-live-events)
