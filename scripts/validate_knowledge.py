#!/usr/bin/env python3
"""
校验知识库数据完整性
"""

import json
import sys
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"

def validate_cuisine(cuisine_file):
    """校验菜系数据"""
    with open(cuisine_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    required_fields = ['id', 'name', 'flavor_profile', 'signature_dishes']
    missing = [f for f in required_fields if f not in data]
    
    if missing:
        print(f"❌ {cuisine_file.name}: missing fields {missing}")
        return False
    
    print(f"✅ {cuisine_file.name}: valid")
    return True

def validate_ingredient(ingredient_file):
    """校验食材数据"""
    with open(ingredient_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    required_fields = ['id', 'name', 'nutrition_per_100g', 'price_range']
    missing = [f for f in required_fields if f not in data]
    
    if missing:
        print(f"❌ {ingredient_file.name}: missing fields {missing}")
        return False
    
    print(f"✅ {ingredient_file.name}: valid")
    return True

def validate_technique(technique_file):
    """校验技法数据"""
    with open(technique_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    required_fields = ['id', 'name', 'heat_level', 'time_range']
    missing = [f for f in required_fields if f not in data]
    
    if missing:
        print(f"❌ {technique_file.name}: missing fields {missing}")
        return False
    
    print(f"✅ {technique_file.name}: valid")
    return True

def validate_all():
    """校验所有数据"""
    errors = 0
    total = 0
    
    # 校验菜系
    print("\n📚 Validating cuisines...")
    for cuisine_file in (KNOWLEDGE_DIR / "cuisines").rglob("*.json"):
        if cuisine_file.name == "index.json":
            continue
        total += 1
        if not validate_cuisine(cuisine_file):
            errors += 1
    
    # 校验食材
    print("\n🥩 Validating ingredients...")
    for ingredient_file in (KNOWLEDGE_DIR / "ingredients").rglob("*.json"):
        if ingredient_file.name == "index.json":
            continue
        total += 1
        if not validate_ingredient(ingredient_file):
            errors += 1
    
    # 校验技法
    print("\n🔪 Validating techniques...")
    for technique_file in (KNOWLEDGE_DIR / "techniques").rglob("*.json"):
        total += 1
        if not validate_technique(technique_file):
            errors += 1
    
    # 汇总
    print(f"\n{'='*50}")
    print(f"Total files: {total}")
    print(f"Valid: {total - errors}")
    print(f"Errors: {errors}")
    
    if errors:
        print(f"\n❌ Validation failed!")
        sys.exit(1)
    else:
        print(f"\n✅ All data validated successfully!")

if __name__ == "__main__":
    validate_all()
