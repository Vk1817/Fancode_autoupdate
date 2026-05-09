import urllib.request
import json
import sys

JSON_SOURCE = "https://raw.githubusercontent.com/drmlive/fancode-live-events/main/fancode.json"
M3U_SOURCE  = "https://raw.githubusercontent.com/drmlive/fancode-live-events/main/fancode.m3u"

TELEGRAM = "https://t.me/addlist/6qALMSdKoVVkNWI1"
AUTHOR   = "Vk1817"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def main():
    # ── JSON ──────────────────────────────────────────
    print(f"[*] Fetching JSON from drmlive/fancode-live-events ...")
    try:
        raw = fetch(JSON_SOURCE)
        data = json.loads(raw.decode("utf-8"))
    except Exception as e:
        print(f"[!] JSON fetch failed: {e}")
        sys.exit(1)

    if not data.get("Telegram"):
        data["Telegram"] = TELEGRAM
    if not data.get("Author"):
        data["Author"] = AUTHOR

    with open("pranav.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("[✓] pranav.json saved")

    # ── M3U ──────────────────────────────────────────
    print(f"[*] Fetching M3U from drmlive/fancode-live-events ...")
    try:
        m3u = fetch(M3U_SOURCE).decode("utf-8")
    except Exception as e:
        print(f"[!] M3U fetch failed: {e}")
        sys.exit(1)

    with open("fancode.m3u", "w", encoding="utf-8") as f:
        f.write(m3u)
    print("[✓] fancode.m3u saved")

if __name__ == "__main__":
    main()
