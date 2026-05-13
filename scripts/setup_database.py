#!/usr/bin/env python3
"""
SQLite 数据库初始化脚本
创建菜谱数据库结构
"""

import sqlite3
import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "recipes.db"

def ensure_dir(path):
    """确保目录存在"""
    path.parent.mkdir(parents=True, exist_ok=True)

def create_database():
    """创建数据库和表结构"""
    ensure_dir(DB_PATH)
    
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # 创建菜谱表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            name_en TEXT,
            cuisine TEXT,
            category TEXT,
            difficulty TEXT,
            time_minutes INTEGER,
            servings INTEGER,
            calories_per_serving REAL,
            cost_per_serving REAL,
            tags TEXT,
            nutrition_calories REAL,
            nutrition_protein REAL,
            nutrition_fat REAL,
            nutrition_carbs REAL,
            source TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 创建食材表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipe_ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id TEXT,
            ingredient_name TEXT,
            amount TEXT,
            type TEXT,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
    ''')
    
    # 创建步骤表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipe_steps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id TEXT,
            step_number INTEGER,
            content TEXT,
            tip TEXT,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
    ''')
    
    # 创建调味料表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipe_seasonings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id TEXT,
            name TEXT,
            amount TEXT,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
    ''')
    
    # 创建关键点表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipe_key_points (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipe_id TEXT,
            point TEXT,
            FOREIGN KEY (recipe_id) REFERENCES recipes(id)
        )
    ''')
    
    # 创建索引
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_cuisine ON recipes(cuisine)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_difficulty ON recipes(difficulty)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_time ON recipes(time_minutes)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_calories ON recipes(nutrition_calories)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_cost ON recipes(cost_per_serving)')
    
    conn.commit()
    conn.close()
    
    print(f"✅ Database created at: {DB_PATH}")

def import_recipe_to_db(recipe):
    """将单个菜谱导入数据库"""
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # 插入菜谱基本信息
    cursor.execute('''
        INSERT OR REPLACE INTO recipes 
        (id, name, name_en, cuisine, category, difficulty, time_minutes, 
         servings, calories_per_serving, cost_per_serving, tags,
         nutrition_calories, nutrition_protein, nutrition_fat, nutrition_carbs, source)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        recipe['id'],
        recipe['name'],
        recipe.get('name_en', ''),
        recipe.get('cuisine', ''),
        recipe.get('category', ''),
        recipe.get('difficulty', 'medium'),
        recipe.get('time_minutes', 30),
        recipe.get('servings', 2),
        recipe.get('calories_per_serving', 0),
        recipe.get('cost_per_serving', 0),
        json.dumps(recipe.get('tags', []), ensure_ascii=False),
        recipe.get('nutrition', {}).get('calories', 0),
        recipe.get('nutrition', {}).get('protein', 0),
        recipe.get('nutrition', {}).get('fat', 0),
        recipe.get('nutrition', {}).get('carbs', 0),
        recipe.get('source', 'unknown')
    ))
    
    # 插入食材
    cursor.execute('DELETE FROM recipe_ingredients WHERE recipe_id = ?', (recipe['id'],))
    for ing in recipe.get('ingredients', []):
        cursor.execute('''
            INSERT INTO recipe_ingredients (recipe_id, ingredient_name, amount, type)
            VALUES (?, ?, ?, ?)
        ''', (recipe['id'], ing['name'], ing.get('amount', ''), ing.get('type', '')))
    
    # 插入步骤
    cursor.execute('DELETE FROM recipe_steps WHERE recipe_id = ?', (recipe['id'],))
    for step in recipe.get('steps', []):
        cursor.execute('''
            INSERT INTO recipe_steps (recipe_id, step_number, content, tip)
            VALUES (?, ?, ?, ?)
        ''', (recipe['id'], step['step'], step['content'], step.get('tip', '')))
    
    # 插入调味料
    cursor.execute('DELETE FROM recipe_seasonings WHERE recipe_id = ?', (recipe['id'],))
    for s in recipe.get('seasonings', []):
        cursor.execute('''
            INSERT INTO recipe_seasonings (recipe_id, name, amount)
            VALUES (?, ?, ?)
        ''', (recipe['id'], s['name'], s.get('amount', '')))
    
    # 插入关键点
    cursor.execute('DELETE FROM recipe_key_points WHERE recipe_id = ?', (recipe['id'],))
    for point in recipe.get('key_points', []):
        cursor.execute('''
            INSERT INTO recipe_key_points (recipe_id, point)
            VALUES (?, ?)
        ''', (recipe['id'], point))
    
    conn.commit()
    conn.close()

def import_all_recipes():
    """导入所有菜谱到数据库"""
    recipes_dir = Path(__file__).parent.parent / "recipes"
    
    if not recipes_dir.exists():
        print("❌ Recipes directory not found")
        return
    
    total = 0
    for json_file in recipes_dir.rglob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                recipe = json.load(f)
                if 'id' in recipe and 'name' in recipe:
                    import_recipe_to_db(recipe)
                    total += 1
                    print(f"  ✅ Imported: {recipe['name']}")
        except Exception as e:
            print(f"  ❌ Error importing {json_file}: {e}")
    
    print(f"\n✅ Total recipes imported: {total}")

def main():
    """主函数"""
    print("🗄️ Food Craft Database Setup")
    print("=" * 50)
    
    # 创建数据库
    create_database()
    
    # 导入菜谱
    print("\n📚 Importing recipes...")
    import_all_recipes()
    
    print("\n" + "=" * 50)
    print("✅ Database setup complete!")

if __name__ == "__main__":
    main()
