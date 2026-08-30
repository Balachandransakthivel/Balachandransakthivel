"""Generate all Bala 3D avatar assets using PIL"""
import os, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WORKSPACE = Path(r"C:\Users\BALACHANDRAN S\Balachandransakthivel\assets")

def gradient_bg(w, h, c1, c2):
    img = Image.new("RGB", (w, h))
    for y in range(h):
        r = int(c1[0] + (c2[0]-c1[0])*y/h)
        g = int(c1[1] + (c2[1]-c1[1])*y/h)
        b = int(c1[2] + (c2[2]-c1[2])*y/h)
        ImageDraw.Draw(img).line([(0,y),(w,y)], fill=(r,g,b))
    return img

def draw_character(img, cx, cy, scale=1.0, pose="stand", expr="smile"):
    d = ImageDraw.Draw(img)
    s = scale
    # Body - white hoodie
    d.rounded_rectangle([cx-35*s, cy-10*s, cx+35*s, cy+60*s], radius=15, fill=(240,240,240), outline=(200,200,200))
    # Hoodie pocket
    d.rounded_rectangle([cx-20*s, cy+20*s, cx+20*s, cy+45*s], radius=8, fill=(225,225,225))
    # Head
    d.ellipse([cx-28*s, cy-65*s, cx+28*s, cy-5*s], fill=(210,170,130))
    # Hair - black styled
    d.ellipse([cx-30*s, cy-70*s, cx+30*s, cy-35*s], fill=(25,25,30))
    d.rectangle([cx-30*s, cy-55*s, cx+30*s, cy-40*s], fill=(25,25,30))
    # Glasses - black rectangular
    d.rounded_rectangle([cx-25*s, cy-42*s, cx-5*s, cy-28*s], radius=4, outline=(30,30,30), width=int(3*s))
    d.rounded_rectangle([cx+5*s, cy-42*s, cx+25*s, cy-28*s], radius=4, outline=(30,30,30), width=int(3*s))
    d.line([cx-5*s, cy-35*s, cx+5*s, cy-35*s], fill=(30,30,30), width=int(2*s))
    # Eyes
    if expr == "wink":
        d.ellipse([cx-18*s, cy-37*s, cx-12*s, cy-31*s], fill=(40,40,40))
        d.arc([cx+8*s, cy-37*s, cx+18*s, cy-30*s], 0, 180, fill=(40,40,40), width=int(2*s))
    else:
        d.ellipse([cx-18*s, cy-37*s, cx-12*s, cy-31*s], fill=(40,40,40))
        d.ellipse([cx+12*s, cy-37*s, cx+18*s, cy-31*s], fill=(40,40,40))
    # Eyebrows
    d.line([cx-22*s, cy-44*s, cx-10*s, cy-46*s], fill=(30,30,30), width=int(2*s))
    d.line([cx+10*s, cy-46*s, cx+22*s, cy-44*s], fill=(30,30,30), width=int(2*s))
    # Nose
    d.arc([cx-4*s, cy-30*s, cx+4*s, cy-20*s], 0, 180, fill=(180,140,100), width=int(1.5*s))
    # Mouth
    if expr == "smile" or expr == "happy":
        d.arc([cx-10*s, cy-22*s, cx+10*s, cy-12*s], 0, 180, fill=(180,100,80), width=int(2*s))
    elif expr == "open":
        d.ellipse([cx-6*s, cy-20*s, cx+6*s, cy-12*s], fill=(180,100,80))
    # Goatee
    d.ellipse([cx-5*s, cy-14*s, cx+5*s, cy-8*s], fill=(30,30,30))
    # Arms
    if pose == "laptop":
        d.line([cx-35*s, cy+10*s, cx-55*s, cy+35*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+55*s, cy+35*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx-60*s, cy+30*s, cx-48*s, cy+42*s], fill=(210,170,130))
        d.ellipse([cx+48*s, cy+30*s, cx+60*s, cy+42*s], fill=(210,170,130))
    elif pose == "wave":
        d.line([cx-35*s, cy+10*s, cx-50*s, cy+40*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+55*s, cy-20*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx+48*s, cy-30*s, cx+62*s, cy-16*s], fill=(210,170,130))
    elif pose == "thumbsup":
        d.line([cx-35*s, cy+10*s, cx-50*s, cy+40*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+50*s, cy-5*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx+45*s, cy-15*s, cx+57*s, cy-3*s], fill=(210,170,130))
        d.rectangle([cx+48*s, cy-25*s, cx+55*s, cy-12*s], fill=(210,170,130))
    elif pose == "celebrate":
        d.line([cx-35*s, cy+10*s, cx-55*s, cy-25*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+55*s, cy-25*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx-62*s, cy-35*s, cx-48*s, cy-21*s], fill=(210,170,130))
        d.ellipse([cx+48*s, cy-35*s, cx+62*s, cy-21*s], fill=(210,170,130))
    elif pose == "think":
        d.line([cx-35*s, cy+10*s, cx-50*s, cy+40*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+40*s, cy-15*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx+33*s, cy-25*s, cx+47*s, cy-11*s], fill=(210,170,130))
    elif pose == "idea":
        d.line([cx-35*s, cy+10*s, cx-50*s, cy+40*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+45*s, cy-20*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx+38*s, cy-30*s, cx+52*s, cy-16*s], fill=(210,170,130))
    elif pose == "coffee":
        d.line([cx-35*s, cy+10*s, cx-50*s, cy+40*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+45*s, cy+25*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx+38*s, cy+18*s, cx+52*s, cy+32*s], fill=(210,170,130))
        d.rounded_rectangle([cx+42*s, cy+5*s, cx+58*s, cy+28*s], radius=4, fill=(255,255,255), outline=(200,200,200))
    else:
        d.line([cx-35*s, cy+10*s, cx-50*s, cy+40*s], fill=(240,240,240), width=int(12*s))
        d.line([cx+35*s, cy+10*s, cx+50*s, cy+40*s], fill=(240,240,240), width=int(12*s))
        d.ellipse([cx-57*s, cy+34*s, cx-43*s, cy+48*s], fill=(210,170,130))
        d.ellipse([cx+43*s, cy+34*s, cx+57*s, cy+48*s], fill=(210,170,130))
    # Pants - black with white stripes
    d.rectangle([cx-30*s, cy+58*s, cx-2*s, cy+110*s], fill=(20,20,25))
    d.rectangle([cx+2*s, cy+58*s, cx+30*s, cy+110*s], fill=(20,20,25))
    d.line([cx-28*s, cy+58*s, cx-28*s, cy+110*s], fill=(255,255,255), width=int(2*s))
    d.line([cx-24*s, cy+58*s, cx-24*s, cy+110*s], fill=(255,255,255), width=int(2*s))
    d.line([cx+24*s, cy+58*s, cx+24*s, cy+110*s], fill=(255,255,255), width=int(2*s))
    d.line([cx+28*s, cy+58*s, cx+28*s, cy+110*s], fill=(255,255,255), width=int(2*s))
    # Shoes - white
    d.rounded_rectangle([cx-35*s, cy+105*s, cx-5*s, cy+118*s], radius=6, fill=(240,240,240), outline=(200,200,200))
    d.rounded_rectangle([cx+5*s, cy+105*s, cx+35*s, cy+118*s], radius=6, fill=(240,240,240), outline=(200,200,200))

def add_glow(img, cx, cy, radius, color):
    overlay = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -2):
        alpha = int(30 * (1 - r/radius))
        d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(*color, alpha))
    return Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

def add_particles(img, count=20, color=(0,200,255)):
    d = ImageDraw.Draw(img)
    import random
    random.seed(42)
    for _ in range(count):
        x = random.randint(0, img.width-1)
        y = random.randint(0, img.height-1)
        r = random.randint(1,3)
        alpha = random.randint(80,200)
        d.ellipse([x-r, y-r, x+r, y+r], fill=(*color[:3],))

# ===== CREATE ALL ASSETS =====
print("Generating assets...")

# 1. Hero banner (wide)
hero = gradient_bg(1200, 400, (10,15,35), (20,10,50))
draw_character(hero, 700, 220, scale=2.2, pose="laptop", expr="smile")
add_particles(hero, 40, (0,200,255))
# Hologram effect
d = ImageDraw.Draw(hero)
d.rounded_rectangle([350, 80, 600, 320], radius=15, outline=(0,200,255), width=2)
d.text((380, 100), "</> CODE", fill=(0,200,255))
d.text((380, 140), "AI MODEL", fill=(150,100,255))
d.text((380, 180), "REACT + TS", fill=(0,200,255))
hero.save(WORKSPACE/"hero"/"hero-3d.gif", "GIF")
print("  [OK] hero/hero-3d.gif")

# 2. Developer master (stand)
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 256, 220, scale=2.0, pose="stand", expr="smile")
add_particles(p, 15, (0,200,255))
p.save(WORKSPACE/"characters"/"developer.png", "PNG")
print("  [OK] characters/developer.png")

# 3. Developer laptop
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 256, 200, scale=1.8, pose="laptop", expr="smile")
# Laptop
d = ImageDraw.Draw(p)
d.rounded_rectangle([180, 280, 340, 310], radius=5, fill=(50,50,60))
d.rectangle([190, 240, 330, 285], fill=(30,40,60))
d.text((200, 250), "</>", fill=(0,200,255))
add_particles(p, 10, (0,200,255))
p.save(WORKSPACE/"characters"/"developer-laptop.png", "PNG")
print("  [OK] characters/developer-laptop.png")

# 4. Developer AI
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 200, 220, scale=2.0, pose="think", expr="happy")
# AI hologram
d = ImageDraw.Draw(p)
d.rounded_rectangle([310, 100, 470, 300], radius=12, outline=(0,200,255), width=2)
d.text((330, 120), "AI", fill=(0,200,255))
d.text((330, 160), "Neural", fill=(150,100,255))
d.text((330, 190), "Network", fill=(150,100,255))
d.text((330, 230), "Data", fill=(0,200,255))
add_particles(p, 20, (0,200,255))
p = add_glow(p, 390, 200, 80, (0,200,255))
p.save(WORKSPACE/"characters"/"developer-ai.png", "PNG")
print("  [OK] characters/developer-ai.png")

# 5. Developer coding
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 256, 200, scale=1.8, pose="laptop", expr="open")
d = ImageDraw.Draw(p)
d.rounded_rectangle([170, 280, 350, 310], radius=5, fill=(50,50,60))
d.rectangle([175, 235, 345, 285], fill=(20,25,40))
for i, line in enumerate(["def build():", "  model.train()", "  return ai"]):
    d.text((185, 245+i*14), line, fill=(0,220,180))
add_particles(p, 10, (0,200,255))
p.save(WORKSPACE/"characters"/"developer-coding.png", "PNG")
print("  [OK] characters/developer-coding.png")

# 6. Developer thinking
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 256, 220, scale=2.0, pose="think", expr="smile")
d = ImageDraw.Draw(p)
d.ellipse([310, 80, 340, 110], fill=(255,200,0))
d.text((305, 55), "?", fill=(150,100,255))
d.text((345, 65), "?", fill=(100,150,255))
add_particles(p, 10, (255,200,0))
p.save(WORKSPACE/"characters"/"developer-thinking.png", "PNG")
print("  [OK] characters/developer-thinking.png")

# 7. Developer idea
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 256, 220, scale=2.0, pose="idea", expr="happy")
d = ImageDraw.Draw(p)
d.ellipse([320, 60, 370, 110], fill=(255,220,50))
d.text((335, 75), "!", fill=(50,50,50))
p = add_glow(p, 345, 85, 40, (255,220,50))
add_particles(p, 15, (255,220,50))
p.save(WORKSPACE/"characters"/"developer-idea.png", "PNG")
print("  [OK] characters/developer-idea.png")

# 8. Developer coffee
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 256, 220, scale=2.0, pose="coffee", expr="smile")
d = ImageDraw.Draw(p)
# Steam
for i in range(3):
    x = 305 + i*15
    d.arc([x-5, 150+i*10, x+5, 170+i*10], 180, 360, fill=(180,180,180), width=1)
p.save(WORKSPACE/"characters"/"developer-coffee.png", "PNG")
print("  [OK] characters/developer-coffee.png")

# 9. Developer focused
p = gradient_bg(512, 512, (15,20,40), (25,15,50))
draw_character(p, 256, 200, scale=1.8, pose="laptop", expr="wink")
d = ImageDraw.Draw(p)
d.rounded_rectangle([170, 280, 350, 310], radius=5, fill=(50,50,60))
d.rectangle([175, 235, 345, 285], fill=(20,25,40))
d.text((185, 250), "FOCUS MODE", fill=(255,100,100))
# Headphones
d.arc([cx:=220, 140, 290, 200], 180, 360, fill=(40,40,40), width=int(6))
d.ellipse([210, 155, 230, 185], fill=(40,40,40))
d.ellipse([280, 155, 300, 185], fill=(40,40,40))
add_particles(p, 10, (255,100,100))
p.save(WORKSPACE/"characters"/"developer-focused.png", "PNG")
print("  [OK] characters/developer-focused.png")

# 10. Developer idle
p = gradient_bg(512, 512, (255,200,220), (255,180,200))
# Hearts background
d2 = ImageDraw.Draw(p)
import random
random.seed(123)
for _ in range(30):
    x, y = random.randint(0,511), random.randint(0,511)
    hs = random.randint(5,15)
    d2.text((x, y), "\u2665", fill=(255,random.randint(150,200),random.randint(180,220)))
draw_character(p, 256, 220, scale=2.0, pose="stand", expr="smile")
p.save(WORKSPACE/"characters"/"developer-idle.gif", "GIF")
print("  [OK] characters/developer-idle.gif")

# 11. Animations - typing
p = gradient_bg(400, 400, (15,20,40), (25,15,50))
draw_character(p, 200, 160, scale=1.5, pose="laptop", expr="smile")
d = ImageDraw.Draw(p)
d.rounded_rectangle([120, 240, 280, 265], radius=4, fill=(50,50,60))
d.rectangle([125, 200, 275, 245], fill=(20,25,40))
d.text((135, 210), "coding...", fill=(0,220,180))
add_particles(p, 10, (0,200,255))
p.save(WORKSPACE/"animations"/"typing.png", "PNG")
print("  [OK] animations/typing.png")

# 12. Waving
p = gradient_bg(400, 400, (15,20,40), (25,15,50))
draw_character(p, 200, 180, scale=1.8, pose="wave", expr="happy")
d = ImageDraw.Draw(p)
d.text((310, 80), "Hi!", fill=(255,255,255))
add_particles(p, 10, (0,200,255))
p.save(WORKSPACE/"animations"/"waving.png", "PNG")
print("  [OK] animations/waving.png")

# 13. Thumbs up
p = gradient_bg(400, 400, (15,20,40), (25,15,50))
draw_character(p, 200, 180, scale=1.8, pose="thumbsup", expr="happy")
d = ImageDraw.Draw(p)
d.text((300, 100), "OK!", fill=(0,255,150))
add_particles(p, 10, (0,255,150))
p.save(WORKSPACE/"animations"/"thumbs-up.png", "PNG")
print("  [OK] animations/thumbs-up.png")

# 14. Celebrating
p = gradient_bg(400, 400, (15,20,40), (25,15,50))
draw_character(p, 200, 180, scale=1.8, pose="celebrate", expr="open")
d = ImageDraw.Draw(p)
for i in range(15):
    x, y = random.randint(50,350), random.randint(30,150)
    c = [(255,200,0),(0,200,255),(255,100,200),(0,255,150)][i%4]
    d.text((x, y), "\u2605", fill=c)
p.save(WORKSPACE/"animations"/"celebrating.png", "PNG")
print("  [OK] animations/celebrating.png")

# 15. Coding animation (gif-like)
p = gradient_bg(400, 400, (15,20,40), (25,15,50))
draw_character(p, 200, 160, scale=1.5, pose="laptop", expr="smile")
d = ImageDraw.Draw(p)
d.rounded_rectangle([120, 240, 280, 265], radius=4, fill=(50,50,60))
d.rectangle([125, 200, 275, 245], fill=(20,25,40))
for i, line in enumerate(["const ai = new AI()", "await model.train()", "deploy()"]):
    d.text((135, 210+i*12), line, fill=(0,220,180))
add_particles(p, 15, (0,200,255))
p.save(WORKSPACE/"animations"/"coding.gif", "GIF")
print("  [OK] animations/coding.gif")

# 16. Rocket
p = gradient_bg(400, 400, (10,10,30), (20,10,40))
# Stars
d = ImageDraw.Draw(p)
random.seed(99)
for _ in range(40):
    x, y = random.randint(0,399), random.randint(0,150)
    d.ellipse([x,y,x+2,y+2], fill=(255,255,255))
# Rocket
d.polygon([(200,50),(180,180),(220,180)], fill=(200,200,210))
d.ellipse([185,40,215,80], fill=(200,200,210))
d.polygon([(180,180),(165,220),(185,180)], fill=(255,100,50))
d.polygon([(220,180),(235,220),(215,180)], fill=(255,100,50))
d.polygon([(190,180),(200,240),(210,180)], fill=(255,200,50))
# Flame
d.polygon([(195,230),(200,270),(205,230)], fill=(255,150,0))
d.polygon([(198,250),(200,290),(202,250)], fill=(255,255,100))
# Developer waving
draw_character(p, 300, 280, scale=0.8, pose="celebrate", expr="happy")
add_particles(p, 20, (255,200,50))
p.save(WORKSPACE/"animations"/"rocket.gif", "GIF")
print("  [OK] animations/rocket.gif")

# 17-20. Project mockups
for name, title, color in [
    ("cafe-pro.png", "CAFE PRO\nRestaurant SaaS", (0,150,200)),
    ("levelup-ai.png", "LEVEL UP AI\nLearning Platform", (150,50,255)),
    ("mediq-ai.png", "MEDIQ AI\nHealthcare Queue", (0,200,150)),
    ("mindease.png", "MIND EASE\nWellness AI", (100,150,255)),
]:
    p = gradient_bg(800, 500, (15,18,35), (25,12,50))
    d = ImageDraw.Draw(p)
    # Browser mockup
    d.rounded_rectangle([50, 40, 750, 460], radius=12, outline=(60,60,80), width=2)
    d.rectangle([50, 40, 750, 75], fill=(30,30,45))
    d.ellipse([65, 52, 77, 64], fill=(255,95,86))
    d.ellipse([85, 52, 97, 64], fill=(255,189,46))
    d.ellipse([105, 52, 117, 64], fill=(39,201,63))
    d.text((350, 50), title.split("\n")[0], fill=(200,200,220))
    # Dashboard cards
    for i in range(3):
        x = 80 + i*220
        d.rounded_rectangle([x, 90, x+200, 200], radius=8, fill=(35,40,60), outline=(60,70,100))
        d.text((x+15, 105), ["Revenue", "Users", "Growth"][i], fill=(150,160,180))
        d.text((x+15, 140), ["$12.5K", "1,240", "+28%"][i], fill=color)
    # Chart area
    d.rounded_rectangle([80, 220, 720, 440], radius=8, fill=(35,40,60))
    pts = [(100,380),(200,320),(300,350),(400,280),(500,300),(600,250),(700,270)]
    d.line(pts, fill=color, width=2)
    for x,y in pts:
        d.ellipse([x-4,y-4,x+4,y+4], fill=color)
    p.save(WORKSPACE/"projects"/name, "PNG")
    print(f"  [OK] projects/{name}")

print("\n" + "="*50)
print("  ALL ASSETS GENERATED!")
print("="*50)
print(f"\n  Location: {WORKSPACE}")
print("\n  Replace these with your actual 3D renders")
print("  using the prompts from the asset pack guide.")
