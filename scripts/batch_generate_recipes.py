#!/usr/bin/env python3
"""
批量生成菜谱脚本 - 生成1000+道菜谱
"""

import json
import os
import random
from pathlib import Path
from datetime import datetime

RECIPES_DIR = Path(__file__).parent.parent / "recipes"

def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)

def save_recipe(recipe, cuisine):
    dir_path = RECIPES_DIR / cuisine / "batch"
    ensure_dir(dir_path)
    filepath = dir_path / f"{recipe['id']}.json"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(recipe, f, ensure_ascii=False, indent=2)

# 食材库
MEATS = [
    {"id": "chicken", "name": "鸡肉", "cal": 167, "p": 19.3, "f": 9.4, "c": 0, "price": 15},
    {"id": "pork", "name": "猪肉", "cal": 242, "p": 13.2, "f": 20.5, "c": 0, "price": 18},
    {"id": "beef", "name": "牛肉", "cal": 250, "p": 26, "f": 15, "c": 0, "price": 45},
    {"id": "lamb", "name": "羊肉", "cal": 203, "p": 17.1, "f": 14.1, "c": 0, "price": 50},
    {"id": "fish", "name": "鱼肉", "cal": 104, "p": 18.4, "f": 3.4, "c": 0, "price": 30},
    {"id": "shrimp", "name": "虾", "cal": 99, "p": 20.4, "f": 1.7, "c": 0, "price": 40},
    {"id": "duck", "name": "鸭肉", "cal": 240, "p": 15.5, "f": 19.7, "c": 0, "price": 25},
    {"id": "egg", "name": "鸡蛋", "cal": 144, "p": 12.6, "f": 10.6, "c": 1.1, "price": 8},
]

VEGETABLES = [
    {"id": "potato", "name": "土豆", "cal": 77, "p": 2, "f": 0.1, "c": 17.5, "price": 3},
    {"id": "tomato", "name": "番茄", "cal": 18, "p": 0.9, "f": 0.2, "c": 3.9, "price": 5},
    {"id": "eggplant", "name": "茄子", "cal": 25, "p": 1, "f": 0.2, "c": 5.7, "price": 5},
    {"id": "cabbage", "name": "白菜", "cal": 16, "p": 1.2, "f": 0.2, "c": 3.2, "price": 3},
    {"id": "broccoli", "name": "西兰花", "cal": 36, "p": 4.3, "f": 0.4, "c": 5.2, "price": 8},
    {"id": "carrot", "name": "胡萝卜", "cal": 41, "p": 0.9, "f": 0.2, "c": 9.6, "price": 3},
    {"id": "cucumber", "name": "黄瓜", "cal": 16, "p": 0.7, "f": 0.1, "c": 3.6, "price": 3},
    {"id": "green_pepper", "name": "青椒", "cal": 20, "p": 0.9, "f": 0.2, "c": 4.6, "price": 5},
    {"id": "mushroom", "name": "蘑菇", "cal": 22, "p": 3.1, "f": 0.3, "c": 3.3, "price": 8},
    {"id": "tofu", "name": "豆腐", "cal": 76, "p": 8.1, "f": 3.7, "c": 2.8, "price": 4},
    {"id": "spinach", "name": "菠菜", "cal": 23, "p": 2.9, "f": 0.4, "c": 3.6, "price": 5},
    {"id": "green_bean", "name": "豆角", "cal": 31, "p": 1.8, "f": 0.1, "c": 7, "price": 6},
    {"id": "corn", "name": "玉米", "cal": 86, "p": 3.3, "f": 1.4, "c": 19, "price": 4},
    {"id": "onion", "name": "洋葱", "cal": 40, "p": 1.1, "f": 0.1, "c": 9.3, "price": 3},
    {"id": "garlic", "name": "蒜", "cal": 149, "p": 6.4, "f": 0.5, "c": 33.1, "price": 5},
    {"id": "ginger", "name": "姜", "cal": 80, "p": 1.8, "f": 0.8, "c": 17.8, "price": 8},
    {"id": "lotus_root", "name": "莲藕", "cal": 74, "p": 2.6, "f": 0.1, "c": 17.2, "price": 10},
    {"id": "pumpkin", "name": "南瓜", "cal": 26, "p": 1, "f": 0.1, "c": 6.5, "price": 4},
]

# 菜系
CUISINES = [
    {"id": "sichuan", "name": "川菜", "flavors": ["麻辣", "鱼香", "宫保", "怪味"]},
    {"id": "cantonese", "name": "粤菜", "flavors": ["清蒸", "白灼", "煲汤", "烧腊"]},
    {"id": "shandong", "name": "鲁菜", "flavors": ["葱烧", "糖醋", "九转", "油焖"]},
    {"id": "hunan", "name": "湘菜", "flavors": ["剁椒", "小炒", "干锅", "烟熏"]},
    {"id": "jiangsu", "name": "苏菜", "flavors": ["红烧", "清炖", "糖醋", "狮子头"]},
    {"id": "zhejiang", "name": "浙菜", "flavors": ["东坡", "西湖", "龙井", "叫花"]},
    {"id": "fujian", "name": "闽菜", "flavors": ["佛跳墙", "荔枝肉", "醉排骨"]},
    {"id": "anhui", "name": "徽菜", "flavors": ["臭鳜鱼", "毛豆腐", "一品锅"]},
    {"id": "northeast", "name": "东北菜", "flavors": ["锅包肉", "地三鲜", "小鸡炖蘑菇"]},
    {"id": "xinjiang", "name": "新疆菜", "flavors": ["大盘鸡", "烤羊肉串", "手抓饭"]},
    {"id": "yunnan", "name": "云南菜", "flavors": ["汽锅鸡", "过桥米线", "野生菌"]},
    {"id": "homestyle", "name": "家常菜", "flavors": ["红烧", "清炒", "凉拌", "炖汤"]},
]

# 烹饪方法
COOKING_METHODS = [
    {"id": "stir_fry", "name": "炒", "prefix": "清炒", "time": 10, "difficulty": "easy"},
    {"id": "braise", "name": "红烧", "prefix": "红烧", "time": 30, "difficulty": "medium"},
    {"id": "steam", "name": "蒸", "prefix": "清蒸", "time": 15, "difficulty": "easy"},
    {"id": "boil", "name": "煮", "prefix": "水煮", "time": 20, "difficulty": "easy"},
    {"id": "fry", "name": "炸", "prefix": "干炸", "time": 15, "difficulty": "medium"},
    {"id": "roast", "name": "烤", "prefix": "烤", "time": 30, "difficulty": "medium"},
    {"id": "cold", "name": "凉拌", "prefix": "凉拌", "time": 10, "difficulty": "easy"},
    {"id": "soup", "name": "汤", "prefix": "", "time": 30, "difficulty": "easy"},
    {"id": "dry_fry", "name": "干煸", "prefix": "干煸", "time": 15, "difficulty": "medium"},
    {"id": "kung_pao", "name": "宫保", "prefix": "宫保", "time": 15, "difficulty": "medium"},
    {"id": "fish_flavor", "name": "鱼香", "prefix": "鱼香", "time": 15, "difficulty": "medium"},
    {"id": "sweet_sour", "name": "糖醋", "prefix": "糖醋", "time": 20, "difficulty": "medium"},
    {"id": "spicy", "name": "麻辣", "prefix": "麻辣", "time": 15, "difficulty": "medium"},
    {"id": "garlic", "name": "蒜蓉", "prefix": "蒜蓉", "time": 10, "difficulty": "easy"},
    {"id": "curry", "name": "咖喱", "prefix": "咖喱", "time": 25, "difficulty": "medium"},
]

# 标签库
TAGS = {
    "家常菜": ["家常菜", "下饭菜", "快手菜"],
    "宴客菜": ["宴客菜", "有排面", "硬菜"],
    "清淡": ["清淡", "健康", "少油"],
    "重口味": ["下饭", "开胃", "重口味"],
    "素菜": ["素菜", "素食", "清淡"],
    "汤品": ["汤品", "营养", "暖胃"],
    "凉菜": ["凉菜", "开胃", "爽口"],
}

def generate_recipe(ingredient, cuisine, method, index):
    """生成单个菜谱"""
    recipe_id = f"{ingredient['id']}_{method['id']}_{cuisine['id']}_{index}"
    
    # 生成菜名
    if method['prefix']:
        name = f"{method['prefix']}{ingredient['name']}"
    else:
        name = f"{ingredient['name']}{method['name']}"
    
    # 选择标签
    tags = random.choice(list(TAGS.values()))
    
    # 生成步骤
    steps = generate_steps(ingredient, method)
    
    # 生成调味料
    seasonings = generate_seasonings(method)
    
    recipe = {
        "id": recipe_id,
        "name": name,
        "cuisine": cuisine['id'],
        "category": "meat" if ingredient in MEATS else "vegetable",
        "difficulty": method['difficulty'],
        "time_minutes": method['time'] + random.randint(-5, 10),
        "servings": random.choice([2, 4]),
        "calories_per_serving": ingredient['cal'] + random.randint(-20, 50),
        "cost_per_serving": ingredient['price'] + random.randint(-3, 8),
        "tags": tags,
        "ingredients": [
            {"name": ingredient['name'], "amount": f"{random.choice([200, 300, 500])}g", "type": ingredient['id']}
        ],
        "seasonings": seasonings,
        "steps": steps,
        "key_points": generate_key_points(method),
        "nutrition": {
            "calories": ingredient['cal'],
            "protein": ingredient['p'],
            "fat": ingredient['f'],
            "carbs": ingredient['c']
        },
        "source": "batch_generated",
        "created_at": datetime.now().isoformat()
    }
    
    return recipe

def generate_steps(ingredient, method):
    """生成步骤"""
    steps = []
    
    if method['id'] == 'stir_fry':
        steps = [
            {"step": 1, "content": f"{ingredient['name']}洗净切好", "tip": ""},
            {"step": 2, "content": "锅中放油，蒜末爆香", "tip": "小火炒蒜"},
            {"step": 3, "content": f"放入{ingredient['name']}大火翻炒", "tip": "大火快炒"},
            {"step": 4, "content": "加盐调味，出锅", "tip": ""}
        ]
    elif method['id'] == 'braise':
        steps = [
            {"step": 1, "content": f"{ingredient['name']}焯水去腥", "tip": "冷水下锅"},
            {"step": 2, "content": "锅中放油，炒糖色", "tip": "小火炒冰糖"},
            {"step": 3, "content": f"放入{ingredient['name']}翻炒上色", "tip": ""},
            {"step": 4, "content": "加入调味料和水，炖煮20分钟", "tip": "小火慢炖"},
            {"step": 5, "content": "大火收汁，出锅", "tip": ""}
        ]
    elif method['id'] == 'steam':
        steps = [
            {"step": 1, "content": f"{ingredient['name']}处理干净，放盘中", "tip": ""},
            {"step": 2, "content": "铺上姜丝，水开后蒸8-10分钟", "tip": "水开后再放"},
            {"step": 3, "content": "倒掉蒸出的水，铺上葱丝", "tip": "蒸出的水有腥味"},
            {"step": 4, "content": "淋上蒸鱼豉油，浇热油", "tip": "油要烧热"}
        ]
    elif method['id'] == 'cold':
        steps = [
            {"step": 1, "content": f"{ingredient['name']}洗净切好", "tip": ""},
            {"step": 2, "content": "焯水后过冷水", "tip": "过冷水保持脆感"},
            {"step": 3, "content": "加入调味料拌匀", "tip": ""}
        ]
    elif method['id'] == 'soup':
        steps = [
            {"step": 1, "content": f"{ingredient['name']}洗净切块", "tip": ""},
            {"step": 2, "content": "锅中加水，放入食材和姜片", "tip": "冷水下锅"},
            {"step": 3, "content": "大火烧开，转小火炖30分钟", "tip": "小火慢炖"},
            {"step": 4, "content": "加盐调味，撒葱花出锅", "tip": "盐最后放"}
        ]
    else:
        steps = [
            {"step": 1, "content": f"{ingredient['name']}处理干净", "tip": ""},
            {"step": 2, "content": f"用{method['name']}的方式烹饪", "tip": ""},
            {"step": 3, "content": "调味出锅", "tip": ""}
        ]
    
    return steps

def generate_seasonings(method):
    """生成调味料"""
    base = [
        {"name": "盐", "amount": "适量"},
        {"name": "食用油", "amount": "适量"}
    ]
    
    if method['id'] == 'braise':
        base.extend([
            {"name": "生抽", "amount": "2勺"},
            {"name": "老抽", "amount": "1勺"},
            {"name": "料酒", "amount": "1勺"},
            {"name": "冰糖", "amount": "适量"}
        ])
    elif method['id'] == 'steam':
        base.extend([
            {"name": "姜丝", "amount": "适量"},
            {"name": "葱丝", "amount": "适量"},
            {"name": "蒸鱼豉油", "amount": "2勺"}
        ])
    elif method['id'] == 'cold':
        base.extend([
            {"name": "蒜末", "amount": "适量"},
            {"name": "醋", "amount": "2勺"},
            {"name": "生抽", "amount": "1勺"},
            {"name": "辣椒油", "amount": "适量"}
        ])
    elif method['id'] == 'stir_fry':
        base.extend([
            {"name": "蒜", "amount": "3瓣"},
            {"name": "生抽", "amount": "1勺"}
        ])
    
    return base

def generate_key_points(method):
    """生成关键点"""
    points = {
        'stir_fry': ["大火快炒，保持脆感"],
        'braise': ["糖色要炒好，小火慢炖"],
        'steam': ["蒸的时间要准确，不要过久"],
        'cold': ["焯水时间不要太长，保持脆感"],
        'soup': ["小火慢炖，汤更鲜美"],
        'fry': ["油温要够，炸到金黄"],
        'roast': ["烤箱要预热，时间要准确"],
        'dry_fry': ["煸到表面微焦才好吃"],
        'kung_pao': ["花生最后放，保持脆感"],
        'fish_flavor': ["鱼香汁的比例是关键"],
        'sweet_sour': ["糖醋比例2:1"],
        'spicy': ["花椒要炒出香味"],
        'garlic': ["蒜蓉要炒香但不能炒糊"],
        'curry': ["咖喱要炒香再加椰浆"],
    }
    return points.get(method['id'], ["掌握好火候"])

def main():
    print("🍽️ Food Craft Batch Recipe Generator")
    print("=" * 50)
    
    total = 0
    all_ingredients = MEATS + VEGETABLES
    
    for cuisine in CUISINES:
        print(f"\n📚 Generating {cuisine['name']} recipes...")
        
        # 为每个食材生成多种做法
        for ingredient in all_ingredients:
            # 随机选择2-4种烹饪方法
            methods = random.sample(COOKING_METHODS, random.randint(2, 4))
            
            for i, method in enumerate(methods):
                recipe = generate_recipe(ingredient, cuisine, method, i)
                save_recipe(recipe, cuisine['id'])
                total += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Total recipes generated: {total}")
    print(f"📂 Recipes saved to: {RECIPES_DIR}")

if __name__ == "__main__":
    main()
