#!/usr/bin/env python3
"""
更新热门菜谱趋势
"""

import json
from datetime import datetime
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

def update_trending():
    """更新热门菜谱趋势"""
    # 这里可以对接下厨房、美食杰等平台的热菜数据
    # 示例：更新菜系的流行度分数
    
    cuisines_dir = KNOWLEDGE_DIR / "cuisines"
    
    updated_count = 0
    for cuisine_file in cuisines_dir.rglob("*.json"):
        if cuisine_file.name == "index.json":
            continue
        
        with open(cuisine_file, 'r', encoding='utf-8') as f:
            cuisine = json.load(f)
        
        # 更新最后更新时间
        cuisine["last_updated"] = datetime.now().isoformat()
        
        with open(cuisine_file, 'w', encoding='utf-8') as f:
            json.dump(cuisine, f, ensure_ascii=False, indent=2)
        
        updated_count += 1
    
    print(f"✅ Updated {updated_count} cuisine files")

if __name__ == "__main__":
    update_trending()
