import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ASSETS_DIR = "/Volumes/Work/spoonart.github.io/assets/banners"
OUTPUT_DIR = "/Volumes/Work/spoonart.github.io/assets/banners"
ARTIFACT_DIR = "/Users/user/.gemini/antigravity/brain/eb20549e-b3f5-4543-ba1a-a72a936bc683"

# First extract the clean monitor screen from media_1792120405793_0a1c2c1f.jpg
im_diag = Image.open(os.path.join(ASSETS_DIR, "media_1792120405793_0a1c2c1f.jpg"))
clean_monitor_crop = im_diag.crop((251, 126, 613, 345))
clean_monitor_crop.save(os.path.join(ASSETS_DIR, "screen_clean.png"))

def get_font(size, weight='bold'):
    index_map = {
        'heavy': 8,
        'bold': 0,
        'demi': 2,
        'medium': 5,
        'regular': 7
    }
    idx = index_map.get(weight, 0)
    try:
        return ImageFont.truetype('/System/Library/Fonts/Avenir Next.ttc', size, index=idx)
    except Exception:
        try:
            return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf' if weight in ['bold', 'heavy'] else '/System/Library/Fonts/Supplemental/Arial.ttf', size)
        except Exception:
            return ImageFont.load_default()

def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def draw_vector_checkmark(draw, center_x, center_y, size=8, color=(16, 185, 129, 255), width=2):
    p1 = (center_x - size * 0.5, center_y)
    p2 = (center_x - size * 0.1, center_y + size * 0.5)
    p3 = (center_x + size * 0.6, center_y - size * 0.5)
    draw.line([p1, p2], fill=color, width=width)
    draw.line([p2, p3], fill=color, width=width)

def draw_vector_star(draw, cx, cy, size=7, color=(250, 204, 21, 255)):
    points = []
    for i in range(10):
        r = size if i % 2 == 0 else size * 0.45
        angle = i * math.pi / 5 - math.pi / 2
        points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(points, fill=color)

def create_shadow(image_rgba, offset=(0, 22), blur=35, opacity=0.7, color=(0, 0, 0)):
    w, h = image_rgba.size
    pad = blur * 3
    alpha = image_rgba.split()[3]
    
    ox = pad + offset[0]
    oy = pad + offset[1]
    
    mask_layer = Image.new('L', (w + pad * 2, h + pad * 2), 0)
    mask_layer.paste(alpha, (ox, oy))
    mask_blurred = mask_layer.filter(ImageFilter.GaussianBlur(blur))
    
    r, g, b = color
    s_col = Image.new('RGBA', (w + pad * 2, h + pad * 2), (r, g, b, 0))
    s_col.putalpha(mask_blurred.point(lambda p: int(p * opacity)))
    
    final_canvas = Image.new('RGBA', (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    final_canvas.paste(s_col, (0, 0), s_col)
    final_canvas.paste(image_rgba, (pad, pad), image_rgba)
    
    return final_canvas, pad

def make_tablet_mockup(screen_img_path, target_width=750):
    screen = Image.open(screen_img_path).convert('RGBA')
    sw, sh = screen.size
    target_height = int(target_width * (sh / sw))
    screen = screen.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    bezel = 18
    fw = target_width + bezel * 2
    fh = target_height + bezel * 2
    radius = 28
    
    frame = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    # Outer dark titanium tablet body
    draw_rounded_rect(draw, [(0, 0), (fw - 1, fh - 1)], radius=radius, fill=(20, 26, 38, 255), outline=(51, 65, 85, 255), width=2)
    draw_rounded_rect(draw, [(3, 3), (fw - 4, fh - 4)], radius=radius - 2, outline=(15, 23, 42, 255), width=2)
    
    cam_x = fw // 2
    cam_y = bezel // 2
    draw.ellipse([(cam_x - 3, cam_y - 3), (cam_x + 3, cam_y + 3)], fill=(10, 15, 25, 255), outline=(40, 50, 70, 255))
    draw.ellipse([(cam_x - 1, cam_y - 1), (cam_x + 1, cam_y + 1)], fill=(20, 60, 100, 255))
    
    screen_radius = 12
    screen_mask = Image.new('L', (target_width, target_height), 0)
    s_draw = ImageDraw.Draw(screen_mask)
    draw_rounded_rect(s_draw, [(0, 0), (target_width, target_height)], radius=screen_radius, fill=255)
    
    frame.paste(screen, (bezel, bezel), screen_mask)
    
    highlight = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(highlight)
    draw_rounded_rect(h_draw, [(1, 1), (fw - 2, fh - 2)], radius=radius, outline=(255, 255, 255, 30), width=1)
    frame = Image.alpha_composite(frame, highlight)
    
    return frame

def make_phone_mockup(screen_img_path, target_width=315):
    screen = Image.open(screen_img_path).convert('RGBA')
    sw, sh = screen.size
    target_height = int(target_width * (sh / sw))
    screen = screen.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    bezel = 12
    fw = target_width + bezel * 2
    fh = target_height + bezel * 2
    radius = 42
    
    frame = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    draw_rounded_rect(draw, [(0, 0), (fw - 1, fh - 1)], radius=radius, fill=(18, 22, 31, 255), outline=(71, 85, 105, 255), width=2)
    draw_rounded_rect(draw, [(2, 2), (fw - 3, fh - 3)], radius=radius - 2, fill=(12, 16, 24, 255))
    
    screen_radius = 32
    screen_mask = Image.new('L', (target_width, target_height), 0)
    s_draw = ImageDraw.Draw(screen_mask)
    draw_rounded_rect(s_draw, [(0, 0), (target_width, target_height)], radius=screen_radius, fill=255)
    
    frame.paste(screen, (bezel, bezel), screen_mask)
    
    # Dynamic Island
    di_w, di_h = 75, 18
    di_x = (fw - di_w) // 2
    di_y = bezel + 6
    draw_rounded_rect(draw, [(di_x, di_y), (di_x + di_w, di_y + di_h)], radius=9, fill=(0, 0, 0, 255))
    draw.ellipse([(di_x + 14, di_y + 4), (di_x + 24, di_y + 14)], fill=(15, 25, 45, 255))
    
    highlight = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(highlight)
    draw_rounded_rect(h_draw, [(1, 1), (fw - 2, fh - 2)], radius=radius, outline=(255, 255, 255, 45), width=1)
    frame = Image.alpha_composite(frame, highlight)
    
    return frame

def make_pod_card_mockup(screen_img_path, target_width=360):
    b99 = Image.open(screen_img_path).convert('RGBA')
    cropped = b99.crop((14, 115, 347, 515))
    cw, ch = cropped.size
    target_height = int(target_width * (ch / cw))
    cropped = cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    pad = 12
    fw = target_width + pad * 2
    fh = target_height + pad * 2 + 38
    radius = 20
    
    frame = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    # White card background with crisp border
    draw_rounded_rect(draw, [(0, 0), (fw - 1, fh - 1)], radius=radius, fill=(255, 255, 255, 255), outline=(203, 213, 225, 255), width=2)
    
    # Header bar
    draw_rounded_rect(draw, [(4, 4), (fw - 5, 38)], radius=14, fill=(248, 250, 252, 255))
    draw.ellipse([(14, 16), (24, 26)], fill=(16, 185, 129, 255))
    f_badge = get_font(13, 'bold')
    draw.text((32, 13), "PROOF OF DELIVERY (POD)", fill=(30, 41, 59, 255), font=f_badge)
    
    f_sub = get_font(11, 'medium')
    draw.text((fw - 120, 15), "Photo + Signature", fill=(100, 116, 139, 255), font=f_sub)
    
    c_mask = Image.new('L', (target_width, target_height), 0)
    c_draw = ImageDraw.Draw(c_mask)
    draw_rounded_rect(c_draw, [(0, 0), (target_width, target_height)], radius=14, fill=255)
    
    frame.paste(cropped, (pad, 42), c_mask)
    return frame

def make_desktop_monitor_mockup(screen_img_path, target_width=520):
    screen = Image.open(screen_img_path).convert('RGBA')
    sw, sh = screen.size
    target_height = int(target_width * (sh / sw))
    screen = screen.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    bezel = 12
    fw = target_width + bezel * 2
    fh = target_height + bezel * 2
    radius = 16
    
    frame = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    # Sleek dark monitor bezel
    draw_rounded_rect(draw, [(0, 0), (fw - 1, fh - 1)], radius=radius, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255), width=2)
    
    screen_radius = 8
    screen_mask = Image.new('L', (target_width, target_height), 0)
    s_draw = ImageDraw.Draw(screen_mask)
    draw_rounded_rect(s_draw, [(0, 0), (target_width, target_height)], radius=screen_radius, fill=255)
    frame.paste(screen, (bezel, bezel), screen_mask)
    
    # Metallic bottom chin highlight
    draw.line([(bezel, fh - 4), (fw - bezel, fh - 4)], fill=(71, 85, 105, 180), width=1)
    
    return frame

# =========================================================================
# BANNER 1: "DARK TECH / FLEET DRIVER HERO"
# =========================================================================
def generate_banner_1():
    W, H = 1920, 1080
    img = Image.new('RGBA', (W, H), (10, 15, 26, 255))
    
    glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow_layer)
    g_draw.ellipse([(1050, 100), (1880, 950)], fill=(14, 116, 144, 40))
    g_draw.ellipse([(1200, 250), (1750, 850)], fill=(37, 99, 235, 35))
    g_draw.ellipse([(-120, -120), (650, 520)], fill=(30, 58, 138, 25))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(110))
    img = Image.alpha_composite(img, glow_layer)
    
    draw = ImageDraw.Draw(img)
    
    # Subtle grid dots
    dot_color = (148, 163, 184, 14)
    step = 42
    for x in range(0, W, step):
        for y in range(0, H, step):
            draw.ellipse([(x - 1, y - 1), (x + 1, y + 1)], fill=dot_color)
            
    # Stylized route lines
    route_color = (6, 182, 212, 35)
    route_color_bright = (56, 189, 248, 70)
    routes = [
        [(880, 180), (1080, 130), (1240, 260), (1480, 200), (1780, 290)],
        [(950, 460), (1130, 400), (1380, 540), (1630, 470), (1880, 580)],
        [(1050, 730), (1250, 660), (1430, 800), (1730, 720), (1890, 870)],
    ]
    for r in routes:
        for i in range(len(r) - 1):
            draw.line([r[i], r[i+1]], fill=route_color, width=2)
            draw.ellipse([(r[i][0]-3, r[i][1]-3), (r[i][0]+3, r[i][1]+3)], fill=route_color_bright)
        draw.ellipse([(r[-1][0]-4, r[-1][1]-4), (r[-1][0]+4, r[-1][1]+4)], fill=route_color_bright)

    # --- LEFT COLUMN ---
    lx = 90
    
    # 1. Category Pill
    tag_bg = [(lx, 85), (lx + 360, 127)]
    draw_rounded_rect(draw, tag_bg, radius=21, fill=(15, 23, 42, 220), outline=(6, 182, 212, 190), width=1)
    draw.ellipse([(lx + 16, 101), (lx + 26, 111)], fill=(16, 185, 129, 255))
    draw.text((lx + 34, 98), "LOGISTICS & FLEET MOBILE APPS", fill=(103, 232, 249, 255), font=get_font(14, 'bold'))
    
    # 2. Headline
    draw.text((lx, 150), "Delivery & Fleet", fill=(255, 255, 255, 255), font=get_font(54, 'heavy'))
    draw.text((lx, 218), "Driver App Platform", fill=(56, 189, 248, 255), font=get_font(54, 'heavy'))
    
    # 3. Subhead
    f_sub = get_font(20, 'regular')
    draw.text((lx, 300), "Turn-by-turn navigation, real-time fleet dispatch, and automated", fill=(148, 163, 184, 255), font=f_sub)
    draw.text((lx, 330), "route optimization built for mission-critical enterprise scale.", fill=(148, 163, 184, 255), font=f_sub)
    
    # 4. Metrics Pillars
    metrics_y = 390
    metrics = [
        ("10,000+", "Daily Delivery Orders"),
        ("5 Countries", "Live in Production"),
        ("100% Solo", "Core Architecture")
    ]
    card_w = 214
    for i, (val, label) in enumerate(metrics):
        cx = lx + i * (card_w + 14)
        draw_rounded_rect(draw, [(cx, metrics_y), (cx + card_w, metrics_y + 86)], radius=14, 
                          fill=(17, 24, 39, 230), outline=(51, 65, 85, 180), width=1)
        draw.text((cx + 18, metrics_y + 15), val, fill=(255, 255, 255, 255), font=get_font(25, 'heavy'))
        draw.text((cx + 18, metrics_y + 51), label, fill=(56, 189, 248, 255), font=get_font(12, 'medium'))

    # 5. Feature Bullets
    feat_y = 515
    features = [
        "Turn-by-turn navigation with dynamic ETA & early/late alerts",
        "Multi-stop route planning & real-time order reassignment",
        "Proof of Delivery (POD): digital signature & photo capture",
        "Tablet in-cab & mobile-optimized UI (Android & iOS)"
    ]
    for i, feat in enumerate(features):
        fy = feat_y + i * 44
        draw_rounded_rect(draw, [(lx, fy + 2), (lx + 24, fy + 26)], radius=6, fill=(14, 116, 144, 160), outline=(6, 182, 212, 220), width=1)
        draw_vector_checkmark(draw, lx + 12, fy + 14, size=8, color=(255, 255, 255, 255), width=2)
        draw.text((lx + 36, fy + 4), feat, fill=(226, 232, 240, 255), font=get_font(16, 'demi'))

    # 6. Tech Stack Badges
    tech_y = 725
    draw.text((lx, tech_y), "ENGINEERED WITH:", fill=(100, 116, 139, 255), font=get_font(12, 'bold'))
    
    tags = ["Android", "Kotlin", "Jetpack Compose", "Maps SDK", "Turn-by-Turn", "Fastlane", "Play Store"]
    tx = lx
    for t in tags:
        tf = get_font(13, 'medium')
        bbox = draw.textbbox((0, 0), t, font=tf)
        tw = bbox[2] - bbox[0] + 24
        draw_rounded_rect(draw, [(tx, tech_y + 22), (tx + tw, tech_y + 52)], radius=8, 
                          fill=(30, 41, 59, 180), outline=(71, 85, 105, 180), width=1)
        draw.text((tx + 12, tech_y + 29), t, fill=(203, 213, 225, 255), font=tf)
        tx += tw + 10
        
    # 7. Trust Bar at Bottom
    foot_y = 835
    draw_rounded_rect(draw, [(lx, foot_y), (lx + 670, foot_y + 72)], radius=16, 
                      fill=(15, 23, 42, 240), outline=(59, 130, 246, 200), width=1)
    draw.ellipse([(lx + 18, foot_y + 22), (lx + 44, foot_y + 48)], fill=(37, 99, 235, 255))
    draw_vector_star(draw, lx + 31, foot_y + 35, size=7, color=(255, 255, 255, 255))
    draw.text((lx + 56, foot_y + 16), "Production-Tested Mobility Architecture", fill=(255, 255, 255, 255), font=get_font(15, 'bold'))
    draw.text((lx + 56, foot_y + 40), "Zero unhandled crashes · Powers peak fleets across Singapore, UAE, Japan", fill=(148, 163, 184, 255), font=get_font(13, 'regular'))

    # --- RIGHT COLUMN MOCKUPS ---
    tablet_img_path = os.path.join(ASSETS_DIR, "media_1792120405803_32e54e5c.png")
    phone_img_path = "/Volumes/Work/spoonart.github.io/assets/shots/swat-driver-2.jpg"
    pod_img_path = os.path.join(ASSETS_DIR, "media_1792120405793_b99472a8.png")
    
    # 1. Base Tablet
    tablet = make_tablet_mockup(tablet_img_path, target_width=750)
    tablet_shadowed, t_pad = create_shadow(tablet, offset=(0, 22), blur=40, opacity=0.75, color=(0, 0, 0))
    tab_x = 990 - t_pad
    tab_y = 95 - t_pad
    img.paste(tablet_shadowed, (tab_x, tab_y), tablet_shadowed)
    
    pill_img = Image.new('RGBA', (320, 44), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(pill_img)
    draw_rounded_rect(p_draw, [(0, 0), (319, 43)], radius=22, fill=(15, 23, 42, 245), outline=(56, 189, 248, 220), width=1)
    p_draw.ellipse([(14, 16), (24, 26)], fill=(16, 185, 129, 255))
    p_draw.text((32, 13), "IN-CAB TABLET DISPATCH UI", fill=(255, 255, 255, 255), font=get_font(12, 'bold'))
    pill_shadowed, p_pad = create_shadow(pill_img, offset=(0, 6), blur=14, opacity=0.55)
    img.paste(pill_shadowed, (1040 - p_pad, 75 - p_pad), pill_shadowed)

    # 2. Foreground Phone
    phone = make_phone_mockup(phone_img_path, target_width=320)
    phone_shadowed, ph_pad = create_shadow(phone, offset=(-12, 28), blur=42, opacity=0.85, color=(0, 0, 0))
    ph_x = 940 - ph_pad
    ph_y = 350 - ph_pad
    img.paste(phone_shadowed, (ph_x, ph_y), phone_shadowed)
    
    phone_pill = Image.new('RGBA', (260, 42), (0, 0, 0, 0))
    pp_draw = ImageDraw.Draw(phone_pill)
    draw_rounded_rect(pp_draw, [(0, 0), (259, 41)], radius=21, fill=(15, 23, 42, 245), outline=(16, 185, 129, 220), width=1)
    pp_draw.ellipse([(14, 15), (24, 25)], fill=(56, 189, 248, 255))
    pp_draw.text((32, 13), "DRIVER NAVIGATION APP", fill=(255, 255, 255, 255), font=get_font(12, 'bold'))
    pp_shadowed, pp_pad = create_shadow(phone_pill, offset=(0, 6), blur=14, opacity=0.55)
    img.paste(pp_shadowed, (970 - pp_pad, 365 - pp_pad), pp_shadowed)

    # 3. Floating POD Card (Shifted to right, completely clean, buttons visible!)
    pod_card = make_pod_card_mockup(pod_img_path, target_width=370)
    pod_shadowed, pod_pad = create_shadow(pod_card, offset=(15, 22), blur=38, opacity=0.75, color=(0, 0, 0))
    pod_x = 1440 - pod_pad
    pod_y = 520 - pod_pad
    img.paste(pod_shadowed, (pod_x, pod_y), pod_shadowed)
    
    # Floating Sync Pill placed above the buttons
    status_card = Image.new('RGBA', (270, 52), (0, 0, 0, 0))
    sc_draw = ImageDraw.Draw(status_card)
    draw_rounded_rect(sc_draw, [(0, 0), (269, 51)], radius=14, fill=(16, 185, 129, 245), outline=(255, 255, 255, 220), width=1)
    draw_vector_checkmark(sc_draw, 22, 26, size=8, color=(255, 255, 255, 255), width=2)
    sc_draw.text((36, 11), "REAL-TIME FLEET SYNC", fill=(255, 255, 255, 255), font=get_font(12, 'bold'))
    sc_draw.text((36, 28), "Instant Dispatcher Updates", fill=(236, 253, 245, 255), font=get_font(10, 'medium'))
    sc_shadowed, sc_pad = create_shadow(status_card, offset=(0, 8), blur=18, opacity=0.5)
    # Positioned at bottom right corner cleanly
    img.paste(sc_shadowed, (1510 - sc_pad, 960 - sc_pad), sc_shadowed)

    out_file = os.path.join(OUTPUT_DIR, "upwork_catalog_banner_dark_tech.png")
    out_file_artifact = os.path.join(ARTIFACT_DIR, "upwork_catalog_banner_dark_tech.png")
    img.convert('RGB').save(out_file, 'PNG', quality=95)
    img.convert('RGB').save(out_file_artifact, 'PNG', quality=95)
    print("Banner 1 refined successfully")

# =========================================================================
# BANNER 2: "COMPLETE END-TO-END ECOSYSTEM"
# =========================================================================
def generate_banner_2():
    W, H = 1920, 1080
    img = Image.new('RGBA', (W, H), (11, 15, 34, 255))
    
    glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow_layer)
    g_draw.ellipse([(950, 80), (1850, 980)], fill=(99, 102, 241, 35))
    g_draw.ellipse([(1200, 250), (1800, 850)], fill=(16, 185, 129, 30))
    g_draw.ellipse([(-100, -100), (600, 500)], fill=(79, 70, 229, 25))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(110))
    img = Image.alpha_composite(img, glow_layer)
    
    draw = ImageDraw.Draw(img)
    
    dot_color = (148, 163, 184, 12)
    step = 42
    for x in range(0, W, step):
        for y in range(0, H, step):
            draw.ellipse([(x - 1, y - 1), (x + 1, y + 1)], fill=dot_color)
            
    lx = 90
    
    # Tag Pill
    tag_bg = [(lx, 85), (lx + 380, 127)]
    draw_rounded_rect(draw, tag_bg, radius=21, fill=(17, 24, 39, 220), outline=(99, 102, 241, 190), width=1)
    draw.ellipse([(lx + 16, 101), (lx + 26, 111)], fill=(129, 140, 248, 255))
    draw.text((lx + 34, 98), "END-TO-END FLEET MOBILITY SUITE", fill=(199, 210, 254, 255), font=get_font(13, 'bold'))
    
    # Headline
    draw.text((lx, 150), "Route Optimization", fill=(255, 255, 255, 255), font=get_font(54, 'heavy'))
    draw.text((lx, 218), "& Dispatch Platform", fill=(129, 140, 248, 255), font=get_font(54, 'heavy'))
    
    # Subhead
    draw.text((lx, 300), "From automated dispatcher route planning to driver turn-by-turn navigation", fill=(148, 163, 184, 255), font=get_font(19, 'regular'))
    draw.text((lx, 330), "and digital proof of delivery — built for high-throughput logistics.", fill=(148, 163, 184, 255), font=get_font(19, 'regular'))
    
    # Metrics
    metrics_y = 390
    metrics = [
        ("10,000+", "Daily Delivery Orders"),
        ("5 Countries", "Singapore · UAE · Japan +"),
        ("B2B & B2C", "Enterprise Logistics")
    ]
    card_w = 214
    for i, (val, label) in enumerate(metrics):
        cx = lx + i * (card_w + 14)
        draw_rounded_rect(draw, [(cx, metrics_y), (cx + card_w, metrics_y + 86)], radius=14, 
                          fill=(17, 24, 39, 230), outline=(79, 70, 229, 160), width=1)
        draw.text((cx + 18, metrics_y + 15), val, fill=(255, 255, 255, 255), font=get_font(25, 'heavy'))
        draw.text((cx + 18, metrics_y + 51), label, fill=(165, 180, 252, 255), font=get_font(12, 'medium'))

    # Features
    feat_y = 515
    features = [
        "Web Dispatcher Portal: multi-vehicle automated route generator",
        "Driver In-Cab Tablet UI: active lane guidance & schedule monitor",
        "Driver Smartphone App: turn-by-turn routing & stop timeline",
        "Instant Proof of Delivery: photo verification & signature capture"
    ]
    for i, feat in enumerate(features):
        fy = feat_y + i * 44
        draw_rounded_rect(draw, [(lx, fy + 2), (lx + 24, fy + 26)], radius=6, fill=(79, 70, 229, 160), outline=(129, 140, 248, 220), width=1)
        draw_vector_checkmark(draw, lx + 12, fy + 14, size=8, color=(255, 255, 255, 255), width=2)
        draw.text((lx + 36, fy + 4), feat, fill=(226, 232, 240, 255), font=get_font(16, 'demi'))

    # Tech Stack
    tech_y = 725
    draw.text((lx, tech_y), "TECHNOLOGIES & CAPABILITIES:", fill=(148, 163, 184, 255), font=get_font(12, 'bold'))
    tags = ["Android Compose", "Kotlin", "Maps SDK", "Route Optimisation", "Real-Time GPS", "CI/CD Pipeline"]
    tx = lx
    for t in tags:
        tf = get_font(13, 'medium')
        bbox = draw.textbbox((0, 0), t, font=tf)
        tw = bbox[2] - bbox[0] + 24
        draw_rounded_rect(draw, [(tx, tech_y + 22), (tx + tw, tech_y + 52)], radius=8, 
                          fill=(30, 41, 59, 180), outline=(71, 85, 105, 180), width=1)
        draw.text((tx + 12, tech_y + 29), t, fill=(203, 213, 225, 255), font=tf)
        tx += tw + 10

    # Trust Card
    foot_y = 835
    draw_rounded_rect(draw, [(lx, foot_y), (lx + 670, foot_y + 72)], radius=16, 
                      fill=(17, 24, 39, 240), outline=(16, 185, 129, 180), width=1)
    draw.ellipse([(lx + 18, foot_y + 22), (lx + 44, foot_y + 48)], fill=(16, 185, 129, 255))
    draw_vector_star(draw, lx + 31, foot_y + 35, size=7, color=(255, 255, 255, 255))
    draw.text((lx + 56, foot_y + 16), "Architected & Shipped Solo", fill=(255, 255, 255, 255), font=get_font(15, 'bold'))
    draw.text((lx + 56, foot_y + 40), "Rewrote 10 map screens to Jetpack Compose · Scaled to 37 modular Gradle modules", fill=(148, 163, 184, 255), font=get_font(13, 'regular'))

    # --- RIGHT COLUMN: 3-TIER ECOSYSTEM (Monitor + Tablet + Phone) ---
    monitor_path = os.path.join(ASSETS_DIR, "screen_clean.png")
    tablet_img_path = os.path.join(ASSETS_DIR, "media_1792120405803_32e54e5c.png")
    phone_img_path = os.path.join(ASSETS_DIR, "media_1792120405809_e27311ed.png")
    
    # 1. Clean Desktop Monitor Mockup (Top Right)
    monitor = make_desktop_monitor_mockup(monitor_path, target_width=560)
    mon_shadowed, m_pad = create_shadow(monitor, offset=(0, 20), blur=35, opacity=0.75)
    img.paste(mon_shadowed, (1290 - m_pad, 100 - m_pad), mon_shadowed)
    
    mp = Image.new('RGBA', (280, 42), (0, 0, 0, 0))
    mp_draw = ImageDraw.Draw(mp)
    draw_rounded_rect(mp_draw, [(0, 0), (279, 41)], radius=21, fill=(15, 23, 42, 245), outline=(129, 140, 248, 220), width=1)
    mp_draw.ellipse([(14, 16), (24, 26)], fill=(129, 140, 248, 255))
    mp_draw.text((32, 13), "DISPATCHER ROUTE PLANNER", fill=(255, 255, 255, 255), font=get_font(12, 'bold'))
    mp_shadow, mpp = create_shadow(mp, offset=(0, 6), blur=14, opacity=0.55)
    img.paste(mp_shadow, (1320 - mpp, 80 - mpp), mp_shadow)

    # 2. In-Cab Tablet (Center-Left)
    tablet = make_tablet_mockup(tablet_img_path, target_width=660)
    tab_shadowed, t_pad = create_shadow(tablet, offset=(0, 24), blur=40, opacity=0.8)
    img.paste(tab_shadowed, (910 - t_pad, 230 - t_pad), tab_shadowed)

    tp = Image.new('RGBA', (260, 42), (0, 0, 0, 0))
    tp_draw = ImageDraw.Draw(tp)
    draw_rounded_rect(tp_draw, [(0, 0), (259, 41)], radius=21, fill=(15, 23, 42, 245), outline=(16, 185, 129, 220), width=1)
    tp_draw.ellipse([(14, 16), (24, 26)], fill=(16, 185, 129, 255))
    tp_draw.text((32, 13), "IN-CAB TABLET DISPATCH", fill=(255, 255, 255, 255), font=get_font(12, 'bold'))
    tp_shadow, tpp = create_shadow(tp, offset=(0, 6), blur=14, opacity=0.55)
    img.paste(tp_shadow, (940 - tpp, 215 - tpp), tp_shadow)

    # 3. Driver Smartphone (Bottom Right Overlapping)
    phone = make_phone_mockup(phone_img_path, target_width=300)
    phone_shadowed, ph_pad = create_shadow(phone, offset=(-10, 25), blur=40, opacity=0.85)
    img.paste(phone_shadowed, (1390 - ph_pad, 430 - ph_pad), phone_shadowed)

    php = Image.new('RGBA', (240, 42), (0, 0, 0, 0))
    php_draw = ImageDraw.Draw(php)
    draw_rounded_rect(php_draw, [(0, 0), (239, 41)], radius=21, fill=(15, 23, 42, 245), outline=(56, 189, 248, 220), width=1)
    php_draw.ellipse([(14, 16), (24, 26)], fill=(56, 189, 248, 255))
    php_draw.text((32, 13), "DRIVER MOBILE APP", fill=(255, 255, 255, 255), font=get_font(12, 'bold'))
    php_shadow, phpp = create_shadow(php, offset=(0, 6), blur=14, opacity=0.55)
    img.paste(php_shadow, (1420 - phpp, 445 - phpp), php_shadow)

    # 4. Floating Proof of Delivery Pill
    status_card = Image.new('RGBA', (320, 62), (0, 0, 0, 0))
    sc_draw = ImageDraw.Draw(status_card)
    draw_rounded_rect(sc_draw, [(0, 0), (319, 61)], radius=16, fill=(16, 185, 129, 250), outline=(255, 255, 255, 220), width=1)
    draw_vector_checkmark(sc_draw, 24, 31, size=9, color=(255, 255, 255, 255), width=2)
    sc_draw.text((42, 13), "PROOF OF DELIVERY READY", fill=(255, 255, 255, 255), font=get_font(13, 'bold'))
    sc_draw.text((42, 33), "Photo Capture & Digital Signature", fill=(236, 253, 245, 255), font=get_font(11, 'medium'))
    sc_shadow, sc_pad = create_shadow(status_card, offset=(0, 10), blur=20, opacity=0.55)
    img.paste(sc_shadow, (960 - sc_pad, 790 - sc_pad), sc_shadow)

    out_file = os.path.join(OUTPUT_DIR, "upwork_catalog_banner_ecosystem.png")
    out_file_artifact = os.path.join(ARTIFACT_DIR, "upwork_catalog_banner_ecosystem.png")
    img.convert('RGB').save(out_file, 'PNG', quality=95)
    img.convert('RGB').save(out_file_artifact, 'PNG', quality=95)
    print("Banner 2 refined successfully")

# =========================================================================
# BANNER 3: "MINIMAL BOLD SEARCH-THUMBNAIL CRUSH"
# =========================================================================
def generate_banner_3():
    W, H = 1920, 1080
    img = Image.new('RGBA', (W, H), (15, 23, 42, 255))
    
    glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow_layer)
    g_draw.ellipse([(1100, 100), (1850, 950)], fill=(56, 189, 248, 25))
    g_draw.ellipse([(1300, 300), (1800, 800)], fill=(16, 185, 129, 25))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(120))
    img = Image.alpha_composite(img, glow_layer)
    
    draw = ImageDraw.Draw(img)
    
    # Ultra-soft grid
    grid_col = (255, 255, 255, 5)
    for x in range(0, W, 60):
        draw.line([(x, 0), (x, H)], fill=grid_col, width=1)
    for y in range(0, H, 60):
        draw.line([(0, y), (W, y)], fill=grid_col, width=1)

    lx = 100
    
    tag_bg = [(lx, 90), (lx + 320, 136)]
    draw_rounded_rect(draw, tag_bg, radius=23, fill=(30, 41, 59, 230), outline=(56, 189, 248, 220), width=1)
    draw.ellipse([(lx + 18, 107), (lx + 28, 117)], fill=(16, 185, 129, 255))
    draw.text((lx + 38, 104), "UPWORK TOP RATED EXPERT", fill=(241, 245, 249, 255), font=get_font(13, 'bold'))
    
    draw.text((lx, 165), "Turn-by-Turn", fill=(255, 255, 255, 255), font=get_font(60, 'heavy'))
    draw.text((lx, 240), "Logistics & Fleet", fill=(56, 189, 248, 255), font=get_font(60, 'heavy'))
    draw.text((lx, 315), "App Development", fill=(255, 255, 255, 255), font=get_font(60, 'heavy'))
    
    draw.text((lx, 410), "Full-cycle Android & iOS mobile engineering for route optimization,", fill=(203, 213, 225, 255), font=get_font(21, 'regular'))
    draw.text((lx, 442), "turn-by-turn navigation, real-time driver dispatch, and POD.", fill=(203, 213, 225, 255), font=get_font(21, 'regular'))
    
    metrics_y = 510
    stat_cards = [
        ("10K+", "Daily Orders", (56, 189, 248, 255)),
        ("5+", "Countries Live", (16, 185, 129, 255)),
        ("11+", "Years Experience", (168, 85, 247, 255))
    ]
    card_w = 210
    for i, (val, label, col) in enumerate(stat_cards):
        cx = lx + i * (card_w + 16)
        draw_rounded_rect(draw, [(cx, metrics_y), (cx + card_w, metrics_y + 105)], radius=18, 
                          fill=(30, 41, 59, 230), outline=(71, 85, 105, 180), width=1)
        draw.text((cx + 20, metrics_y + 16), val, fill=col, font=get_font(36, 'heavy'))
        draw.text((cx + 20, metrics_y + 64), label, fill=(241, 245, 249, 255), font=get_font(13, 'bold'))

    feat_y = 650
    features = [
        "Dynamic turn-by-turn routing with ahead/behind schedule warnings",
        "Driver stop timeline, order transfer, & multi-stop manifest",
        "Photo proof & digital signature capture with offline sync",
        "Senior Mobile Architect: Jetpack Compose, Kotlin, Fastlane CI/CD"
    ]
    for i, feat in enumerate(features):
        fy = feat_y + i * 44
        draw_rounded_rect(draw, [(lx, fy + 2), (lx + 24, fy + 26)], radius=6, fill=(56, 189, 248, 160), outline=(56, 189, 248, 240), width=1)
        draw_vector_checkmark(draw, lx + 12, fy + 14, size=8, color=(255, 255, 255, 255), width=2)
        draw.text((lx + 36, fy + 4), feat, fill=(226, 232, 240, 255), font=get_font(16, 'demi'))

    foot_y = 860
    tech_tags = ["Android Lead", "Kotlin Expert", "Jetpack Compose", "Turn-by-Turn Maps", "Production Ready"]
    tx = lx
    for t in tech_tags:
        tf = get_font(14, 'bold')
        bbox = draw.textbbox((0, 0), t, font=tf)
        tw = bbox[2] - bbox[0] + 28
        draw_rounded_rect(draw, [(tx, foot_y), (tx + tw, foot_y + 44)], radius=22, 
                          fill=(2, 132, 199, 220), outline=(56, 189, 248, 255), width=1)
        draw.text((tx + 14, foot_y + 12), t, fill=(255, 255, 255, 255), font=tf)
        tx += tw + 12

    tablet_img_path = os.path.join(ASSETS_DIR, "media_1792120405803_32e54e5c.png")
    phone_img_path = "/Volumes/Work/spoonart.github.io/assets/shots/swat-driver-2.jpg"
    pod_img_path = os.path.join(ASSETS_DIR, "media_1792120405793_b99472a8.png")
    
    tablet = make_tablet_mockup(tablet_img_path, target_width=760)
    tab_shadowed, t_pad = create_shadow(tablet, offset=(0, 24), blur=45, opacity=0.75)
    img.paste(tab_shadowed, (980 - t_pad, 110 - t_pad), tab_shadowed)

    phone = make_phone_mockup(phone_img_path, target_width=320)
    phone_shadowed, ph_pad = create_shadow(phone, offset=(-12, 28), blur=45, opacity=0.85)
    img.paste(phone_shadowed, (940 - ph_pad, 360 - ph_pad), phone_shadowed)

    pod_card = make_pod_card_mockup(pod_img_path, target_width=370)
    pod_shadowed, pod_pad = create_shadow(pod_card, offset=(15, 22), blur=38, opacity=0.75)
    img.paste(pod_shadowed, (1440 - pod_pad, 520 - pod_pad), pod_shadowed)

    out_file = os.path.join(OUTPUT_DIR, "upwork_catalog_banner_minimal_bold.png")
    out_file_artifact = os.path.join(ARTIFACT_DIR, "upwork_catalog_banner_minimal_bold.png")
    img.convert('RGB').save(out_file, 'PNG', quality=95)
    img.convert('RGB').save(out_file_artifact, 'PNG', quality=95)
    print("Banner 3 refined successfully")

generate_banner_1()
generate_banner_2()
generate_banner_3()
print("All refined banners generated successfully!")
