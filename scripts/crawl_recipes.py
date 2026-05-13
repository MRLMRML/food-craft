#!/usr/bin/env python3
"""
菜谱爬取脚本
数据源：下厨房、美食杰等公开菜谱数据
"""

import json
import os
from pathlib import Path
from datetime import datetime

RECIPES_DIR = Path(__file__).parent.parent / "recipes"

def ensure_dir(path):
    """确保目录存在"""
    path.mkdir(parents=True, exist_ok=True)

def save_recipe(recipe, cuisine, category="general"):
    """保存单个菜谱"""
    dir_path = RECIPES_DIR / cuisine / category
    ensure_dir(dir_path)
    
    filename = f"{recipe['id']}.json"
    filepath = dir_path / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(recipe, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ Saved: {recipe['name']} -> {filepath}")

def crawl_chinese_recipes():
    """爬取中国菜谱（示例数据结构）"""
    print("\n📚 Crawling Chinese recipes...")
    
    # 示例：川菜菜谱
    sichuan_recipes = [
        {
            "id": "gongbao_chicken",
            "name": "宫保鸡丁",
            "name_en": "Kung Pao Chicken",
            "cuisine": "sichuan",
            "category": "meat",
            "difficulty": "medium",
            "time_minutes": 25,
            "servings": 2,
            "calories_per_serving": 200,
            "cost_per_serving": 15,
            "tags": ["家常菜", "下饭菜", "川菜"],
            "ingredients": [
                {"name": "鸡腿肉", "amount": "300g", "type": "meat"},
                {"name": "花生米", "amount": "50g", "type": "nuts"},
                {"name": "干辣椒", "amount": "10个", "type": "spice"},
                {"name": "花椒", "amount": "1小把", "type": "spice"}
            ],
            "seasonings": [
                {"name": "生抽", "amount": "1勺"},
                {"name": "醋", "amount": "2勺"},
                {"name": "糖", "amount": "1.5勺"},
                {"name": "料酒", "amount": "1勺"},
                {"name": "淀粉", "amount": "1勺"}
            ],
            "steps": [
                {"step": 1, "content": "鸡肉切丁，加料酒、生抽、淀粉腌制15分钟", "tip": "切丁大小要均匀"},
                {"step": 2, "content": "调碗汁：醋2勺、糖1.5勺、生抽1勺、淀粉1勺", "tip": "提前调好是关键"},
                {"step": 3, "content": "冷油下花生，小火炸至微黄捞出", "tip": "冷油下锅，小火慢炸"},
                {"step": 4, "content": "锅留底油，爆香干辣椒和花椒", "tip": "小火！花椒炒黑会发苦"},
                {"step": 5, "content": "下鸡丁滑炒至变色", "tip": "大火快炒"},
                {"step": 6, "content": "倒入碗汁，大火翻炒均匀", "tip": "碗汁要搅匀再倒"},
                {"step": 7, "content": "关火，撒花生米，翻两下出锅", "tip": "关火后再放花生，保持脆感"}
            ],
            "key_points": [
                "花椒要炒出香味但不能炒黑",
                "碗汁的糖醋比是灵魂，2:1.5是黄金比例",
                "花生最后放，关火后再放，保持脆感"
            ],
            "nutrition": {
                "calories": 200,
                "protein": 18,
                "fat": 12,
                "carbs": 8
            },
            "source": "xiachufang",
            "created_at": datetime.now().isoformat()
        },
        {
            "id": "mapo_tofu",
            "name": "麻婆豆腐",
            "name_en": "Mapo Tofu",
            "cuisine": "sichuan",
            "category": "vegetable",
            "difficulty": "easy",
            "time_minutes": 15,
            "servings": 2,
            "calories_per_serving": 150,
            "cost_per_serving": 8,
            "tags": ["家常菜", "下饭菜", "川菜", "素菜"],
            "ingredients": [
                {"name": "嫩豆腐", "amount": "1块", "type": "tofu"},
                {"name": "肉末", "amount": "50g", "type": "meat"},
                {"name": "豆瓣酱", "amount": "1勺", "type": "sauce"},
                {"name": "花椒粉", "amount": "适量", "type": "spice"}
            ],
            "seasonings": [
                {"name": "生抽", "amount": "1勺"},
                {"name": "淀粉", "amount": "1勺"},
                {"name": "葱花", "amount": "适量"}
            ],
            "steps": [
                {"step": 1, "content": "豆腐切块，焯水去豆腥", "tip": "焯水时加点盐"},
                {"step": 2, "content": "锅中放油，炒香肉末", "tip": "炒到微焦更香"},
                {"step": 3, "content": "加入豆瓣酱炒出红油", "tip": "小火炒出红油"},
                {"step": 4, "content": "加入适量水，放入豆腐", "tip": "水不要太多"},
                {"step": 5, "content": "煮3分钟，勾芡，撒花椒粉和葱花", "tip": "勾芡要均匀"}
            ],
            "key_points": [
                "豆腐要焯水去豆腥",
                "豆瓣酱要炒出红油",
                "花椒粉最后撒，保持麻味"
            ],
            "nutrition": {
                "calories": 150,
                "protein": 12,
                "fat": 10,
                "carbs": 5
            },
            "source": "xiachufang",
            "created_at": datetime.now().isoformat()
        }
    ]
    
    for recipe in sichuan_recipes:
        save_recipe(recipe, "chinese", "sichuan")
    
    return len(sichuan_recipes)

def crawl_more_cuisines():
    """爬取更多菜系（扩展数据）"""
    print("\n📚 Crawling more cuisines...")
    
    # 这里可以添加更多菜系的爬取逻辑
    # 实际实现时，可以从下厨房、美食杰等网站爬取
    
    return 0

def main():
    """主函数"""
    print("🍽️ Food Craft Recipe Crawler")
    print("=" * 50)
    
    total = 0
    
    # 爬取中国菜谱
    total += crawl_chinese_recipes()
    
    # 爬取更多菜系
    total += crawl_more_cuisines()
    
    print("\n" + "=" * 50)
    print(f"✅ Total recipes crawled: {total}")
    print(f"📂 Recipes saved to: {RECIPES_DIR}")

if __name__ == "__main__":
    main()
