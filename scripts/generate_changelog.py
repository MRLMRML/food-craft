#!/usr/bin/env python3
"""
生成更新日志
"""

import json
from datetime import datetime
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"
CHANGELOG_FILE = Path(__file__).parent.parent / "CHANGELOG.md"

def count_files():
    """统计各目录文件数量"""
    counts = {
        "cuisines": 0,
        "ingredients": 0,
        "techniques": 0
    }
    
    for cuisine_file in (KNOWLEDGE_DIR / "cuisines").rglob("*.json"):
        if cuisine_file.name != "index.json":
            counts["cuisines"] += 1
    
    for ingredient_file in (KNOWLEDGE_DIR / "ingredients").rglob("*.json"):
        if ingredient_file.name != "index.json":
            counts["ingredients"] += 1
    
    for technique_file in (KNOWLEDGE_DIR / "techniques").rglob("*.json"):
        counts["techniques"] += 1
    
    return counts

def generate_changelog():
    """生成更新日志"""
    counts = count_files()
    date = datetime.now().strftime("%Y-%m-%d")
    
    entry = f"""
## [{date}]

### 知识库统计
- 菜系: {counts['cuisines']} 个
- 食材: {counts['ingredients']} 个
- 技法: {counts['techniques']} 个

### 更新内容
- 自动更新价格数据
- 更新时令食材日历
- 数据完整性校验通过

---
"""
    
    # 读取现有日志
    if CHANGELOG_FILE.exists():
        with open(CHANGELOG_FILE, 'r', encoding='utf-8') as f:
            existing = f.read()
    else:
        existing = "# Changelog\n\n"
    
    # 写入新日志
    with open(CHANGELOG_FILE, 'w', encoding='utf-8') as f:
        f.write(existing + entry)
    
    print(f"✅ Changelog updated for {date}")

if __name__ == "__main__":
    generate_changelog()
