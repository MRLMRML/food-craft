#!/usr/bin/env python3
"""
更新食材价格数据
数据源：盒马、美团买菜、叮咚买菜等公开数据
"""

import json
import os
from datetime import datetime
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

def fetch_prices():
    """
    从生鲜电商获取价格数据
    注意：实际实现需要处理反爬、API限制等
    """
    # 示例数据，实际实现需要对接真实数据源
    prices = {
        "meat": {
            "chicken_leg": {
                "min": 12,
                "max": 25,
                "average": 18,
                "unit": "元/500g",
                "source": "盒马",
                "city": "上海",
                "updated": datetime.now().isoformat()
            },
            "pork_belly": {
                "min": 15,
                "max": 30,
                "average": 22,
                "unit": "元/500g",
                "source": "美团买菜",
                "city": "上海",
                "updated": datetime.now().isoformat()
            },
            "beef_sirloin": {
                "min": 40,
                "max": 80,
                "average": 60,
                "unit": "元/500g",
                "source": "盒马",
                "city": "上海",
                "updated": datetime.now().isoformat()
            }
        },
        "vegetables": {
            "tomato": {
                "min": 3,
                "max": 8,
                "average": 5,
                "unit": "元/500g",
                "source": "美团买菜",
                "city": "上海",
                "updated": datetime.now().isoformat()
            },
            "potato": {
                "min": 2,
                "max": 5,
                "average": 3,
                "unit": "元/500g",
                "source": "叮咚买菜",
                "city": "上海",
                "updated": datetime.now().isoformat()
            }
        }
    }
    return prices

def update_price_index():
    """更新价格索引文件"""
    prices = fetch_prices()
    
    price_file = KNOWLEDGE_DIR / "price_index.json"
    
    # 读取现有数据
    if price_file.exists():
        with open(price_file, 'r', encoding='utf-8') as f:
            existing = json.load(f)
    else:
        existing = {"version": "1.0.0", "price_index": {}}
    
    # 合并更新
    for category, items in prices.items():
        if category not in existing["price_index"]:
            existing["price_index"][category] = {}
        existing["price_index"][category].update(items)
    
    existing["last_updated"] = datetime.now().isoformat()
    
    # 写入文件
    with open(price_file, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Price index updated at {datetime.now().isoformat()}")

if __name__ == "__main__":
    update_price_index()
