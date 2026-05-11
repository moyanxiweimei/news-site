import re, os, base64
from pathlib import Path

BASE = Path('/Users/maxiaoxu/.openclaw/workspace/news-site')

with open(BASE / 'index.html', 'r') as f:
    html = f.read()

print(f"原始大小: {len(html):,} bytes ({len(html)/1024:.1f} KB)")

# 1. 提取所有 base64 图片并保存为文件
base64_pattern = re.compile(r"src='(data:image/([^;]+);base64,([^']+))'")
matches = base64_pattern.findall(html)
print(f"找到 {len(matches)} 个 base64 图片")

# 跟踪已提取的图片避免重复
extracted = {}
counter = {}

for full, mime, data in matches:
    # 生成文件名
    ext = mime.split('/')[-1]  # jpeg -> jpg
    if ext == 'jpeg':
        ext = 'jpg'
    
    # 根据内容生成唯一标识（取前50字符的hash）
    short_hash = hash(data[:100]) % 10000
    if short_hash in extracted:
        replacement = extracted[short_hash]
    else:
        # 确定文件名前缀（根据上下文判断板块）
        # 简单方法：根据附近文字判断
        idx = html.find(full)
        context = html[max(0, idx-200):min(len(html), idx+200)]
        
        # 尝试从上下文推断板块
        section = 'image'
        for s in ['finance', 'tech', 'products', 'auto', 'vc', 'medical', 'education', 'aerospace']:
            if s in context.lower():
                section = s
                break
        
        # 计数器
        if section not in counter:
            counter[section] = 1
        else:
            counter[section] += 1
        
        filename = f"{section}_{counter[section]}.{ext}"
        filepath = BASE / 'images' / filename
        
        # 解码并保存
        try:
            img_data = base64.b64decode(data)
            with open(filepath, 'wb') as f:
                f.write(img_data)
            print(f"  保存: {filename} ({len(img_data)} bytes)")
            replacement = f"images/{filename}"
            extracted[short_hash] = replacement
        except Exception as e:
            print(f"  失败: {filename} - {e}")
            replacement = ""
    
    # 替换 HTML 中的 base64
    html = html.replace(f"src='{full}'", f"src='{replacement}'", 1)

print(f"\n已保存 {len(extracted)} 个唯一图片")

# 2. 提取内联 CSS
style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
if style_match:
    css = style_match.group(1)
    # 保存到 style.css
    with open(BASE / 'style.css', 'w') as f:
        f.write(css)
    print(f"CSS 已提取: {len(css)} bytes")
    
    # 替换内联 CSS 为外部引用
    html = html.replace(style_match.group(0), '<link rel="stylesheet" href="style.css">')

# 3. 提取内联 JS
script_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if script_match:
    js = script_match.group(1)
    with open(BASE / 'script.js', 'w') as f:
        f.write(js)
    print(f"JS 已提取: {len(js)} bytes")
    
    html = html.replace(script_match.group(0), '<script src="script.js"></script>')

# 4. 压缩 HTML（移除多余空白）
html = re.sub(r'>\s+<', '><', html)
html = re.sub(r'\n\s*\n', '\n', html)

# 5. 写入优化后的 HTML
with open(BASE / 'index.html', 'w') as f:
    f.write(html)

final_size = len(html)
print(f"\n优化后 HTML: {final_size:,} bytes ({final_size/1024:.1f} KB)")
print(f"总计缩减: {(1 - final_size/len(open(BASE / 'index.html').read()))*100:.1f}%")
print(f"\n✅ 优化完成！")
print(f"  - index.html: {final_size/1024:.1f} KB")
print(f"  - style.css: 外部样式表")
print(f"  - script.js: 外部脚本")
print(f"  - images/: {len(extracted)} 个图片文件")
