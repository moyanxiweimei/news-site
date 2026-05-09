
import asyncio
from playwright.async_api import async_playwright
import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

async def download_image(url, filepath):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read()
            if len(data) < 10000:
                return False, f"too small ({len(data)} bytes)"
            with open(filepath, 'wb') as f:
                f.write(data)
        return True, len(data)
    except Exception as e:
        return False, str(e)

async def search_baidu_visible(keyword, category, count=4):
    print(f"\n=== 打开浏览器搜索: {keyword} ===")
    
    async with async_playwright() as p:
        # 有界面，你能看到我在操作！
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 800}
        )
        page = await context.new_page()
        
        # 访问百度图片
        search_url = f"https://image.baidu.com/search/index?tn=baiduimage&word={keyword}"
        await page.goto(search_url)
        
        # 等待图片加载
        await page.wait_for_selector('img', timeout=10000)
        await page.wait_for_timeout(3000)
        
        # 在页面内执行JS，提取百度图片的真实大图URL
        # 百度图片把数据存在pageData或initData里
        img_urls = await page.evaluate('''() => {
            const urls = [];
            // 方法1: 从window.pageData提取
            if (window.pageData && window.pageData.data) {
                for (const item of window.pageData.data) {
                    if (item.thumbURL) urls.push(item.thumbURL);
                    if (item.middleURL) urls.push(item.middleURL);
                    if (item.objURL) urls.push(item.objURL);
                }
            }
            // 方法2: 从img标签提取
            document.querySelectorAll('img').forEach(img => {
                const src = img.getAttribute('data-src') || img.src;
                if (src && src.includes('baidu.com') && !urls.includes(src)) {
                    urls.push(src);
                }
            });
            return urls.slice(0, 20);
        }''')
        
        print(f"提取到 {len(img_urls)} 个URL")
        for i, u in enumerate(img_urls[:5]):
            print(f"  {i+1}. {u[:80]}...")
        
        downloaded = []
        for i, url in enumerate(img_urls):
            if len(downloaded) >= count:
                break
            filepath = f'/Users/maxiaoxu/.openclaw/workspace/news-site/images/{category}_{len(downloaded)+1}.jpg'
            print(f"  下载 {category}_{len(downloaded)+1}.jpg ...", end="")
            success, info = await download_image(url, filepath)
            if success:
                print(f" 成功 ({info} bytes)")
                downloaded.append(filepath)
            else:
                print(f" 跳过 ({info})")
        
        await browser.close()
        return downloaded

async def main():
    os.makedirs('/Users/maxiaoxu/.openclaw/workspace/news-site/images', exist_ok=True)
    
    results = {}
    results['education'] = await search_baidu_visible('教育', 'education', 4)
    results['medical'] = await search_baidu_visible('医疗', 'medical', 4)
    results['aerospace'] = await search_baidu_visible('航空航天', 'aerospace', 4)
    
    print("\n=== 全部完成 ===")
    for cat, files in results.items():
        print(f"{cat}: {len(files)} 张")

if __name__ == "__main__":
    asyncio.run(main())
