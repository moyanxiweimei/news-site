
import json

with open('/Users/maxiaoxu/.openclaw/workspace/news-site/all-news.json', 'r') as f:
    data = json.load(f)

# 定义图片映射
image_maps = {
    'medical': ['images/medical_1.jpg', 'images/medical_2.jpg', 'images/medical_3.jpg', 'images/medical_4.jpg', 'images/medical_1.jpg'],
    'education': ['images/education_1.jpg', 'images/education_2.jpg', 'images/education_3.jpg', 'images/education_4.jpg', 'images/education_1.jpg'],
    'aerospace': ['images/aerospace_1.jpg', 'images/aerospace_2.jpg', 'images/aerospace_3.jpg', 'images/aerospace_4.jpg', 'images/aerospace_1.jpg']
}

# 为每个板块添加图片
for section, images in image_maps.items():
    items = data.get('news', {}).get(section, [])
    for i, item in enumerate(items):
        if i < len(images):
            item['image'] = images[i]

with open('/Users/maxiaoxu/.openclaw/workspace/news-site/all-news.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✅ all-news.json 图片添加完成')
for section in ['medical', 'education', 'aerospace']:
    items = data['news'][section]
    print(f'{section}: {len(items)} 条，前3条图片:')
    for i in range(min(3, len(items))):
        print(f'  - {items[i].get("image", "无")}')
