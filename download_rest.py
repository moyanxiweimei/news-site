from playwright.sync_api import sync_playwright
import requests, os, time, re

os.makedirs('images', exist_ok=True)

searches = {
    'finance': '金融 股票 财经',
    'tech': '人工智能 科技 机器人',
    'auto': '电动汽车 汽车',
    'vc': '创业 投资 融资',
    'products': '智能手机 数码产品'
}

results = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    for name, keyword in searches.items():
        print(f"\n=== 搜索: {name} ({keyword}) ===")
        page = browser.new_page()
        page.goto(f"https://image.baidu.com/search/index?tn=baiduimage&word={keyword}", wait_until='networkidle')
        time.sleep(3)
        
        # 提取所有图片URL
        content = page.content()
        urls = re.findall(r'https?://[^\s"<>]+\.baidu\.com/[^\s"<>]+', content)
        urls = [u for u in urls if 'img' in u or 'gips' in u or 'it/u=' in u]
        urls = list(dict.fromkeys(urls))  # 去重
        
        print(f"找到 {len(urls)} 个候选URL")
        
        downloaded = 0
        for i, url in enumerate(urls):
            if downloaded >= 2:
                break
            if 'logo' in url.lower() or 'icon' in url.lower():
                continue
            try:
                r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0', 'Referer': 'https://image.baidu.com/'}, timeout=10)
                if r.status_code == 200 and len(r.content) > 10000:
                    ext = '.jpg' if b'JFIF' in r.content[:20] else '.png'
                    path = f'images/{name}_{downloaded+1}{ext}'
                    with open(path, 'wb') as f:
                        f.write(r.content)
                    print(f"  下载 {path} ({len(r.content)} bytes)")
                    downloaded += 1
            except Exception as e:
                pass
        
        results[name] = downloaded
        page.close()
    
    browser.close()

print(f"\n=== 完成 ===")
for k, v in results.items():
    print(f"{k}: {v} 张")
