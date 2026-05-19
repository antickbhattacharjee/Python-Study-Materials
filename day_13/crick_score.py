import requests

# 1. API endpoint (free public)
url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

# 2. RapidAPI headers (you can get free key from RapidAPI)
headers = {
    "x-rapidapi-key": "49463dacd9mshdb62add85a5aa9cp1aa42fjsne5fad75f70e0",  # 👈 Replace with your RapidAPI key
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}
# 3. Send GET request
response = requests.get(url, headers=headers)

# 4. Convert to JSON
data = response.json()

# 5. Extract basic info
print("🏏 LIVE MATCHES\n")
for match_type in data.get("typeMatches", []):
    series_name = match_type.get("seriesMatches", [])
    for s in series_name:
        if "seriesAdWrapper" in s:
            series = s["seriesAdWrapper"]["seriesName"]
            matches = s["seriesAdWrapper"]["matches"]
            for m in matches:
                info = m["matchInfo"]
                team1 = info["team1"]["teamName"]
                team2 = info["team2"]["teamName"]
                status = info["status"]
                print(f"{series} → {team1} vs {team2} : {status}")
            print()
