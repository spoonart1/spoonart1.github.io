import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def make_rounded_mask(size, radius):
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=255)
    return mask

def add_drop_shadow(image, offset=(0, 15), blur_radius=25, shadow_color=(0, 0, 0, 140)):
    w, h = image.size
    shadow_w = w + blur_radius * 4
    shadow_h = h + blur_radius * 4
    shadow = Image.new('RGBA', (shadow_w, shadow_h), (0, 0, 0, 0))
    
    # Shadow shape
    s_draw = ImageDraw.Draw(shadow)
    sx0 = blur_radius * 2 + offset[0]
    sy0 = blur_radius * 2 + offset[1]
    
    # Create shadow mask from image alpha if available
    if image.mode == 'RGBA':
        alpha = image.split()[3]
        s_base = Image.new('L', (shadow_w, shadow_h), 0)
        s_base.paste(alpha, (sx0, sy0))
        s_blur = s_base.filter(ImageFilter.GaussianBlur(blur_radius))
        
        # Colorize
        s_colored = Image.new('RGBA', (shadow_w, shadow_h), shadow_color[:3] + (0,))
        s_colored.putalpha(s_blur.point(lambda p: int(p * (shadow_color[3] / 255.0))))
        shadow = s_colored
    else:
        # Rectangle shadow
        s_draw.rectangle([sx0, sy0, sx0 + w, sy0 + h], fill=shadow_color)
        shadow = shadow.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # Paste image on top
    result = Image.new('RGBA', (shadow_w, shadow_h), (0, 0, 0, 0))
    result.paste(shadow, (0, 0), shadow)
    result.paste(image, (blur_radius * 2, blur_radius * 2), image if image.mode == 'RGBA' else None)
    return result, blur_radius * 2

print("Drop shadow helper ready")
