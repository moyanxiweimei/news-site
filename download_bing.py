
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
            if len(data) < 5000:  # 小于5KB肯定是缩略图
                return False, "too small"
            with open(filepath, 'wb') as f:
                f.write(data)
        return True, len(data)
    except Exception as e:
        return False, str(e)

async def search_bing(keyword, category, count=4):
    print(f"\n=== 必应搜索: {keyword} ===")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = await context.new_page()
        
        # Bing图片搜索
        search_url = f"https://www.bing.com/images/search?q={keyword}"
        await page.goto(search_url)
        await page.wait_for_timeout(4000)
        
        # 获取大图URL - Bing用的是murl参数
        images = await page.query_selector_all('.iusc, .mimg')
        img_urls = []
        for img in images:
            # 尝试多种属性
            for attr in ['m', 'data-src', 'src']:
                val = await img.get_attribute(attr)
                if val and val.startswith('http') and 'bing' not in val:
                    if val not in img_urls:
                        img_urls.append(val)
                    break
        
        print(f"找到 {len(img_urls)} 张候选")
        
        downloaded = []
        for i, url in enumerate(img_urls):
            if len(downloaded) >= count:
                break
            filepath = f'/Users/maxiaoxu/.openclaw/workspace/news-site/images/{category}_{len(downloaded)+1}.jpg'
            print(f"  尝试下载 {category}_{len(downloaded)+1} ...", end="")
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
    
    # 重新下载，覆盖之前的小文件
    results = {}
    results['education'] = await search_bing('education classroom', 'education', 4)
    results['medical'] = await search_bing('medical hospital doctor', 'medical', 4)
    results['aerospace'] = await search_bing('aerospace space rocket', 'aerospace', 4)
    
    print("\n=== 全部完成 ===")
    for cat, files in results.items():
        print(f"{cat}: {len(files)} 张")

if __name__ == "__main__":
    asyncio.run(main())
