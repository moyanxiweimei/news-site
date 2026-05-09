
import json
import base64
import os

# Load data
with open('all-news.json') as f:
    data = json.load(f)
news = data['news']
images = data['images']

# Load real image mapping
with open('image-map.json') as f:
    img_map = json.load(f)['real_images']

# Load hd-images for fallback
with open('hd-images.json') as f:
    hd_images = json.load(f)

themes = {
    'finance': ('💰', '大公司 / 财经要闻', False),
    'tech': ('🤖', 'AI / 科技', True),
    'medical': ('🏥', '医疗健康', False),
    'education': ('📚', '教育科技', True),
    'aerospace': ('🚀', '航空航天', False),
    'products': ('📱', '产品 / 消费电子', True),
    'auto': ('🚗', '汽车 / 出行', False),
    'vc': ('🏢', '创投 / 商业', True),
}

def get_image_url(key, idx, item):
    """Get image URL - prefer real photo, fallback to base64 gradient"""
    # Check if there's a real image for this specific item
    section_map = img_map.get(key, {})
    real_url = section_map.get(str(idx))
    if real_url:
        return real_url
    # Fallback to base64 gradient
    return f"data:image/jpeg;base64,{hd_images.get(key, '')}"

def card(item, idx, grid, img_url):
    feat = ' featured' if idx == 0 else ''
    badge = ''
    if item.get('badge'):
        cls = 'hot' if item['badge'] in ['热点','重磅'] else ('new' if item['badge'] in ['融资','免签'] else '')
        badge = f"<div class='card-badge {cls}'>{item['badge']}</div>"
    return f"""
<article class='news-card{feat}' data-grid='{grid}' data-index='{idx}'>
  <div class='card-image-wrapper'>
    <img src='{img_url}' alt="{item['title']}" class='card-image'>
    {badge}
  </div>
  <div class='card-body'>
    <h3>{item['title']}</h3>
    <p>{item['summary']}</p>
    <div class='card-meta'>
      <span>{item.get('source','资讯')} · {item['date']}</span>
      <span class='card-link'>查看详情 →</span>
    </div>
  </div>
</article>"""

def section(key, items, theme):
    icon, title, dark = theme
    d = ' dark' if dark else ''
    cards = '\n'.join([card(item, i, f'{key}-grid', get_image_url(key, i, item)) for i, item in enumerate(items)])
    return f"""
<section id='{key}' class='news-section{d}'>
  <div class='section-header'>
    <span class='section-icon'>{icon}</span>
    <h2>{title}</h2>
  </div>
  <div class='news-grid' id='{key}-grid'>
    {cards}
  </div>
</section>"""

sections_html = []
for key in ['finance','tech','medical','education','aerospace','products','auto','vc']:
    items = news.get(key, [])
    if items:
        sections_html.append(section(key, items, themes[key]))

with open('style.css') as f:
    css = f.read()

# Build per-item image mapping for JS
item_images = {}
for key in themes:
    item_images[key] = {}
    for i, item in enumerate(news.get(key, [])):
        item_images[key][i] = get_image_url(key, i, item)

news_json = json.dumps(news, ensure_ascii=False)
item_img_json = json.dumps(item_images, ensure_ascii=False)

parts = []
parts.append("<!DOCTYPE html><html lang='zh-CN'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='Cache-Control' content='no-cache'><title>今日资讯 v9.0 - Daily News</title><style>")
parts.append(css)

# Add modal styles
parts.append("""
/* ===== Modal Overlay ===== */
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); backdrop-filter: blur(8px); z-index: 200; display: none; align-items: center; justify-content: center; padding: 20px; }
.modal-overlay.active { display: flex; }
.modal-box { background: var(--card-bg); border-radius: 20px; max-width: 700px; width: 100%; max-height: 85vh; overflow-y: auto; position: relative; box-shadow: 0 20px 60px rgba(0,0,0,0.3); }
.modal-close { position: absolute; top: 16px; right: 16px; width: 36px; height: 36px; border-radius: 50%; background: rgba(128,128,128,0.2); border: none; font-size: 1.2rem; cursor: pointer; z-index: 10; display: flex; align-items: center; justify-content: center; color: var(--text2); }
.modal-img { width: 100%; height: 280px; object-fit: cover; border-radius: 20px 20px 0 0; display: block; }
.modal-body { padding: 32px; }
.modal-body h2 { font-size: 1.4rem; margin-bottom: 12px; }
.modal-body .meta { color: var(--text2); margin-bottom: 20px; font-size: 0.9rem; }
.modal-body .content { line-height: 1.8; color: var(--text2); }
.modal-body .content p { margin-bottom: 12px; }
@media (max-width: 768px) { .modal-body { padding: 24px; } .modal-img { height: 200px; } }
</style></head><body>""")

# Navbar
parts.append("""
<nav class='navbar'><div class='nav-inner'>
  <div class='logo'>📰 今日资讯</div>
  <div class='nav-links'>
    <a href='#hero' class='active'>首页</a>
    <a href='#finance'>财经</a>
    <a href='#tech'>科技</a>
    <a href='#medical'>医疗</a>
    <a href='#education'>教育</a>
    <a href='#aerospace'>航天</a>
    <a href='#products'>产品</a>
    <a href='#auto'>出行</a>
  </div>
  <button class='theme-btn' id='themeBtn'>🌙</button>
</div></nav>""")

# Hero
parts.append("""
<section id='hero' class='hero'>
  <div class='hero-content'>
    <div class='hero-badge'>实时更新</div>
    <h1><span class='gradient-text'>洞察行业脉搏</span><br>掌握全球热点</h1>
    <p>2025年5月8日 · 9大行业 · 27条精选资讯</p>
    <div class='hero-stats'>
      <div class='stat'><span class='stat-number'>9</span><span class='stat-label'>行业</span></div>
      <div class='stat'><span class='stat-number'>27</span><span class='stat-label'>资讯</span></div>
    </div>
  </div>
</section>""")

# Sections
parts.append('\n'.join(sections_html))

# Modal
parts.append("""
<div class='modal-overlay' id='modalOverlay'>
  <div class='modal-box'>
    <button class='modal-close' id='modalClose'>✕</button>
    <img class='modal-img' id='modalImg' src='' alt=''>
    <div class='modal-body'>
      <h2 id='modalTitle'></h2>
      <div class='meta' id='modalMeta'></div>
      <div class='content' id='modalContent'></div>
    </div>
  </div>
</div>""")

# Footer
parts.append("""
<footer class='footer'>
  <div class='footer-content'>
    <div class='footer-logo'>📰 今日资讯</div>
    <p class='footer-desc'>精选全球热点，洞察行业趋势</p>
    <div class='footer-divider'></div>
    <p class='footer-copyright'>数据来源：36氪、少数派、澎湃新闻等 | 仅供个人学习参考</p>
  </div>
</footer>""")

# JS
js = f"""
<script>
// Theme toggle
document.getElementById('themeBtn').addEventListener('click', function() {{
    if (document.body.classList.contains('dark')) {{
        document.body.classList.remove('dark');
        this.textContent = '🌙';
    }} else {{
        document.body.classList.add('dark');
        this.textContent = '☀️';
    }}
}});

// News data
var newsData = {news_json};
var itemImages = {item_img_json};

// Modal
var modalOverlay = document.getElementById('modalOverlay');
var modalImg = document.getElementById('modalImg');
var modalTitle = document.getElementById('modalTitle');
var modalMeta = document.getElementById('modalMeta');
var modalContent = document.getElementById('modalContent');

document.querySelectorAll('.news-card').forEach(function(card) {{
    card.addEventListener('click', function() {{
        var grid = this.dataset.grid;
        var idx = parseInt(this.dataset.index);
        var key = grid.replace('-grid', '');
        var items = newsData[key];
        var item = items[idx];
        if (!item) return;
        
        modalImg.src = itemImages[key][idx];
        modalImg.alt = item.title;
        modalTitle.textContent = item.title;
        modalMeta.textContent = (item.source || '资讯') + ' · ' + item.date;
        modalContent.innerHTML = '<p>' + (item.detail || item.summary).replace(/\\n\\n/g, '</p><p>').replace(/\\n/g, '<br>') + '</p>';
        
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }});
}});

document.getElementById('modalClose').addEventListener('click', function() {{
    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
}});
modalOverlay.addEventListener('click', function(e) {{
    if (e.target === this) {{
        this.classList.remove('active');
        document.body.style.overflow = '';
    }}
}});
</script>
</body>
</html>"""

parts.append(js)

html = '\n'.join(parts)

with open('index.html', 'w') as f:
    f.write(html)

print(f'Generated: {len(html)} bytes ({len(html)/1024:.1f} KB)')
print('Real images used:')
for key, items in item_images.items():
    for idx, url in items.items():
        if not url.startswith('data:'):
            print(f'  {key}[{idx}]: {url}')
