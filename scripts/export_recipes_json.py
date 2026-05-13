#!/usr/bin/env python3
"""
将所有菜谱合并成一个JSON文件，供前端使用
"""

import json
from pathlib import Path

RECIPES_DIR = Path(__file__).parent.parent / "recipes"
OUTPUT_DIR = Path(__file__).parent.parent / "frontend"

def load_all_recipes():
    recipes = []
    for json_file in RECIPES_DIR.rglob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                recipe = json.load(f)
                if 'id' in recipe and 'name' in recipe:
                    recipes.append(recipe)
        except:
            pass
    return recipes

def main():
    print("📦 Loading all recipes...")
    recipes = load_all_recipes()
    print(f"  Loaded {len(recipes)} recipes")
    
    output_file = OUTPUT_DIR / "recipes.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(recipes, f, ensure_ascii=False)
    
    print(f"✅ Saved to {output_file}")
    print(f"   File size: {output_file.stat().st_size / 1024:.1f} KB")

if __name__ == "__main__":
    main()
