#!/usr/bin/env python3
"""
场景菜谱批量生成脚本
"""

import json
import random
from pathlib import Path
from datetime import datetime

RECIPES_DIR = Path(__file__).parent.parent / "recipes"

def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)

def save_recipe(recipe, scene):
    dir_path = RECIPES_DIR / scene / "special"
    ensure_dir(dir_path)
    filepath = dir_path / f"{recipe['id']}.json"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(recipe, f, ensure_ascii=False, indent=2)

# 场景配置
SCENES = [
    {"id": "children", "name": "儿童餐", "cal_range": (400, 600), "tags": ["儿童", "营养", "可爱"]},
    {"id": "elderly", "name": "老人餐", "cal_range": (450, 650), "tags": ["老人", "软烂", "易消化"]},
    {"id": "weight_loss", "name": "减脂餐", "cal_range": (300, 500), "tags": ["减脂", "低卡", "高蛋白"]},
    {"id": "muscle_gain", "name": "增肌餐", "cal_range": (600, 900), "tags": ["增肌", "高蛋白", "高热量"]},
    {"id": "vegetarian", "name": "素食餐", "cal_range": (350, 550), "tags": ["素食", "健康", "清淡"]},
]

# 场景专属食材
SCENE_INGREDIENTS = {
    "children": [
        {"id": "egg", "name": "鸡蛋", "cal": 144, "p": 12.6, "f": 10.6, "price": 8},
        {"id": "chicken", "name": "鸡肉", "cal": 167, "p": 19.3, "f": 9.4, "price": 15},
        {"id": "fish", "name": "鱼肉", "cal": 104, "p": 18.4, "f": 3.4, "price": 30},
        {"id": "tofu", "name": "豆腐", "cal": 76, "p": 8.1, "f": 3.7, "price": 4},
        {"id": "carrot", "name": "胡萝卜", "cal": 41, "p": 0.9, "f": 0.2, "price": 3},
        {"id": "corn", "name": "玉米", "cal": 86, "p": 3.3, "f": 1.4, "price": 4},
        {"id": "tomato", "name": "番茄", "cal": 18, "p": 0.9, "f": 0.2, "price": 5},
        {"id": "potato", "name": "土豆", "cal": 77, "p": 2, "f": 0.1, "price": 3},
    ],
    "elderly": [
        {"id": "fish", "name": "鱼肉", "cal": 104, "p": 18.4, "f": 3.4, "price": 30},
        {"id": "tofu", "name": "豆腐", "cal": 76, "p": 8.1, "f": 3.7, "price": 4},
        {"id": "egg", "name": "鸡蛋", "cal": 144, "p": 12.6, "f": 10.6, "price": 8},
        {"id": "spinach", "name": "菠菜", "cal": 23, "p": 2.9, "f": 0.4, "price": 5},
        {"id": "pumpkin", "name": "南瓜", "cal": 26, "p": 1, "f": 0.1, "price": 4},
        {"id": "lotus_root", "name": "莲藕", "cal": 74, "p": 2.6, "f": 0.1, "price": 10},
    ],
    "weight_loss": [
        {"id": "chicken_breast", "name": "鸡胸肉", "cal": 133, "p": 23.3, "f": 5, "price": 15},
        {"id": "shrimp", "name": "虾", "cal": 99, "p": 20.4, "f": 1.7, "price": 40},
        {"id": "broccoli", "name": "西兰花", "cal": 36, "p": 4.3, "f": 0.4, "price": 8},
        {"id": "cucumber", "name": "黄瓜", "cal": 16, "p": 0.7, "f": 0.1, "price": 3},
        {"id": "egg", "name": "鸡蛋", "cal": 144, "p": 12.6, "f": 10.6, "price": 8},
    ],
    "muscle_gain": [
        {"id": "beef", "name": "牛肉", "cal": 250, "p": 26, "f": 15, "price": 45},
        {"id": "chicken", "name": "鸡肉", "cal": 167, "p": 19.3, "f": 9.4, "price": 15},
        {"id": "egg", "name": "鸡蛋", "cal": 144, "p": 12.6, "f": 10.6, "price": 8},
        {"id": "salmon", "name": "三文鱼", "cal": 208, "p": 20.4, "f": 13.4, "price": 60},
        {"id": "rice", "name": "米饭", "cal": 116, "p": 2.6, "f": 0.3, "price": 3},
    ],
    "vegetarian": [
        {"id": "tofu", "name": "豆腐", "cal": 76, "p": 8.1, "f": 3.7, "price": 4},
        {"id": "mushroom", "name": "蘑菇", "cal": 22, "p": 3.1, "f": 0.3, "price": 8},
        {"id": "eggplant", "name": "茄子", "cal": 25, "p": 1, "f": 0.2, "price": 5},
        {"id": "broccoli", "name": "西兰花", "cal": 36, "p": 4.3, "f": 0.4, "price": 8},
        {"id": "corn", "name": "玉米", "cal": 86, "p": 3.3, "f": 1.4, "price": 4},
        {"id": "potato", "name": "土豆", "cal": 77, "p": 2, "f": 0.1, "price": 3},
    ],
}

# 烹饪方法
SCENE_METHODS = [
    {"id": "steam", "name": "蒸", "prefix": "清蒸", "time": 15, "difficulty": "easy"},
    {"id": "boil", "name": "煮", "prefix": "水煮", "time": 20, "difficulty": "easy"},
    {"id": "stir_fry", "name": "炒", "prefix": "清炒", "time": 10, "difficulty": "easy"},
    {"id": "soup", "name": "汤", "prefix": "", "time": 30, "difficulty": "easy"},
    {"id": "cold", "name": "凉拌", "prefix": "凉拌", "time": 10, "difficulty": "easy"},
    {"id": "braise", "name": "炖", "prefix": "炖", "time": 30, "difficulty": "easy"},
]

def generate_scene_recipe(ingredient, scene, method, index):
    recipe_id = f"{ingredient['id']}_{method['id']}_{scene['id']}_{index}"
    
    if method['prefix']:
        name = f"{method['prefix']}{ingredient['name']}"
    else:
        name = f"{ingredient['name']}{method['name']}"
    
    cal_min, cal_max = scene['cal_range']
    calories = random.randint(cal_min, cal_max)
    
    steps = [
        {"step": 1, "content": f"{ingredient['name']}处理干净", "tip": ""},
        {"step": 2, "content": f"用{method['name']}方式烹饪", "tip": ""},
        {"step": 3, "content": "调味出锅", "tip": ""}
    ]
    
    if scene['id'] == 'children':
        steps.append({"step": 4, "content": "摆盘成可爱造型", "tip": "增加食欲"})
    elif scene['id'] == 'elderly':
        steps.append({"step": 4, "content": "确保软烂易嚼", "tip": "方便老人食用"})
    elif scene['id'] == 'weight_loss':
        steps.append({"step": 4, "content": "少油少盐调味", "tip": "控制热量"})
    elif scene['id'] == 'muscle_gain':
        steps.append({"step": 4, "content": "搭配碳水一起食用", "tip": "补充能量"})
    
    recipe = {
        "id": recipe_id,
        "name": name,
        "cuisine": "homestyle",
        "category": scene['id'],
        "difficulty": method['difficulty'],
        "time_minutes": method['time'] + random.randint(-5, 10),
        "servings": random.choice([1, 2, 4]),
        "calories_per_serving": calories,
        "cost_per_serving": ingredient['price'] + random.randint(-3, 10),
        "tags": scene['tags'],
        "ingredients": [
            {"name": ingredient['name'], "amount": f"{random.choice([150, 200, 300])}g", "type": ingredient['id']}
        ],
        "seasonings": [
            {"name": "盐", "amount": "适量"},
            {"name": "食用油", "amount": "少许"}
        ],
        "steps": steps,
        "key_points": [f"适合{scene['name']}的烹饪方式"],
        "nutrition": {
            "calories": calories,
            "protein": ingredient['p'],
            "fat": ingredient['f'],
            "carbs": 30
        },
        "source": "scene_batch",
        "created_at": datetime.now().isoformat()
    }
    
    return recipe

def main():
    print("🎯 Scene-based Recipe Generator")
    print("=" * 50)
    
    total = 0
    
    for scene in SCENES:
        print(f"\n📚 Generating {scene['name']} recipes...")
        ingredients = SCENE_INGREDIENTS[scene['id']]
        
        for ingredient in ingredients:
            methods = random.sample(SCENE_METHODS, random.randint(3, 5))
            
            for i, method in enumerate(methods):
                recipe = generate_scene_recipe(ingredient, scene, method, i)
                save_recipe(recipe, scene['id'])
                total += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Total scene recipes generated: {total}")

if __name__ == "__main__":
    main()
