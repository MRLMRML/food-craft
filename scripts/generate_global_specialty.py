#!/usr/bin/env python3
"""全球特色食材 - 亚洲、欧洲、美洲等"""

import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"

GLOBAL_SPECIALTY = {
    "asian": [
        {"id": "tofu_firm", "name": "老豆腐", "en": "Firm Tofu", "cal": 144, "p": 15.6, "f": 8.7, "c": 4.3, "price": 5},
        {"id": "tofu_silken", "name": "嫩豆腐", "en": "Silken Tofu", "cal": 55, "p": 4.8, "f": 2.7, "c": 1.9, "price": 4},
        {"id": "tofu_fried", "name": "油豆腐", "en": "Fried Tofu", "cal": 271, "p": 17.0, "f": 20.0, "c": 5.0, "price": 8},
        {"id": "tofu_skin_asian", "name": "腐竹", "en": "Tofu Skin", "cal": 460, "p": 44.6, "f": 22.3, "c": 22.3, "price": 15},
        {"id": "tofu_dried_asian", "name": "豆腐干", "en": "Dried Tofu", "cal": 140, "p": 16.2, "f": 5.3, "c": 10.7, "price": 6},
        {"id": "natto_asian", "name": "纳豆", "en": "Natto", "cal": 212, "p": 17.7, "f": 11.0, "c": 14.4, "price": 15},
        {"id": "tempeh_asian", "name": "天贝", "en": "Tempeh", "cal": 195, "p": 20.3, "f": 11.0, "c": 7.6, "price": 18},
        {"id": "miso_asian", "name": "味噌", "en": "Miso", "cal": 199, "p": 12.8, "f": 6.0, "c": 26.5, "price": 25},
        {"id": "kimchi_asian", "name": "泡菜", "en": "Kimchi", "cal": 23, "p": 1.7, "f": 0.5, "c": 4.0, "price": 12},
        {"id": "pickled_ginger_asian", "name": "腌姜", "en": "Pickled Ginger", "cal": 22, "p": 0.3, "f": 0.1, "c": 5.3, "price": 15},
        {"id": "seaweed_nori", "name": "海苔", "en": "Nori", "cal": 35, "p": 5.8, "f": 0.3, "c": 5.1, "price": 20},
        {"id": "seaweed_wakame", "name": "裙带菜", "en": "Wakame", "cal": 45, "p": 3.0, "f": 0.6, "c": 9.1, "price": 25},
        {"id": "seaweed_kombu", "name": "昆布", "en": "Kombu", "cal": 43, "p": 1.7, "f": 0.6, "c": 9.6, "price": 30},
        {"id": "bamboo_shoot_asian", "name": "竹笋", "en": "Bamboo Shoot", "cal": 27, "p": 2.6, "f": 0.2, "c": 5.1, "price": 10},
        {"id": "lotus_root_asian2", "name": "莲藕", "en": "Lotus Root", "cal": 74, "p": 2.6, "f": 0.1, "c": 17.2, "price": 10},
        {"id": "taro_asian2", "name": "芋头", "en": "Taro", "cal": 112, "p": 1.5, "f": 0.2, "c": 26.5, "price": 8},
        {"id": "yam_asian2", "name": "山药", "en": "Yam", "cal": 118, "p": 1.5, "f": 0.2, "c": 27.9, "price": 10},
        {"id": "daikon_asian3", "name": "白萝卜", "en": "Daikon", "cal": 18, "p": 0.6, "f": 0.1, "c": 4.1, "price": 4},
        {"id": "bok_choy_asian", "name": "小白菜", "en": "Bok Choy", "cal": 13, "p": 1.5, "f": 0.2, "c": 2.2, "price": 5},
        {"id": "chinese_broccoli_asian", "name": "芥兰", "en": "Chinese Broccoli", "cal": 22, "p": 2.0, "f": 0.3, "c": 4.0, "price": 6},
        {"id": "choy_sum_asian", "name": "菜心", "en": "Choy Sum", "cal": 20, "p": 1.5, "f": 0.3, "c": 3.5, "price": 5},
        {"id": "water_spinach_asian", "name": "空心菜", "en": "Water Spinach", "cal": 25, "p": 2.6, "f": 0.3, "c": 4.5, "price": 4},
        {"id": "amaranth_asian", "name": "苋菜", "en": "Amaranth", "cal": 23, "p": 2.5, "f": 0.3, "c": 4.0, "price": 5},
        {"id": "snow_pea_asian", "name": "荷兰豆", "en": "Snow Pea", "cal": 42, "p": 2.8, "f": 0.3, "c": 7.6, "price": 8},
        {"id": "long_bean_asian", "name": "长豇豆", "en": "Long Bean", "cal": 47, "p": 2.8, "f": 0.4, "c": 8.4, "price": 6},
        {"id": "bitter_gourd_asian2", "name": "苦瓜", "en": "Bitter Gourd", "cal": 17, "p": 1.0, "f": 0.2, "c": 3.7, "price": 5},
        {"id": "okra_asian", "name": "秋葵", "en": "Okra", "cal": 33, "p": 2.0, "f": 0.1, "c": 7.5, "price": 8},
        {"id": "eggplant_asian", "name": "茄子", "en": "Eggplant", "cal": 25, "p": 1.0, "f": 0.2, "c": 5.7, "price": 5},
        {"id": "shiitake_asian2", "name": "香菇", "en": "Shiitake", "cal": 34, "p": 2.2, "f": 0.5, "c": 6.8, "price": 15},
        {"id": "enoki_asian2", "name": "金针菇", "en": "Enoki", "cal": 37, "p": 2.7, "f": 0.3, "c": 7.8, "price": 8},
        {"id": "king_oyster_asian2", "name": "杏鲍菇", "en": "King Oyster", "cal": 34, "p": 1.3, "f": 0.4, "c": 8.3, "price": 10},
        {"id": "oyster_mushroom_asian2", "name": "平菇", "en": "Oyster Mushroom", "cal": 33, "p": 3.3, "f": 0.4, "c": 6.1, "price": 6},
        {"id": "wood_ear_asian2", "name": "木耳", "en": "Wood Ear", "cal": 37, "p": 1.5, "f": 0.2, "c": 6.5, "price": 15},
        {"id": "tremella_asian", "name": "银耳", "en": "Tremella", "cal": 200, "p": 10.0, "f": 1.4, "c": 63.3, "price": 30},
        {"id": "ginger_asian", "name": "生姜", "en": "Ginger", "cal": 80, "p": 1.8, "f": 0.8, "c": 17.8, "price": 10},
        {"id": "galangal_asian", "name": "南姜", "en": "Galangal", "cal": 71, "p": 1.1, "f": 0.5, "c": 15.8, "price": 20},
        {"id": "turmeric_asian", "name": "姜黄", "en": "Turmeric", "cal": 312, "p": 9.7, "f": 3.3, "c": 67.1, "price": 25},
        {"id": "lemongrass_asian", "name": "香茅", "en": "Lemongrass", "cal": 99, "p": 1.8, "f": 0.5, "c": 25.3, "price": 12},
        {"id": "kaffir_lime_asian", "name": "青柠叶", "en": "Kaffir Lime", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 15},
        {"id": "curry_leaf_asian", "name": "咖喱叶", "en": "Curry Leaf", "cal": 108, "p": 6.0, "f": 1.0, "c": 18.7, "price": 15},
        {"id": "shiso_asian", "name": "紫苏", "en": "Shiso", "cal": 37, "p": 3.8, "f": 0.7, "c": 6.0, "price": 12},
    ],
    "european": [
        {"id": "olive_green", "name": "绿橄榄", "en": "Green Olive", "cal": 115, "p": 0.8, "f": 10.7, "c": 6.3, "price": 20},
        {"id": "olive_black", "name": "黑橄榄", "en": "Black Olive", "cal": 115, "p": 0.8, "f": 10.7, "c": 6.3, "price": 18},
        {"id": "capers", "name": "刺山柑", "en": "Capers", "cal": 23, "p": 2.4, "f": 0.9, "c": 4.9, "price": 35},
        {"id": "anchovy_euro", "name": "鳀鱼", "en": "Anchovy", "cal": 210, "p": 29.0, "f": 10.0, "c": 0, "price": 40},
        {"id": "prosciutto_euro", "name": "意式火腿", "en": "Prosciutto", "cal": 250, "p": 30.0, "f": 14.0, "c": 0, "price": 80},
        {"id": "pancetta_euro", "name": "意式培根", "en": "Pancetta", "cal": 460, "p": 30.0, "f": 37.0, "c": 0, "price": 50},
        {"id": "chorizo_euro", "name": "西班牙辣肠", "en": "Chorizo", "cal": 455, "p": 24.0, "f": 38.0, "c": 1.9, "price": 45},
        {"id": "salami", "name": "萨拉米", "en": "Salami", "cal": 378, "p": 21.0, "f": 31.0, "c": 2.0, "price": 50},
        {"id": "mortadella", "name": "摩泰台拉香肠", "en": "Mortadella", "cal": 310, "p": 16.0, "f": 26.0, "c": 2.0, "price": 40},
        {"id": "bresaola", "name": "风干牛肉", "en": "Bresaola", "cal": 151, "p": 32.0, "f": 2.0, "c": 0, "price": 90},
        {"id": "gruyere_euro", "name": "格鲁耶尔奶酪", "en": "Gruyère", "cal": 413, "p": 29.8, "f": 32.3, "c": 0.4, "price": 70},
        {"id": "emmental_euro", "name": "埃曼塔尔奶酪", "en": "Emmental", "cal": 393, "p": 28.4, "f": 30.5, "c": 0.4, "price": 60},
        {"id": "comte", "name": "孔泰奶酪", "en": "Comté", "cal": 412, "p": 27.0, "f": 34.0, "c": 0.5, "price": 65},
        {"id": "manchego", "name": "曼彻格奶酪", "en": "Manchego", "cal": 392, "p": 25.0, "f": 32.0, "c": 1.0, "price": 55},
        {"id": "pecorino", "name": "佩科里诺奶酪", "en": "Pecorino", "cal": 387, "p": 31.8, "f": 28.0, "c": 0.5, "price": 50},
        {"id": "asiago", "name": "阿齐亚戈奶酪", "en": "Asiago", "cal": 368, "p": 29.0, "f": 28.0, "c": 1.0, "price": 45},
        {"id": "fontina", "name": "芳提娜奶酪", "en": "Fontina", "cal": 389, "p": 25.6, "f": 31.1, "c": 1.6, "price": 50},
        {"id": "taleggio", "name": "塔雷吉欧奶酪", "en": "Taleggio", "cal": 340, "p": 18.0, "f": 28.0, "c": 1.0, "price": 55},
        {"id": "roquefort", "name": "洛克福奶酪", "en": "Roquefort", "cal": 369, "p": 21.5, "f": 30.6, "c": 2.0, "price": 70},
        {"id": "stilton", "name": "斯蒂尔顿奶酪", "en": "Stilton", "cal": 410, "p": 25.0, "f": 35.0, "c": 0.1, "price": 65},
        {"id": "gorgonzola", "name": "戈贡佐拉奶酪", "en": "Gorgonzola", "cal": 350, "p": 21.0, "f": 28.0, "c": 2.0, "price": 60},
        {"id": "truffle_black_euro", "name": "黑松露", "en": "Black Truffle", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 500},
        {"id": "truffle_white_euro", "name": "白松露", "en": "White Truffle", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 800},
        {"id": "saffron", "name": "藏红花", "en": "Saffron", "cal": 310, "p": 11.4, "f": 5.9, "c": 65.4, "price": 300},
        {"id": "herbes_provence", "name": "普罗旺斯香草", "en": "Herbes de Provence", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 25},
        {"id": "bouquet_garni", "name": "香草束", "en": "Bouquet Garni", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 15},
    ],
    "american": [
        {"id": "corn_tortilla", "name": "玉米饼", "en": "Corn Tortilla", "cal": 218, "p": 5.7, "f": 2.9, "c": 44.6, "price": 10},
        {"id": "flour_tortilla", "name": "面粉饼", "en": "Flour Tortilla", "cal": 312, "p": 8.0, "f": 8.0, "c": 52.0, "price": 12},
        {"id": "taco_shell", "name": "塔可壳", "en": "Taco Shell", "cal": 470, "p": 7.0, "f": 24.0, "c": 58.0, "price": 15},
        {"id": "nacho_chip", "name": "玉米片", "en": "Nacho Chip", "cal": 510, "p": 7.0, "f": 27.0, "c": 60.0, "price": 12},
        {"id": "hot_dog_bun", "name": "热狗面包", "en": "Hot Dog Bun", "cal": 270, "p": 9.0, "f": 3.5, "c": 50.0, "price": 8},
        {"id": "hamburger_bun", "name": "汉堡面包", "en": "Hamburger Bun", "cal": 270, "p": 9.0, "f": 3.5, "c": 50.0, "price": 8},
        {"id": "bagel", "name": "百吉饼", "en": "Bagel", "cal": 250, "p": 10.0, "f": 1.5, "c": 50.0, "price": 10},
        {"id": "english_muffin", "name": "英式松饼", "en": "English Muffin", "cal": 235, "p": 8.0, "f": 2.0, "c": 46.0, "price": 10},
        {"id": "croissant", "name": "牛角面包", "en": "Croissant", "cal": 406, "p": 8.2, "f": 21.0, "c": 45.0, "price": 12},
        {"id": "baguette", "name": "法棍", "en": "Baguette", "cal": 274, "p": 10.0, "f": 1.5, "c": 55.0, "price": 10},
        {"id": "sourdough", "name": "酸面包", "en": "Sourdough", "cal": 270, "p": 10.0, "f": 1.5, "c": 54.0, "price": 15},
        {"id": "rye_bread", "name": "黑麦面包", "en": "Rye Bread", "cal": 259, "p": 8.5, "f": 3.3, "c": 48.3, "price": 12},
        {"id": "pita", "name": "皮塔饼", "en": "Pita", "cal": 275, "p": 9.0, "f": 1.7, "c": 55.0, "price": 8},
        {"id": "naan", "name": "印度飞饼", "en": "Naan", "cal": 310, "p": 9.0, "f": 7.0, "c": 52.0, "price": 10},
        {"id": "pretzel", "name": "椒盐卷饼", "en": "Pretzel", "cal": 338, "p": 9.2, "f": 3.1, "c": 68.0, "price": 8},
        {"id": "crouton", "name": "面包丁", "en": "Crouton", "cal": 407, "p": 12.0, "f": 6.0, "c": 74.0, "price": 15},
        {"id": "breadcrumb", "name": "面包糠", "en": "Breadcrumb", "cal": 395, "p": 13.0, "f": 5.0, "c": 72.0, "price": 10},
        {"id": "cornbread", "name": "玉米面包", "en": "Cornbread", "cal": 328, "p": 7.0, "f": 12.0, "c": 48.0, "price": 12},
        {"id": "pancake_mix", "name": "松饼粉", "en": "Pancake Mix", "cal": 360, "p": 8.0, "f": 4.0, "c": 72.0, "price": 15},
        {"id": "waffle_mix", "name": "华夫饼粉", "en": "Waffle Mix", "cal": 360, "p": 8.0, "f": 4.0, "c": 72.0, "price": 15},
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
    
    for category, items in GLOBAL_SPECIALTY.items():
        for item in items:
            create_ingredient_file(category, item)
            count += 1
    
    print(f"✅ Created {count} global specialty ingredient files")
    print(f"📂 Total ingredient files: {len(list(KNOWLEDGE_DIR.rglob('*.json')))}")

if __name__ == "__main__":
    main()
