import requests

# 🔑 Your Pexels API key
API_KEY = "hbWhM0zTFYAObKVVL10YcSAbXMMcFF86hSVeIXZeA4ITue24PkdShTTB"
headers = {"Authorization": API_KEY}

# Queries you want to fetch
queries = [
    "indian men advertising",
    "indian men business",
    "indian men lifestyle",
    "indian men commercial"
]

# Loop through queries
for q in queries:
    count = 0  # track how many videos downloaded per query
    page = 1

    while count < 60:  # stop after 60 videos per query
        url = f"https://api.pexels.com/videos/search?query={q}&per_page=80&page={page}"
        response = requests.get(url, headers=headers)
        data = response.json()

        for i, video in enumerate(data["videos"]):
            if count >= 60:  # break if we already hit 60
                break
            link = video["video_files"][0]["link"]
            filename = f"{q.replace(' ', '_')}_page{page}_{i}.mp4"
            r = requests.get(link)
            with open(filename, "wb") as f:
                f.write(r.content)
            count += 1
            print(f"Downloaded {filename}")

        page += 1 
