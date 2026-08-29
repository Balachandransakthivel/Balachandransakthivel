"""
Setup script - creates placeholder images and the full asset structure.
Run this first, then replace placeholder.png with your actual images.
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WORKSPACE = Path(r"C:\Users\BALACHANDRAN S\Balachandransakthivel")
ASSETS = WORKSPACE / "assets"

FOLDERS = {
    "hero": ASSETS / "hero",
    "characters": ASSETS / "characters",
    "projects": ASSETS / "projects",
    "animations": ASSETS / "animations",
}

# Colors for placeholders
COLORS = {
    "hero": (15, 23, 42),        # Dark navy
    "character": (30, 41, 59),   # Slate
    "animation": (30, 27, 75),   # Indigo dark
    "project": (17, 24, 39),     # Gray 900
}

def create_folders():
    for folder in FOLDERS.values():
        folder.mkdir(parents=True, exist_ok=True)
    print("[OK] Folders created")

def make_placeholder(name, width, height, color, label=""):
    """Create a placeholder image with label text"""
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle([2, 2, width-3, height-3], outline=(100, 116, 139), width=2)
    
    # Draw label
    if label:
        try:
            font = ImageFont.truetype("arial.ttf", max(14, min(width, height) // 15))
        except:
            font = ImageFont.load_default()
        
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = (width - tw) // 2
        y = (height - th) // 2
        draw.text((x, y), label, fill=(148, 163, 184), font=font)
    
    return img

def create_placeholders():
    """Create all placeholder images"""
    
    # Hero (wide banner)
    hero = make_placeholder("hero-3d.gif", 1200, 400, COLORS["hero"], "HERO - Replace with hero-3d.gif")
    hero.save(ASSETS / "hero" / "hero-3d.gif", "GIF")
    print("  [OK] hero/hero-3d.gif")
    
    # Characters
    char_placeholders = [
        ("developer.png", 512, 512, "MASTER - Replace with developer.png"),
        ("developer-laptop.png", 512, 512, "Replace with developer-laptop.png"),
        ("developer-ai.png", 512, 512, "Replace with developer-ai.png"),
        ("developer-idle.gif", 512, 512, "Replace with developer-idle.gif"),
        ("developer-thinking.png", 512, 512, "Replace with developer-thinking.png"),
        ("developer-coding.png", 512, 512, "Replace with developer-coding.png"),
        ("developer-idea.png", 512, 512, "Replace with developer-idea.png"),
        ("developer-coffee.png", 512, 512, "Replace with developer-coffee.png"),
        ("developer-focused.png", 512, 512, "Replace with developer-focused.png"),
    ]
    for fname, w, h, label in char_placeholders:
        img = make_placeholder(fname, w, h, COLORS["character"], label)
        ext = fname.split(".")[-1]
        img.save(ASSETS / "characters" / fname, ext.upper())
        print(f"  [OK] characters/{fname}")
    
    # Animations
    anim_placeholders = [
        ("coding.gif", 400, 400, "Replace with coding.gif"),
        ("rocket.gif", 400, 400, "Replace with rocket.gif"),
        ("typing.png", 400, 400, "Replace with typing.png"),
        ("waving.png", 400, 400, "Replace with waving.png"),
        ("thumbs-up.png", 400, 400, "Replace with thumbs-up.png"),
        ("celebrating.png", 400, 400, "Replace with celebrating.png"),
    ]
    for fname, w, h, label in anim_placeholders:
        img = make_placeholder(fname, w, h, COLORS["animation"], label)
        ext = fname.split(".")[-1]
        img.save(ASSETS / "animations" / fname, ext.upper())
        print(f"  [OK] animations/{fname}")
    
    # Projects
    proj_placeholders = [
        ("cafe-pro.png", 800, 500, "Replace with cafe-pro.png"),
        ("levelup-ai.png", 800, 500, "Replace with levelup-ai.png"),
        ("mediq-ai.png", 800, 500, "Replace with mediq-ai.png"),
        ("mindease.png", 800, 500, "Replace with mindease.png"),
    ]
    for fname, w, h, label in proj_placeholders:
        img = make_placeholder(fname, w, h, COLORS["project"], label)
        img.save(ASSETS / "projects" / fname, "PNG")
        print(f"  [OK] projects/{fname}")

def show_status():
    print("\n" + "=" * 60)
    print("  ASSET STRUCTURE CREATED")
    print("=" * 60)
    for name, folder in FOLDERS.items():
        files = list(folder.glob("*"))
        print(f"\n  {name}/ ({len(files)} files)")
        for f in sorted(files):
            size_kb = f.stat().st_size // 1024
            print(f"    {f.name:35s} {size_kb:5d} KB")
    
    print("\n" + "=" * 60)
    print("  NEXT STEPS")
    print("=" * 60)
    print("""
  1. Save your images to: assets/characters/ and assets/animations/
     - Replace placeholder files with actual images
  
  2. To crop poses from actionpack.png, save it to workspace and run:
     python extract_poses.py avatar.png actionpack.png
  
  3. Then update your README.md to use these assets
""")

if __name__ == "__main__":
    print("=" * 60)
    print("  BALA 3D AVATAR ASSET SETUP")
    print("=" * 60)
    create_folders()
    print("\nCreating placeholder images...")
    create_placeholders()
    show_status()
