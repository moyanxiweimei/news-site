from PIL import Image, ImageDraw, ImageFont
import os

IMGDIR = os.path.expanduser("~/.openclaw/workspace/news-site/images")
os.makedirs(IMGDIR, exist_ok=True)

W, H = 800, 450

def draw_gradient(draw, w, h, c1, c2):
    for y in range(h):
        ratio = y / h
        r = int(c1[0] + (c2[0] - c1[0]) * ratio)
        g = int(c1[1] + (c2[1] - c1[1]) * ratio)
        b = int(c1[2] + (c2[2] - c1[2]) * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def get_font(size, bold=False):
    font_paths = [
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except:
            continue
    return ImageFont.load_default()

# All images to generate: (filename, gradient1, gradient2, main_text, sub_text)
images = [
    # Finance
    ("finance_1", (30, 58, 138), (37, 99, 235), "META", "员工抗议数据采集"),
    ("finance_2", (37, 99, 235), (59, 130, 246), "安克创新", "精简产品线"),
    ("finance_3", (30, 64, 175), (30, 58, 138), "岚图汽车", "东风增持超70%"),
    # Tech  
    ("tech_1", (126, 34, 206), (147, 51, 234), "TikTok GO", "本地生活服务"),
    ("tech_2", (147, 51, 234), (168, 85, 247), "Googlebook", "处理器合作"),
    ("tech_3", (168, 85, 247), (192, 132, 252), "Meta", "员工抗议追踪"),
    # Medical
    ("medical_1", (21, 128, 61), (22, 163, 74), "OPPO", "母亲节文案致歉"),
    ("medical_2", (22, 163, 74), (34, 197, 94), "AI心理", "精神健康赛道"),
    ("medical_3", (34, 197, 94), (74, 222, 128), "无创血糖", "监测技术突破"),
    ("medical_4", (74, 222, 128), (134, 239, 172), "医保目录", "7款创新药纳入"),
    ("medical_5", (134, 239, 172), (187, 247, 208), "脑机接口", "抑郁症II期"),
    # Education
    ("education_1", (194, 65, 12), (234, 88, 12), "UNESCO", "高校人数翻倍"),
    ("education_2", (234, 88, 12), (249, 115, 22), "ChatGPT", "Edu中文版"),
    ("education_3", (249, 115, 22), (251, 146, 60), "VR教学", "千校试点"),
    ("education_4", (251, 146, 60), (253, 186, 116), "职教修订", "产教融合优惠"),
    ("education_5", (253, 186, 116), (255, 237, 213), "课后服务", "AI个性化辅导"),
    # Aerospace
    ("aerospace_1", (15, 23, 42), (30, 41, 59), "天舟十号", "41项实验物资"),
    ("aerospace_2", (30, 41, 59), (51, 65, 85), "维新宇航", "eVTOL首飞"),
    ("aerospace_3", (51, 65, 85), (71, 85, 105), "天联科技", "数千万融资"),
    ("aerospace_4", (71, 85, 105), (100, 116, 139), "探月四期", "月球南极"),
    ("aerospace_5", (100, 116, 139), (148, 163, 184), "超音速客机", "4小时北京纽约"),
    # Products
    ("products_1", (190, 24, 93), (219, 39, 119), "红魔11S", "脉动水冷引擎"),
    ("products_2", (219, 39, 119), (236, 72, 153), "佳明", "Forerunner新品"),
    ("products_3", (236, 72, 153), (244, 114, 182), "樱桃MX8.3", "PRO键盘开售"),
    # Auto
    ("auto_1", (15, 118, 110), (13, 148, 136), "岚图汽车", "东风增持"),
    ("auto_2", (13, 148, 136), (20, 184, 166), "蔚来乐道", "换电站3300座"),
    ("auto_3", (20, 184, 166), (45, 212, 191), "问界M6", "华为智选车"),
    # VC
    ("vc_1", (154, 52, 18), (180, 83, 9), "闪铸", "Creator 5预售"),
    ("vc_2", (180, 83, 9), (217, 119, 6), "SNUC", "NUC 15 Pro"),
    ("vc_3", (217, 119, 6), (245, 158, 11), "iQOO 15T", "青云配色"),
]

for filename, c1, c2, main_text, sub_text in images:
    img = Image.new('RGB', (W, H), c1)
    draw = ImageDraw.Draw(img)
    
    # Gradient background
    draw_gradient(draw, W, H, c1, c2)
    
    # Decorative circles (subtle)
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.ellipse([(-100, -100), (150, 150)], fill=(255, 255, 255, 15))
    overlay_draw.ellipse([(W-120, H-120), (W+80, H+80)], fill=(255, 255, 255, 10))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    # Main text (large)
    font_main = get_font(72, bold=True)
    bbox = draw.textbbox((0, 0), main_text, font=font_main)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((W - tw) / 2, (H - th) / 2 - 40), main_text, font=font_main, fill=(255, 255, 255))
    
    # Sub text (smaller)
    font_sub = get_font(36)
    bbox2 = draw.textbbox((0, 0), sub_text, font=font_sub)
    tw2, th2 = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
    draw.text(((W - tw2) / 2, (H - th) / 2 + 50), sub_text, font=font_sub, fill=(255, 255, 255, 200))
    
    # Category tag at bottom
    font_tag = get_font(24)
    tag_text = filename.split('_')[0].upper()
    bbox3 = draw.textbbox((0, 0), tag_text, font=font_tag)
    tw3 = bbox3[2] - bbox3[0]
    draw.rectangle([(W - tw3 - 40, H - 50), (W - 20, H - 20)], fill=(255, 255, 255, 30))
    draw.text((W - tw3 - 30, H - 48), tag_text, font=font_tag, fill=(255, 255, 255, 180))
    
    img.save(os.path.join(IMGDIR, f"{filename}.jpg"), "JPEG", quality=92)
    print(f"  ✓ {filename}.jpg")

print("\nDone! All images regenerated with news-relevant text.")
