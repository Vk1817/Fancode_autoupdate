# 📡 FanCode Live Events — Auto-Update Hub

<div align="center">

[![Auto Update](https://img.shields.io/badge/Auto%20Update-Every%205%20Min-brightgreen?logo=github-actions&logoColor=white)](https://github.com/Vk1817/Fancode-New-Auto-Update/actions)
[![Last Commit](https://img.shields.io/github/last-commit/Vk1817/Fancode-New-Auto-Update?color=blue&label=Last%20Updated&logo=github)](https://github.com/Vk1817/Fancode-New-Auto-Update/commits/main)
[![Stars](https://img.shields.io/github/stars/Vk1817/Fancode-New-Auto-Update?style=social)](https://github.com/Vk1817/Fancode-New-Auto-Update/stargazers)
[![Forks](https://img.shields.io/github/forks/Vk1817/Fancode-New-Auto-Update?style=social)](https://github.com/Vk1817/Fancode-New-Auto-Update/network/members)
[![Repo Size](https://img.shields.io/github/repo-size/Vk1817/Fancode-New-Auto-Update?logo=github)](https://github.com/Vk1817/Fancode-New-Auto-Update)
[![Telegram](https://img.shields.io/badge/Telegram-Join%20Channel-blue?logo=telegram)](https://t.me/addlist/6qALMSdKoVVkNWI1)

**A fully automated, zero-maintenance pipeline that keeps FanCode live event data always fresh — updated every 5 minutes via GitHub Actions.**

[📥 Get JSON Data](#-data-files) • [📺 Get M3U Playlist](#-data-files) • [📢 Join Telegram](#-join-our-telegram)

</div>

---

## 📢 Join Our Telegram

Stay updated with the latest FanCode streams, announcements, and channel updates:

<div align="center">

### 👉 [Join Telegram Channel](https://t.me/addlist/6qALMSdKoVVkNWI1)

</div>

---

## 🚀 What is This?

This repository automatically fetches live FanCode match data from the original source and makes it available in two formats:

- **`pranav.json`** — Full structured JSON with all match metadata, stream URLs, headers, and CDN details
- **`fancode.m3u`** — Ready-to-use M3U playlist for IPTV players (only includes LIVE + STARTED streams)

The entire pipeline runs on **GitHub Actions**, meaning no server, no hosting, and no manual work is needed.

---

## 📂 Data Files

Use these raw URLs directly in your apps or IPTV players:

| File | Description | Raw URL |
|------|-------------|---------|
| `pranav.json` | Full JSON data | [`pranav.json`](https://raw.githubusercontent.com/Vk1817/Fancode-New-Auto-Update/main/pranav.json) |
| `fancode.m3u` | M3U Playlist | [`fancode.m3u`](https://raw.githubusercontent.com/Vk1817/Fancode-New-Auto-Update/main/fancode.m3u) |

---

## ⚙️ How It Works

```
Every 5 Minutes
      │
      ▼
GitHub Actions triggers update_json.py
      │
      ▼
Fetches latest data from original source API
      │
      ├──► Saves full JSON → pranav.json
      │
      └──► Filters LIVE streams → fancode.m3u
      │
      ▼
Auto-commits & pushes to this repository
```

### M3U Filter Logic

The playlist only includes matches that meet **all** of the following:
- `status == "LIVE"`
- `streamingStatus == "STARTED"`
- A valid `Primary_Playback_URL` is present

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3 |
| Automation | GitHub Actions |
| Data Format | JSON + M3U |
| Schedule | Every 5 minutes (cron) |

---

## 📈 Repository Stats

| Metric | Badge |
|--------|-------|
| Auto Update | [![Auto Update](https://img.shields.io/badge/Auto%20Update-Every%205%20Min-brightgreen?logo=github-actions)](https://github.com/Vk1817/Fancode-New-Auto-Update/actions) |
| Last Commit | [![Last Commit](https://img.shields.io/github/last-commit/Vk1817/Fancode-New-Auto-Update?logo=github)](https://github.com/Vk1817/Fancode-New-Auto-Update/commits/main) |
| Stars | [![Stars](https://img.shields.io/github/stars/Vk1817/Fancode-New-Auto-Update?style=social)](https://github.com/Vk1817/Fancode-New-Auto-Update/stargazers) |
| Forks | [![Forks](https://img.shields.io/github/forks/Vk1817/Fancode-New-Auto-Update?style=social)](https://github.com/Vk1817/Fancode-New-Auto-Update/network/members) |
| Repo Size | [![Repo Size](https://img.shields.io/github/repo-size/Vk1817/Fancode-New-Auto-Update?logo=github)](https://github.com/Vk1817/Fancode-New-Auto-Update) |

---

## 💖 Credits & Attribution

This project is made possible thanks to the original data source:

| | |
|-|-|
| **Original Author** | [DOCTOR_STRANGE](https://github.com/doctor-8trange) |
| **Source Repo** | [doctor-8trange/zyphx8](https://github.com/doctor-8trange/zyphx8) |
| **Original Telegram** | [jitendraunatti_github](https://t.me/jitendraunatti_github) |

> Full credit goes to the original creator for maintaining the FanCode data pipeline. Please support them too! ⭐

---

## 👤 Maintained By

<div align="center">

**[Vk1817](https://github.com/Vk1817)**

📣 Telegram: [https://t.me/addlist/6qALMSdKoVVkNWI1](https://t.me/addlist/6qALMSdKoVVkNWI1)

If you find this useful, please **⭐ Star** the repo — it helps a lot!

</div>
