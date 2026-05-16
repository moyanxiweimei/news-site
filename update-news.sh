#!/bin/bash
# Daily News Updater
# Usage: ./update-news.sh

set -e

WORKDIR="$HOME/.openclaw/workspace/news-site"
IMGDIR="$WORKDIR/images"
cd "$WORKDIR"

echo "=== 📰 Daily News Update - $(date '+%Y-%m-%d %H:%M') ==="

# Get today's date in Chinese format
TODAY_YEAR=$(date '+%Y')
TODAY_MONTH=$(date '+%-m')
TODAY_DAY=$(date '+%-d')
DATE_CN="${TODAY_YEAR}年${TODAY_MONTH}月${TODAY_DAY}日"
DATE_SHORT="${TODAY_MONTH}月${TODAY_DAY}日"

echo "Today: $DATE_CN"

# Fetch IT之家 RSS for latest news
echo ""
echo "📡 Fetching news from IT之家..."
curl -sL "https://www.ithome.com/rss/" -o /tmp/ithome_rss.xml

# Parse RSS and extract recent news (today and yesterday)
python3 << 'PYTHON'
import xml.etree.ElementTree as ET
import re
import json
import os
from datetime import datetime, timedelta

rss_file = "/tmp/ithome_rss.xml"
tree = ET.parse(rss_file)
root = tree.getroot()

# Get items
items = []
for item in root.findall('.//item'):
    title = item.find('title')
    desc = item.find('description')
    link = item.find('link')
    pubDate = item.find('pubDate')
    
    if title is not None and desc is not None:
        # Extract image from description (handle URLs with query params like ?x-bce-process=...)
        img_match = re.search(r'src="(https?://[^"]+\.(?:jpg|jpeg|png)(?:\?[^"]*)?)"', desc.text or '')
        img_url = img_match.group(1) if img_match else None
        
        # Clean description (remove HTML)
        clean_desc = re.sub(r'<[^>]+>', '', desc.text or '')
        clean_desc = clean_desc.replace('IT之家', '').strip()
        clean_desc = clean_desc[:120] + '...' if len(clean_desc) > 120 else clean_desc
        
        items.append({
            'title': title.text,
            'summary': clean_desc,
            'link': link.text if link is not None else '',
            'image': img_url,
            'pubDate': pubDate.text if pubDate is not None else ''
        })

# Categorize news
categories = {
    'finance': [],
    'tech': [],
    'medical': [],
    'education': [],
    'aerospace': [],
    'products': [],
    'auto': [],
    'vc': []
}

# Keywords for categorization
keywords = {
    'finance': ['融资', '上市', '股价', '财报', '投资', '并购', '收购', 'IPO', '美元', '人民币', 'Meta', '员工', '奖金', '版权', '转播'],
    'tech': ['AI', '人工智能', '芯片', '处理器', '算法', '大模型', 'TikTok', 'Google', 'Meta', '科技', '开源', 'API', '云服务'],
    'medical': ['医疗', '医院', '药品', '疫苗', '基因', '脑机', '健康', '医保', '诊断', '治疗', '抑郁症', 'OPPO', '文案'],
    'education': ['教育', '学校', '大学', '高校', '学生', '考试', 'VR', '教学', ' UNESCO', '职业教育', '课后'],
    'aerospace': ['航天', '火箭', '卫星', '太空', '月球', '火星', 'eVTOL', '飞行器', '超音速', '空间站', '天舟'],
    'products': ['手机', '耳机', '键盘', '鼠标', '手表', '显示器', '笔记本', '平板', '相机', '红魔', '佳明', '樱桃', '吹风机'],
    'auto': ['汽车', '电动车', '新能源', '自动驾驶', '蔚来', '比亚迪', '岚图', '问界', '充电', '换电', '电池'],
    'vc': ['创业', '3D打印', '机器人', '硬件', 'NUC', '迷你主机', 'iQOO', '闪铸', '融资']
}

for item in items[:40]:  # Process top 40 news
    title = item['title']
    assigned = False
    
    for cat, words in keywords.items():
        if any(w in title for w in words):
            categories[cat].append(item)
            assigned = True
            break
    
    if not assigned:
        # Default to tech or products
        if '发布' in title or '推出' in title or '新品' in title or 'Pro' in title:
            categories['products'].append(item)
        else:
            categories['tech'].append(item)

# Save categorized news
with open('/tmp/news_categorized.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, ensure_ascii=False, indent=2)

print(f"Categorized {sum(len(v) for v in categories.values())} news items")
for cat, news in categories.items():
    print(f"  {cat}: {len(news)} items")
PYTHON

# Update HTML date
echo ""
echo "📝 Updating index.html..."
sed -i '' "s/[0-9]\{4\}年[0-9]\{1,2\}月[0-9]\{1,2\}日/$DATE_CN/g" index.html

# Update all dates in meta
echo "📝 Updating dates..."
# Use python for complex HTML updates
python3 << 'PYTHON'
import json
import re
import os

with open('/tmp/news_categorized.json', 'r', encoding='utf-8') as f:
    news = json.load(f)

date_short = os.popen("date '+%-m月%-d日'").read().strip()

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Simple update: just update the dates for now
html = re.sub(r'(36氪|IT之家|中国航天报|健康科技日报|医保局官网|神经科学前沿|AI教育周刊|教育信息化|职业教育观察|基础教育周刊|深空探测实验室|航空周刊) · [0-9]{1,2}月[0-9]{1,2}日', r'\1 · ' + date_short, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML dates updated")
PYTHON

# Download real images for news that have them
echo ""
echo "🖼️ Downloading images..."
python3 << 'PYTHON'
import json
import os
import subprocess

IMGDIR = os.path.expanduser("~/.openclaw/workspace/news-site/images")

with open('/tmp/news_categorized.json', 'r', encoding='utf-8') as f:
    news = json.load(f)

# Map categories to image filenames
cat_map = {
    'finance': ['finance_1', 'finance_2', 'finance_3'],
    'tech': ['tech_1', 'tech_2', 'tech_3'],
    'medical': ['medical_1', 'medical_2', 'medical_3'],
    'education': ['education_1', 'education_2', 'education_3'],
    'aerospace': ['aerospace_1', 'aerospace_2', 'aerospace_3'],
    'products': ['products_1', 'products_2', 'products_3'],
    'auto': ['auto_1', 'auto_2', 'auto_3'],
    'vc': ['vc_1', 'vc_2', 'vc_3']
}

for cat, img_names in cat_map.items():
    items = news.get(cat, [])
    for i, img_name in enumerate(img_names):
        if i < len(items) and items[i].get('image'):
            url = items[i]['image']
            # Convert to jpg if png
            if url.endswith('.png'):
                tmp_path = os.path.join(IMGDIR, f"{img_name}_tmp.png")
                jpg_path = os.path.join(IMGDIR, f"{img_name}.jpg")
                subprocess.run(['curl', '-sL', url, '-o', tmp_path], check=False)
                if os.path.exists(tmp_path) and os.path.getsize(tmp_path) > 5000:
                    subprocess.run(['sips', '-s', 'format', 'jpeg', tmp_path, '--out', jpg_path], 
                                  check=False, capture_output=True)
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
                    print(f"  ✓ {img_name}.jpg (from IT之家)")
                else:
                    print(f"  ✗ {img_name} download failed")
            else:
                path = os.path.join(IMGDIR, f"{img_name}.jpg")
                subprocess.run(['curl', '-sL', url, '-o', path], check=False)
                if os.path.exists(path) and os.path.getsize(path) > 5000:
                    print(f"  ✓ {img_name}.jpg (from IT之家)")
                else:
                    print(f"  ✗ {img_name} download failed")
        else:
            print(f"  ⏭ {img_name} (no image available)")
PYTHON

# Update version for cache busting
echo ""
echo "🔄 Busting cache..."
# Update image version
sed -i '' 's/\.jpg?v=[0-9]*/.jpg?v='"$(date +%s)"'/g' index.html

# Check images - report failures
echo ""
echo "🔍 Checking images..."
python3 << 'PYTHON'
import os

IMGDIR = os.path.expanduser("~/.openclaw/workspace/news-site/images")

# Categories and their expected images
cat_map = {
    'finance': ['finance_1', 'finance_2', 'finance_3'],
    'tech': ['tech_1', 'tech_2', 'tech_3'],
    'medical': ['medical_1', 'medical_2', 'medical_3'],
    'education': ['education_1', 'education_2', 'education_3'],
    'aerospace': ['aerospace_1', 'aerospace_2', 'aerospace_3'],
    'products': ['products_1', 'products_2', 'products_3'],
    'auto': ['auto_1', 'auto_2', 'auto_3'],
    'vc': ['vc_1', 'vc_2', 'vc_3']
}

missing = []
for cat, img_names in cat_map.items():
    for img_name in img_names:
        path = os.path.join(IMGDIR, f"{img_name}.jpg")
        if not os.path.exists(path) or os.path.getsize(path) < 5000:
            missing.append(img_name)

if missing:
    print(f"⚠️ Missing or too-small images ({len(missing)}): {', '.join(missing)}")
else:
    print("✅ All images present and valid")
PYTHON

# Commit and push
echo ""
echo "🚀 Committing and pushing..."
git add -A
git commit -m "📰 Auto-update: $(date '+%Y-%m-%d') daily news" || echo "Nothing to commit"
git push origin main || echo "Push failed"

echo ""
echo "✅ Done! Updated at $(date '+%H:%M:%S')"
echo "🌐 Site: https://moyanxiweimei.github.io/news-site/"
