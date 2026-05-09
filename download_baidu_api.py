
import urllib.request
import urllib.parse
import json
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

def download_image(url, filepath):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read()
            if len(data) < 8000:
                return False, f"too small ({len(data)} bytes)"
            with open(filepath, 'wb') as f:
                f.write(data)
        return True, len(data)
    except Exception as e:
        return False, str(e)

def search_baidu_json(keyword, category, count=4):
    print(f"\n=== 百度API搜索: {keyword} ===")
    
    encoded_word = urllib.parse.quote(keyword)
    url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word={encoded_word}&pn=0&rn=30"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://image.baidu.com/'
    }
    
    req = urllib.request.Request(url, headers=headers)
    downloaded = []
    
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            data = json.loads(response.read().decode('utf-8'))
        
        images = data.get('data', [])
        print(f"API返回 {len(images)} 张图片信息")
        
        for img in images:
            if len(downloaded) >= count:
                break
            
            # 尝试多个字段获取大图URL
            img_url = img.get('thumbURL') or img.get('middleURL') or img.get('objURL') or img.get('hoverURL')
            if not img_url or not img_url.startswith('http'):
                continue
            
            filepath = f'/Users/maxiaoxu/.openclaw/workspace/news-site/images/{category}_{len(downloaded)+1}.jpg'
            print(f"  下载 {category}_{len(downloaded)+1}.jpg ...", end="")
            success, info = download_image(img_url, filepath)
            if success:
                print(f" 成功 ({info} bytes)")
                downloaded.append(filepath)
            else:
                print(f" 失败 ({info})")
                
    except Exception as e:
        print(f"API请求失败: {e}")
    
    return downloaded

if __name__ == "__main__":
    os.makedirs('/Users/maxiaoxu/.openclaw/workspace/news-site/images', exist_ok=True)
    
    results = {}
    results['education'] = search_baidu_json('教育', 'education', 4)
    results['medical'] = search_baidu_json('医疗', 'medical', 4)
    results['aerospace'] = search_baidu_json('航空航天', 'aerospace', 4)
    
    print("\n=== 完成 ===")
    for cat, files in results.items():
        print(f"{cat}: {len(files)} 张")
        for f in files:
            print(f"  - {os.path.basename(f)}")
