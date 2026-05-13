#!/usr/bin/env python3
"""更多全球食材 - 调味料、酱料、饮料等"""

import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"

CONDIMENT_INGREDIENTS = {
    "sauce": [
        {"id": "soy_sauce_light", "name": "生抽", "en": "Light Soy Sauce", "cal": 53, "p": 8.6, "f": 0.1, "c": 4.9, "price": 12},
        {"id": "soy_sauce_dark", "name": "老抽", "en": "Dark Soy Sauce", "cal": 53, "p": 8.6, "f": 0.1, "c": 4.9, "price": 12},
        {"id": "tamari", "name": "日式酱油", "en": "Tamari", "cal": 60, "p": 10.0, "f": 0.1, "c": 5.0, "price": 25},
        {"id": "ponzu", "name": "柑橘醋", "en": "Ponzu", "cal": 40, "p": 2.0, "f": 0, "c": 8.0, "price": 30},
        {"id": "teriyaki_sauce", "name": "照烧酱", "en": "Teriyaki Sauce", "cal": 150, "p": 5.0, "f": 0, "c": 30.0, "price": 18},
        {"id": "hoisin", "name": "海鲜酱", "en": "Hoisin", "cal": 220, "p": 3.0, "f": 3.0, "c": 45.0, "price": 15},
        {"id": "plum_sauce", "name": "梅子酱", "en": "Plum Sauce", "cal": 180, "p": 0.5, "f": 0.1, "c": 45.0, "price": 12},
        {"id": "sweet_chili", "name": "甜辣酱", "en": "Sweet Chili", "cal": 200, "p": 0.5, "f": 0.2, "c": 50.0, "price": 12},
        {"id": "sriracha_sauce", "name": "是拉差辣椒酱", "en": "Sriracha", "cal": 100, "p": 2.0, "f": 1.0, "c": 20.0, "price": 15},
        {"id": "sambal", "name": "叁巴酱", "en": "Sambal", "cal": 80, "p": 2.0, "f": 3.0, "c": 12.0, "price": 18},
        {"id": "gochujang", "name": "韩式辣酱", "en": "Gochujang", "cal": 220, "p": 5.0, "f": 1.5, "c": 45.0, "price": 20},
        {"id": "doenjang", "name": "韩式大酱", "en": "Doenjang", "cal": 130, "p": 10.0, "f": 5.0, "c": 10.0, "price": 18},
        {"id": "tahini", "name": "芝麻酱", "en": "Tahini", "cal": 595, "p": 17.0, "f": 53.8, "c": 21.2, "price": 25},
        {"id": "harissa", "name": "哈里萨辣酱", "en": "Harissa", "cal": 70, "p": 2.0, "f": 4.0, "c": 8.0, "price": 25},
        {"id": "chimichurri", "name": "奇米丘里酱", "en": "Chimichurri", "cal": 200, "p": 2.0, "f": 18.0, "c": 8.0, "price": 30},
        {"id": "pesto", "name": "青酱", "en": "Pesto", "cal": 350, "p": 5.0, "f": 32.0, "c": 10.0, "price": 35},
        {"id": "marinara", "name": "意式番茄酱", "en": "Marinara", "cal": 50, "p": 1.5, "f": 1.0, "c": 9.0, "price": 15},
        {"id": "bolognese", "name": "肉酱", "en": "Bolognese", "cal": 120, "p": 8.0, "f": 6.0, "c": 8.0, "price": 20},
        {"id": "alfredo", "name": "白酱", "en": "Alfredo", "cal": 300, "p": 5.0, "f": 28.0, "c": 8.0, "price": 25},
        {"id": "bechamel", "name": "贝夏梅酱", "en": "Béchamel", "cal": 150, "p": 5.0, "f": 12.0, "c": 8.0, "price": 20},
        {"id": "hollandaise", "name": "荷兰酱", "en": "Hollandaise", "cal": 400, "p": 5.0, "f": 40.0, "c": 3.0, "price": 30},
        {"id": "aioli", "name": "蒜泥蛋黄酱", "en": "Aioli", "cal": 600, "p": 2.0, "f": 65.0, "c": 3.0, "price": 25},
        {"id": "remoulade", "name": "雷穆拉酱", "en": "Rémoulade", "cal": 350, "p": 1.5, "f": 35.0, "c": 8.0, "price": 20},
        {"id": "tartar", "name": "鞑靼酱", "en": "Tartar", "cal": 300, "p": 1.0, "f": 30.0, "c": 8.0, "price": 18},
        {"id": "cocktail", "name": "鸡尾酒酱", "en": "Cocktail", "cal": 150, "p": 1.0, "f": 10.0, "c": 15.0, "price": 15},
        {"id": "barbecue", "name": "烧烤酱", "en": "Barbecue", "cal": 150, "p": 1.0, "f": 0.5, "c": 35.0, "price": 12},
        {"id": "mustard_dijon", "name": "第戎芥末", "en": "Dijon Mustard", "cal": 66, "p": 4.0, "f": 4.0, "c": 5.0, "price": 20},
        {"id": "mustard_yellow", "name": "黄芥末", "en": "Yellow Mustard", "cal": 60, "p": 3.7, "f": 3.3, "c": 5.8, "price": 10},
        {"id": "mustard_whole", "name": "整粒芥末", "en": "Whole Grain Mustard", "cal": 66, "p": 4.0, "f": 4.0, "c": 5.0, "price": 18},
        {"id": "ketchup_asian", "name": "番茄酱", "en": "Ketchup", "cal": 100, "p": 1.0, "f": 0.1, "c": 25.0, "price": 10},
        {"id": "mayo", "name": "蛋黄酱", "en": "Mayonnaise", "cal": 680, "p": 1.0, "f": 75.0, "c": 1.0, "price": 15},
        {"id": "mirin", "name": "味醂", "en": "Mirin", "cal": 241, "p": 0.3, "f": 0, "c": 47.0, "price": 25},
        {"id": "rice_vinegar", "name": "米醋", "en": "Rice Vinegar", "cal": 20, "p": 0, "f": 0, "c": 5.0, "price": 12},
        {"id": "apple_cider_vinegar", "name": "苹果醋", "en": "Apple Cider Vinegar", "cal": 22, "p": 0, "f": 0, "c": 0.9, "price": 15},
        {"id": "balsamic", "name": "巴萨米克醋", "en": "Balsamic Vinegar", "cal": 88, "p": 0.5, "f": 0, "c": 17.0, "price": 40},
        {"id": "sherry_vinegar", "name": "雪利酒醋", "en": "Sherry Vinegar", "cal": 20, "p": 0, "f": 0, "c": 3.0, "price": 35},
        {"id": "red_wine_vinegar", "name": "红酒醋", "en": "Red Wine Vinegar", "cal": 19, "p": 0, "f": 0, "c": 0.3, "price": 20},
        {"id": "white_wine_vinegar", "name": "白酒醋", "en": "White Wine Vinegar", "cal": 19, "p": 0, "f": 0, "c": 0.2, "price": 20},
    ],
    "drink": [
        {"id": "green_tea", "name": "绿茶", "en": "Green Tea", "cal": 1, "p": 0.2, "f": 0, "c": 0, "price": 50},
        {"id": "black_tea", "name": "红茶", "en": "Black Tea", "cal": 1, "p": 0.2, "f": 0, "c": 0, "price": 40},
        {"id": "oolong_tea", "name": "乌龙茶", "en": "Oolong Tea", "cal": 1, "p": 0.2, "f": 0, "c": 0, "price": 60},
        {"id": "white_tea", "name": "白茶", "en": "White Tea", "cal": 1, "p": 0.2, "f": 0, "c": 0, "price": 80},
        {"id": "pu_erh", "name": "普洱茶", "en": "Pu-erh Tea", "cal": 1, "p": 0.2, "f": 0, "c": 0, "price": 100},
        {"id": "matcha", "name": "抹茶", "en": "Matcha", "cal": 324, "p": 30.0, "f": 5.0, "c": 38.0, "price": 120},
        {"id": "chai", "name": "印度奶茶", "en": "Chai", "cal": 50, "p": 1.0, "f": 1.5, "c": 8.0, "price": 25},
        {"id": "herbal_tea", "name": "花草茶", "en": "Herbal Tea", "cal": 1, "p": 0, "f": 0, "c": 0, "price": 30},
        {"id": "rooibos", "name": "路易波士茶", "en": "Rooibos", "cal": 1, "p": 0, "f": 0, "c": 0, "price": 35},
        {"id": "coffee_bean", "name": "咖啡豆", "en": "Coffee Bean", "cal": 2, "p": 0.1, "f": 0, "c": 0, "price": 80},
        {"id": "espresso", "name": "浓缩咖啡", "en": "Espresso", "cal": 9, "p": 0.1, "f": 0.2, "c": 1.7, "price": 5},
        {"id": "cocoa", "name": "可可粉", "en": "Cocoa", "cal": 228, "p": 20.0, "f": 14.0, "c": 58.0, "price": 40},
        {"id": "chocolate_dark", "name": "黑巧克力", "en": "Dark Chocolate", "cal": 546, "p": 5.0, "f": 31.0, "c": 60.0, "price": 50},
        {"id": "chocolate_milk", "name": "牛奶巧克力", "en": "Milk Chocolate", "cal": 535, "p": 7.7, "f": 30.0, "c": 59.0, "price": 40},
        {"id": "chocolate_white", "name": "白巧克力", "en": "White Chocolate", "cal": 539, "p": 5.9, "f": 32.0, "c": 59.0, "price": 45},
        {"id": "protein_powder", "name": "蛋白粉", "en": "Protein Powder", "cal": 370, "p": 80.0, "f": 3.0, "c": 8.0, "price": 100},
        {"id": "collagen", "name": "胶原蛋白", "en": "Collagen", "cal": 350, "p": 90.0, "f": 0, "c": 0, "price": 120},
    ],
    "baking": [
        {"id": "flour_all_purpose", "name": "中筋面粉", "en": "All-Purpose Flour", "cal": 364, "p": 10.3, "f": 1.0, "c": 76.3, "price": 5},
        {"id": "flour_bread", "name": "高筋面粉", "en": "Bread Flour", "cal": 361, "p": 12.0, "f": 1.0, "c": 72.5, "price": 6},
        {"id": "flour_cake", "name": "低筋面粉", "en": "Cake Flour", "cal": 362, "p": 8.0, "f": 0.8, "c": 76.3, "price": 7},
        {"id": "flour_whole_wheat", "name": "全麦面粉", "en": "Whole Wheat Flour", "cal": 340, "p": 13.2, "f": 2.5, "c": 72.0, "price": 6},
        {"id": "flour_almond", "name": "杏仁粉", "en": "Almond Flour", "cal": 571, "p": 21.0, "f": 50.0, "c": 20.0, "price": 40},
        {"id": "flour_coconut", "name": "椰子粉", "en": "Coconut Flour", "cal": 443, "p": 19.0, "f": 14.0, "c": 60.0, "price": 35},
        {"id": "flour_rice", "name": "米粉", "en": "Rice Flour", "cal": 366, "p": 6.0, "f": 1.4, "c": 80.0, "price": 8},
        {"id": "flour_tapioca", "name": "木薯粉", "en": "Tapioca Flour", "cal": 358, "p": 0.2, "f": 0.1, "c": 88.7, "price": 10},
        {"id": "flour_potato", "name": "土豆淀粉", "en": "Potato Starch", "cal": 357, "p": 0.1, "f": 0.1, "c": 88.0, "price": 8},
        {"id": "flour_corn", "name": "玉米淀粉", "en": "Corn Starch", "cal": 381, "p": 0.3, "f": 0.1, "c": 91.3, "price": 6},
        {"id": "baking_powder", "name": "泡打粉", "en": "Baking Powder", "cal": 53, "p": 0, "f": 0, "c": 27.7, "price": 8},
        {"id": "baking_soda", "name": "小苏打", "en": "Baking Soda", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 5},
        {"id": "yeast", "name": "酵母", "en": "Yeast", "cal": 325, "p": 40.4, "f": 7.6, "c": 41.2, "price": 10},
        {"id": "gelatin", "name": "明胶", "en": "Gelatin", "cal": 335, "p": 85.6, "f": 0.1, "c": 0, "price": 20},
        {"id": "agar", "name": "琼脂", "en": "Agar", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 25},
        {"id": "cornstarch", "name": "玉米淀粉", "en": "Cornstarch", "cal": 381, "p": 0.3, "f": 0.1, "c": 91.3, "price": 6},
        {"id": "cocoa_powder", "name": "可可粉", "en": "Cocoa Powder", "cal": 228, "p": 20.0, "f": 14.0, "c": 58.0, "price": 30},
        {"id": "vanilla_extract", "name": "香草精", "en": "Vanilla Extract", "cal": 288, "p": 0.1, "f": 0.1, "c": 12.7, "price": 50},
        {"id": "almond_extract", "name": "杏仁精", "en": "Almond Extract", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 45},
        {"id": "peppermint_extract", "name": "薄荷精", "en": "Peppermint Extract", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 40},
        {"id": "lemon_extract", "name": "柠檬精", "en": "Lemon Extract", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 35},
        {"id": "orange_extract", "name": "橙子精", "en": "Orange Extract", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 35},
        {"id": "coconut_extract", "name": "椰子精", "en": "Coconut Extract", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 35},
        {"id": "rum_extract", "name": "朗姆精", "en": "Rum Extract", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 40},
        {"id": "food_coloring", "name": "食用色素", "en": "Food Coloring", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 15},
        {"id": "sprinkles", "name": "糖珠", "en": "Sprinkles", "cal": 375, "p": 0, "f": 0, "c": 94.0, "price": 15},
        {"id": "fondant", "name": "翻糖", "en": "Fondant", "cal": 375, "p": 0, "f": 0, "c": 94.0, "price": 25},
        {"id": "marzipan", "name": "杏仁膏", "en": "Marzipan", "cal": 452, "p": 8.0, "f": 27.0, "c": 48.0, "price": 40},
        {"id": "royal_icing", "name": "皇家糖霜", "en": "Royal Icing", "cal": 375, "p": 0, "f": 0, "c": 94.0, "price": 15},
        {"id": "cream_of_tartar", "name": "塔塔粉", "en": "Cream of Tartar", "cal": 258, "p": 0, "f": 0, "c": 64.0, "price": 20},
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
    
    for category, items in CONDIMENT_INGREDIENTS.items():
        for item in items:
            create_ingredient_file(category, item)
            count += 1
    
    print(f"✅ Created {count} condiment/ingredient files")
    print(f"📂 Total ingredient files: {len(list(KNOWLEDGE_DIR.rglob('*.json')))}")

if __name__ == "__main__":
    main()
