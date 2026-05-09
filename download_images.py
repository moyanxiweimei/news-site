
import asyncio
from playwright.async_api import async_playwright
import os
import urllib.request
import ssl

# 忽略SSL验证
ssl._create_default_https_context = ssl._create_unverified_context

async def download_image(url, filepath):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"  下载失败: {e}")
        return False

async def search_and_download(keyword, category, count=4):
    print(f"\n=== 搜索: {keyword} ===")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # 无界面模式更快
        context = await browser.new_context()
        page = await context.new_page()
        
        # 百度图片搜索
        search_url = f"https://image.baidu.com/search/index?tn=baiduimage&word={keyword}"
        await page.goto(search_url)
        await page.wait_for_timeout(3000)
        
        # 提取真实图片URL
        images = await page.query_selector_all('img')
        img_urls = []
        for img in images:
            src = await img.get_attribute('src') or await img.get_attribute('data-src')
            if src and 'baidu.com/it/u=' in src and src not in img_urls:
                img_urls.append(src)
        
        print(f"找到 {len(img_urls)} 张候选图片")
        
        # 下载前count张
        downloaded = []
        for i, url in enumerate(img_urls[:count]):
            filepath = f'/Users/maxiaoxu/.openclaw/workspace/news-site/images/{category}_{i+1}.jpg'
            print(f"  下载 {category}_{i+1}.jpg ...", end="")
            success = await download_image(url, filepath)
            if success:
                size = os.path.getsize(filepath)
                print(f" 成功 ({size} bytes)")
                downloaded.append(filepath)
            if len(downloaded) >= count:
                break
        
        await browser.close()
        return downloaded

async def main():
    os.makedirs('/Users/maxiaoxu/.openclaw/workspace/news-site/images', exist_ok=True)
    
    # 三个主题各下载4张
    results = {}
    results['education'] = await search_and_download('教育', 'education', 4)
    results['medical'] = await search_and_download('医疗', 'medical', 4)
    results['aerospace'] = await search_and_download('航空航天', 'aerospace', 4)
    
    print("\n=== 下载完成 ===")
    for cat, files in results.items():
        print(f"{cat}: {len(files)} 张图片")
        for f in files:
            print(f"  - {os.path.basename(f)}")

if __name__ == "__main__":
    asyncio.run(main())
