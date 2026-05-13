#!/usr/bin/env python3
"""
LLM 生成菜谱脚本
基于食材库和菜系库，生成菜谱数据
"""

import json
import os
from pathlib import Path
from datetime import datetime
import random

RECIPES_DIR = Path(__file__).parent.parent / "recipes"
INGREDIENTS_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"
CUISINES_DIR = Path(__file__).parent.parent / "knowledge" / "cuisines"

def ensure_dir(path):
    """确保目录存在"""
    path.mkdir(parents=True, exist_ok=True)

def load_ingredients():
    """加载所有食材"""
    ingredients = []
    for json_file in INGREDIENTS_DIR.rglob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'id' in data and 'name' in data:
                    ingredients.append(data)
        except:
            pass
    return ingredients

def load_cuisines():
    """加载所有菜系"""
    cuisines = []
    for json_file in CUISINES_DIR.rglob("*.json"):
        if json_file.name == "index.json":
            continue
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'id' in data and 'name' in data:
                    cuisines.append(data)
        except:
            pass
    return cuisines

def generate_recipe_from_template(ingredient, cuisine, template):
    """从模板生成菜谱"""
    recipe = {
        "id": f"{ingredient['id']}_{template['method']}_{cuisine['id']}",
        "name": f"{template['name_prefix']}{ingredient['name']}",
        "name_en": f"{template['name_prefix_en']} {ingredient.get('name_en', '')}",
        "cuisine": cuisine['id'],
        "category": ingredient.get('category', 'unknown'),
        "difficulty": template['difficulty'],
        "time_minutes": template['time_minutes'],
        "servings": 2,
        "calories_per_serving": ingredient.get('nutrition_per_100g', {}).get('calories', 100),
        "cost_per_serving": ingredient.get('price_range', {}).get('average', 10),
        "tags": template.get('tags', []),
        "ingredients": [
            {"name": ingredient['name'], "amount": "300g", "type": ingredient.get('category', 'unknown')}
        ],
        "seasonings": template.get('seasonings', []),
        "steps": template.get('steps', []),
        "key_points": template.get('key_points', []),
        "nutrition": {
            "calories": ingredient.get('nutrition_per_100g', {}).get('calories', 100),
            "protein": ingredient.get('nutrition_per_100g', {}).get('protein', 10),
            "fat": ingredient.get('nutrition_per_100g', {}).get('fat', 5),
            "carbs": ingredient.get('nutrition_per_100g', {}).get('carbs', 10)
        },
        "source": "llm_generated",
        "created_at": datetime.now().isoformat()
    }
    return recipe

# 菜谱模板库
RECIPE_TEMPLATES = [
    {
        "method": "stir_fry",
        "name_prefix": "清炒",
        "name_prefix_en": "Stir-fried",
        "difficulty": "easy",
        "time_minutes": 10,
        "tags": ["家常菜", "快手菜"],
        "seasonings": [
            {"name": "盐", "amount": "适量"},
            {"name": "蒜", "amount": "3瓣"},
            {"name": "食用油", "amount": "适量"}
        ],
        "steps": [
            {"step": 1, "content": "食材洗净切好", "tip": ""},
            {"step": 2, "content": "锅中放油，蒜末爆香", "tip": "小火炒蒜"},
            {"step": 3, "content": "放入食材大火翻炒", "tip": "大火快炒"},
            {"step": 4, "content": "加盐调味，出锅", "tip": ""}
        ],
        "key_points": ["大火快炒，保持脆感"]
    },
    {
        "method": "braise",
        "name_prefix": "红烧",
        "name_prefix_en": "Braised",
        "difficulty": "medium",
        "time_minutes": 30,
        "tags": ["家常菜", "下饭菜"],
        "seasonings": [
            {"name": "生抽", "amount": "2勺"},
            {"name": "老抽", "amount": "1勺"},
            {"name": "料酒", "amount": "1勺"},
            {"name": "冰糖", "amount": "适量"},
            {"name": "姜片", "amount": "3片"}
        ],
        "steps": [
            {"step": 1, "content": "食材焯水去腥", "tip": "冷水下锅"},
            {"step": 2, "content": "锅中放油，炒糖色", "tip": "小火炒冰糖"},
            {"step": 3, "content": "放入食材翻炒上色", "tip": ""},
            {"step": 4, "content": "加入调味料和水，炖煮20分钟", "tip": "小火慢炖"},
            {"step": 5, "content": "大火收汁，出锅", "tip": ""}
        ],
        "key_points": ["糖色要炒好，小火慢炖"]
    },
    {
        "method": "steam",
        "name_prefix": "清蒸",
        "name_prefix_en": "Steamed",
        "difficulty": "easy",
        "time_minutes": 15,
        "tags": ["清淡", "健康"],
        "seasonings": [
            {"name": "姜丝", "amount": "适量"},
            {"name": "葱丝", "amount": "适量"},
            {"name": "蒸鱼豉油", "amount": "2勺"},
            {"name": "食用油", "amount": "适量"}
        ],
        "steps": [
            {"step": 1, "content": "食材处理干净，放盘中", "tip": ""},
            {"step": 2, "content": "铺上姜丝，水开后蒸8-10分钟", "tip": "水开后再放"},
            {"step": 3, "content": "倒掉蒸出的水，铺上葱丝", "tip": "蒸出的水有腥味"},
            {"step": 4, "content": "淋上蒸鱼豉油，浇热油", "tip": "油要烧热"}
        ],
        "key_points": ["蒸的时间要准确，不要过久"]
    },
    {
        "method": "cold_dish",
        "name_prefix": "凉拌",
        "name_prefix_en": "Cold",
        "difficulty": "easy",
        "time_minutes": 10,
        "tags": ["凉菜", "开胃"],
        "seasonings": [
            {"name": "蒜末", "amount": "适量"},
            {"name": "醋", "amount": "2勺"},
            {"name": "生抽", "amount": "1勺"},
            {"name": "辣椒油", "amount": "适量"},
            {"name": "香油", "amount": "少许"}
        ],
        "steps": [
            {"step": 1, "content": "食材洗净切好", "tip": ""},
            {"step": 2, "content": "焯水后过冷水", "tip": "过冷水保持脆感"},
            {"step": 3, "content": "加入调味料拌匀", "tip": ""}
        ],
        "key_points": ["焯水时间不要太长，保持脆感"]
    },
    {
        "method": "soup",
        "name_prefix": "",
        "name_prefix_en": "Soup",
        "difficulty": "easy",
        "time_minutes": 30,
        "tags": ["汤品", "营养"],
        "seasonings": [
            {"name": "盐", "amount": "适量"},
            {"name": "姜片", "amount": "3片"},
            {"name": "葱花", "amount": "适量"}
        ],
        "steps": [
            {"step": 1, "content": "食材洗净切块", "tip": ""},
            {"step": 2, "content": "锅中加水，放入食材和姜片", "tip": "冷水下锅"},
            {"step": 3, "content": "大火烧开，转小火炖30分钟", "tip": "小火慢炖"},
            {"step": 4, "content": "加盐调味，撒葱花出锅", "tip": "盐最后放"}
        ],
        "key_points": ["小火慢炖，汤更鲜美"]
    }
]

def generate_recipes_for_ingredient(ingredient, cuisines):
    """为单个食材生成多种做法的菜谱"""
    recipes = []
    
    # 随机选择2-3种做法
    templates = random.sample(RECIPE_TEMPLATES, min(3, len(RECIPE_TEMPLATES)))
    
    # 随机选择1-2个菜系
    selected_cuisines = random.sample(cuisines, min(2, len(cuisines)))
    
    for template in templates:
        for cuisine in selected_cuisines:
            recipe = generate_recipe_from_template(ingredient, cuisine, template)
            recipes.append(recipe)
    
    return recipes

def save_recipe(recipe, cuisine_id):
    """保存单个菜谱"""
    dir_path = RECIPES_DIR / cuisine_id / "generated"
    ensure_dir(dir_path)
    
    filename = f"{recipe['id']}.json"
    filepath = dir_path / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(recipe, f, ensure_ascii=False, indent=2)
    
    return filepath

def main():
    """主函数"""
    print("🍽️ Food Craft Recipe Generator")
    print("=" * 50)
    
    # 加载食材和菜系
    print("\n📚 Loading ingredients and cuisines...")
    ingredients = load_ingredients()
    cuisines = load_cuisines()
    
    print(f"  Found {len(ingredients)} ingredients")
    print(f"  Found {len(cuisines)} cuisines")
    
    # 为每个食材生成菜谱
    print("\n🍳 Generating recipes...")
    total_recipes = 0
    
    # 选择部分食材生成菜谱（避免过多）
    selected_ingredients = random.sample(
        ingredients, 
        min(50, len(ingredients))
    )
    
    for ingredient in selected_ingredients:
        recipes = generate_recipes_for_ingredient(ingredient, cuisines)
        
        for recipe in recipes:
            cuisine_id = recipe['cuisine']
            save_recipe(recipe, cuisine_id)
            total_recipes += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Total recipes generated: {total_recipes}")
    print(f"📂 Recipes saved to: {RECIPES_DIR}")

if __name__ == "__main__":
    main()
