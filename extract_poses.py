"""
Bala 3D Avatar Pose Extractor
Extracts individual poses from the action pack grid image
and organizes them into the GitHub asset folder structure.
"""

import os
import sys
from pathlib import Path
from PIL import Image

WORKSPACE = Path(r"C:\Users\BALACHANDRAN S\Balachandransakthivel")
ASSETS = WORKSPACE / "assets"

FOLDERS = {
    "hero": ASSETS / "hero",
    "characters": ASSETS / "characters",
    "projects": ASSETS / "projects",
    "animations": ASSETS / "animations",
}

# Mapping from grid position to output filename and folder
POSE_MAP = {
    # Top row (5 items)
    "idle_pose": ("characters", "developer-idle.png"),
    "coding": ("characters", "developer-coding.png"),
    "working_on_laptop": ("characters", "developer-laptop.png"),
    "ai_interaction": ("characters", "developer-ai.png"),
    "thinking": ("characters", "developer-thinking.png"),
    # Middle row (4 items) - Animation GIF Actions
    "typing_animation": ("animations", "typing.png"),
    "waving_hello": ("animations", "waving.png"),
    "thumbs_up": ("animations", "thumbs-up.png"),
    "celebrating": ("animations", "celebrating.png"),
    # Bottom row (4 items) - Special Actions
    "rocket_launch": ("animations", "rocket.png"),
    "idea_moment": ("characters", "developer-idea.png"),
    "coffee_break": ("characters", "developer-coffee.png"),
    "focused_mode": ("characters", "developer-focused.png"),
}


def create_folders():
    for folder in FOLDERS.values():
        folder.mkdir(parents=True, exist_ok=True)
    print("[OK] Asset folders created.")


def copy_avatar(avatar_path: str):
    """Copy the master avatar to characters/developer.png"""
    src = Path(avatar_path)
    if not src.exists():
        print(f"[WARN] Avatar not found: {src}")
        return False
    dst = FOLDERS["characters"] / "developer.png"
    img = Image.open(src)
    img.save(dst, "PNG")
    print(f"[OK] Master avatar saved: {dst}")
    return True


def extract_from_grid(grid_path: str):
    """
    Extract poses from the action pack grid image.
    
    The grid image typically has:
    - Top row: 5 cells (Idle, Coding, Laptop, AI, Thinking)
    - Middle row: 4 cells (Typing, Waving, ThumbsUp, Celebrating)
    - Bottom row: 4 cells (Rocket, Idea, Coffee, Focused)
    
    This function tries to auto-detect cells by finding
    the content boundaries.
    """
    src = Path(grid_path)
    if not src.exists():
        print(f"[ERROR] Grid image not found: {src}")
        return False

    img = Image.open(src)
    w, h = img.size
    print(f"[INFO] Grid image size: {w}x{h}")

    # Save a copy as hero image (wide format)
    hero_dst = FOLDERS["hero"] / "hero-original.png"
    img.save(hero_dst, "PNG")
    print(f"[OK] Hero original saved: {hero_dst}")

    # For the grid extraction, we need to define crop regions.
    # The image has headers/labels, so we need to estimate cell positions.
    
    # Strategy: Show the image and let user define grid manually,
    # OR use approximate percentages based on typical action pack layouts.
    
    print("\n[INFO] Analyzing grid layout...")
    print(f"  Image dimensions: {w} x {h}")
    
    # Approximate grid positions (as percentages of image size)
    # These are estimates - adjust if the actual grid differs
    
    # Top row: starts ~12% from top, ends ~38% from top
    # Each of 5 cells takes ~20% width, starting ~2% from left
    top_row_y1 = int(h * 0.10)
    top_row_y2 = int(h * 0.37)
    
    # Middle row: starts ~42% from top, ends ~65% from top  
    # Each of 4 cells takes ~25% width
    mid_row_y1 = int(h * 0.42)
    mid_row_y2 = int(h * 0.65)
    
    # Bottom row: starts ~70% from top, ends ~93% from top
    # Each of 4 cells takes ~25% width
    bot_row_y1 = int(h * 0.70)
    bot_row_y2 = int(h * 0.93)
    
    # Define crop boxes for each pose: (left, upper, right, lower)
    cells = {
        # Top row (5 cells)
        "idle_pose":       (int(w*0.01), top_row_y1, int(w*0.19), top_row_y2),
        "coding":          (int(w*0.21), top_row_y1, int(w*0.39), top_row_y2),
        "working_on_laptop": (int(w*0.41), top_row_y1, int(w*0.59), top_row_y2),
        "ai_interaction":  (int(w*0.61), top_row_y1, int(w*0.79), top_row_y2),
        "thinking":        (int(w*0.81), top_row_y1, int(w*0.99), top_row_y2),
        # Middle row (4 cells)
        "typing_animation": (int(w*0.01), mid_row_y1, int(w*0.24), mid_row_y2),
        "waving_hello":    (int(w*0.26), mid_row_y1, int(w*0.49), mid_row_y2),
        "thumbs_up":       (int(w*0.51), mid_row_y1, int(w*0.74), mid_row_y2),
        "celebrating":     (int(w*0.76), mid_row_y1, int(w*0.99), mid_row_y2),
        # Bottom row (4 cells)
        "rocket_launch":   (int(w*0.01), bot_row_y1, int(w*0.24), bot_row_y2),
        "idea_moment":     (int(w*0.26), bot_row_y1, int(w*0.49), bot_row_y2),
        "coffee_break":    (int(w*0.51), bot_row_y1, int(w*0.74), bot_row_y2),
        "focused_mode":    (int(w*0.76), bot_row_y1, int(w*0.99), bot_row_y2),
    }
    
    print(f"  Top row Y: {top_row_y1} - {top_row_y2}")
    print(f"  Mid row Y: {mid_row_y1} - {mid_row_y2}")
    print(f"  Bot row Y: {bot_row_y1} - {bot_row_y2}")
    
    extracted = 0
    for pose_name, crop_box in cells.items():
        folder, filename = POSE_MAP[pose_name]
        dst = FOLDERS[folder] / filename
        
        cropped = img.crop(crop_box)
        cropped.save(dst, "PNG")
        print(f"  [OK] {pose_name:25s} -> {folder}/{filename}  (crop: {crop_box})")
        extracted += 1
    
    print(f"\n[OK] Extracted {extracted} poses from grid.")
    return True


def extract_custom_grid(grid_path: str, grid_config: dict):
    """
    Extract using custom grid coordinates.
    grid_config format:
    {
        "rows": [
            {"y_start": 0.10, "y_end": 0.37, "cells": 5},
            {"y_start": 0.42, "y_end": 0.65, "cells": 4},
            {"y_start": 0.70, "y_end": 0.93, "cells": 4},
        ],
        "x_margin": 0.01,
        "x_gap": 0.02,
    }
    """
    src = Path(grid_path)
    img = Image.open(src)
    w, h = img.size
    
    poses_order = list(POSE_MAP.keys())
    pose_idx = 0
    
    for row in grid_config["rows"]:
        y1 = int(h * row["y_start"])
        y2 = int(h * row["y_end"])
        n_cells = row["cells"]
        cell_width = w / n_cells
        margin = int(w * grid_config.get("x_margin", 0.01))
        gap = int(w * grid_config.get("x_gap", 0.02))
        
        for i in range(n_cells):
            if pose_idx >= len(poses_order):
                break
            x1 = int(i * cell_width) + margin
            x2 = int((i + 1) * cell_width) - margin
            
            pose_name = poses_order[pose_idx]
            folder, filename = POSE_MAP[pose_name]
            dst = FOLDERS[folder] / filename
            
            cropped = img.crop((x1, y1, x2, y2))
            cropped.save(dst, "PNG")
            print(f"  [OK] {pose_name:25s} -> {folder}/{filename}")
            pose_idx += 1
    
    print(f"\n[OK] Extracted {pose_idx} poses.")
    return True


def main():
    print("=" * 60)
    print("  BALA 3D AVATAR POSE EXTRACTOR")
    print("=" * 60)
    
    create_folders()
    
    # Check for image files in workspace
    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
    found_images = []
    for f in WORKSPACE.iterdir():
        if f.suffix.lower() in image_extensions and f.is_file():
            found_images.append(f)
    
    # Also check for images that might have been saved with temp names
    for f in WORKSPACE.glob("*.*"):
        if f.suffix.lower() in image_extensions and f.is_file():
            if f not in found_images:
                found_images.append(f)
    
    if found_images:
        print(f"\n[INFO] Found {len(found_images)} image(s) in workspace:")
        for img in found_images:
            print(f"  - {img.name} ({img.stat().st_size // 1024}KB)")
    else:
        print("\n[INFO] No images found in workspace yet.")
    
    # Try to find avatar and grid images
    avatar_path = None
    grid_path = None
    
    for img in found_images:
        name_lower = img.name.lower()
        # Look for the avatar (single character, might be on pink background)
        if "avatar" in name_lower or "idle" in name_lower or "single" in name_lower:
            avatar_path = img
        # Look for the grid/action pack
        elif "pack" in name_lower or "grid" in name_lower or "action" in name_lower or "all" in name_lower:
            grid_path = img
    
    # If we couldn't auto-detect, ask user
    if not avatar_path and not grid_path:
        print("\n" + "=" * 60)
        print("  MANUAL MODE")
        print("=" * 60)
        print("\nPlease provide the image file paths.")
        print("Example:")
        print('  python extract_poses.py avatar.png actionpack.png')
        print("\nOr place the images in the workspace folder and run again.")
        return
    
    if avatar_path:
        print(f"\n[INFO] Avatar detected: {avatar_path.name}")
        copy_avatar(str(avatar_path))
    
    if grid_path:
        print(f"[INFO] Grid/Action pack detected: {grid_path.name}")
        extract_from_grid(str(grid_path))
    
    print("\n" + "=" * 60)
    print("  EXTRACTION COMPLETE")
    print("=" * 60)
    print(f"\nAssets saved to: {ASSETS}")
    print("\nFolder structure:")
    for name, folder in FOLDERS.items():
        files = list(folder.glob("*"))
        print(f"  {name}/ ({len(files)} files)")
        for f in files:
            print(f"    - {f.name}")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        # Command line arguments: avatar_path grid_path
        create_folders()
        copy_avatar(sys.argv[1])
        extract_from_grid(sys.argv[2])
    elif len(sys.argv) == 2:
        # Single argument - try as grid image
        create_folders()
        extract_from_grid(sys.argv[1])
    else:
        main()
