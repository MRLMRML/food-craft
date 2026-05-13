#!/usr/bin/env python3
"""最终补充食材 - 达到1000+"""

import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"

FINAL_INGREDIENTS = {
    "protein_extra": [
        {"id": "whey_protein", "name": "乳清蛋白", "en": "Whey Protein", "cal": 370, "p": 80.0, "f": 3.0, "c": 8.0, "price": 120},
        {"id": "casein_protein", "name": "酪蛋白", "en": "Casein Protein", "cal": 360, "p": 75.0, "f": 2.0, "c": 10.0, "price": 130},
        {"id": "soy_protein", "name": "大豆蛋白", "en": "Soy Protein", "cal": 340, "p": 80.0, "f": 1.0, "c": 7.0, "price": 80},
        {"id": "pea_protein", "name": "豌豆蛋白", "en": "Pea Protein", "cal": 350, "p": 82.0, "f": 2.0, "c": 5.0, "price": 90},
        {"id": "rice_protein", "name": "大米蛋白", "en": "Rice Protein", "cal": 350, "p": 78.0, "f": 2.0, "c": 8.0, "price": 85},
        {"id": "hemp_protein", "name": "火麻蛋白", "en": "Hemp Protein", "cal": 340, "p": 50.0, "f": 12.0, "c": 18.0, "price": 100},
        {"id": "collagen_peptide", "name": "胶原蛋白肽", "en": "Collagen Peptide", "cal": 350, "p": 90.0, "f": 0, "c": 0, "price": 150},
        {"id": "spirulina_powder", "name": "螺旋藻粉", "en": "Spirulina Powder", "cal": 290, "p": 57.5, "f": 7.7, "c": 23.9, "price": 150},
        {"id": "chlorella_powder", "name": "小球藻粉", "en": "Chlorella Powder", "cal": 336, "p": 58.4, "f": 9.3, "c": 23.0, "price": 180},
        {"id": "bee_pollen", "name": "蜂花粉", "en": "Bee Pollen", "cal": 264, "p": 24.0, "f": 5.0, "c": 35.0, "price": 200},
        {"id": "royal_jelly", "name": "蜂王浆", "en": "Royal Jelly", "cal": 150, "p": 5.0, "f": 5.0, "c": 20.0, "price": 300},
        {"id": "propolis", "name": "蜂胶", "en": "Propolis", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 250},
    ],
    "superfood": [
        {"id": "acai_berry", "name": "巴西莓粉", "en": "Acai Powder", "cal": 70, "p": 1.5, "f": 5.0, "c": 4.0, "price": 120},
        {"id": "goji_berry_super", "name": "枸杞干", "en": "Goji Berry", "cal": 349, "p": 14.3, "f": 0.4, "c": 77.1, "price": 50},
        {"id": "maca_powder", "name": "玛卡粉", "en": "Maca Powder", "cal": 325, "p": 14.0, "f": 2.0, "c": 64.0, "price": 100},
        {"id": "cacao_nib", "name": "可可碎粒", "en": "Cacao Nib", "cal": 228, "p": 12.0, "f": 14.0, "c": 46.0, "price": 60},
        {"id": "cacao_powder", "name": "生可可粉", "en": "Cacao Powder", "cal": 228, "p": 20.0, "f": 14.0, "c": 58.0, "price": 50},
        {"id": "lucuma", "name": "路客马果粉", "en": "Lucuma", "cal": 329, "p": 4.0, "f": 1.0, "c": 87.0, "price": 80},
        {"id": "baobab", "name": "猴面包树果粉", "en": "Baobab", "cal": 250, "p": 3.0, "f": 0.5, "c": 80.0, "price": 90},
        {"id": "moringa", "name": "辣木粉", "en": "Moringa", "cal": 205, "p": 27.0, "f": 2.3, "c": 38.0, "price": 70},
        {"id": "wheatgrass", "name": "小麦草粉", "en": "Wheatgrass", "cal": 300, "p": 25.0, "f": 5.0, "c": 40.0, "price": 60},
        {"id": "barley_grass", "name": "大麦草粉", "en": "Barley Grass", "cal": 280, "p": 22.0, "f": 4.0, "c": 38.0, "price": 55},
        {"id": "chaga", "name": "白桦茸", "en": "Chaga", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 200},
        {"id": "lion_mane_mushroom", "name": "猴头菇粉", "en": "Lion's Mane", "cal": 35, "p": 2.5, "f": 0.3, "c": 7.6, "price": 150},
        {"id": "reishi_mushroom", "name": "灵芝粉", "en": "Reishi", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 180},
        {"id": "cordyceps", "name": "虫草花", "en": "Cordyceps", "cal": 200, "p": 25.0, "f": 3.0, "c": 20.0, "price": 250},
        {"id": "turmeric_latte", "name": "姜黄拿铁粉", "en": "Turmeric Latte", "cal": 350, "p": 8.0, "f": 10.0, "c": 60.0, "price": 45},
    ],
    "international": [
        {"id": "kimchi_korean", "name": "韩式泡菜", "en": "Kimchi", "cal": 23, "p": 1.7, "f": 0.5, "c": 4.0, "price": 15},
        {"id": "sauerkraut_german", "name": "德国酸菜", "en": "Sauerkraut", "cal": 19, "p": 0.9, "f": 0.1, "c": 4.3, "price": 12},
        {"id": "pickled_japanese", "name": "日式腌菜", "en": "Tsukemono", "cal": 20, "p": 1.0, "f": 0.2, "c": 4.0, "price": 18},
        {"id": "chutney_indian", "name": "印度酸辣酱", "en": "Chutney", "cal": 100, "p": 1.0, "f": 3.0, "c": 18.0, "price": 20},
        {"id": "relish_american", "name": "美式酸黄瓜酱", "en": "Relish", "cal": 100, "p": 0.5, "f": 0.2, "c": 25.0, "price": 12},
        {"id": "salsa_mexican", "name": "墨西哥莎莎酱", "en": "Salsa", "cal": 36, "p": 1.5, "f": 0.2, "c": 7.0, "price": 15},
        {"id": "guacamole_mexican", "name": "墨西哥牛油果酱", "en": "Guacamole", "cal": 150, "p": 2.0, "f": 13.0, "c": 8.0, "price": 25},
        {"id": "tzatziki_greek", "name": "希腊酸奶黄瓜酱", "en": "Tzatziki", "cal": 60, "p": 3.0, "f": 4.0, "c": 4.0, "price": 20},
        {"id": "hummus_middle_east", "name": "中东鹰嘴豆泥", "en": "Hummus", "cal": 166, "p": 8.0, "f": 10.0, "c": 14.0, "price": 18},
        {"id": "baba_ganoush", "name": "中东茄泥", "en": "Baba Ganoush", "cal": 130, "p": 3.0, "f": 10.0, "c": 8.0, "price": 20},
        {"id": "labneh", "name": "中东酸奶", "en": "Labneh", "cal": 160, "p": 8.0, "f": 12.0, "c": 6.0, "price": 25},
        {"id": "zaatar_mix", "name": "中东香料", "en": "Za'atar", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 25},
        {"id": "dukkah_mix", "name": "埃及香料", "en": "Dukkah", "cal": 400, "p": 15.0, "f": 30.0, "c": 25.0, "price": 30},
        {"id": "berbere", "name": "埃塞俄比亚香料", "en": "Berbere", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 25},
        {"id": "ras_el_hanout", "name": "摩洛哥香料", "en": "Ras el Hanout", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 30},
        {"id": "shichimi_japanese", "name": "日式七味粉", "en": "Shichimi", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 20},
        {"id": "togarashi_japanese", "name": "日式一味粉", "en": "Togarashi", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 18},
        {"id": "furikake", "name": "日式拌饭料", "en": "Furikake", "cal": 300, "p": 15.0, "f": 10.0, "c": 35.0, "price": 25},
        {"id": "tajin_mexican", "name": "墨西哥调味料", "en": "Tajín", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 15},
        {"id": "old_bay_american", "name": "美式海鲜调味料", "en": "Old Bay", "cal": 0, "p": 0, "f": 0, "c": 0, "price": 18},
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
    
    for category, items in FINAL_INGREDIENTS.items():
        for item in items:
            create_ingredient_file(category, item)
            count += 1
    
    print(f"✅ Created {count} final ingredient files")
    print(f"📂 Total ingredient files: {len(list(KNOWLEDGE_DIR.rglob('*.json')))}")

if __name__ == "__main__":
    main()
