import re, json, os
from pathlib import Path

BASE = Path('/Users/maxiaoxu/.openclaw/workspace/news-site')

with open(BASE / 'script.js', 'r') as f:
    js = f.read()

# 提取 JSON 数据
json_match = re.search(r'var newsData = ({.*?});', js, re.DOTALL)
if json_match:
    json_str = json_match.group(1)
    # 解析 JSON
    try:
        news_data = json.loads(json_str)
        # 保存到文件
        with open(BASE / 'news-data.json', 'w') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
        print(f"✅ 新闻数据已保存到 news-data.json ({len(json_str)} bytes)")
        
        # 替换 JS 中的数据为 fetch 加载
        new_js = js.replace(
            json_match.group(0),
            'var newsData = {};\n\n// 加载新闻数据\nfetch("news-data.json")\n  .then(r => r.json())\n  .then(data => {\n    newsData = data;\n    initNews();\n  })\n  .catch(e => console.error("加载新闻数据失败:", e));'
        )
        
        with open(BASE / 'script.js', 'w') as f:
            f.write(new_js)
        
        print(f"✅ JS 已更新，使用 fetch 加载数据")
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析失败: {e}")
else:
    print("❌ 未找到新闻数据")

# 检查最终大小
sizes = {
    'index.html': os.path.getsize(BASE / 'index.html'),
    'style.css': os.path.getsize(BASE / 'style.css'),
    'script.js': os.path.getsize(BASE / 'script.js'),
    'news-data.json': os.path.getsize(BASE / 'news-data.json'),
}

print(f"\n📊 最终文件大小:")
total = 0
for name, size in sizes.items():
    print(f"  {name}: {size/1024:.1f} KB")
    total += size
print(f"  总计: {total/1024:.1f} KB")
