#!/usr/bin/env python3
"""
国际菜系批量生成脚本
"""

import json
import random
from pathlib import Path
from datetime import datetime

RECIPES_DIR = Path(__file__).parent.parent / "recipes"

def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)

def save_recipe(recipe, cuisine):
    dir_path = RECIPES_DIR / cuisine / "international"
    ensure_dir(dir_path)
    filepath = dir_path / f"{recipe['id']}.json"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(recipe, f, ensure_ascii=False, indent=2)

# 国际菜系配置
INTERNATIONAL_CUISINES = [
    {"id": "japanese", "name": "日本料理", "flavors": ["照烧", "味噌", "天妇罗", "寿司"]},
    {"id": "korean", "name": "韩国料理", "flavors": ["韩式辣酱", "泡菜", "烤肉", "石锅"]},
    {"id": "thai", "name": "泰国菜", "flavors": ["冬阴功", "绿咖喱", "泰式炒河粉", "芒果糯米饭"]},
    {"id": "vietnamese", "name": "越南菜", "flavors": ["河粉", "春卷", "法棍三明治", "鱼露"]},
    {"id": "indian", "name": "印度菜", "flavors": ["咖喱", "坦都里", "飞饼", "酸奶"]},
    {"id": "french", "name": "法国菜", "flavors": ["红酒", "黄油", "奶酪", "法式炖菜"]},
    {"id": "italian", "name": "意大利菜", "flavors": ["意面", "披萨", "烩饭", "提拉米苏"]},
    {"id": "mexican", "name": "墨西哥菜", "flavors": ["塔可", "玉米饼", "牛油果", "辣椒"]},
    {"id": "turkish", "name": "土耳其菜", "flavors": ["烤肉", "旋转烤肉", "果仁蜜饼", "酸奶"]},
    {"id": "spanish", "name": "西班牙菜", "flavors": ["海鲜饭", "Tapas", "火腿", "橄榄油"]},
    {"id": "german", "name": "德国菜", "flavors": ["香肠", "猪肘", "酸菜", "啤酒"]},
    {"id": "british", "name": "英国菜", "flavors": ["炸鱼薯条", "牧羊人派", "周日烤肉", "英式早餐"]},
    {"id": "american", "name": "美国菜", "flavors": ["汉堡", "BBQ", "牛排", "苹果派"]},
    {"id": "mediterranean", "name": "地中海菜", "flavors": ["橄榄油", "海鲜", "蔬菜沙拉", "鹰嘴豆"]},
]

# 国际食材
INTERNATIONAL_INGREDIENTS = [
    {"id": "chicken", "name": "鸡肉", "cal": 167, "p": 19.3, "f": 9.4, "price": 15},
    {"id": "beef", "name": "牛肉", "cal": 250, "p": 26, "f": 15, "price": 45},
    {"id": "pork", "name": "猪肉", "cal": 242, "p": 13.2, "f": 20.5, "price": 18},
    {"id": "lamb", "name": "羊肉", "cal": 203, "p": 17.1, "f": 14.1, "price": 50},
    {"id": "fish", "name": "鱼肉", "cal": 104, "p": 18.4, "f": 3.4, "price": 30},
    {"id": "shrimp", "name": "虾", "cal": 99, "p": 20.4, "f": 1.7, "price": 40},
    {"id": "tofu", "name": "豆腐", "cal": 76, "p": 8.1, "f": 3.7, "price": 4},
    {"id": "egg", "name": "鸡蛋", "cal": 144, "p": 12.6, "f": 10.6, "price": 8},
    {"id": "rice", "name": "米饭", "cal": 116, "p": 2.6, "f": 0.3, "price": 3},
    {"id": "noodle", "name": "面条", "cal": 110, "p": 3.5, "f": 0.5, "price": 5},
]

# 国际烹饪方法
INTERNATIONAL_METHODS = [
    {"id": "teriyaki", "name": "照烧", "prefix": "照烧", "time": 15, "difficulty": "easy"},
    {"id": "miso", "name": "味噌", "prefix": "味噌", "time": 20, "difficulty": "easy"},
    {"id": "tempura", "name": "天妇罗", "prefix": "天妇罗", "time": 15, "difficulty": "medium"},
    {"id": "kimchi", "name": "泡菜", "prefix": "泡菜", "time": 10, "difficulty": "easy"},
    {"id": "bulgogi", "name": "韩式烤肉", "prefix": "韩式烤肉", "time": 20, "difficulty": "medium"},
    {"id": "curry", "name": "咖喱", "prefix": "咖喱", "time": 25, "difficulty": "medium"},
    {"id": "tandoori", "name": "坦都里", "prefix": "坦都里", "time": 30, "difficulty": "medium"},
    {"id": "stir_fry_thai", "name": "泰式炒", "prefix": "泰式", "time": 10, "difficulty": "easy"},
    {"id": "bbq", "name": "BBQ", "prefix": "BBQ", "time": 30, "difficulty": "medium"},
    {"id": "grill", "name": "烤", "prefix": "烤", "time": 20, "difficulty": "medium"},
    {"id": "saute", "name": "煎", "prefix": "香煎", "time": 15, "difficulty": "easy"},
    {"id": "braise_western", "name": "西式炖", "prefix": "西式炖", "time": 45, "difficulty": "medium"},
    {"id": "bake", "name": "焗", "prefix": "芝士焗", "time": 25, "difficulty": "medium"},
]

def generate_international_recipe(ingredient, cuisine, method, index):
    recipe_id = f"{ingredient['id']}_{method['id']}_{cuisine['id']}_{index}"
    
    if method['prefix']:
        name = f"{method['prefix']}{ingredient['name']}"
    else:
        name = f"{ingredient['name']}{method['name']}"
    
    flavor = random.choice(cuisine['flavors'])
    
    steps = [
        {"step": 1, "content": f"{ingredient['name']}处理干净", "tip": ""},
        {"step": 2, "content": f"用{flavor}风味调味", "tip": ""},
        {"step": 3, "content": f"用{method['name']}方式烹饪", "tip": ""},
        {"step": 4, "content": "调味出锅", "tip": ""}
    ]
    
    seasonings = [
        {"name": "盐", "amount": "适量"},
        {"name": "胡椒", "amount": "适量"},
        {"name": "橄榄油", "amount": "适量"}
    ]
    
    recipe = {
        "id": recipe_id,
        "name": name,
        "cuisine": cuisine['id'],
        "category": "international",
        "difficulty": method['difficulty'],
        "time_minutes": method['time'] + random.randint(-5, 10),
        "servings": random.choice([2, 4]),
        "calories_per_serving": ingredient['cal'] + random.randint(-20, 50),
        "cost_per_serving": ingredient['price'] + random.randint(-3, 15),
        "tags": [cuisine['name'], "国际美食"],
        "ingredients": [
            {"name": ingredient['name'], "amount": f"{random.choice([200, 300, 500])}g", "type": ingredient['id']}
        ],
        "seasonings": seasonings,
        "steps": steps,
        "key_points": [f"掌握好{flavor}风味的调味"],
        "nutrition": {
            "calories": ingredient['cal'],
            "protein": ingredient['p'],
            "fat": ingredient['f'],
            "carbs": 20
        },
        "source": "international_batch",
        "created_at": datetime.now().isoformat()
    }
    
    return recipe

def main():
    print("🌍 International Cuisine Recipe Generator")
    print("=" * 50)
    
    total = 0
    
    for cuisine in INTERNATIONAL_CUISINES:
        print(f"\n📚 Generating {cuisine['name']} recipes...")
        
        for ingredient in INTERNATIONAL_INGREDIENTS:
            methods = random.sample(INTERNATIONAL_METHODS, random.randint(2, 4))
            
            for i, method in enumerate(methods):
                recipe = generate_international_recipe(ingredient, cuisine, method, i)
                save_recipe(recipe, cuisine['id'])
                total += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Total international recipes generated: {total}")

if __name__ == "__main__":
    main()
