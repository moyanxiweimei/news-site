
import asyncio
from playwright.async_api import async_playwright
import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

async def download_image(url, filepath, min_size=15000):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read()
            if len(data) < min_size:
                return False, f"too small ({len(data)} bytes)"
            with open(filepath, 'wb') as f:
                f.write(data)
        return True, len(data)
    except Exception as e:
        return False, str(e)

async def search_baidu_real(keyword, category, count=4):
    print(f"\n=== 搜索: {keyword} ===")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        search_url = f"https://image.baidu.com/search/index?tn=baiduimage&word={keyword}"
        await page.goto(search_url)
        await page.wait_for_selector('img', timeout=10000)
        await page.wait_for_timeout(3000)
        
        # 滚动页面加载更多图片
        for _ in range(3):
            await page.evaluate('window.scrollBy(0, 800)')
            await page.wait_for_timeout(1500)
        
        # 提取真实图片URL（过滤掉logo和图标）
        img_urls = await page.evaluate('''() => {
            const urls = [];
            document.querySelectorAll('img').forEach(img => {
                const src = img.getAttribute('data-src') || img.src;
                if (src && src.includes('baidu.com') && src.includes('it/u=')) {
                    // 替换小尺寸参数为大尺寸
                    let bigUrl = src
                        .replace(/size=f\d+,\d+/, '')
                        .replace(/w=\d+/, 'w=800')
                        .replace(/h=\d+/, 'h=600');
                    if (!urls.includes(bigUrl)) urls.push(bigUrl);
                }
            });
            return urls.slice(0, 30);
        }''')
        
        print(f"提取到 {len(img_urls)} 个候选URL")
        
        downloaded = []
        skip_count = 0
        for url in img_urls:
            if len(downloaded) >= count:
                break
            filepath = f'/Users/maxiaoxu/.openclaw/workspace/news-site/images/{category}_{len(downloaded)+1}.jpg'
            print(f"  下载 {category}_{len(downloaded)+1}.jpg ...", end="")
            success, info = await download_image(url, filepath, min_size=20000)
            if success:
                # 验证不是logo（通过检查文件大小，logo通常很小）
                print(f" 成功 ({info} bytes)")
                downloaded.append(filepath)
            else:
                print(f" 跳过 ({info})")
                skip_count += 1
                if skip_count > 25:
                    print("  跳过太多，停止")
                    break
        
        await browser.close()
        return downloaded

async def main():
    os.makedirs('/Users/maxiaoxu/.openclaw/workspace/news-site/images', exist_ok=True)
    
    # 重新下载，覆盖之前的小图标
    results = {}
    results['education'] = await search_baidu_real('教育', 'education', 4)
    results['medical'] = await search_baidu_real('医疗', 'medical', 4)
    results['aerospace'] = await search_baidu_real('航空航天', 'aerospace', 4)
    
    print("\n=== 最终结果 ===")
    for cat, files in results.items():
        print(f"{cat}: {len(files)} 张")
        for f in files:
            size = os.path.getsize(f)
            print(f"  - {os.path.basename(f)} ({size} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
