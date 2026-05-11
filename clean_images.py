import re, os
from pathlib import Path

BASE = Path('/Users/maxiaoxu/.openclaw/workspace/news-site')

with open(BASE / 'index.html', 'r') as f:
    html = f.read()

print(f"当前大小: {len(html):,} bytes ({len(html)/1024:.1f} KB)")

# 图片映射
image_map = {
    'finance': ['images/finance_1.jpg', 'images/finance_2.jpg', 'images/finance_3.jpg'],
    'tech': ['images/tech_1.jpg', 'images/tech_2.jpg', 'images/tech_3.jpg'],
    'products': ['images/products_1.jpg', 'images/products_2.jpg'],
    'auto': ['images/auto_1.jpg', 'images/auto_2.jpg'],
    'vc': ['images/vc_1.jpg', 'images/vc_2.jpg'],
    'medical': ['images/medical_1.jpg', 'images/medical_2.jpg', 'images/medical_3.jpg', 'images/medical_4.jpg'],
    'education': ['images/education_1.jpg', 'images/education_2.jpg', 'images/education_3.jpg', 'images/education_4.jpg'],
    'aerospace': ['images/aerospace_1.jpg', 'images/aerospace_2.jpg', 'images/aerospace_3.jpg', 'images/aerospace_4.jpg'],
}

# 处理每个 section，替换其中的图片
section_pattern = re.compile(
    r"<section id='([^']+)' class='news-section'>(.*?)</section>",
    re.DOTALL
)

def process_section(match):
    section_id = match.group(1)
    section_html = match.group(0)
    
    if section_id not in image_map:
        return section_html
    
    images = image_map[section_id]
    img_idx = 0
    
    def replace_img(m):
        nonlocal img_idx
        alt_text = m.group(2) if m.lastindex >= 2 else ''
        img = images[img_idx % len(images)]
        img_idx += 1
        return f"src='{img}' alt=\"{alt_text}\" class='card-image' loading='lazy'"
    
    # 替换该 section 中的所有 img 标签
    return re.sub(
        r"src='[^']+' alt=\"([^\"]+)\" class='card-image' loading='lazy'",
        replace_img,
        section_html
    )

html = section_pattern.sub(process_section, html)

# 移除所有剩余的 base64 图片
html = re.sub(r"src='data:image/[^']+'", r"src=''", html)

# 移除所有腾讯云图片
html = re.sub(r"src='https://moyanxiweimei-[^']+'", r"src=''", html)

# 移除所有 Unsplash 图片
html = re.sub(r"src='https://images\.unsplash\.com/[^']+'", r"src=''", html)

print(f"清理后大小: {len(html):,} bytes ({len(html)/1024:.1f} KB)")

with open(BASE / 'index.html', 'w') as f:
    f.write(html)

print("✅ 图片清理完成！")
