#!/usr/bin/env python3
"""更多全球食材 - 坚果、种子、油脂、奶制品、蛋类等"""

import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"

MORE_INGREDIENTS = {
    "nuts": [
        {"id": "almond", "name": "杏仁", "en": "Almond", "cal": 579, "p": 21.2, "f": 49.9, "c": 21.6, "price": 40},
        {"id": "cashew_nut", "name": "腰果", "en": "Cashew", "cal": 553, "p": 18.2, "f": 43.9, "c": 30.2, "price": 45},
        {"id": "walnut_nut", "name": "核桃", "en": "Walnut", "cal": 654, "p": 15.2, "f": 65.2, "c": 13.7, "price": 35},
        {"id": "pecan", "name": "碧根果", "en": "Pecan", "cal": 691, "p": 9.2, "f": 72.0, "c": 13.9, "price": 50},
        {"id": "pistachio", "name": "开心果", "en": "Pistachio", "cal": 560, "p": 20.2, "f": 45.3, "c": 27.2, "price": 55},
        {"id": "macadamia", "name": "夏威夷果", "en": "Macadamia", "cal": 718, "p": 7.9, "f": 75.8, "c": 13.8, "price": 60},
        {"id": "hazelnut", "name": "榛子", "en": "Hazelnut", "cal": 628, "p": 15.0, "f": 60.8, "c": 16.7, "price": 45},
        {"id": "brazil_nut", "name": "巴西坚果", "en": "Brazil Nut", "cal": 659, "p": 14.3, "f": 67.1, "c": 11.7, "price": 55},
        {"id": "pine_nut", "name": "松子", "en": "Pine Nut", "cal": 673, "p": 13.7, "f": 68.4, "c": 13.1, "price": 80},
        {"id": "chestnut", "name": "栗子", "en": "Chestnut", "cal": 213, "p": 2.4, "f": 2.3, "c": 45.5, "price": 15},
        {"id": "coconut", "name": "椰子", "en": "Coconut", "cal": 354, "p": 3.3, "f": 33.5, "c": 15.2, "price": 10},
        {"id": "coconut_flake", "name": "椰子片", "en": "Coconut Flake", "cal": 660, "p": 6.9, "f": 64.5, "c": 23.7, "price": 20},
    ],
    "seeds": [
        {"id": "sunflower_seed", "name": "葵花籽", "en": "Sunflower Seed", "cal": 584, "p": 20.8, "f": 51.5, "c": 20.0, "price": 12},
        {"id": "pumpkin_seed", "name": "南瓜籽", "en": "Pumpkin Seed", "cal": 559, "p": 30.2, "f": 49.1, "c": 10.7, "price": 20},
        {"id": "flax_seed", "name": "亚麻籽", "en": "Flax Seed", "cal": 534, "p": 18.3, "f": 42.2, "c": 28.9, "price": 25},
        {"id": "chia_seed", "name": "奇亚籽", "en": "Chia Seed", "cal": 486, "p": 16.5, "f": 30.7, "c": 42.1, "price": 40},
        {"id": "hemp_seed", "name": "火麻仁", "en": "Hemp Seed", "cal": 553, "p": 31.6, "f": 48.8, "c": 8.7, "price": 35},
        {"id": "sesame_seed_asian", "name": "芝麻", "en": "Sesame Seed", "cal": 573, "p": 17.7, "f": 49.7, "c": 23.5, "price": 15},
        {"id": "nigella_seed", "name": "黑种草籽", "en": "Nigella Seed", "cal": 345, "p": 16.8, "f": 22.3, "c": 44.2, "price": 25},
        {"id": "poppy_seed_asian", "name": "罂粟籽", "en": "Poppy Seed", "cal": 525, "p": 18.0, "f": 41.6, "c": 28.1, "price": 30},
        {"id": "watermelon_seed", "name": "西瓜籽", "en": "Watermelon Seed", "cal": 557, "p": 28.3, "f": 47.4, "c": 15.3, "price": 15},
    ],
    "oils": [
        {"id": "olive_oil", "name": "橄榄油", "en": "Olive Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 50},
        {"id": "extra_virgin_olive", "name": "特级初榨橄榄油", "en": "Extra Virgin Olive Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 80},
        {"id": "coconut_oil", "name": "椰子油", "en": "Coconut Oil", "cal": 862, "p": 0, "f": 100, "c": 0, "price": 40},
        {"id": "avocado_oil", "name": "牛油果油", "en": "Avocado Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 60},
        {"id": "sesame_oil_asian", "name": "芝麻油", "en": "Sesame Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 30},
        {"id": "peanut_oil", "name": "花生油", "en": "Peanut Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 25},
        {"id": "vegetable_oil", "name": "植物油", "en": "Vegetable Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 15},
        {"id": "canola_oil", "name": "菜籽油", "en": "Canola Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 12},
        {"id": "sunflower_oil", "name": "葵花籽油", "en": "Sunflower Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 15},
        {"id": "grapeseed_oil", "name": "葡萄籽油", "en": "Grapeseed Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 35},
        {"id": "walnut_oil", "name": "核桃油", "en": "Walnut Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 50},
        {"id": "truffle_oil", "name": "松露油", "en": "Truffle Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 100},
        {"id": "chili_oil_asian", "name": "辣椒油", "en": "Chili Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 20},
        {"id": "mustard_oil", "name": "芥末油", "en": "Mustard Oil", "cal": 884, "p": 0, "f": 100, "c": 0, "price": 25},
        {"id": "ghee", "name": "酥油", "en": "Ghee", "cal": 900, "p": 0, "f": 100, "c": 0, "price": 60},
        {"id": "lard", "name": "猪油", "en": "Lard", "cal": 902, "p": 0, "f": 100, "c": 0, "price": 10},
        {"id": "tallow", "name": "牛油", "en": "Tallow", "cal": 902, "p": 0, "f": 100, "c": 0, "price": 15},
        {"id": "duck_fat", "name": "鸭油", "en": "Duck Fat", "cal": 900, "p": 0, "f": 100, "c": 0, "price": 30},
        {"id": "schmaltz", "name": "鸡油", "en": "Schmaltz", "cal": 900, "p": 0, "f": 100, "c": 0, "price": 20},
    ],
    "dairy": [
        {"id": "whole_milk", "name": "全脂牛奶", "en": "Whole Milk", "cal": 61, "p": 3.2, "f": 3.3, "c": 4.8, "price": 8},
        {"id": "skim_milk", "name": "脱脂牛奶", "en": "Skim Milk", "cal": 34, "p": 3.4, "f": 0.1, "c": 5.0, "price": 8},
        {"id": "heavy_cream", "name": "浓奶油", "en": "Heavy Cream", "cal": 340, "p": 2.1, "f": 36.1, "c": 2.8, "price": 25},
        {"id": "sour_cream", "name": "酸奶油", "en": "Sour Cream", "cal": 198, "p": 2.4, "f": 19.4, "c": 3.4, "price": 15},
        {"id": "cream_cheese", "name": "奶油奶酪", "en": "Cream Cheese", "cal": 342, "p": 5.9, "f": 34.2, "c": 4.1, "price": 25},
        {"id": "ricotta", "name": "里科塔奶酪", "en": "Ricotta", "cal": 174, "p": 11.3, "f": 13.0, "c": 3.0, "price": 30},
        {"id": "mozzarella", "name": "马苏里拉奶酪", "en": "Mozzarella", "cal": 280, "p": 28.0, "f": 17.1, "c": 3.1, "price": 35},
        {"id": "parmesan", "name": "帕玛森奶酪", "en": "Parmesan", "cal": 431, "p": 38.5, "f": 29.0, "c": 4.1, "price": 80},
        {"id": "cheddar", "name": "切达奶酪", "en": "Cheddar", "cal": 403, "p": 24.9, "f": 33.1, "c": 1.3, "price": 40},
        {"id": "gouda", "name": "高达奶酪", "en": "Gouda", "cal": 356, "p": 24.9, "f": 27.4, "c": 2.2, "price": 45},
        {"id": "brie", "name": "布里奶酪", "en": "Brie", "cal": 334, "p": 20.8, "f": 27.7, "c": 0.5, "price": 50},
        {"id": "camembert", "name": "卡门培尔奶酪", "en": "Camembert", "cal": 300, "p": 19.8, "f": 24.3, "c": 0.5, "price": 50},
        {"id": "blue_cheese", "name": "蓝纹奶酪", "en": "Blue Cheese", "cal": 353, "p": 21.4, "f": 28.7, "c": 2.3, "price": 60},
        {"id": "feta", "name": "菲达奶酪", "en": "Feta", "cal": 264, "p": 14.2, "f": 21.3, "c": 4.1, "price": 40},
        {"id": "goat_cheese", "name": "山羊奶酪", "en": "Goat Cheese", "cal": 364, "p": 21.6, "f": 29.8, "c": 0.1, "price": 55},
        {"id": "gruyere", "name": "格鲁耶尔奶酪", "en": "Gruyère", "cal": 413, "p": 29.8, "f": 32.3, "c": 0.4, "price": 70},
        {"id": "emmental", "name": "埃曼塔尔奶酪", "en": "Emmental", "cal": 393, "p": 28.4, "f": 30.5, "c": 0.4, "price": 60},
        {"id": "provolone", "name": "普罗卧干酪", "en": "Provolone", "cal": 351, "p": 25.6, "f": 26.6, "c": 2.1, "price": 40},
        {"id": "mascarpone", "name": "马斯卡彭奶酪", "en": "Mascarpone", "cal": 429, "p": 4.8, "f": 44.0, "c": 4.6, "price": 45},
        {"id": "yogurt", "name": "酸奶", "en": "Yogurt", "cal": 59, "p": 10.0, "f": 0.4, "c": 3.6, "price": 8},
        {"id": "greek_yogurt", "name": "希腊酸奶", "en": "Greek Yogurt", "cal": 97, "p": 9.0, "f": 5.0, "c": 3.6, "price": 15},
        {"id": "kefir", "name": "开菲尔", "en": "Kefir", "cal": 41, "p": 3.3, "f": 1.0, "c": 4.7, "price": 20},
        {"id": "butter_unsalted", "name": "无盐黄油", "en": "Unsalted Butter", "cal": 717, "p": 0.9, "f": 81.1, "c": 0.1, "price": 30},
        {"id": "butter_salted", "name": "有盐黄油", "en": "Salted Butter", "cal": 717, "p": 0.9, "f": 81.1, "c": 0.1, "price": 28},
        {"id": "clarified_butter", "name": "澄清黄油", "en": "Clarified Butter", "cal": 900, "p": 0, "f": 100, "c": 0, "price": 40},
    ],
    "eggs": [
        {"id": "chicken_egg", "name": "鸡蛋", "en": "Chicken Egg", "cal": 155, "p": 12.6, "f": 10.6, "c": 1.1, "price": 10},
        {"id": "duck_egg_asian", "name": "鸭蛋", "en": "Duck Egg", "cal": 185, "p": 12.8, "f": 13.8, "c": 1.0, "price": 15},
        {"id": "quail_egg_asian", "name": "鹌鹑蛋", "en": "Quail Egg", "cal": 158, "p": 13.1, "f": 11.1, "c": 0.6, "price": 20},
        {"id": "goose_egg", "name": "鹅蛋", "en": "Goose Egg", "cal": 185, "p": 13.9, "f": 13.3, "c": 1.4, "price": 25},
        {"id": "ostrich_egg", "name": "鸵鸟蛋", "en": "Ostrich Egg", "cal": 118, "p": 9.7, "f": 8.6, "c": 0.7, "price": 80},
        {"id": "turkey_egg", "name": "火鸡蛋", "en": "Turkey Egg", "cal": 171, "p": 13.7, "f": 11.9, "c": 1.2, "price": 30},
    ],
    "sweeteners": [
        {"id": "honey", "name": "蜂蜜", "en": "Honey", "cal": 304, "p": 0.3, "f": 0, "c": 82.4, "price": 40},
        {"id": "maple_syrup", "name": "枫糖浆", "en": "Maple Syrup", "cal": 260, "p": 0, "f": 0.1, "c": 67.0, "price": 60},
        {"id": "agave", "name": "龙舌兰糖浆", "en": "Agave", "cal": 310, "p": 0, "f": 0, "c": 76.0, "price": 45},
        {"id": "molasses", "name": "糖蜜", "en": "Molasses", "cal": 290, "p": 0, "f": 0.1, "c": 74.7, "price": 25},
        {"id": "brown_rice_syrup", "name": "米糖浆", "en": "Brown Rice Syrup", "cal": 316, "p": 0, "f": 0, "c": 79.0, "price": 35},
        {"id": "date_sugar", "name": "椰枣糖", "en": "Date Sugar", "cal": 280, "p": 2.5, "f": 0.2, "c": 75.0, "price": 40},
        {"id": "coconut_sugar", "name": "椰子糖", "en": "Coconut Sugar", "cal": 375, "p": 1.1, "f": 0.5, "c": 94.0, "price": 30},
        {"id": "stevia", "name": "甜菊糖", "en": "Stevia", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 50},
        {"id": "erythritol", "name": "赤藓糖醇", "en": "Erythritol", "cal": 0, "p": 0, "f": 0, "c": 100, "price": 40},
        {"id": "xylitol", "name": "木糖醇", "en": "Xylitol", "cal": 240, "p": 0, "f": 0, "c": 100, "price": 35},
    ],
    "fermented": [
        {"id": "kimchi", "name": "泡菜", "en": "Kimchi", "cal": 23, "p": 1.7, "f": 0.5, "c": 4.0, "price": 15},
        {"id": "sauerkraut", "name": "德国酸菜", "en": "Sauerkraut", "cal": 19, "p": 0.9, "f": 0.1, "c": 4.3, "price": 12},
        {"id": "miso", "name": "味噌", "en": "Miso", "cal": 199, "p": 12.8, "f": 6.0, "c": 26.5, "price": 25},
        {"id": "tempeh_fermented", "name": "天贝", "en": "Tempeh", "cal": 195, "p": 20.3, "f": 11.0, "c": 7.6, "price": 20},
        {"id": "natto", "name": "纳豆", "en": "Natto", "cal": 212, "p": 17.7, "f": 11.0, "c": 14.4, "price": 18},
        {"id": "pickled_ginger", "name": "腌姜", "en": "Pickled Ginger", "cal": 22, "p": 0.3, "f": 0.1, "c": 5.3, "price": 15},
        {"id": "pickled_cucumber", "name": "酸黄瓜", "en": "Pickled Cucumber", "cal": 14, "p": 0.5, "f": 0.1, "c": 3.2, "price": 10},
        {"id": "pickled_jalapeno", "name": "腌墨西哥辣椒", "en": "Pickled Jalapeno", "cal": 17, "p": 0.5, "f": 0.1, "c": 4.0, "price": 12},
        {"id": "pickled_onion", "name": "腌洋葱", "en": "Pickled Onion", "cal": 23, "p": 0.6, "f": 0.1, "c": 5.5, "price": 10},
        {"id": "pickled_turnip", "name": "腌萝卜", "en": "Pickled Turnip", "cal": 18, "p": 0.5, "f": 0.1, "c": 4.2, "price": 8},
        {"id": "pickled_radish", "name": "腌苤蓝", "en": "Pickled Radish", "cal": 18, "p": 0.5, "f": 0.1, "c": 4.2, "price": 8},
        {"id": "pickled_mango", "name": "腌芒果", "en": "Pickled Mango", "cal": 50, "p": 0.5, "f": 0.2, "c": 12.0, "price": 15},
        {"id": "pickled_lemon", "name": "腌柠檬", "en": "Pickled Lemon", "cal": 20, "p": 0.5, "f": 0.1, "c": 5.0, "price": 20},
        {"id": "pickled_pepper", "name": "腌辣椒", "en": "Pickled Pepper", "cal": 18, "p": 0.5, "f": 0.1, "c": 4.0, "price": 10},
        {"id": "pickled_garlic", "name": "腌蒜", "en": "Pickled Garlic", "cal": 120, "p": 4.0, "f": 0.5, "c": 25.0, "price": 15},
        {"id": "pickled_egg", "name": "腌蛋", "en": "Pickled Egg", "cal": 160, "p": 12.0, "f": 10.0, "c": 2.0, "price": 8},
    ],
    "canned": [
        {"id": "canned_tomato", "name": "罐装番茄", "en": "Canned Tomato", "cal": 24, "p": 1.0, "f": 0.2, "c": 5.1, "price": 8},
        {"id": "canned_bean", "name": "罐装豆子", "en": "Canned Bean", "cal": 110, "p": 7.0, "f": 0.5, "c": 20.0, "price": 8},
        {"id": "canned_corn", "name": "罐装玉米", "en": "Canned Corn", "cal": 67, "p": 2.3, "f": 0.5, "c": 15.0, "price": 6},
        {"id": "canned_tuna", "name": "罐装金枪鱼", "en": "Canned Tuna", "cal": 116, "p": 25.5, "f": 0.8, "c": 0, "price": 15},
        {"id": "canned_salmon", "name": "罐装三文鱼", "en": "Canned Salmon", "cal": 136, "p": 20.0, "f": 6.0, "c": 0, "price": 20},
        {"id": "canned_sardine", "name": "罐装沙丁鱼", "en": "Canned Sardine", "cal": 208, "p": 24.6, "f": 11.4, "c": 0, "price": 12},
        {"id": "canned_anchovy", "name": "罐装鳀鱼", "en": "Canned Anchovy", "cal": 131, "p": 20.4, "f": 4.8, "c": 0, "price": 15},
        {"id": "canned_chickpea", "name": "罐装鹰嘴豆", "en": "Canned Chickpea", "cal": 120, "p": 6.0, "f": 2.0, "c": 18.0, "price": 10},
        {"id": "canned_coconut", "name": "罐装椰浆", "en": "Canned Coconut Milk", "cal": 197, "p": 2.0, "f": 20.0, "c": 3.0, "price": 12},
        {"id": "canned_pumpkin", "name": "罐装南瓜", "en": "Canned Pumpkin", "cal": 34, "p": 1.1, "f": 0.3, "c": 8.1, "price": 10},
        {"id": "canned_mushroom", "name": "罐装蘑菇", "en": "Canned Mushroom", "cal": 25, "p": 1.7, "f": 0.5, "c": 4.0, "price": 8},
        {"id": "canned_olive", "name": "罐装橄榄", "en": "Canned Olive", "cal": 115, "p": 0.8, "f": 10.7, "c": 6.3, "price": 15},
        {"id": "canned_artichoke", "name": "罐装朝鲜蓟", "en": "Canned Artichoke", "cal": 47, "p": 2.9, "f": 0.2, "c": 10.5, "price": 18},
        {"id": "canned_roasted_pepper", "name": "罐装烤辣椒", "en": "Canned Roasted Pepper", "cal": 25, "p": 1.0, "f": 0.3, "c": 5.0, "price": 12},
    ],
}

def create_ingredient_file(category, item):
    """创建单个食材文件"""
    dir_path = KNOWLEDGE_DIR / category
    dir_path.mkdir(parents=True, exist_ok=True)
    
    file_path = dir_path / f"{item['id']}.json"
    
    data = {
        "id": item["id"],
        "name": item["name"],
        "name_en": item["en"],
        "category": category,
        "subcategory": category,
        "nutrition_per_100g": {
            "calories": item["cal"],
            "protein": item["p"],
            "fat": item["f"],
            "carbs": item["c"],
            "fiber": 0
        },
        "price_range": {
            "min": int(item["price"] * 0.7),
            "max": int(item["price"] * 1.3),
            "average": item["price"],
            "unit": "元/斤",
            "last_updated": "2024-01-15"
        },
        "seasonal_availability": {
            "全年": True,
            "best_season": None
        },
        "storage": {
            "fresh": "按照食材特性保存",
            "tips": "参考食材说明"
        },
        "pairing": {
            "classic": [],
            "usage": []
        },
        "tips": []
    }
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    """主函数"""
    count = 0
    
    for category, items in MORE_INGREDIENTS.items():
        for item in items:
            create_ingredient_file(category, item)
            count += 1
    
    print(f"✅ Created {count} additional ingredient files")
    print(f"📂 Total ingredient files: {len(list(KNOWLEDGE_DIR.rglob('*.json')))}")

if __name__ == "__main__":
    main()
