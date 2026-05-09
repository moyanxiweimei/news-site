from playwright.sync_api import sync_playwright
import requests, os, time

os.makedirs('images', exist_ok=True)

searches = {
    'finance': 'finance stock market chart',
    'tech': 'artificial intelligence robot technology',
    'products': 'smartphone gadget electronics',
    'auto': 'electric car automotive',
    'vc': 'startup business investment'
}

results = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    for name, keyword in searches.items():
        print(f"\n=== 搜索: {name} ===")
        page = browser.new_page()
        page.goto(f"https://www.bing.com/images/search?q={keyword.replace(' ', '+')}", wait_until='networkidle')
        time.sleep(2)
        
        urls = page.eval_on_selector_all('img.mimg', 'els => els.map(e => e.src).filter(s => s && s.startsWith("http") && !s.includes("bing.net/th") && s.length > 100)')
        
        if not urls:
            urls = page.eval_on_selector_all('img[src]', 'els => els.map(e => e.src).filter(s => s && s.startsWith("http") && !s.includes("bing") && s.length > 100)')
        
        print(f"找到 {len(urls)} 个URL")
        
        downloaded = 0
        for i, url in enumerate(urls[:5]):
            if downloaded >= 2:
                break
            try:
                r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                if r.status_code == 200 and len(r.content) > 5000:
                    ext = '.jpg' if 'jpeg' in r.headers.get('content-type', '') or 'jpg' in r.headers.get('content-type', '') else '.png'
                    path = f'images/{name}_{downloaded+1}{ext}'
                    with open(path, 'wb') as f:
                        f.write(r.content)
                    print(f"  下载 {path} ({len(r.content)} bytes)")
                    downloaded += 1
            except Exception as e:
                print(f"  失败: {e}")
        
        results[name] = downloaded
        page.close()
    
    browser.close()

print(f"\n=== 完成 ===")
for k, v in results.items():
    print(f"{k}: {v} 张")
