#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import time
import os

# Keywords for each image
images = {
    "finance_1": "artificial intelligence startup technology",
    "finance_2": "businessman city skyline corporate",
    "finance_3": "BMW car automotive factory",
    "tech_1": "AI video generation digital art",
    "tech_2": "robot hand mechanical precision",
    "tech_3": "humanoid robot android futuristic",
    "medical_1": "AI medical diagnosis doctor tablet",
    "medical_2": "DNA gene editing laboratory biotechnology",
    "medical_3": "smartwatch wearable health monitoring",
    "medical_4": "medicine pills pharmacy healthcare",
    "medical_5": "brain neural network neuroscience",
    "education_1": "AI classroom robot teaching education",
    "education_2": "university student computer campus",
    "education_3": "VR headset virtual reality learning",
    "education_4": "vocational training workshop technical",
    "education_5": "after school tutoring children learning",
    "aerospace_1": "rocket launch space fire",
    "aerospace_2": "SpaceX starship rocket landing",
    "aerospace_3": "satellite space orbit earth",
    "aerospace_4": "moon lunar surface astronaut",
    "aerospace_5": "supersonic jet airplane aviation",
    "products_1": "home appliances electronics kitchen",
    "products_2": "gaming smartphone mobile RGB",
    "auto_1": "Brazil Rio de Janeiro travel",
    "auto_2": "electric car factory manufacturing",
    "vc_1": "startup office technology business",
    "vc_2": "video creation studio content creator",
}

base_dir = os.path.expanduser("~/.openclaw/workspace/news-site/images")

def download_image(name, keyword):
    try:
        # Search Unsplash
        query = urllib.parse.quote(keyword)
        search_url = f"https://unsplash.com/napi/search/photos?query={query}&per_page=5"
        
        req = urllib.request.Request(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        
        if not data.get("results"):
            print(f"  No results for {name}: {keyword}")
            return False
        
        # Get first result's regular URL and modify to 800px
        img_url = data["results"][0]["urls"]["regular"]
        # Replace width parameter with 800
        img_url = img_url.replace("w=1080", "w=800")
        
        # Download image
        img_req = urllib.request.Request(img_url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        
        with urllib.request.urlopen(img_req, timeout=30) as resp:
            img_data = resp.read()
        
        filepath = os.path.join(base_dir, f"{name}.jpg")
        with open(filepath, "wb") as f:
            f.write(img_data)
        
        size = len(img_data)
        print(f"  Downloaded {name}.jpg ({size} bytes) - {keyword}")
        return True
        
    except Exception as e:
        print(f"  Failed {name}: {e}")
        return False

print("Downloading images from Unsplash...")
success = 0
for name, keyword in images.items():
    if download_image(name, keyword):
        success += 1
    time.sleep(0.5)  # Be polite

print(f"\nDone: {success}/{len(images)} images downloaded")
