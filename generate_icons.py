from PIL import Image, ImageDraw, ImageFilter
import math
import random
import os

os.makedirs('images', exist_ok=True)

def create_icon_image(width, height, bg_colors, icon_type):
    """Create an image with an industry-specific icon"""
    img = Image.new('RGB', (width, height), bg_colors[0])
    draw = ImageDraw.Draw(img)
    
    # Background gradient
    for y in range(height):
        ratio = y / height
        r = int(bg_colors[0][0] + (bg_colors[1][0] - bg_colors[0][0]) * ratio)
        g = int(bg_colors[0][1] + (bg_colors[1][1] - bg_colors[0][1]) * ratio)
        b = int(bg_colors[0][2] + (bg_colors[1][2] - bg_colors[0][2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    cx, cy = width // 2, height // 2
    
    if icon_type == 'finance':
        # Chart line
        points = [(80, 300), (200, 220), (350, 260), (500, 160), (650, 200)]
        for i in range(len(points)-1):
            draw.line([points[i], points[i+1]], fill=(255, 255, 255), width=5)
        # Bars
        for x, h in [(120, 180), (260, 240), (400, 200), (540, 160)]:
            draw.rectangle([x, height-h-80, x+50, height-80], fill=(255, 255, 255, 120))
        # Dollar sign
        draw.text((width-150, 60), "$", fill=(255, 255, 255), font=None)
        
    elif icon_type == 'tech':
        # Central chip
        chip = 100
        draw.rectangle([cx-chip//2, cy-chip//2, cx+chip//2, cy+chip//2], 
                      fill=(255, 255, 255), outline=(255, 255, 255), width=3)
        # Circuit lines
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = cx + int(60 * math.cos(rad))
            y1 = cy + int(60 * math.sin(rad))
            x2 = cx + int(160 * math.cos(rad))
            y2 = cy + int(160 * math.sin(rad))
            draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255), width=3)
            draw.ellipse([x2-6, y2-6, x2+6, y2+6], fill=(255, 255, 255))
        # CPU text
        draw.text((cx-25, cy-10), "AI", fill=(255, 255, 255))
        
    elif icon_type == 'medical':
        # Medical cross
        cs = 60
        draw.rectangle([cx-cs//2, cy-cs*2, cx+cs//2, cy+cs*2], fill=(255, 255, 255))
        draw.rectangle([cx-cs*2, cy-cs//2, cx+cs*2, cy+cs//2], fill=(255, 255, 255))
        # Heartbeat line
        hb = [(80, 250), (160, 250), (200, 180), (240, 320), (280, 250), (360, 250)]
        for i in range(len(hb)-1):
            draw.line([hb[i], hb[i+1]], fill=(255, 255, 255), width=4)
        # Plus signs
        for px, py in [(120, 120), (600, 150), (680, 280)]:
            draw.line([(px-15, py), (px+15, py)], fill=(255, 255, 255), width=3)
            draw.line([(px, py-15), (px, py+15)], fill=(255, 255, 255), width=3)
            
    elif icon_type == 'education':
        # Book
        bw, bh = 140, 180
        draw.rectangle([cx-bw//2, cy-bh//2, cx+bw//2, cy+bh//2], 
                      fill=(255, 255, 255), outline=(255, 255, 255), width=3)
        draw.line([(cx, cy-bh//2), (cx, cy+bh//2)], fill=(255, 255, 255), width=2)
        # Lightbulb
        draw.ellipse([cx+120, cy-140, cx+200, cy-60], fill=(255, 255, 255, 100), outline=(255, 255, 255), width=2)
        # Graduation cap
        cap_points = [(cx-80, cy-140), (cx, cy-170), (cx+80, cy-140), (cx, cy-110)]
        draw.polygon(cap_points, fill=(255, 255, 255))
        
    elif icon_type == 'aerospace':
        # Rocket body
        rocket = [(cx, cy-120), (cx-30, cy+40), (cx-15, cy+40), 
                 (cx-15, cy+80), (cx+15, cy+80), (cx+15, cy+40), (cx+30, cy+40)]
        draw.polygon(rocket, fill=(255, 255, 255))
        # Flame
        flame = [(cx-12, cy+80), (cx, cy+140), (cx+12, cy+80)]
        draw.polygon(flame, fill=(255, 150, 50))
        # Stars
        for _ in range(30):
            x, y = random.randint(0, width), random.randint(0, height)
            draw.ellipse([x-2, y-2, x+2, y+2], fill=(255, 255, 255))
        # Circle orbit
        draw.ellipse([cx-200, cy-100, cx+200, cy+100], outline=(255, 255, 255, 80), width=1)
        
    elif icon_type == 'products':
        # Phone
        pw, ph = 100, 200
        draw.rounded_rectangle([cx-pw//2, cy-ph//2, cx+pw//2, cy+ph//2], 
                              radius=15, fill=(255, 255, 255), outline=(255, 255, 255), width=3)
        draw.rectangle([cx-pw//2+10, cy-ph//2+20, cx+pw//2-10, cy+ph//2-30], 
                      fill=(255, 255, 255, 50))
        # Small phone
        draw.rounded_rectangle([cx+80, cy-60, cx+160, cy+40], 
                              radius=10, fill=(255, 255, 255), outline=(255, 255, 255), width=2)
        # Watch
        draw.ellipse([cx-160, cy-40, cx-100, cy+20], fill=(255, 255, 255), outline=(255, 255, 255), width=2)
        
    elif icon_type == 'auto':
        # Car body
        car = [(80, 320), (140, 260), (320, 260), (380, 240), (520, 240), 
               (580, 260), (720, 260), (720, 320), (680, 320), (660, 290),
               (540, 290), (520, 320), (280, 320), (260, 290), (120, 290), (80, 320)]
        draw.polygon(car, fill=(255, 255, 255))
        # Wheels
        draw.ellipse([150, 300, 220, 370], fill=(255, 255, 255, 80), outline=(255, 255, 255), width=3)
        draw.ellipse([560, 300, 630, 370], fill=(255, 255, 255, 80), outline=(255, 255, 255), width=3)
        # Road
        draw.line([(0, 370), (width, 370)], fill=(255, 255, 255), width=2)
        
    elif icon_type == 'vc':
        # Upward arrow
        arrow = [(cx-50, cy+40), (cx, cy-80), (cx+50, cy+40), (cx+20, cy+40), 
                (cx+20, cy+80), (cx-20, cy+80), (cx-20, cy+40)]
        draw.polygon(arrow, fill=(255, 255, 255))
        # Bar chart
        for x, h in [(80, 120), (180, 200), (280, 280), (480, 160), (580, 240)]:
            draw.rectangle([x, height-h-80, x+60, height-80], fill=(255, 255, 255, 80))
        # Trend line
        trend = [(80, 300), (200, 250), (320, 280), (500, 200), (620, 220)]
        for i in range(len(trend)-1):
            draw.line([trend[i], trend[i+1]], fill=(255, 255, 255), width=3)
    
    # Vignette
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    for y in range(height):
        for x in range(width):
            dx = x - width/2
            dy = y - height/2
            dist = math.sqrt(dx*dx + dy*dy) / math.sqrt(width*width/4 + height*height/4)
            alpha = int(30 * min(dist, 1.0))
            overlay_draw.point((x, y), fill=(0, 0, 0, alpha))
    
    img = img.convert('RGBA')
    img = Image.alpha_composite(img, overlay)
    img = img.convert('RGB')
    
    return img

# Generate all images
categories = {
    'finance': {'colors': [(0, 100, 200), (100, 0, 200)], 'icon': 'finance'},
    'tech': {'colors': [(0, 150, 100), (0, 100, 200)], 'icon': 'tech'},
    'medical': {'colors': [(0, 120, 180), (0, 180, 120)], 'icon': 'medical'},
    'education': {'colors': [(200, 120, 0), (200, 60, 0)], 'icon': 'education'},
    'aerospace': {'colors': [(0, 50, 150), (80, 0, 180)], 'icon': 'aerospace'},
    'products': {'colors': [(200, 60, 50), (180, 0, 100)], 'icon': 'products'},
    'auto': {'colors': [(200, 100, 0), (180, 0, 50)], 'icon': 'auto'},
    'vc': {'colors': [(100, 0, 180), (180, 0, 100)], 'icon': 'vc'},
}

for name, info in categories.items():
    img = create_icon_image(800, 400, info['colors'], info['icon'])
    img.save(f'images/{name}.jpg', 'JPEG', quality=75)
    size = os.path.getsize(f'images/{name}.jpg')
    print(f'{name}.jpg: {size} bytes')

print('\nAll icon images generated!')
