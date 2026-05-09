import urllib.request
import urllib.parse
import re
import os
import json
from PIL import Image

# Search queries for each news item
search_queries = {
    "finance": [
        None,  # "月之暗面完成20亿美元新融资" - AI company
        None,  # "李嘉诚抛售资产套现约455亿" - Li Ka-shing
        "BMW iX3 electric car official"  # "宝马一季度利润降25%"
    ],
    "tech": [
        None,  # "DeepSeek-R2模型提前上线" - AI model
        None,  # "华为小艺接入盘古大模型" - Huawei
        "Unitree Go2 humanoid robot walking"  # "宇树UniStore全面开放"
    ],
    "medical": [
        None,  # "AI辅助诊断首次通过国家药监局三类医疗器械审批"
        None,  # "基因编辑疗法获批临床试验"
        None,  # "国家医保局调整DRG付费权重"
        None,  # "全球首款AI病理诊断系统落地"
        None,  # "马斯克Neuralink获FDA批准人体试验"
    ],
    "education": [
        None,  # "教育部发布AI+教育行动计划"
        None,  # "Duolingo推出AI口语教练"
        None,  # "OpenAI开放GPT-4教育折扣"
        None,  # "清华大学成立AI学院"
        None,  # "联合国教科文组织发布AI教育伦理指南"
    ],
    "aerospace": [
        None,  # "SpaceX星舰第四次试飞成功"
        None,  # "中国空间站完成首个商业载荷任务"
        None,  # "NASA宣布阿尔忒弥斯登月新计划"
        "moon surface craters closeup"  # "月球南极探测任务启动"
    ],
    "products": [
        None,  # "苹果发布iPad Pro M4芯片"
        None,  # "三星宣布退出中国家电市场"
    ],
    "auto": [
        None,  # "小米SU7交付量突破10万辆"
        "BMW M8 GTE racing car front"  # "宝马一季度利润降25%"
    ],
    "vc": [
        None,  # "红杉中国完成新一期90亿美元基金募集"
        None,  # "中国对巴西等五国试行免签入境"
    ]
}

def search_bing_images(query, num=3):
    """Search Bing images and return URLs"""
    if not query:
        return []
    
    encoded = urllib.parse.quote(query)
    url = f'https://www.bing.com/images/search?q={encoded}&form=HDRSC2&first=1'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        
        # Extract image URLs from Bing's murl format
        # Bing stores image URLs in murl parameter
        pattern = r'murl=([^&]+\.(?:jpg|jpeg|png|webp))'
        matches = re.findall(pattern, html, re.IGNORECASE)
        
        # Decode URL-encoded strings
        urls = []
        for m in matches[:num]:
            try:
                decoded = urllib.parse.unquote(m)
                if decoded.startswith('http'):
                    urls.append(decoded)
            except:
                pass
        
        return urls
    except Exception as e:
        print(f"Search error for '{query}': {e}")
        return []

def download_image(url, path, max_size_kb=100):
    """Download and compress image"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=15)
        data = resp.read()
        
        # Save temporarily
        temp = '/tmp/temp_img.jpg'
        with open(temp, 'wb') as f:
            f.write(data)
        
        # Compress
        img = Image.open(temp)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Resize to reasonable dimensions
        img.thumbnail((800, 450), Image.Resampling.LANCZOS)
        
        # Save with quality reduction until size is acceptable
        quality = 85
        while quality > 50:
            img.save(path, 'JPEG', quality=quality, optimize=True)
            size_kb = os.path.getsize(path) / 1024
            if size_kb <= max_size_kb:
                break
            quality -= 5
        
        final_size = os.path.getsize(path) / 1024
        print(f"  Downloaded: {final_size:.1f} KB")
        return True
        
    except Exception as e:
        print(f"  Download error: {e}")
        return False

# Main execution
print("Searching and downloading images...")
print("=" * 50)

results = {}
for section, queries in search_queries.items():
    for idx, query in enumerate(queries):
        if not query:
            continue
        
        print(f"\n[{section}][{idx}] Searching: {query}")
        urls = search_bing_images(query, num=5)
        
        if not urls:
            print("  No images found")
            continue
        
        # Try downloading each URL until one works
        saved = False
        for i, url in enumerate(urls):
            safe_name = query.replace(' ', '_')[:30]
            path = f'/tmp/img_{section}_{idx}_{i}.jpg'
            
            print(f"  Trying URL {i+1}...", end=' ')
            if download_image(url, path):
                results[f"{section}_{idx}"] = path
                saved = True
                break
        
        if not saved:
            print("  All downloads failed")

print("\n" + "=" * 50)
print(f"Successfully downloaded: {len(results)} images")
for key, path in results.items():
    size = os.path.getsize(path) / 1024
    print(f"  {key}: {path} ({size:.1f} KB)")
