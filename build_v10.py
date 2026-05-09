
import json
import os

# Load data
with open('all-news.json') as f:
    data = json.load(f)
news = data['news']

with open('hd-images.json') as f:
    hd_images = json.load(f)

with open('image-map.json') as f:
    img_map = json.load(f)['real_images']

themes = {
    'finance': ('💰', '大公司 / 财经要闻'),
    'tech': ('🤖', 'AI / 科技'),
    'medical': ('🏥', '医疗健康'),
    'education': ('📚', '教育科技'),
    'aerospace': ('🚀', '航空航天'),
    'products': ('📱', '产品 / 消费电子'),
    'auto': ('🚗', '汽车 / 出行'),
    'vc': ('🏢', '创投 / 商业'),
}

def get_image_url(key, idx):
    section_map = img_map.get(key, {})
    real_url = section_map.get(str(idx))
    if real_url:
        return real_url
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
    <img src='{img_url}' alt="{item['title']}" class='card-image' loading='lazy'>
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
    icon, title = theme
    cards = '\n'.join([card(item, i, f'{key}-grid', get_image_url(key, i)) for i, item in enumerate(items)])
    return f"""
<section id='{key}' class='news-section'>
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

item_images = {}
for key in themes:
    item_images[key] = {}
    for i, item in enumerate(news.get(key, [])):
        item_images[key][i] = get_image_url(key, i)

news_json = json.dumps(news, ensure_ascii=False)
item_img_json = json.dumps(item_images, ensure_ascii=False)

css = """
* { margin: 0; padding: 0; box-sizing: border-box; }
:root { --bg: #f8f9fa; --surface: #ffffff; --text: #1a1a2e; --text-secondary: #5a5a7a; --text-muted: #8a8aa0; --accent: #6366f1; --accent-light: #818cf8; --border: rgba(0,0,0,0.06); --shadow: 0 1px 3px rgba(0,0,0,0.08); --shadow-lg: 0 10px 40px rgba(0,0,0,0.12); --radius: 16px; }
.dark { --bg: #0f0f1a; --surface: #1a1a2e; --text: #e8e8f0; --text-secondary: #a0a0b8; --text-muted: #707090; --accent: #818cf8; --accent-light: #a5b4fc; --border: rgba(255,255,255,0.06); --shadow: 0 1px 3px rgba(0,0,0,0.3); --shadow-lg: 0 10px 40px rgba(0,0,0,0.4); }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; transition: background 0.3s, color 0.3s; }

/* Navbar */
.navbar { position: fixed; top: 0; left: 0; right: 0; background: rgba(248,249,250,0.9); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); z-index: 1000; }
.dark .navbar { background: rgba(15,15,26,0.9); }
.nav-inner { max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: center; height: 60px; padding: 0 24px; position: relative; }
.logo { position: absolute; left: 24px; font-size: 1.25rem; font-weight: 800; color: var(--accent); letter-spacing: -0.02em; }
.nav-links { display: flex; gap: 28px; align-items: center; }
.nav-links a { color: var(--text-secondary); text-decoration: none; font-size: 0.875rem; font-weight: 500; white-space: nowrap; transition: color 0.2s; position: relative; }
.nav-links a:hover { color: var(--accent); }
.nav-links a::after { content: ''; position: absolute; bottom: -6px; left: 50%; transform: translateX(-50%); width: 0; height: 2px; background: var(--accent); border-radius: 1px; transition: width 0.3s; }
.nav-links a:hover::after { width: 100%; }
.theme-btn { position: absolute; right: 24px; background: none; border: none; font-size: 1.25rem; cursor: pointer; padding: 8px; border-radius: 50%; transition: transform 0.2s, background 0.2s; }
.theme-btn:hover { transform: scale(1.1); background: var(--border); }

/* Hero */
.hero { padding: 140px 24px 80px; text-align: center; max-width: 800px; margin: 0 auto; }
.hero-badge { display: inline-block; padding: 8px 20px; background: linear-gradient(135deg, var(--accent), var(--accent-light)); color: white; font-size: 0.75rem; font-weight: 700; border-radius: 100px; margin-bottom: 24px; letter-spacing: 0.05em; }
.hero h1 { font-size: clamp(2.2rem, 5vw, 3.5rem); font-weight: 800; line-height: 1.15; margin-bottom: 16px; letter-spacing: -0.03em; }
.hero p { color: var(--text-secondary); font-size: 1.15rem; max-width: 500px; margin: 0 auto 32px; }
.hero-stats { display: flex; justify-content: center; gap: 48px; }
.stat { text-align: center; }
.stat-number { display: block; font-size: 2.5rem; font-weight: 800; color: var(--accent); line-height: 1; }
.stat-label { font-size: 0.875rem; color: var(--text-muted); margin-top: 4px; }

/* Sections */
.news-section { max-width: 1200px; margin: 0 auto; padding: 48px 24px; }
.section-header { display: flex; align-items: center; gap: 12px; margin-bottom: 32px; }
.section-icon { font-size: 1.75rem; }
.section-header h2 { font-size: 1.5rem; font-weight: 700; color: var(--text); }

/* Grid */
.news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 24px; }
@media (max-width: 768px) { .news-grid { grid-template-columns: 1fr; } }

/* Cards */
.news-card { background: var(--surface); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); border: 1px solid var(--border); transition: transform 0.3s ease, box-shadow 0.3s ease; cursor: pointer; }
.news-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); }
.card-image-wrapper { position: relative; width: 100%; height: 0; padding-bottom: 56.25%; overflow: hidden; background: linear-gradient(135deg, var(--accent), var(--accent-light)); }
.card-image { position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; object-position: center; transition: transform 0.5s ease; }
.news-card:hover .card-image { transform: scale(1.05); }
.card-badge { position: absolute; top: 12px; left: 12px; padding: 4px 12px; background: linear-gradient(135deg, #ff4757, #ff6348); color: white; font-size: 0.7rem; font-weight: 700; border-radius: 100px; z-index: 2; }
.card-badge.hot { background: linear-gradient(135deg, #ff4757, #ff6348); }
.card-badge.new { background: linear-gradient(135deg, var(--accent), var(--accent-light)); }
.card-body { padding: 24px; }
.card-body h3 { font-size: 1.1rem; font-weight: 700; line-height: 1.4; margin-bottom: 10px; color: var(--text); }
.card-body p { font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6; margin-bottom: 16px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.card-meta { display: flex; justify-content: space-between; align-items: center; font-size: 0.8rem; color: var(--text-muted); }
.card-link { color: var(--accent); font-weight: 600; }

/* Modal */
.modal-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); backdrop-filter: blur(12px); z-index: 2000; align-items: center; justify-content: center; padding: 24px; opacity: 0; transition: opacity 0.3s; }
.modal-overlay.active { display: flex; opacity: 1; }
.modal-box { background: var(--surface); border-radius: 24px; max-width: 720px; width: 100%; max-height: 90vh; overflow-y: auto; position: relative; box-shadow: 0 25px 80px rgba(0,0,0,0.3); transform: scale(0.95); transition: transform 0.3s; }
.modal-overlay.active .modal-box { transform: scale(1); }
.modal-close { position: absolute; top: 20px; right: 20px; width: 44px; height: 44px; border-radius: 50%; background: rgba(255,255,255,0.9); border: none; font-size: 1.25rem; cursor: pointer; z-index: 10; display: flex; align-items: center; justify-content: center; color: #333; box-shadow: 0 2px 8px rgba(0,0,0,0.15); transition: transform 0.2s; }
.modal-close:hover { transform: rotate(90deg); }
.modal-img { width: 100%; height: 320px; object-fit: cover; object-position: center; border-radius: 24px 24px 0 0; display: block; }
.modal-body { padding: 40px; }
.modal-body h2 { font-size: 1.6rem; font-weight: 800; line-height: 1.3; margin-bottom: 12px; color: var(--text); }
.modal-body .meta { color: var(--text-muted); margin-bottom: 24px; font-size: 0.9rem; }
.modal-body .content { line-height: 1.9; color: var(--text-secondary); font-size: 1rem; }
.modal-body .content p { margin-bottom: 16px; }
@media (max-width: 768px) { .modal-body { padding: 24px; } .modal-img { height: 220px; } .modal-box { border-radius: 20px; } }

/* Footer */
.footer { text-align: center; padding: 60px 24px; color: var(--text-muted); font-size: 0.85rem; border-top: 1px solid var(--border); margin-top: 40px; }

/* Mobile */
@media (max-width: 768px) {
  .nav-inner { padding: 0 16px; }
  .logo { left: 16px; font-size: 1.1rem; }
  .theme-btn { right: 16px; }
  .nav-links { gap: 16px; }
  .nav-links a { font-size: 0.8rem; }
  .hero { padding: 120px 16px 60px; }
  .hero-stats { gap: 32px; }
  .news-section { padding: 32px 16px; }
}
"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache">
<title>今日资讯 v10.0 - Daily News</title>
<style>
{css}
</style>
</head>
<body>

<nav class="navbar">
  <div class="nav-inner">
    <div class="logo">📰 今日资讯</div>
    <div class="nav-links">
      <a href="#hero">首页</a>
      <a href="#finance">财经</a>
      <a href="#tech">科技</a>
      <a href="#medical">医疗</a>
      <a href="#education">教育</a>
      <a href="#aerospace">航天</a>
      <a href="#products">产品</a>
      <a href="#auto">出行</a>
    </div>
    <button class="theme-btn" id="themeBtn">🌙</button>
  </div>
</nav>

<section class="hero" id="hero">
  <div class="hero-badge">实时更新</div>
  <h1>洞察行业脉搏<br>掌握全球热点</h1>
  <p>2025年5月8日 · 9大行业 · 27条精选资讯</p>
  <div class="hero-stats">
    <div class="stat"><span class="stat-number">9</span><span class="stat-label">行业分类</span></div>
    <div class="stat"><span class="stat-number">27</span><span class="stat-label">精选资讯</span></div>
  </div>
</section>

{'\n'.join(sections_html)}

<div class="modal-overlay" id="modalOverlay">
  <div class="modal-box">
    <button class="modal-close" id="modalClose">✕</button>
    <img class="modal-img" id="modalImg" src="" alt="">
    <div class="modal-body">
      <h2 id="modalTitle"></h2>
      <div class="meta" id="modalMeta"></div>
      <div class="content" id="modalContent"></div>
    </div>
  </div>
</div>

<footer class="footer">
  <p>数据来源：36氪、少数派、澎湃新闻等 | 仅供个人学习参考</p>
</footer>

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
    var item = newsData[key][idx];
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

with open('index.html', 'w') as f:
    f.write(html)

print(f'Generated: {len(html)} bytes ({len(html)/1024:.1f} KB)')
