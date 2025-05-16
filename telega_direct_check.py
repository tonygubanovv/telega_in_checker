import pandas as pd
import requests
import time

def check_telega_card(username):
    url = f"https://telega.in/channels/{username}/card"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return url if response.status_code == 200 else "—"
    except:
        return "—"

def extract_username(url):
    if "t.me/" in url:
        return url.split("t.me/")[-1].strip("/")
    return url.strip("@").strip()

with open("channels.txt", "r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]

results = []
for idx, link in enumerate(links, 1):
    username = extract_username(link)
    print(f"🔍 {idx}/{len(links)} — {username}")
    telega_url = check_telega_card(username)
    results.append({"Источник": link, "Telega.in": telega_url})
    time.sleep(1.2)

df = pd.DataFrame(results)
df.to_excel("telega_results_direct.xlsx", index=False)
print("✅ Готово: telega_results_direct.xlsx создан.")
