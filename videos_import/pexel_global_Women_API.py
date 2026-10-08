import requests

API_KEY = "hbWhM0zTFYAObKVVL10YcSAbXMMcFF86hSVeIXZeA4ITue24PkdShTTB"
headers = {"Authorization": API_KEY}

regions = ["chinese", "japanese", "british", "american", "african"]
gender = "women"   # 👈 focus on women only

# Each region gets 80 videos → 5 regions × 80 = 400 total
for region in regions:
    query = f"{region} {gender}"
    count = 0
    page = 1

    while count < 40:  # stop after 40 videos per region
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=80&page={page}"
        response = requests.get(url, headers=headers)
        data = response.json()

        if "videos" not in data:
            print(f"No videos found for query '{query}' on page {page}")
            break

        for i, video in enumerate(data["videos"]):
            if count >= 40:
                break
            link = video["video_files"][0]["link"]
            filename = f"{query.replace(' ', '_')}_page{page}_{i}.mp4"
            r = requests.get(link)
            with open(filename, "wb") as f:
                f.write(r.content)
            count += 1
            print(f"Downloaded {filename}")

        page += 1
