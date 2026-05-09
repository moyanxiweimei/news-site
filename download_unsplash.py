import requests, os, json

os.makedirs('images', exist_ok=True)

# 需要下载的图片
images_to_download = {
    'finance_1.jpg': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&q=80',
    'finance_2.jpg': 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&q=80',
    'finance_3.jpg': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80',
    'tech_1.jpg': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=80',
    'tech_2.jpg': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&q=80',
    'tech_3.jpg': 'https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=800&q=80',
    'products_1.jpg': 'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=800&q=80',
    'products_2.jpg': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&q=80',
    'auto_1.jpg': 'https://images.unsplash.com/photo-1555212697-194d092e3b8f?w=800&q=80',
    'auto_2.jpg': 'https://images.unsplash.com/photo-1617788138017-80ad40651399?w=800&q=80',
    'vc_1.jpg': 'https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&q=80',
    'vc_2.jpg': 'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=800&q=80',
}

results = {}
for filename, url in images_to_download.items():
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        if r.status_code == 200 and len(r.content) > 5000:
            path = f'images/{filename}'
            with open(path, 'wb') as f:
                f.write(r.content)
            results[filename] = len(r.content)
            print(f"✅ {filename} ({len(r.content)} bytes)")
        else:
            print(f"❌ {filename} - status={r.status_code}, size={len(r.content)}")
    except Exception as e:
        print(f"❌ {filename} - {e}")

# 更新 all-news.json 为本地路径
with open('all-news.json', 'r') as f:
    data = json.load(f)

local_images = {
    'finance': ['images/finance_1.jpg', 'images/finance_2.jpg', 'images/finance_3.jpg'],
    'tech': ['images/tech_1.jpg', 'images/tech_2.jpg', 'images/tech_3.jpg'],
    'products': ['images/products_1.jpg', 'images/products_2.jpg'],
    'auto': ['images/auto_1.jpg', 'images/auto_2.jpg'],
    'vc': ['images/vc_1.jpg', 'images/vc_2.jpg'],
}

for section, images in local_images.items():
    items = data.get('news', {}).get(section, [])
    for i, item in enumerate(items):
        if i < len(images):
            item['image'] = images[i]

with open('all-news.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\n✅ all-news.json 已更新为本地图片路径")
