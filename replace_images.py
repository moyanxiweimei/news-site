
import re

# 读取HTML
with open('/Users/maxiaoxu/.openclaw/workspace/news-site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 定义三个板块和图片映射
sections = {
    'medical': ['images/medical_1.jpg', 'images/medical_2.jpg', 'images/medical_3.jpg', 'images/medical_4.jpg'],
    'education': ['images/education_1.jpg', 'images/education_2.jpg', 'images/education_3.jpg', 'images/education_4.jpg'],
    'aerospace': ['images/aerospace_1.jpg', 'images/aerospace_2.jpg', 'images/aerospace_3.jpg', 'images/aerospace_4.jpg']
}

# 替换函数
def replace_section_images(html, section_id, image_paths):
    # 找到section的开始和结束
    section_start = html.find(f"<section id='{section_id}'")
    if section_start == -1:
        section_start = html.find(f'<section id="{section_id}"')
    if section_start == -1:
        print(f"未找到 {section_id} 板块")
        return html
    
    # 找到下一个section的开始作为结束位置
    next_section = html.find("<section id='", section_start + 1)
    if next_section == -1:
        next_section = len(html)
    
    section_html = html[section_start:next_section]
    
    # 找到所有 <img src='data:image...'> 或 <img src='images/...'> 
    # 使用正则替换
    img_pattern = r"<img\s+src='[^']+'"
    imgs = re.findall(img_pattern, section_html)
    print(f"{section_id}: 找到 {len(imgs)} 个img标签")
    
    # 替换前N个img标签的src
    replaced_count = 0
    for i, img_tag in enumerate(imgs):
        if i < len(image_paths):
            new_img = f"<img src='{image_paths[i]}'"
            section_html = section_html.replace(img_tag, new_img, 1)
            replaced_count += 1
            print(f"  替换 {i+1}: {image_paths[i]}")
    
    # 把修改后的section放回去
    html = html[:section_start] + section_html + html[next_section:]
    return html

# 逐个板块替换
for section_id, images in sections.items():
    html = replace_section_images(html, section_id, images)

# 保存
with open('/Users/maxiaoxu/.openclaw/workspace/news-site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ 网页图片替换完成！")
