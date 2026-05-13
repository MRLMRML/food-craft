#!/usr/bin/env python3
"""
更新时令食材日历
"""

import json
from datetime import datetime
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

def get_current_season():
    """获取当前季节"""
    month = datetime.now().month
    if month in [3, 4, 5]:
        return "春季"
    elif month in [6, 7, 8]:
        return "夏季"
    elif month in [9, 10, 11]:
        return "秋季"
    else:
        return "冬季"

def update_seasonal_calendar():
    """更新时令食材日历"""
    calendar_file = KNOWLEDGE_DIR / "seasonal_calendar.json"
    
    if calendar_file.exists():
        with open(calendar_file, 'r', encoding='utf-8') as f:
            calendar = json.load(f)
    else:
        calendar = {"version": "1.0.0", "months": {}}
    
    # 更新最后更新时间
    calendar["last_updated"] = datetime.now().isoformat()
    
    # 写入文件
    with open(calendar_file, 'w', encoding='utf-8') as f:
        json.dump(calendar, f, ensure_ascii=False, indent=2)
    
    current_season = get_current_season()
    print(f"✅ Seasonal calendar updated at {datetime.now().isoformat()}")
    print(f"   Current season: {current_season}")

if __name__ == "__main__":
    update_seasonal_calendar()
