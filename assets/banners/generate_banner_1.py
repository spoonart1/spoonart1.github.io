import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ASSETS_DIR = "/Volumes/Work/spoonart.github.io/assets/banners"
OUTPUT_DIR = "/Volumes/Work/spoonart.github.io/assets/banners"
ARTIFACT_DIR = "/Users/user/.gemini/antigravity/brain/eb20549e-b3f5-4543-ba1a-a72a936bc683"

def get_font(size, weight='bold'):
    # Available weights in Avenir Next:
    # 0: Bold, 2: Demi Bold, 5: Medium, 7: Regular, 8: Heavy
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

def create_shadow(image_rgba, offset=(0, 20), blur=35, opacity=0.6, color=(0, 0, 0)):
    w, h = image_rgba.size
    pad = blur * 3
    shadow_layer = Image.new('RGBA', (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    alpha = image_rgba.split()[3]
    
    # Create mask in position
    ox = pad + offset[0]
    oy = pad + offset[1]
    
    mask_layer = Image.new('L', (w + pad * 2, h + pad * 2), 0)
    mask_layer.paste(alpha, (ox, oy))
    mask_blurred = mask_layer.filter(ImageFilter.GaussianBlur(blur))
    
    # Apply color and opacity
    r, g, b = color
    s_col = Image.new('RGBA', (w + pad * 2, h + pad * 2), (r, g, b, 0))
    s_col.putalpha(mask_blurred.point(lambda p: int(p * opacity)))
    
    # Composite image over shadow
    final_canvas = Image.new('RGBA', (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    final_canvas.paste(s_col, (0, 0), s_col)
    final_canvas.paste(image_rgba, (pad, pad), image_rgba)
    
    return final_canvas, pad

def make_tablet_mockup(screen_img_path, target_width=640):
    screen = Image.open(screen_img_path).convert('RGBA')
    # Aspect ratio of screen
    sw, sh = screen.size
    target_height = int(target_width * (sh / sw))
    screen = screen.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Bezel dimensions
    bezel = 18
    fw = target_width + bezel * 2
    fh = target_height + bezel * 2
    radius = 28
    
    frame = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    # Outer tablet body (dark metallic slate)
    draw_rounded_rect(draw, [(0, 0), (fw - 1, fh - 1)], radius=radius, fill=(24, 32, 47, 255), outline=(51, 65, 85, 255), width=2)
    # Inner subtle rim
    draw_rounded_rect(draw, [(3, 3), (fw - 4, fh - 4)], radius=radius - 2, outline=(15, 23, 42, 255), width=2)
    
    # Front camera dot (at top bezel center)
    cam_x = fw // 2
    cam_y = bezel // 2
    draw.ellipse([(cam_x - 3, cam_y - 3), (cam_x + 3, cam_y + 3)], fill=(10, 15, 25, 255), outline=(40, 50, 70, 255))
    draw.ellipse([(cam_x - 1, cam_y - 1), (cam_x + 1, cam_y + 1)], fill=(20, 60, 100, 255))
    
    # Rounded mask for screen
    screen_radius = 12
    screen_mask = Image.new('L', (target_width, target_height), 0)
    s_draw = ImageDraw.Draw(screen_mask)
    draw_rounded_rect(s_draw, [(0, 0), (target_width, target_height)], radius=screen_radius, fill=255)
    
    frame.paste(screen, (bezel, bezel), screen_mask)
    
    # Gloss highlight along top-left edge
    highlight = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(highlight)
    draw_rounded_rect(h_draw, [(1, 1), (fw - 2, fh - 2)], radius=radius, outline=(255, 255, 255, 35), width=1)
    frame = Image.alpha_composite(frame, highlight)
    
    return frame

def make_phone_mockup(screen_img_path, target_width=290):
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
    
    # Outer dark titanium rim
    draw_rounded_rect(draw, [(0, 0), (fw - 1, fh - 1)], radius=radius, fill=(18, 22, 31, 255), outline=(71, 85, 105, 255), width=2)
    draw_rounded_rect(draw, [(2, 2), (fw - 3, fh - 3)], radius=radius - 2, fill=(12, 16, 24, 255))
    
    # Rounded mask for screen
    screen_radius = 32
    screen_mask = Image.new('L', (target_width, target_height), 0)
    s_draw = ImageDraw.Draw(screen_mask)
    draw_rounded_rect(s_draw, [(0, 0), (target_width, target_height)], radius=screen_radius, fill=255)
    
    frame.paste(screen, (bezel, bezel), screen_mask)
    
    # Dynamic Island / Punch Hole at top
    di_w, di_h = 75, 18
    di_x = (fw - di_w) // 2
    di_y = bezel + 6
    draw_rounded_rect(draw, [(di_x, di_y), (di_x + di_w, di_y + di_h)], radius=9, fill=(0, 0, 0, 255))
    # Camera dot inside island
    draw.ellipse([(di_x + 14, di_y + 4), (di_x + 24, di_y + 14)], fill=(15, 25, 45, 255))
    
    # Outer highlight
    highlight = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(highlight)
    draw_rounded_rect(h_draw, [(1, 1), (fw - 2, fh - 2)], radius=radius, outline=(255, 255, 255, 45), width=1)
    frame = Image.alpha_composite(frame, highlight)
    
    return frame

def make_pod_card_mockup(screen_img_path, target_width=320):
    b99 = Image.open(screen_img_path).convert('RGBA')
    # Crop the relevant card area (recipient, photo, signature, go to next stop)
    # The image is 361 x 641
    cropped = b99.crop((14, 115, 347, 515))
    cw, ch = cropped.size
    target_height = int(target_width * (ch / cw))
    cropped = cropped.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    pad = 10
    fw = target_width + pad * 2
    fh = target_height + pad * 2 + 36 # Extra top bar for header
    radius = 20
    
    frame = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    # Card background (clean white/glass)
    draw_rounded_rect(draw, [(0, 0), (fw - 1, fh - 1)], radius=radius, fill=(255, 255, 255, 250), outline=(226, 232, 240, 255), width=2)
    
    # Top card header banner
    draw_rounded_rect(draw, [(4, 4), (fw - 5, 36)], radius=12, fill=(241, 245, 249, 255))
    
    # Green status dot & text
    draw.ellipse([(14, 15), (24, 25)], fill=(16, 185, 129, 255))
    f_badge = get_font(13, 'bold')
    draw.text((32, 12), "PROOF OF DELIVERY (POD)", fill=(30, 41, 59, 255), font=f_badge)
    
    f_sub = get_font(11, 'medium')
    draw.text((fw - 110, 13), "Photo + Signature", fill=(100, 116, 139, 255), font=f_sub)
    
    # Rounded mask for cropped image
    c_mask = Image.new('L', (target_width, target_height), 0)
    c_draw = ImageDraw.Draw(c_mask)
    draw_rounded_rect(c_draw, [(0, 0), (target_width, target_height)], radius=14, fill=255)
    
    frame.paste(cropped, (pad, 40), c_mask)
    
    return frame

def draw_background_grid_and_routes(base_draw, width, height, theme='dark_tech'):
    # Subtle routing vector lines suggesting a GPS navigation map
    if theme == 'dark_tech':
        route_color = (6, 182, 212, 38) # Cyan glow
        route_color_bright = (59, 130, 246, 50) # Blue glow
        dot_color = (148, 163, 184, 18)
    elif theme == 'ecosystem':
        route_color = (16, 185, 129, 35) # Emerald
        route_color_bright = (14, 165, 233, 45) # Sky blue
        dot_color = (148, 163, 184, 18)
    else:
        route_color = (99, 102, 241, 35) # Indigo
        route_color_bright = (168, 85, 247, 45) # Purple
        dot_color = (148, 163, 184, 18)

    # Grid dots
    step = 40
    for x in range(0, width, step):
        for y in range(0, height, step):
            base_draw.ellipse([(x - 1, y - 1), (x + 1, y + 1)], fill=dot_color)
            
    # Stylized route network lines across right side
    routes = [
        [(850, 200), (1050, 150), (1200, 280), (1450, 220), (1750, 310)],
        [(920, 480), (1100, 420), (1350, 560), (1600, 490), (1850, 600)],
        [(1020, 750), (1220, 680), (1400, 820), (1700, 740), (1880, 890)],
        [(1150, 100), (1250, 350), (1300, 650), (1400, 920)],
        [(1500, 150), (1550, 450), (1650, 700), (1700, 950)],
    ]
    for r in routes:
        for i in range(len(r) - 1):
            base_draw.line([r[i], r[i+1]], fill=route_color, width=2)
            # Route nodes
            base_draw.ellipse([(r[i][0]-3, r[i][1]-3), (r[i][0]+3, r[i][1]+3)], fill=route_color_bright)
        base_draw.ellipse([(r[-1][0]-4, r[-1][1]-4), (r[-1][0]+4, r[-1][1]+4)], fill=route_color_bright)

def create_banner_1_dark_tech():
    W, H = 1920, 1080 # 16:9 ratio
    img = Image.new('RGBA', (W, H), (10, 15, 26, 255))
    
    # Ambient gradient glow
    glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow_layer)
    # Right-hand ambient tech glow (cyan/blue)
    g_draw.ellipse([(1100, 150), (1850, 900)], fill=(14, 116, 144, 45))
    g_draw.ellipse([(1250, 300), (1750, 800)], fill=(37, 99, 235, 40))
    # Left-hand subtle glow
    g_draw.ellipse([(-100, -100), (600, 500)], fill=(30, 58, 138, 30))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(100))
    img = Image.alpha_composite(img, glow_layer)
    
    draw = ImageDraw.Draw(img)
    draw_background_grid_and_routes(draw, W, H, theme='dark_tech')
    
    # --- LEFT COLUMN: VALUE PROPOSITION & CREDIBILITY ---
    lx = 100
    
    # Category Tag Pill
    tag_bg = [(lx, 100), (lx + 360, 142)]
    draw_rounded_rect(draw, tag_bg, radius=21, fill=(15, 23, 42, 220), outline=(6, 182, 212, 180), width=1)
    # Pulsing dot
    draw.ellipse([(lx + 16, 116), (lx + 26, 126)], fill=(16, 185, 129, 255))
    f_tag = get_font(14, 'bold')
    draw.text((lx + 34, 113), "LOGISTICS & FLEET MOBILE APPS", fill=(103, 232, 249, 255), font=f_tag)
    
    # Main Headline (Crisp, High Impact, legible on Upwork search thumbnail)
    f_h1 = get_font(56, 'heavy')
    f_h1_accent = get_font(56, 'heavy')
    
    draw.text((lx, 168), "Delivery & Fleet", fill=(255, 255, 255, 255), font=f_h1)
    draw.text((lx, 236), "Driver App", fill=(56, 189, 248, 255), font=f_h1_accent)
    draw.text((lx + 330, 236), "Development", fill=(255, 255, 255, 255), font=f_h1)
    
    # Subheadline
    f_sub = get_font(20, 'regular')
    sub_text1 = "Turn-by-turn navigation, real-time fleet dispatch, and automated"
    sub_text2 = "route optimization built for production enterprise operations."
    draw.text((lx, 318), sub_text1, fill=(148, 163, 184, 255), font=f_sub)
    draw.text((lx, 348), sub_text2, fill=(148, 163, 184, 255), font=f_sub)
    
    # --- METRICS PILLARS (Trust & Production Proof) ---
    metrics_y = 410
    metrics = [
        ("10,000+", "Daily Delivery Orders"),
        ("5 Countries", "Live in Production"),
        ("100% Solo", "Core Architecture")
    ]
    card_w = 210
    for i, (val, label) in enumerate(metrics):
        cx = lx + i * (card_w + 16)
        # Card background
        draw_rounded_rect(draw, [(cx, metrics_y), (cx + card_w, metrics_y + 88)], radius=14, 
                          fill=(17, 24, 39, 230), outline=(51, 65, 85, 180), width=1)
        f_val = get_font(25, 'heavy')
        f_lbl = get_font(12, 'medium')
        # Value
        draw.text((cx + 18, metrics_y + 16), val, fill=(255, 255, 255, 255), font=f_val)
        # Label
        draw.text((cx + 18, metrics_y + 52), label, fill=(56, 189, 248, 255), font=f_lbl)

    # --- FEATURE BULLETS ---
    feat_y = 535
    features = [
        "Turn-by-turn navigation with dynamic ETA & early/late warnings",
        "Multi-stop route planning & automatic order reassignment",
        "Proof of Delivery (POD): digital signature & photo capture",
        "Tablet in-cab & mobile-optimized UI (Android & iOS)"
    ]
    f_feat = get_font(16, 'demi')
    for i, feat in enumerate(features):
        fy = feat_y + i * 44
        # Glowing bullet badge
        draw_rounded_rect(draw, [(lx, fy + 2), (lx + 24, fy + 26)], radius=6, fill=(14, 116, 144, 180), outline=(6, 182, 212, 255), width=1)
        draw.text((lx + 6, fy + 4), "✓", fill=(255, 255, 255, 255), font=get_font(14, 'bold'))
        draw.text((lx + 36, fy + 4), feat, fill=(226, 232, 240, 255), font=f_feat)

    # --- TECH STACK PILLS AT BOTTOM ---
    tech_y = 750
    draw.text((lx, tech_y), "ENGINEERED WITH:", fill=(100, 116, 139, 255), font=get_font(12, 'bold'))
    
    tags = ["Android", "Kotlin", "Jetpack Compose", "Maps SDK", "Turn-by-Turn", "Fastlane", "Play Store"]
    tx = lx
    for t in tags:
        tf = get_font(13, 'medium')
        bbox = draw.textbbox((0, 0), t, font=tf)
        tw = bbox[2] - bbox[0] + 24
        draw_rounded_rect(draw, [(tx, tech_y + 24), (tx + tw, tech_y + 54)], radius=8, 
                          fill=(30, 41, 59, 180), outline=(71, 85, 105, 180), width=1)
        draw.text((tx + 12, tech_y + 31), t, fill=(203, 213, 225, 255), font=tf)
        tx += tw + 10
        
    # --- FOOTER BADGE / VALUE BANNER ---
    foot_y = 860
    draw_rounded_rect(draw, [(lx, foot_y), (lx + 660, foot_y + 68)], radius=16, 
                      fill=(15, 23, 42, 240), outline=(59, 130, 246, 200), width=1)
    draw.ellipse([(lx + 20, foot_y + 24), (lx + 40, foot_y + 44)], fill=(37, 99, 235, 255))
    draw.text((lx + 26, foot_y + 25), "★", fill=(255, 255, 255, 255), font=get_font(14, 'bold'))
    draw.text((lx + 52, foot_y + 16), "Production-Tested Mobility Architecture", fill=(255, 255, 255, 255), font=get_font(15, 'bold'))
    draw.text((lx + 52, foot_y + 38), "Zero unhandled crashes · Handles peak delivery traffic across Asia & Middle East", fill=(148, 163, 184, 255), font=get_font(13, 'regular'))

    # =========================================================================
    # --- RIGHT COLUMN: LAYERED DEVICE MOCKUPS (TABLET + PHONE + POD CARD) ---
    # =========================================================================
    tablet_img_path = os.path.join(ASSETS_DIR, "media_1792120405803_32e54e5c.png")
    phone_img_path = "/Volumes/Work/spoonart.github.io/assets/shots/swat-driver-2.jpg"
    pod_img_path = os.path.join(ASSETS_DIR, "media_1792120405793_b99472a8.png")
    
    # 1. Build Tablet Mockup (Base layer, right side)
    tablet = make_tablet_mockup(tablet_img_path, target_width=780)
    tablet_shadowed, t_pad = create_shadow(tablet, offset=(0, 25), blur=40, opacity=0.75, color=(0, 0, 0))
    
    # Position tablet: Top-Right
    tab_x = 980 - t_pad
    tab_y = 110 - t_pad
    img.paste(tablet_shadowed, (tab_x, tab_y), tablet_shadowed)
    
    # Floating Pill over Tablet: "🟢 In-Cab Navigation Tablet"
    pill_img = Image.new('RGBA', (320, 48), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(pill_img)
    draw_rounded_rect(p_draw, [(0, 0), (319, 47)], radius=24, fill=(15, 23, 42, 240), outline=(56, 189, 248, 220), width=1)
    p_draw.ellipse([(14, 18), (26, 30)], fill=(16, 185, 129, 255))
    p_draw.text((36, 15), "IN-CAB TABLET DISPATCH UI", fill=(255, 255, 255, 255), font=get_font(13, 'bold'))
    pill_shadowed, p_pad = create_shadow(pill_img, offset=(0, 8), blur=16, opacity=0.6)
    img.paste(pill_shadowed, (1030 - p_pad, 130 - p_pad), pill_shadowed)

    # 2. Build Phone Mockup (Overlapping left-center of tablet)
    phone = make_phone_mockup(phone_img_path, target_width=320)
    phone_shadowed, ph_pad = create_shadow(phone, offset=(-10, 30), blur=45, opacity=0.85, color=(0, 0, 0))
    
    ph_x = 940 - ph_pad
    ph_y = 350 - ph_pad
    img.paste(phone_shadowed, (ph_x, ph_y), phone_shadowed)
    
    # Floating Pill over Phone: "📱 Driver Mobile App"
    phone_pill = Image.new('RGBA', (260, 44), (0, 0, 0, 0))
    pp_draw = ImageDraw.Draw(phone_pill)
    draw_rounded_rect(pp_draw, [(0, 0), (259, 43)], radius=22, fill=(15, 23, 42, 240), outline=(16, 185, 129, 220), width=1)
    pp_draw.ellipse([(14, 16), (24, 26)], fill=(56, 189, 248, 255))
    pp_draw.text((32, 13), "DRIVER NAVIGATION APP", fill=(255, 255, 255, 255), font=get_font(12, 'bold'))
    pp_shadowed, pp_pad = create_shadow(phone_pill, offset=(0, 8), blur=15, opacity=0.6)
    img.paste(pp_shadowed, (970 - pp_pad, 365 - pp_pad), pp_shadowed)

    # 3. Build Proof of Delivery (POD) Floating Card
    pod_card = make_pod_card_mockup(pod_img_path, target_width=360)
    pod_shadowed, pod_pad = create_shadow(pod_card, offset=(15, 25), blur=40, opacity=0.75, color=(0, 0, 0))
    
    pod_x = 1430 - pod_pad
    pod_y = 540 - pod_pad
    img.paste(pod_shadowed, (pod_x, pod_y), pod_shadowed)
    
    # Floating status check badge next to POD
    status_card = Image.new('RGBA', (270, 60), (0, 0, 0, 0))
    sc_draw = ImageDraw.Draw(status_card)
    draw_rounded_rect(sc_draw, [(0, 0), (269, 59)], radius=14, fill=(16, 185, 129, 245), outline=(255, 255, 255, 200), width=1)
    sc_draw.text((16, 12), "✓ REAL-TIME SYNC", fill=(255, 255, 255, 255), font=get_font(13, 'bold'))
    sc_draw.text((16, 32), "Instant Dispatcher Updates", fill=(236, 253, 245, 255), font=get_font(11, 'medium'))
    sc_shadowed, sc_pad = create_shadow(status_card, offset=(0, 10), blur=20, opacity=0.5)
    img.paste(sc_shadowed, (1480 - sc_pad, 870 - sc_pad), sc_shadowed)

    out_file1 = os.path.join(OUTPUT_DIR, "upwork_catalog_banner_dark_tech.png")
    out_file1_artifact = os.path.join(ARTIFACT_DIR, "upwork_catalog_banner_dark_tech.png")
    img.convert('RGB').save(out_file1, 'PNG', quality=95)
    img.convert('RGB').save(out_file1_artifact, 'PNG', quality=95)
    print("Banner 1 generated:", out_file1)

create_banner_1_dark_tech()
