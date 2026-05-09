
import json

with open('all-news.json') as f:
    data = json.load(f)

news = data['news']
images = data['images']

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

with open('style.css') as f:
    css = f.read()

def card(item, idx, grid, img_b64):
    feat = ' featured' if idx == 0 else ''
    badge = ''
    if item.get('badge'):
        cls = 'hot' if item['badge'] in ['热点','重磅'] else ('new' if item['badge'] in ['融资','免签'] else '')
        badge = f"<div class='card-badge {cls}'>{item['badge']}</div>"
    src = f"data:image/jpeg;base64,{img_b64}"
    return f"""
<article class='news-card{feat}' data-grid='{grid}' data-index='{idx}'>
  <div class='card-image-wrapper'>
    <img src='{src}' alt="{item['title']}" class='card-image'>
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

def section(key, items, theme, img_b64):
    icon, title, dark = theme
    d = ' dark' if dark else ''
    cards = '\n'.join([card(item, i, f'{key}-grid', img_b64) for i, item in enumerate(items)])
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
        img_name = {'finance':'finance','tech':'tech','medical':'medical','education':'education','aerospace':'aerospace','products':'products','auto':'auto','vc':'vc'}[key]
        sections_html.append(section(key, items, themes[key], images.get(img_name, '')))

news_json = json.dumps(news, ensure_ascii=False)
img_map = {k: f"data:image/jpeg;base64,{images.get({'finance':'finance','tech':'tech','medical':'medical','education':'education','aerospace':'aerospace','products':'products','auto':'auto','vc':'vc'}[k], '')}" for k in themes}
img_json = json.dumps(img_map, ensure_ascii=False)

extra_css = """
/* ===== Modal Overlay ===== */
.modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.7); backdrop-filter: blur(10px); z-index: 200; display: none; align-items: center; justify-content: center; padding: 20px; opacity: 0; transition: opacity 0.3s ease; }
.modal-overlay.active { display: flex; opacity: 1; }
.modal-container { background: var(--card-bg); border-radius: 24px; max-width: 800px; width: 100%; max-height: 90vh; overflow-y: auto; position: relative; transform: scale(0.9); transition: transform 0.3s cubic-bezier(0.23, 1, 0.32, 1); box-shadow: 0 25px 80px rgba(0,0,0,0.3); }
.modal-overlay.active .modal-container { transform: scale(1); }
.modal-close { position: absolute; top: 20px; right: 20px; width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.1); border: none; color: var(--text); font-size: 1.2rem; cursor: pointer; z-index: 10; display: flex; align-items: center; justify-content: center; transition: background 0.3s; }
.modal-close:hover { background: rgba(255,255,255,0.2); transform: rotate(90deg); }
.modal-image-wrapper { width: 100%; height: 280px; overflow: hidden; border-radius: 24px 24px 0 0; position: relative; }
.modal-image-wrapper img { width: 100%; height: 100%; object-fit: cover; }
.modal-image-wrapper::after { content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 50%; background: linear-gradient(to top, var(--card-bg), transparent); }
.modal-content { padding: 40px; }
.modal-badge { display: inline-block; padding: 6px 16px; background: linear-gradient(135deg, var(--accent), #a855f7); color: white; font-size: 0.8rem; font-weight: 700; border-radius: 100px; margin-bottom: 16px; }
.modal-title { font-size: 1.6rem; font-weight: 800; line-height: 1.3; margin-bottom: 12px; }
.modal-meta { font-size: 0.9rem; color: var(--text2); margin-bottom: 24px; }
.modal-body { line-height: 1.9; color: var(--text2); font-size: 1rem; }
.modal-body p { margin-bottom: 16px; }
.modal-link { display: inline-flex; align-items: center; gap: 8px; padding: 12px 24px; background: linear-gradient(135deg, var(--accent), #a855f7); color: white; text-decoration: none; border-radius: 100px; font-weight: 700; margin-top: 24px; transition: transform 0.3s; }
.modal-link:hover { transform: translateX(4px); }
@media (max-width: 768px) { .modal-content { padding: 24px; } .modal-image-wrapper { height: 200px; } .modal-title { font-size: 1.3rem; } }
"""

# Build HTML parts
parts = []
parts.append("<!DOCTYPE html><html lang='zh-CN'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><meta http-equiv='Cache-Control' content='no-cache'><title>今日资讯 v5.0 - Daily News</title><style>")
parts.append(css)
parts.append(extra_css)
parts.append("</style></head><body>")

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
</div></nav>
""")

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
</section>
""")

# Sections
parts.append('\n'.join(sections_html))

# Modal
parts.append("""
<div class='modal-overlay' id='modalOverlay'>
  <div class='modal-container'>
    <button class='modal-close' id='modalClose'>✕</button>
    <div class='modal-image-wrapper'>
      <img src='' alt='' id='modalImage'>
    </div>
    <div class='modal-content'>
      <div class='modal-badge' id='modalBadge'>新闻</div>
      <h2 class='modal-title' id='modalTitle'></h2>
      <div class='modal-meta' id='modalMeta'></div>
      <div class='modal-body' id='modalBody'></div>
      <a href='#' class='modal-link' id='modalLink' target='_blank'>查看原文 →</a>
    </div>
  </div>
</div>
""")

# Footer
parts.append("""
<footer class='footer'>
  <div class='footer-content'>
    <div class='footer-logo'>📰 今日资讯</div>
    <p class='footer-desc'>精选全球热点，洞察行业趋势</p>
    <div class='footer-divider'></div>
    <p class='footer-copyright'>数据来源：36氪、少数派、澎湃新闻等 | 仅供个人学习参考</p>
  </div>
</footer>
""")

# JS
js = f"""
<script>
// Theme toggle
var themeBtn = document.getElementById('themeBtn');
var body = document.body;
themeBtn.addEventListener('click', function() {{
    if (body.classList.contains('dark')) {{
        body.classList.remove('dark');
        themeBtn.textContent = '🌙';
    }} else {{
        body.classList.add('dark');
        themeBtn.textContent = '☀️';
    }}
}});

// News data
var newsData = {news_json};
var sectionImages = {img_json};

// Modal
var modalOverlay = document.getElementById('modalOverlay');
var modalImage = document.getElementById('modalImage');
var modalTitle = document.getElementById('modalTitle');
var modalMeta = document.getElementById('modalMeta');
var modalBody = document.getElementById('modalBody');
var modalLink = document.getElementById('modalLink');
var modalBadge = document.getElementById('modalBadge');

document.querySelectorAll('.news-card').forEach(function(card) {{
    card.addEventListener('click', function() {{
        var grid = this.dataset.grid;
        var idx = parseInt(this.dataset.index);
        var key = grid.replace('-grid', '');
        var items = newsData[key];
        var item = items[idx];
        if (!item) return;
        
        modalImage.src = sectionImages[key];
        modalImage.alt = item.title;
        modalTitle.textContent = item.title;
        modalMeta.textContent = (item.source || '资讯') + ' · ' + item.date;
        modalBody.innerHTML = '<p>' + (item.detail || item.summary).replace(/\\n\\n/g, '</p><p>').replace(/\\n/g, '<br>') + '</p>';
        modalLink.href = item.link || '#';
        modalBadge.textContent = item.badge || '新闻';
        
        modalOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }});
}});

// Close modal
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
"""

parts.append(js)
parts.append("</body></html>")

html = '\n'.join(parts)

with open('index.html', 'w') as f:
    f.write(html)

print(f'Generated: {len(html)} bytes ({len(html)/1024:.1f} KB)')
