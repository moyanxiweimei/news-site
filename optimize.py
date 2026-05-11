import re, os, json
from pathlib import Path

BASE = Path('/Users/maxiaoxu/.openclaw/workspace/news-site')

# 读取原始 HTML
with open(BASE / 'index.html', 'r') as f:
    html = f.read()

print(f"原始大小: {len(html):,} bytes ({len(html)/1024:.1f} KB)")

# 1. 提取新闻数据从 script.js
with open(BASE / 'script.js', 'r') as f:
    js = f.read()

# 提取 staticNews 数据
static_match = re.search(r'const staticNews = ({.*?});', js, re.DOTALL)
if static_match:
    static_json = static_match.group(1)
    # 修复 JSON 格式（JS 对象 -> JSON）
    static_json = re.sub(r'(\w+):', r'"\1":', static_json)
    static_json = static_json.replace("'", '"')
    try:
        static_news = json.loads(static_json)
    except:
        static_news = {}
else:
    static_news = {}

print(f"提取到板块: {list(static_news.keys()) if static_news else '无'}")

# 2. 创建优化的 HTML
# 首先找到 <body> 和 </body> 之间的内容
body_match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
if not body_match:
    print("未找到 body 内容")
    exit(1)

body_content = body_match.group(1)

# 3. 构建优化后的完整 HTML
optimized_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="今日资讯 - 聚合全球财经、科技、产品、汽车、创投、医疗、教育、航天最新动态">
<meta name="theme-color" content="#6366f1">
<meta http-equiv="Cache-Control" content="max-age=3600">
<title>今日资讯 - Daily News</title>
<style>
/* ===== CSS Variables ===== */
:root {
  --bg: #f8f9fa;
  --surface: #ffffff;
  --surface-hover: #f0f0f5;
  --text: #1a1a2e;
  --text-secondary: #5a5a7a;
  --text-muted: #8a8aa0;
  --accent: #6366f1;
  --accent-light: #818cf8;
  --accent-gradient: linear-gradient(135deg, #6366f1, #818cf8);
  --border: rgba(0,0,0,0.06);
  --shadow: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.1);
  --shadow-lg: 0 12px 40px rgba(0,0,0,0.15);
  --radius: 16px;
  --radius-sm: 12px;
  --radius-lg: 24px;
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-bounce: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.dark {
  --bg: #0f0f1a;
  --surface: #1a1a2e;
  --surface-hover: #22223a;
  --text: #e8e8f0;
  --text-secondary: #a0a0b8;
  --text-muted: #707090;
  --accent: #818cf8;
  --accent-light: #a5b4fc;
  --accent-gradient: linear-gradient(135deg, #818cf8, #a5b4fc);
  --border: rgba(255,255,255,0.06);
  --shadow: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-sm: 0 2px 8px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.4);
  --shadow-lg: 0 12px 40px rgba(0,0,0,0.5);
}

/* ===== Reset & Base ===== */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; font-size: 16px; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "PingFang SC", "Noto Sans SC", sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  transition: background 0.3s, color 0.3s;
  overflow-x: hidden;
}

/* ===== Performance: Content Visibility ===== */
.news-section { content-visibility: auto; contain-intrinsic-size: 0 500px; }

/* ===== Custom Scrollbar ===== */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--text-muted); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }
::selection { background: var(--accent); color: white; }

/* ===== Loading Skeleton ===== */
@keyframes skeleton {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
.skeleton {
  background: linear-gradient(90deg, var(--surface) 25%, var(--surface-hover) 50%, var(--surface) 75%);
  background-size: 200% 100%;
  animation: skeleton 1.5s infinite;
}

/* ===== Navbar ===== */
.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  background: rgba(248,249,250,0.85);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid var(--border);
  z-index: 1000;
  transition: var(--transition);
}
.dark .navbar { background: rgba(15,15,26,0.85); }

.nav-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  padding: 0 24px;
  position: relative;
}

.logo {
  position: absolute;
  left: 24px;
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--accent);
  letter-spacing: -0.02em;
  text-decoration: none;
  transition: var(--transition);
}
.logo:hover { transform: scale(1.05); }

.nav-links {
  display: flex;
  gap: 28px;
  align-items: center;
}

.nav-links a {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  white-space: nowrap;
  transition: color 0.2s;
  position: relative;
  padding: 4px 0;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 2px;
  background: var(--accent);
  border-radius: 1px;
  transition: width 0.3s;
}

.nav-links a:hover { color: var(--accent); }
.nav-links a:hover::after { width: 100%; }

.theme-btn {
  position: absolute;
  right: 24px;
  background: none;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  padding: 8px;
  border-radius: 50%;
  transition: var(--transition);
}

.theme-btn:hover { transform: scale(1.1) rotate(15deg); background: var(--border); }

/* ===== Hero ===== */
.hero {
  padding: 140px 24px 80px;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.hero-badge {
  display: inline-block;
  padding: 8px 20px;
  background: var(--accent-gradient);
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  border-radius: 100px;
  margin-bottom: 24px;
  letter-spacing: 0.05em;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(99,102,241,0.4); }
  50% { box-shadow: 0 0 0 12px rgba(99,102,241,0); }
}

.hero h1 {
  font-size: clamp(2.2rem, 5vw, 3.5rem);
  font-weight: 800;
  line-height: 1.15;
  margin-bottom: 16px;
  letter-spacing: -0.03em;
}

.hero p {
  color: var(--text-secondary);
  font-size: 1.15rem;
  max-width: 500px;
  margin: 0 auto 32px;
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 48px;
}

.stat-number {
  display: block;
  font-size: 2.5rem;
  font-weight: 800;
  line-height: 1;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--text-muted);
  margin-top: 4px;
}

/* ===== Sections ===== */
.news-section {
  max-width: 1200px;
  margin: 0 auto;
  padding: 48px 24px;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 32px;
}

.section-icon {
  font-size: 1.75rem;
  display: inline-block;
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
}

.section-header h2 {
  font-size: 1.5rem;
  font-weight: 700;
}

/* ===== Grid ===== */
.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 24px;
}

/* ===== Cards ===== */
.news-card {
  background: var(--surface);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  transition: var(--transition);
  cursor: pointer;
  will-change: transform;
  transform: translateZ(0);
}

.news-card:hover {
  transform: translateY(-8px) translateZ(0);
  box-shadow: var(--shadow-lg);
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%;
  overflow: hidden;
  background: var(--accent-gradient);
}

.card-image-wrapper img {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}

.news-card:hover .card-image-wrapper img {
  transform: scale(1.08);
}

.card-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 4px 12px;
  background: linear-gradient(135deg, #ff4757, #ff6348);
  color: white;
  font-size: 0.7rem;
  font-weight: 700;
  border-radius: 100px;
  z-index: 2;
  box-shadow: 0 2px 8px rgba(255,71,87,0.3);
}

.card-badge.hot { background: linear-gradient(135deg, #ff4757, #ff6348); }
.card-badge.new { background: var(--accent-gradient); }
.card-badge.major { background: linear-gradient(135deg, #ff9500, #ff6b35); }

.card-body { padding: 24px; }

.card-body h3 {
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: 10px;
  color: var(--text);
  transition: color 0.2s;
}

.news-card:hover .card-body h3 { color: var(--accent); }

.card-body p {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8rem;
  color: var(--text-muted);
}

.card-link {
  color: var(--accent);
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 4px;
  transition: gap 0.2s;
}

.news-card:hover .card-link { gap: 8px; }

/* ===== Scroll Reveal ===== */
.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

.news-grid .news-card:nth-child(1) { transition-delay: 0s; }
.news-grid .news-card:nth-child(2) { transition-delay: 0.08s; }
.news-grid .news-card:nth-child(3) { transition-delay: 0.16s; }
.news-grid .news-card:nth-child(4) { transition-delay: 0.24s; }
.news-grid .news-card:nth-child(5) { transition-delay: 0.32s; }

/* ===== Modal ===== */
.modal-overlay {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(16px);
  z-index: 2000;
  align-items: center;
  justify-content: center;
  padding: 24px;
  opacity: 0;
  transition: opacity 0.3s;
}

.modal-overlay.active {
  display: flex;
  opacity: 1;
}

.modal-box {
  background: var(--surface);
  border-radius: var(--radius-lg);
  max-width: 720px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 25px 80px rgba(0,0,0,0.3);
  transform: scale(0.9) translateY(20px);
  transition: var(--transition-bounce);
}

.modal-overlay.active .modal-box {
  transform: scale(1) translateY(0);
}

.modal-close {
  position: absolute;
  top: 20px;
  right: 20px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255,255,255,0.9);
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #333;
  box-shadow: 0 2px 12px rgba(0,0,0,0.15);
  transition: transform 0.3s, background 0.2s;
}

.modal-close:hover {
  transform: rotate(90deg) scale(1.1);
  background: #fff;
}

.modal-img {
  width: 100%;
  height: 320px;
  object-fit: cover;
  object-position: center;
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
  display: block;
}

.modal-body {
  padding: 40px;
}

.modal-body h2 {
  font-size: 1.6rem;
  font-weight: 800;
  line-height: 1.3;
  margin-bottom: 12px;
}

.modal-body .meta {
  color: var(--text-muted);
  margin-bottom: 24px;
  font-size: 0.9rem;
}

.modal-body .content {
  line-height: 1.9;
  color: var(--text-secondary);
  font-size: 1rem;
}

.modal-body .content p {
  margin-bottom: 16px;
}

.modal-badge {
  display: inline-block;
  padding: 6px 16px;
  background: var(--accent-gradient);
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
  border-radius: 100px;
  margin-bottom: 16px;
}

/* ===== Footer ===== */
.footer {
  text-align: center;
  padding: 60px 24px;
  color: var(--text-muted);
  font-size: 0.85rem;
  border-top: 1px solid var(--border);
  margin-top: 40px;
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .news-grid { grid-template-columns: 1fr; }
  .hero { padding: 120px 16px 60px; }
  .hero-stats { gap: 32px; }
  .nav-inner { padding: 0 16px; }
  .logo { left: 16px; font-size: 1.1rem; }
  .theme-btn { right: 16px; }
  .nav-links { gap: 16px; }
  .nav-links a { font-size: 0.8rem; }
  .modal-body { padding: 24px; }
  .modal-img { height: 220px; }
  .modal-box { border-radius: var(--radius); }
}
</style>
</head>
<body>
'''

# 保留原始 body 内容，但移除内联样式（因为我们已经有了）
# 移除 body 中的 <style> 标签
body_clean = re.sub(r'<style>.*?</style>', '', body_content, flags=re.DOTALL)

# 移除 base64 图片，保留结构（JS 会动态加载真实图片）
# 将 base64 图片替换为占位符或移除
body_clean = re.sub(
    r"<img src='data:image/[^']+'",
    "<img src=''",
    body_clean
)

# 移除腾讯云图片，也用 JS 动态加载
body_clean = re.sub(
    r"<img src='https://moyanxiweimei-[^']+'",
    "<img src=''",
    body_clean
)

# 添加 reveal class 到 sections
body_clean = body_clean.replace('class="news-section"', 'class="news-section reveal"')

optimized_html += body_clean

# 添加优化后的 JS
optimized_html += '''
<script>
// ===== Theme =====
const themeBtn = document.getElementById('themeBtn');
if (themeBtn) {
  themeBtn.addEventListener('click', toggleTheme);
}

function toggleTheme() {
  document.body.classList.toggle('dark');
  const isDark = document.body.classList.contains('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  if (themeBtn) themeBtn.textContent = isDark ? '☀️' : '🌙';
}

// Load saved theme
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
  document.body.classList.add('dark');
  if (themeBtn) themeBtn.textContent = '☀️';
}

// ===== Scroll Reveal =====
const observerOptions = { root: null, rootMargin: '0px', threshold: 0.1 };
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      // Unobserve after reveal for performance
      revealObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ===== Active Nav Link =====
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

function updateActiveNav() {
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    if (window.scrollY >= sectionTop - 200) {
      current = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === '#' + current) {
      link.classList.add('active');
    }
  });
}

window.addEventListener('scroll', updateActiveNav, { passive: true });

// ===== Modal =====
function openModal(title, image, meta, content, badge) {
  const overlay = document.getElementById('modalOverlay');
  const modalImg = document.getElementById('modalImg');
  const modalTitle = document.getElementById('modalTitle');
  const modalMeta = document.getElementById('modalMeta');
  const modalContent = document.getElementById('modalContent');
  const modalBadge = document.getElementById('modalBadge');
  
  if (modalImg) modalImg.src = image || '';
  if (modalTitle) modalTitle.textContent = title;
  if (modalMeta) modalMeta.textContent = meta;
  if (modalContent) modalContent.innerHTML = content;
  if (modalBadge) modalBadge.textContent = badge || '新闻';
  
  if (overlay) overlay.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const overlay = document.getElementById('modalOverlay');
  if (overlay) overlay.classList.remove('active');
  document.body.style.overflow = '';
}

// Close on overlay click
document.getElementById('modalOverlay')?.addEventListener('click', function(e) {
  if (e.target === this) closeModal();
});

// Close on Escape
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});

// ===== Card Click Events =====
document.querySelectorAll('.news-card').forEach(card => {
  card.addEventListener('click', function() {
    const title = this.querySelector('h3')?.textContent || '';
    const img = this.querySelector('img')?.src || '';
    const meta = this.querySelector('.card-meta span')?.textContent || '';
    const summary = this.querySelector('p')?.textContent || '';
    const badge = this.querySelector('.card-badge')?.textContent || '';
    
    openModal(title, img, meta, '<p>' + summary + '</p>', badge);
  });
});

// ===== Image Lazy Loading with Skeleton =====
document.querySelectorAll('.card-image-wrapper img').forEach(img => {
  if (!img.src || img.src === window.location.href) {
    img.style.display = 'none';
  }
  
  img.addEventListener('load', function() {
    this.style.display = '';
    this.parentElement?.classList.remove('skeleton');
  });
  
  img.addEventListener('error', function() {
    this.style.display = 'none';
    this.parentElement?.classList.add('skeleton');
  });
});

// ===== Performance: Preload Critical Resources =====
if ('IntersectionObserver' in window) {
  const imgObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        if (img.dataset.src) {
          img.src = img.dataset.src;
          img.removeAttribute('data-src');
        }
        imgObserver.unobserve(img);
      }
    });
  }, { rootMargin: '50px' });
  
  document.querySelectorAll('img[data-src]').forEach(img => imgObserver.observe(img));
}

// ===== Smooth Scroll for Nav Links =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
</script>
</body>
</html>
'''

# 写入优化后的文件
with open(BASE / 'index.html', 'w') as f:
    f.write(optimized_html)

final_size = len(optimized_html)
print(f"优化后大小: {final_size:,} bytes ({final_size/1024:.1f} KB)")
print(f"缩减: {(1 - final_size/len(html))*100:.1f}%")
