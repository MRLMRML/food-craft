#!/usr/bin/env python3
"""更多全球食材 - 补充到1000+"""

import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"

EXTRA_INGREDIENTS = {
    "snack": [
        {"id": "potato_chip", "name": "薯片", "en": "Potato Chip", "cal": 536, "p": 7.0, "f": 35.0, "c": 50.0, "price": 15},
        {"id": "tortilla_chip", "name": "玉米片", "en": "Tortilla Chip", "cal": 510, "p": 7.0, "f": 27.0, "c": 60.0, "price": 12},
        {"id": "popcorn", "name": "爆米花", "en": "Popcorn", "cal": 387, "p": 12.0, "f": 4.5, "c": 78.0, "price": 10},
        {"id": "pretzel_snack", "name": "椒盐脆饼", "en": "Pretzel", "cal": 338, "p": 9.2, "f": 3.1, "c": 68.0, "price": 10},
        {"id": "cracker", "name": "饼干", "en": "Cracker", "cal": 484, "p": 7.0, "f": 22.0, "c": 64.0, "price": 12},
        {"id": "rice_cake", "name": "米饼", "en": "Rice Cake", "cal": 387, "p": 7.0, "f": 3.0, "c": 81.0, "price": 8},
        {"id": "granola", "name": "燕麦棒", "en": "Granola", "cal": 471, "p": 10.0, "f": 20.0, "c": 64.0, "price": 20},
        {"id": "trail_mix", "name": "什锦干果", "en": "Trail Mix", "cal": 462, "p": 15.0, "f": 27.0, "c": 45.0, "price": 30},
        {"id": "jerky", "name": "肉干", "en": "Jerky", "cal": 410, "p": 33.0, "f": 26.0, "c": 11.0, "price": 40},
        {"id": "dried_fruit", "name": "果干", "en": "Dried Fruit", "cal": 359, "p": 1.0, "f": 0.5, "c": 89.0, "price": 25},
        {"id": "chocolate_chip", "name": "巧克力豆", "en": "Chocolate Chip", "cal": 500, "p": 5.0, "f": 30.0, "c": 58.0, "price": 20},
        {"id": "gummy_bear", "name": "软糖", "en": "Gummy Bear", "cal": 343, "p": 0.0, "f": 0.0, "c": 86.0, "price": 15},
        {"id": "marshmallow", "name": "棉花糖", "en": "Marshmallow", "cal": 318, "p": 1.8, "f": 0.2, "c": 81.0, "price": 12},
        {"id": "caramel", "name": "焦糖", "en": "Caramel", "cal": 382, "p": 1.0, "f": 8.0, "c": 77.0, "price": 15},
        {"id": "toffee", "name": "太妃糖", "en": "Toffee", "cal": 460, "p": 1.5, "f": 22.0, "c": 65.0, "price": 18},
    ],
    "breakfast": [
        {"id": "oatmeal", "name": "燕麦片", "en": "Oatmeal", "cal": 389, "p": 16.9, "f": 6.9, "c": 66.3, "price": 12},
        {"id": "granola_cereal", "name": "燕麦格兰诺拉", "en": "Granola", "cal": 471, "p": 10.0, "f": 20.0, "c": 64.0, "price": 25},
        {"id": "corn_flake", "name": "玉米片", "en": "Corn Flake", "cal": 357, "p": 7.5, "f": 0.4, "c": 84.0, "price": 15},
        {"id": "bran_flake", "name": "麦麸片", "en": "Bran Flake", "cal": 330, "p": 12.0, "f": 2.5, "c": 73.0, "price": 18},
        {"id": "wheat_germ", "name": "麦胚", "en": "Wheat Germ", "cal": 360, "p": 23.0, "f": 10.0, "c": 52.0, "price": 20},
        {"id": "muesli", "name": "木斯里", "en": "Muesli", "cal": 340, "p": 10.0, "f": 5.0, "c": 65.0, "price": 22},
        {"id": "cream_of_wheat", "name": "麦片粥", "en": "Cream of Wheat", "cal": 360, "p": 12.0, "f": 1.0, "c": 76.0, "price": 10},
        {"id": "grits", "name": "玉米粥", "en": "Grits", "cal": 65, "p": 1.4, "f": 0.2, "c": 14.0, "price": 8},
        {"id": "pancake", "name": "松饼", "en": "Pancake", "cal": 227, "p": 6.0, "f": 10.0, "c": 28.0, "price": 15},
        {"id": "waffle", "name": "华夫饼", "en": "Waffle", "cal": 291, "p": 7.9, "f": 14.1, "c": 32.0, "price": 18},
        {"id": "french_toast", "name": "法式吐司", "en": "French Toast", "cal": 214, "p": 8.0, "f": 10.0, "c": 22.0, "price": 15},
        {"id": "bagel_breakfast", "name": "百吉饼", "en": "Bagel", "cal": 250, "p": 10.0, "f": 1.5, "c": 50.0, "price": 10},
        {"id": "muffin", "name": "英式松饼", "en": "Muffin", "cal": 296, "p": 5.0, "f": 13.0, "c": 40.0, "price": 12},
        {"id": "scone", "name": "司康", "en": "Scone", "cal": 360, "p": 6.0, "f": 15.0, "c": 50.0, "price": 15},
        {"id": "croissant_breakfast", "name": "牛角面包", "en": "Croissant", "cal": 406, "p": 8.2, "f": 21.0, "c": 45.0, "price": 12},
    ],
    "dessert": [
        {"id": "ice_cream", "name": "冰淇淋", "en": "Ice Cream", "cal": 207, "p": 3.5, "f": 11.0, "c": 24.0, "price": 20},
        {"id": "gelato", "name": "意式冰淇淋", "en": "Gelato", "cal": 160, "p": 3.0, "f": 8.0, "c": 20.0, "price": 30},
        {"id": "sorbet", "name": "雪芭", "en": "Sorbet", "cal": 120, "p": 0.5, "f": 0.2, "c": 30.0, "price": 25},
        {"id": "frozen_yogurt", "name": "冻酸奶", "en": "Frozen Yogurt", "cal": 127, "p": 3.0, "f": 4.0, "c": 22.0, "price": 20},
        {"id": "pudding", "name": "布丁", "en": "Pudding", "cal": 130, "p": 3.0, "f": 4.0, "c": 22.0, "price": 15},
        {"id": "custard", "name": "蛋奶冻", "en": "Custard", "cal": 122, "p": 4.0, "f": 4.0, "c": 18.0, "price": 18},
        {"id": "flan", "name": "焦糖布丁", "en": "Flan", "cal": 145, "p": 4.0, "f": 5.0, "c": 22.0, "price": 20},
        {"id": "creme_brulee", "name": "法式焦糖布丁", "en": "Crème Brûlée", "cal": 340, "p": 5.0, "f": 28.0, "c": 18.0, "price": 35},
        {"id": "tiramisu", "name": "提拉米苏", "en": "Tiramisu", "cal": 240, "p": 4.0, "f": 14.0, "c": 25.0, "price": 35},
        {"id": "cheesecake", "name": "芝士蛋糕", "en": "Cheesecake", "cal": 321, "p": 6.0, "f": 23.0, "c": 26.0, "price": 30},
        {"id": "brownie", "name": "布朗尼", "en": "Brownie", "cal": 466, "p": 5.0, "f": 27.0, "c": 50.0, "price": 20},
        {"id": "cookie", "name": "曲奇", "en": "Cookie", "cal": 502, "p": 5.0, "f": 25.0, "c": 65.0, "price": 18},
        {"id": "macaron", "name": "马卡龙", "en": "Macaron", "cal": 400, "p": 8.0, "f": 18.0, "c": 55.0, "price": 50},
        {"id": "eclair", "name": "闪电泡芙", "en": "Éclair", "cal": 262, "p": 5.0, "f": 14.0, "c": 30.0, "price": 25},
        {"id": "profiterole", "name": "泡芙", "en": "Profiterole", "cal": 250, "p": 4.0, "f": 15.0, "c": 25.0, "price": 20},
        {"id": "cannoli", "name": "卡诺里", "en": "Cannoli", "cal": 280, "p": 6.0, "f": 14.0, "c": 35.0, "price": 25},
        {"id": "baklava", "name": "果仁蜜饼", "en": "Baklava", "cal": 428, "p": 7.0, "f": 27.0, "c": 44.0, "price": 30},
        {"id": "mochi", "name": "麻薯", "en": "Mochi", "cal": 260, "p": 3.0, "f": 1.0, "c": 60.0, "price": 20},
        {"id": "dango", "name": "团子", "en": "Dango", "cal": 200, "p": 3.0, "f": 0.5, "c": 45.0, "price": 15},
        {"id": "taiyaki", "name": "鲷鱼烧", "en": "Taiyaki", "cal": 220, "p": 4.0, "f": 2.0, "c": 48.0, "price": 12},
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
    
    for category, items in EXTRA_INGREDIENTS.items():
        for item in items:
            create_ingredient_file(category, item)
            count += 1
    
    print(f"✅ Created {count} extra ingredient files")
    print(f"📂 Total ingredient files: {len(list(KNOWLEDGE_DIR.rglob('*.json')))}")

if __name__ == "__main__":
    main()
