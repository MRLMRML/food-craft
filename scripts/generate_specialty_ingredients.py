#!/usr/bin/env python3
"""全球特色食材 - 水果、蔬菜、肉类等"""

import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"

SPECIALTY_INGREDIENTS = {
    "fruit": [
        {"id": "avocado", "name": "牛油果", "en": "Avocado", "cal": 160, "p": 2.0, "f": 14.7, "c": 8.5, "price": 10},
        {"id": "fig", "name": "无花果", "en": "Fig", "cal": 74, "p": 0.8, "f": 0.3, "c": 19.2, "price": 20},
        {"id": "pomegranate", "name": "石榴", "en": "Pomegranate", "cal": 83, "p": 1.7, "f": 1.2, "c": 18.7, "price": 12},
        {"id": "persimmon", "name": "柿子", "en": "Persimmon", "cal": 70, "p": 0.6, "f": 0.2, "c": 18.6, "price": 8},
        {"id": "lychee", "name": "荔枝", "en": "Lychee", "cal": 66, "p": 0.8, "f": 0.4, "c": 16.5, "price": 15},
        {"id": "rambutan", "name": "红毛丹", "en": "Rambutan", "cal": 68, "p": 0.7, "f": 0.2, "c": 16.0, "price": 20},
        {"id": "dragon_fruit", "name": "火龙果", "en": "Dragon Fruit", "cal": 50, "p": 1.1, "f": 0.4, "c": 11.0, "price": 12},
        {"id": "passion_fruit", "name": "百香果", "en": "Passion Fruit", "cal": 97, "p": 2.2, "f": 0.7, "c": 23.4, "price": 10},
        {"id": "guava", "name": "番石榴", "en": "Guava", "cal": 68, "p": 2.6, "f": 1.0, "c": 14.3, "price": 8},
        {"id": "papaya", "name": "木瓜", "en": "Papaya", "cal": 43, "p": 0.5, "f": 0.3, "c": 10.8, "price": 8},
        {"id": "jackfruit", "name": "菠萝蜜", "en": "Jackfruit", "cal": 95, "p": 1.7, "f": 0.6, "c": 23.3, "price": 15},
        {"id": "durian", "name": "榴莲", "en": "Durian", "cal": 147, "p": 1.5, "f": 5.3, "c": 27.1, "price": 30},
        {"id": "mangosteen", "name": "山竹", "en": "Mangosteen", "cal": 73, "p": 0.6, "f": 0.6, "c": 17.9, "price": 20},
        {"id": "starfruit", "name": "杨桃", "en": "Starfruit", "cal": 31, "p": 1.0, "f": 0.3, "c": 6.7, "price": 10},
        {"id": "longan", "name": "龙眼", "en": "Longan", "cal": 60, "p": 1.3, "f": 0.1, "c": 15.0, "price": 12},
        {"id": "kumquat", "name": "金桔", "en": "Kumquat", "cal": 71, "p": 1.9, "f": 0.9, "c": 15.9, "price": 15},
        {"id": "tangerine", "name": "橘子", "en": "Tangerine", "cal": 53, "p": 0.8, "f": 0.3, "c": 13.3, "price": 5},
        {"id": "grapefruit", "name": "西柚", "en": "Grapefruit", "cal": 42, "p": 0.8, "f": 0.1, "c": 10.7, "price": 8},
        {"id": "lime", "name": "青柠", "en": "Lime", "cal": 30, "p": 0.7, "f": 0.2, "c": 10.5, "price": 5},
        {"id": "yuzu", "name": "柚子", "en": "Yuzu", "cal": 20, "p": 0.5, "f": 0.1, "c": 5.0, "price": 25},
        {"id": "persian_lime", "name": "波斯青柠", "en": "Persian Lime", "cal": 30, "p": 0.7, "f": 0.2, "c": 10.5, "price": 8},
        {"id": "meyer_lemon", "name": "迈耶柠檬", "en": "Meyer Lemon", "cal": 29, "p": 1.1, "f": 0.3, "c": 9.3, "price": 15},
        {"id": "blood_orange", "name": "血橙", "en": "Blood Orange", "cal": 47, "p": 0.9, "f": 0.1, "c": 11.8, "price": 12},
        {"id": "clementine", "name": "克莱门氏小柑橘", "en": "Clementine", "cal": 47, "p": 0.9, "f": 0.2, "c": 12.0, "price": 10},
        {"id": "mandarin", "name": "柑橘", "en": "Mandarin", "cal": 53, "p": 0.8, "f": 0.3, "c": 13.3, "price": 6},
        {"id": "apricot", "name": "杏", "en": "Apricot", "cal": 48, "p": 1.4, "f": 0.4, "c": 11.1, "price": 15},
        {"id": "plum", "name": "李子", "en": "Plum", "cal": 46, "p": 0.7, "f": 0.3, "c": 11.4, "price": 8},
        {"id": "nectarine", "name": "油桃", "en": "Nectarine", "cal": 44, "p": 1.1, "f": 0.3, "c": 10.6, "price": 10},
        {"id": "peach", "name": "桃子", "en": "Peach", "cal": 39, "p": 0.9, "f": 0.3, "c": 9.5, "price": 8},
        {"id": "cherry", "name": "樱桃", "en": "Cherry", "cal": 50, "p": 1.0, "f": 0.3, "c": 12.2, "price": 30},
        {"id": "blueberry", "name": "蓝莓", "en": "Blueberry", "cal": 57, "p": 0.7, "f": 0.3, "c": 14.5, "price": 30},
        {"id": "raspberry", "name": "覆盆子", "en": "Raspberry", "cal": 52, "p": 1.2, "f": 0.7, "c": 11.9, "price": 35},
        {"id": "blackberry", "name": "黑莓", "en": "Blackberry", "cal": 43, "p": 1.4, "f": 0.5, "c": 9.6, "price": 35},
        {"id": "cranberry", "name": "蔓越莓", "en": "Cranberry", "cal": 46, "p": 0.4, "f": 0.1, "c": 12.2, "price": 40},
        {"id": "gooseberry", "name": "醋栗", "en": "Gooseberry", "cal": 44, "p": 0.9, "f": 0.6, "c": 10.0, "price": 25},
        {"id": "mulberry", "name": "桑葚", "en": "Mulberry", "cal": 43, "p": 1.4, "f": 0.4, "c": 9.8, "price": 20},
        {"id": "elderberry", "name": "接骨木莓", "en": "Elderberry", "cal": 73, "p": 0.7, "f": 0.5, "c": 18.4, "price": 50},
        {"id": "acai", "name": "巴西莓", "en": "Acai", "cal": 70, "p": 1.5, "f": 5.0, "c": 4.0, "price": 80},
        {"id": "goji_berry_fruit", "name": "枸杞", "en": "Goji Berry", "cal": 349, "p": 14.3, "f": 0.4, "c": 77.1, "price": 40},
        {"id": "date", "name": "椰枣", "en": "Date", "cal": 277, "p": 1.8, "f": 0.2, "c": 75.0, "price": 30},
        {"id": "prune", "name": "西梅干", "en": "Prune", "cal": 240, "p": 2.2, "f": 0.4, "c": 63.9, "price": 25},
        {"id": "raisin", "name": "葡萄干", "en": "Raisin", "cal": 299, "p": 3.1, "f": 0.5, "c": 79.2, "price": 20},
        {"id": "currant", "name": "醋栗干", "en": "Currant", "cal": 283, "p": 4.1, "f": 0.4, "c": 74.1, "price": 30},
        {"id": "tamarind", "name": "罗望子", "en": "Tamarind", "cal": 239, "p": 2.8, "f": 0.6, "c": 62.5, "price": 15},
        {"id": "quince", "name": "榅桲", "en": "Quince", "cal": 57, "p": 0.4, "f": 0.1, "c": 15.3, "price": 20},
        {"id": "loquat", "name": "枇杷", "en": "Loquat", "cal": 47, "p": 0.4, "f": 0.2, "c": 12.1, "price": 12},
    ],
    "vegetables_exotic": [
        {"id": "artichoke", "name": "朝鲜蓟", "en": "Artichoke", "cal": 47, "p": 3.3, "f": 0.2, "c": 10.5, "price": 20},
        {"id": "fennel", "name": "茴香", "en": "Fennel", "cal": 31, "p": 1.2, "f": 0.2, "c": 7.3, "price": 12},
        {"id": "endive_asian", "name": "菊苣", "en": "Endive", "cal": 17, "p": 1.3, "f": 0.2, "c": 3.4, "price": 15},
        {"id": "radicchio_asian", "name": "紫菊苣", "en": "Radicchio", "cal": 23, "p": 1.4, "f": 0.3, "c": 4.5, "price": 18},
        {"id": "escarole", "name": "宽叶菊苣", "en": "Escarole", "cal": 19, "p": 1.3, "f": 0.2, "c": 3.7, "price": 15},
        {"id": "frisee", "name": "卷心菊苣", "en": "Frisee", "cal": 17, "p": 1.3, "f": 0.2, "c": 3.4, "price": 18},
        {"id": "watercress_asian", "name": "西洋菜", "en": "Watercress", "cal": 11, "p": 2.3, "f": 0.1, "c": 1.3, "price": 12},
        {"id": "arugula_asian", "name": "芝麻菜", "en": "Arugula", "cal": 25, "p": 2.6, "f": 0.7, "c": 3.7, "price": 15},
        {"id": "mache", "name": "莴苣", "en": "Mâche", "cal": 21, "p": 2.0, "f": 0.4, "c": 3.6, "price": 20},
        {"id": "dandelion_asian", "name": "蒲公英叶", "en": "Dandelion", "cal": 45, "p": 2.7, "f": 0.7, "c": 9.2, "price": 10},
        {"id": "purslane_asian", "name": "马齿苋", "en": "Purslane", "cal": 20, "p": 2.0, "f": 0.4, "c": 3.4, "price": 8},
        {"id": "sorrel_asian", "name": "酸模", "en": "Sorrel", "cal": 22, "p": 2.0, "f": 0.7, "c": 3.2, "price": 15},
        {"id": "amaranth_leaf", "name": "苋菜叶", "en": "Amaranth Leaf", "cal": 23, "p": 2.5, "f": 0.3, "c": 4.0, "price": 8},
        {"id": "chard", "name": "甜菜叶", "en": "Chard", "cal": 19, "p": 1.8, "f": 0.2, "c": 3.7, "price": 10},
        {"id": "collard_asian", "name": "羽衣甘蓝", "en": "Collard", "cal": 32, "p": 3.0, "f": 0.6, "c": 5.4, "price": 12},
        {"id": "mustard_asian", "name": "芥菜", "en": "Mustard", "cal": 27, "p": 2.9, "f": 0.4, "c": 4.7, "price": 6},
        {"id": "turnip_green", "name": "萝卜叶", "en": "Turnip Green", "cal": 20, "p": 1.5, "f": 0.3, "c": 3.9, "price": 5},
        {"id": "beet_green_asian", "name": "甜菜叶", "en": "Beet Green", "cal": 22, "p": 2.2, "f": 0.1, "c": 4.3, "price": 8},
        {"id": "ramps_asian", "name": "野韭", "en": "Ramps", "cal": 35, "p": 2.0, "f": 0.3, "c": 7.1, "price": 25},
        {"id": "fiddlehead", "name": "蕨菜", "en": "Fiddlehead", "cal": 34, "p": 4.6, "f": 0.4, "c": 5.5, "price": 20},
        {"id": "nopales", "name": "仙人掌叶", "en": "Nopales", "cal": 16, "p": 1.3, "f": 0.1, "c": 3.3, "price": 15},
        {"id": "yuca", "name": "木薯", "en": "Yuca", "cal": 160, "p": 1.4, "f": 0.3, "c": 38.1, "price": 8},
        {"id": "malanga_asian", "name": "芋", "en": "Malanga", "cal": 98, "p": 1.5, "f": 0.2, "c": 23.1, "price": 12},
        {"id": "breadfruit", "name": "面包果", "en": "Breadfruit", "cal": 103, "p": 1.1, "f": 0.2, "c": 27.1, "price": 15},
        {"id": "plantain", "name": "大蕉", "en": "Plantain", "cal": 122, "p": 1.3, "f": 0.4, "c": 31.9, "price": 8},
        {"id": "chayote_asian", "name": "佛手瓜", "en": "Chayote", "cal": 19, "p": 0.8, "f": 0.1, "c": 4.5, "price": 8},
        {"id": "jicama_asian", "name": "豆薯", "en": "Jicama", "cal": 38, "p": 0.7, "f": 0.1, "c": 8.8, "price": 12},
        {"id": "daikon_asian2", "name": "大根", "en": "Daikon", "cal": 18, "p": 0.6, "f": 0.1, "c": 4.1, "price": 4},
        {"id": "burdock_asian", "name": "牛蒡", "en": "Burdock", "cal": 72, "p": 1.5, "f": 0.2, "c": 17.3, "price": 12},
    ],
    "meat_exotic": [
        {"id": "ostrich", "name": "鸵鸟肉", "en": "Ostrich", "cal": 114, "p": 22.0, "f": 2.8, "c": 0, "price": 80},
        {"id": "emu", "name": "鸸鹋肉", "en": "Emu", "cal": 104, "p": 23.0, "f": 1.5, "c": 0, "price": 90},
        {"id": "crocodile", "name": "鳄鱼肉", "en": "Crocodile", "cal": 100, "p": 21.0, "f": 1.8, "c": 0, "price": 120},
        {"id": "alligator", "name": "短吻鳄肉", "en": "Alligator", "cal": 100, "p": 21.0, "f": 1.8, "c": 0, "price": 100},
        {"id": "turtle", "name": "甲鱼肉", "en": "Turtle", "cal": 85, "p": 18.0, "f": 1.0, "c": 0, "price": 60},
        {"id": "frog_leg", "name": "青蛙腿", "en": "Frog Leg", "cal": 73, "p": 16.4, "f": 0.3, "c": 0, "price": 40},
        {"id": "snail", "name": "蜗牛", "en": "Snail", "cal": 90, "p": 16.1, "f": 1.4, "c": 2.0, "price": 50},
        {"id": "horse", "name": "马肉", "en": "Horse", "cal": 133, "p": 21.0, "f": 4.6, "c": 0, "price": 80},
        {"id": "goat", "name": "山羊肉", "en": "Goat", "cal": 143, "p": 27.1, "f": 3.0, "c": 0, "price": 45},
        {"id": "mutton", "name": "绵羊肉", "en": "Mutton", "cal": 294, "p": 24.5, "f": 21.8, "c": 0, "price": 55},
        {"id": "veal", "name": "小牛肉", "en": "Veal", "cal": 172, "p": 24.4, "f": 7.6, "c": 0, "price": 70},
        {"id": "boar", "name": "野猪肉", "en": "Boar", "cal": 160, "p": 28.0, "f": 4.0, "c": 0, "price": 80},
        {"id": "buffalo", "name": "水牛肉", "en": "Buffalo", "cal": 146, "p": 28.4, "f": 2.4, "c": 0, "price": 50},
        {"id": "llama", "name": "羊驼肉", "en": "Llama", "cal": 120, "p": 23.0, "f": 2.0, "c": 0, "price": 150},
        {"id": "alpaca", "name": "羊驼肉", "en": "Alpaca", "cal": 120, "p": 23.0, "f": 2.0, "c": 0, "price": 160},
    ],
    "seafood_exotic": [
        {"id": "sea_bass_chilean", "name": "智利海鲈", "en": "Chilean Sea Bass", "cal": 185, "p": 16.0, "f": 13.0, "c": 0, "price": 120},
        {"id": "monkfish", "name": "鮟鱇鱼", "en": "Monkfish", "cal": 76, "p": 14.4, "f": 1.5, "c": 0, "price": 60},
        {"id": "john_dory", "name": "海鲂", "en": "John Dory", "cal": 83, "p": 17.0, "f": 1.0, "c": 0, "price": 80},
        {"id": "turbot", "name": "大菱鲆", "en": "Turbot", "cal": 95, "p": 16.0, "f": 3.0, "c": 0, "price": 90},
        {"id": "dover_sole", "name": "多佛鳎鱼", "en": "Dover Sole", "cal": 91, "p": 18.8, "f": 1.2, "c": 0, "price": 100},
        {"id": "lingcod", "name": " lingcod", "en": "Lingcod", "cal": 85, "p": 18.0, "f": 1.0, "c": 0, "price": 50},
        {"id": "sablefish", "name": "黑鳕鱼", "en": "Sablefish", "cal": 250, "p": 17.0, "f": 20.0, "c": 0, "price": 90},
        {"id": "wahoo", "name": "刺鲅", "en": "Wahoo", "cal": 120, "p": 22.0, "f": 3.0, "c": 0, "price": 70},
        {"id": "amberjack", "name": "琥珀鱼", "en": "Amberjack", "cal": 130, "p": 23.0, "f": 4.0, "c": 0, "price": 60},
        {"id": "yellowtail", "name": "黄尾鱼", "en": "Yellowtail", "cal": 170, "p": 23.0, "f": 8.0, "c": 0, "price": 80},
        {"id": "butterfish", "name": "鲳鱼", "en": "Butterfish", "cal": 150, "p": 18.0, "f": 8.0, "c": 0, "price": 50},
        {"id": "pomfret_asian", "name": "鲳鱼", "en": "Pomfret", "cal": 140, "p": 18.5, "f": 7.3, "c": 0, "price": 60},
        {"id": "threadfin", "name": "马鲅", "en": "Threadfin", "cal": 110, "p": 20.0, "f": 3.0, "c": 0, "price": 45},
        {"id": "grouper_asian", "name": "石斑鱼", "en": "Grouper", "cal": 92, "p": 18.8, "f": 1.0, "c": 0, "price": 70},
        {"id": "red_snapper", "name": "红鲷鱼", "en": "Red Snapper", "cal": 100, "p": 20.5, "f": 1.3, "c": 0, "price": 60},
        {"id": "mango_snapper", "name": "芒果鲷", "en": "Mango Snapper", "cal": 100, "p": 20.0, "f": 1.5, "c": 0, "price": 55},
        {"id": "lane_snapper", "name": "车道鲷", "en": "Lane Snapper", "cal": 100, "p": 20.0, "f": 1.5, "c": 0, "price": 50},
        {"id": "mutton_snapper", "name": "羊肉鲷", "en": "Mutton Snapper", "cal": 100, "p": 20.0, "f": 1.5, "c": 0, "price": 55},
        {"id": "yellowtail_snapper", "name": "黄尾鲷", "en": "Yellowtail Snapper", "cal": 100, "p": 20.0, "f": 1.5, "c": 0, "price": 50},
        {"id": "schoolmaster", "name": "校长鲷", "en": "Schoolmaster", "cal": 100, "p": 20.0, "f": 1.5, "c": 0, "price": 45},
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
    
    for category, items in SPECIALTY_INGREDIENTS.items():
        for item in items:
            create_ingredient_file(category, item)
            count += 1
    
    print(f"✅ Created {count} specialty ingredient files")
    print(f"📂 Total ingredient files: {len(list(KNOWLEDGE_DIR.rglob('*.json')))}")

if __name__ == "__main__":
    main()
