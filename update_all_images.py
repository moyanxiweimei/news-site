
import json

with open('/Users/maxiaoxu/.openclaw/workspace/news-site/all-news.json', 'r') as f:
    data = json.load(f)

# Unsplash 高质量免费图片链接
unsplash_images = {
    'finance': [
        'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&q=80',
        'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&q=80',
        'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80'
    ],
    'tech': [
        'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&q=80',
        'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&q=80',
        'https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=800&q=80'
    ],
    'products': [
        'https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=800&q=80',
        'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&q=80'
    ],
    'auto': [
        'https://images.unsplash.com/photo-1555212697-194d092e3b8f?w=800&q=80',
        'https://images.unsplash.com/photo-1617788138017-80ad40651399?w=800&q=80'
    ],
    'vc': [
        'https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&q=80',
        'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=800&q=80'
    ]
}

# 为每个板块添加图片
for section, images in unsplash_images.items():
    items = data.get('news', {}).get(section, [])
    for i, item in enumerate(items):
        if i < len(images):
            item['image'] = images[i]

with open('/Users/maxiaoxu/.openclaw/workspace/news-site/all-news.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('✅ all-news.json 所有板块图片添加完成！')
for section in ['finance', 'tech', 'products', 'auto', 'vc', 'medical', 'education', 'aerospace']:
    items = data['news'][section]
    has_img = sum(1 for i in items if 'image' in i)
    print(f'{section}: {len(items)} items, {has_img} have images')
