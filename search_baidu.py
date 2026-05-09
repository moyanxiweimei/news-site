
import asyncio
from playwright.async_api import async_playwright
import os

async def search_baidu_images():
    os.makedirs('/Users/maxiaoxu/.openclaw/workspace/news-site/images', exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # 有界面，你可以看到
        context = await browser.new_context()
        page = await context.new_page()
        
        # 打开百度图片搜索 - 教育
        print("正在打开百度图片搜索 教育...")
        await page.goto("https://image.baidu.com/search/index?tn=baiduimage&word=教育")
        await page.wait_for_timeout(3000)
        
        # 截图看看效果
        await page.screenshot(path='/Users/maxiaoxu/.openclaw/workspace/news-site/baidu_edu.png')
        print("已截图: baidu_edu.png")
        
        # 提取图片URL（百度图片用的是data-src或src）
        images = await page.query_selector_all('img')
        img_urls = []
        for img in images[:20]:  # 前20张
            src = await img.get_attribute('src') or await img.get_attribute('data-src')
            if src and src.startswith('http'):
                img_urls.append(src)
        
        print(f"找到 {len(img_urls)} 张图片URL")
        for i, url in enumerate(img_urls[:5]):
            print(f"  {i+1}. {url[:80]}...")
        
        await browser.close()
        return img_urls

if __name__ == "__main__":
    urls = asyncio.run(search_baidu_images())
