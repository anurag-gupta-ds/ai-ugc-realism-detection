import requests

API_KEY = "hbWhM0zTFYAObKVVL10YcSAbXMMcFF86hSVeIXZeA4ITue24PkdShTTB"
headers = {"Authorization": API_KEY}

queries = [
    "indian women advertising",
    "indian women business",
    "indian women lifestyle",
    "indian women commercial"
]

for q in queries:
    count = 0
    page = 1

    while count < 100:  # stop after 100 videos per query
        url = f"https://api.pexels.com/videos/search?query={q}&per_page=80&page={page}"
        response = requests.get(url, headers=headers)
        data = response.json()

        # ✅ Check if "videos" key exists
        if "videos" not in data:
            print(f"No videos found for query '{q}' on page {page}")
            break

        for i, video in enumerate(data["videos"]):
            if count >= 100:
                break
            link = video["video_files"][0]["link"]
            filename = f"{q.replace(' ', '_')}_page{page}_{i}.mp4"
            r = requests.get(link)
            with open(filename, "wb") as f:
                f.write(r.content)
            count += 1
            print(f"Downloaded {filename}")

        page += 1
