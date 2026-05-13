#!/usr/bin/env python3
"""批量生成食材JSON文件"""

import json
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge" / "ingredients"

ingredients = {
    "vegetables": [
        {"id": "white_radish", "name": "白萝卜", "name_en": "White Radish", "calories": 16, "protein": 0.7, "fat": 0.1, "carbs": 3.4, "price_avg": 3, "unit": "元/斤", "best_season": "冬季", "suitable": ["炖汤", "腌制", "凉拌"], "tips": ["炖汤要后放", "腌萝卜要加盐杀水"]},
        {"id": "green_radish", "name": "青萝卜", "name_en": "Green Radish", "calories": 20, "protein": 0.8, "fat": 0.1, "carbs": 4.5, "price_avg": 3, "unit": "元/斤", "best_season": "冬季", "suitable": ["炖汤", "凉拌"], "tips": ["青萝卜比白萝卜更脆"]},
        {"id": "taro", "name": "芋头", "name_en": "Taro", "calories": 79, "protein": 2.2, "fat": 0.2, "carbs": 17.1, "price_avg": 6, "unit": "元/斤", "best_season": "秋冬", "suitable": ["炖肉", "蒸", "煮粥"], "tips": ["芋头要煮到软糯", "处理时戴手套防痒"]},
        {"id": "yam", "name": "山药", "name_en": "Yam", "calories": 57, "protein": 1.9, "fat": 0.2, "carbs": 11.6, "price_avg": 8, "unit": "元/斤", "best_season": "秋冬", "suitable": ["炖汤", "炒", "煮粥"], "tips": ["山药去皮后泡醋水防氧化", "铁棍山药更粉糯"]},
        {"id": "water_chestnut", "name": "荸荠", "name_en": "Water Chestnut", "calories": 61, "protein": 1.2, "fat": 0.2, "carbs": 14.2, "price_avg": 8, "unit": "元/斤", "best_season": "冬春", "suitable": ["生吃", "炒", "煮汤"], "tips": ["荸荠要削皮后食用", "可以当水果生吃"]},
        {"id": "bamboo_shoot", "name": "竹笋", "name_en": "Bamboo Shoot", "calories": 27, "protein": 2.6, "fat": 0.2, "carbs": 5.1, "price_avg": 10, "unit": "元/斤", "best_season": "春季", "suitable": ["炒", "炖", "凉拌"], "tips": ["竹笋要焯水去涩味", "春笋最嫩"]},
        {"id": "winter_bamboo", "name": "冬笋", "name_en": "Winter Bamboo", "calories": 28, "protein": 3.1, "fat": 0.2, "carbs": 5.0, "price_avg": 15, "unit": "元/斤", "best_season": "冬季", "suitable": ["炒", "炖肉"], "tips": ["冬笋比春笋更鲜嫩"]},
        {"id": "water_spinach", "name": "空心菜", "name_en": "Water Spinach", "calories": 25, "protein": 2.6, "fat": 0.3, "carbs": 4.5, "price_avg": 4, "unit": "元/斤", "best_season": "夏季", "suitable": ["炒", "凉拌"], "tips": ["空心菜要大火快炒", "蒜蓉空心菜是经典"]},
        {"id": "choy_sum", "name": "菜心", "name_en": "Choy Sum", "calories": 20, "protein": 1.5, "fat": 0.3, "carbs": 3.5, "price_avg": 5, "unit": "元/斤", "best_season": "秋冬", "suitable": ["炒", "白灼", "蒜蓉"], "tips": ["菜心要选嫩的", "白灼菜心是经典粤菜"]},
        {"id": "chinese_broccoli", "name": "芥兰", "name_en": "Chinese Broccoli", "calories": 22, "protein": 2.0, "fat": 0.3, "carbs": 4.0, "price_avg": 6, "unit": "元/斤", "best_season": "秋冬", "suitable": ["炒", "白灼"], "tips": ["芥兰要去皮", "蚝油芥兰是经典"]},
        {"id": "snow_pea", "name": "荷兰豆", "name_en": "Snow Pea", "calories": 42, "protein": 2.8, "fat": 0.3, "carbs": 7.6, "price_avg": 8, "unit": "元/斤", "best_season": "春季", "suitable": ["炒", "凉拌"], "tips": ["荷兰豆要去筋", "大火快炒保持脆感"]},
        {"id": "snap_pea", "name": "甜豆", "name_en": "Snap Pea", "calories": 42, "protein": 2.8, "fat": 0.3, "carbs": 7.5, "price_avg": 10, "unit": "元/斤", "best_season": "春季", "suitable": ["炒", "凉拌"], "tips": ["甜豆比荷兰豆更甜脆"]},
        {"id": "asparagus", "name": "芦笋", "name_en": "Asparagus", "calories": 20, "protein": 2.2, "fat": 0.2, "carbs": 3.9, "price_avg": 15, "unit": "元/把", "best_season": "春季", "suitable": ["炒", "烤", "白灼"], "tips": ["芦笋要去掉老根", "白灼芦笋要焯水30秒"]},
        {"id": "broccolini", "name": "西兰苔", "name_en": "Broccolini", "calories": 35, "protein": 3.5, "fat": 0.4, "carbs": 5.5, "price_avg": 12, "unit": "元/把", "best_season": "全年", "suitable": ["炒", "烤"], "tips": ["西兰苔比西兰花更嫩"]},
        {"id": "zucchini", "name": "西葫芦", "name_en": "Zucchini", "calories": 17, "protein": 1.2, "fat": 0.3, "carbs": 3.1, "price_avg": 4, "unit": "元/个", "best_season": "夏季", "suitable": ["炒", "煎", "烤"], "tips": ["西葫芦要大火快炒", "可以做煎饼"]},
        {"id": "bitter_melon", "name": "苦瓜", "name_en": "Bitter Melon", "calories": 19, "protein": 1.0, "fat": 0.2, "carbs": 4.3, "price_avg": 5, "unit": "元/根", "best_season": "夏季", "suitable": ["炒", "凉拌", "酿"], "tips": ["苦瓜要去瓤，用盐腌去苦味"]},
        {"id": "winter_gourd", "name": "冬瓜", "name_en": "Winter Gourd", "calories": 12, "protein": 0.4, "fat": 0.2, "carbs": 2.6, "price_avg": 2, "unit": "元/斤", "best_season": "夏季", "suitable": ["炖汤", "红烧"], "tips": ["冬瓜炖汤要带皮，更清热"]},
        {"id": "loofah", "name": "丝瓜", "name_en": "Loofah", "calories": 20, "protein": 1.0, "fat": 0.2, "carbs": 4.4, "price_avg": 4, "unit": "元/根", "best_season": "夏季", "suitable": ["炒", "煮汤"], "tips": ["丝瓜要现切现炒，防止变黑"]},
        {"id": "okra", "name": "秋葵", "name_en": "Okra", "calories": 33, "protein": 2.0, "fat": 0.1, "carbs": 7.5, "price_avg": 10, "unit": "元/斤", "best_season": "夏季", "suitable": ["炒", "凉拌", "烤"], "tips": ["秋葵焯水时加点盐保持翠绿"]},
        {"id": "edamame", "name": "毛豆", "name_en": "Edamame", "calories": 131, "protein": 13.0, "fat": 5.0, "carbs": 10.0, "price_avg": 6, "unit": "元/斤", "best_season": "夏季", "suitable": ["煮", "炒", "凉拌"], "tips": ["盐水毛豆要剪口更入味"]},
        {"id": "pea", "name": "豌豆", "name_en": "Pea", "calories": 81, "protein": 5.4, "fat": 0.4, "carbs": 14.5, "price_avg": 8, "unit": "元/斤", "best_season": "春季", "suitable": ["炒", "煮汤"], "tips": ["豌豆要焯水后再炒"]},
        {"id": "lotus_seed", "name": "莲子", "name_en": "Lotus Seed", "calories": 89, "protein": 4.9, "fat": 0.6, "carbs": 17.3, "price_avg": 25, "unit": "元/斤", "best_season": "秋季", "suitable": ["煮粥", "炖汤", "甜品"], "tips": ["莲子要去芯，否则会苦"]},
        {"id": "lily_bulb", "name": "百合", "name_en": "Lily Bulb", "calories": 162, "protein": 3.2, "fat": 0.1, "carbs": 38.8, "price_avg": 20, "unit": "元/斤", "best_season": "秋季", "suitable": ["炒", "煮汤", "甜品"], "tips": ["鲜百合要最后放，保持脆感"]},
        {"id": "tremella", "name": "银耳", "name_en": "Tremella", "calories": 200, "protein": 10.0, "fat": 1.4, "carbs": 63.3, "price_avg": 30, "unit": "元/朵", "best_season": "全年", "suitable": ["煮汤", "甜品"], "tips": ["银耳要冷水泡发，炖到出胶"]},
        {"id": "seaweed", "name": "海带", "name_en": "Seaweed", "calories": 12, "protein": 1.2, "fat": 0.1, "carbs": 2.0, "price_avg": 5, "unit": "元/斤", "best_season": "全年", "suitable": ["炖汤", "凉拌", "炒"], "tips": ["干海带要泡发后使用"]},
        {"id": "kelp", "name": "昆布", "name_en": "Kelp", "calories": 12, "protein": 1.7, "fat": 0.1, "carbs": 2.0, "price_avg": 15, "unit": "元/袋", "best_season": "全年", "suitable": ["煮汤", "日料"], "tips": ["昆布是日式高汤的基底"]},
        {"id": "enoki", "name": "金针菇", "name_en": "Enoki Mushroom", "calories": 37, "protein": 2.7, "fat": 0.4, "carbs": 7.8, "price_avg": 5, "unit": "元/袋", "best_season": "全年", "suitable": ["火锅", "炒", "凉拌"], "tips": ["金针菇要煮熟，生吃有毒"]},
        {"id": "king_oyster", "name": "杏鲍菇", "name_en": "King Oyster Mushroom", "calories": 34, "protein": 1.3, "fat": 0.4, "carbs": 8.3, "price_avg": 8, "unit": "元/个", "best_season": "全年", "suitable": ["炒", "烤", "煎"], "tips": ["杏鲍菇手撕比刀切更好吃"]},
        {"id": "oyster_mushroom", "name": "平菇", "name_en": "Oyster Mushroom", "calories": 33, "protein": 3.3, "fat": 0.4, "carbs": 6.1, "price_avg": 5, "unit": "元/斤", "best_season": "全年", "suitable": ["炒", "煮汤", "炸"], "tips": ["平菇要焯水去腥味"]},
        {"id": "needle_mushroom", "name": "茶树菇", "name_en": "Needle Mushroom", "calories": 280, "protein": 23.0, "fat": 3.0, "carbs": 40.0, "price_avg": 25, "unit": "元/袋", "best_season": "全年", "suitable": ["炖肉", "炒"], "tips": ["干茶树菇要泡发后使用"]},
    ],
    "meat": [
        {"id": "pork_shoulder", "name": "梅花肉", "name_en": "Pork Shoulder", "calories": 190, "protein": 17.0, "fat": 13.0, "carbs": 0, "price_avg": 20, "unit": "元/500g", "best_season": "全年", "suitable": ["炒", "煎", "烤"], "tips": ["梅花肉肥瘦相间，口感嫩"]},
        {"id": "pork_hock", "name": "猪蹄", "name_en": "Pork Hock", "calories": 260, "protein": 22.0, "fat": 19.0, "carbs": 0, "price_avg": 18, "unit": "元/个", "best_season": "全年", "suitable": ["红烧", "炖汤", "卤"], "tips": ["猪蹄要炖到软烂才好吃"]},
        {"id": "pork_liver", "name": "猪肝", "name_en": "Pork Liver", "calories": 129, "protein": 19.3, "fat": 3.5, "carbs": 5.0, "price_avg": 12, "unit": "元/500g", "best_season": "全年", "suitable": ["炒", "煮汤"], "tips": ["猪肝要泡水去血水，大火快炒"]},
        {"id": "pork_intestine", "name": "猪大肠", "name_en": "Pork Intestine", "calories": 196, "protein": 6.9, "fat": 18.7, "carbs": 0, "price_avg": 15, "unit": "元/500g", "best_season": "全年", "suitable": ["红烧", "卤", "炒"], "tips": ["猪大肠要清洗干净，用醋和盐搓洗"]},
        {"id": "beef_short_rib", "name": "牛小排", "name_en": "Beef Short Rib", "calories": 290, "protein": 17.0, "fat": 24.0, "carbs": 0, "price_avg": 80, "unit": "元/500g", "best_season": "全年", "suitable": ["煎", "烤"], "tips": ["牛小排要煎到5分熟最好吃"]},
        {"id": "beef_tongue", "name": "牛舌", "name_en": "Beef Tongue", "calories": 225, "protein": 14.9, "fat": 18.0, "carbs": 0, "price_avg": 50, "unit": "元/500g", "best_season": "全年", "suitable": ["烤", "卤", "煎"], "tips": ["牛舌要煮熟后切片"]},
        {"id": "beef_tripe", "name": "牛肚", "name_en": "Beef Tripe", "calories": 85, "protein": 14.0, "fat": 3.0, "carbs": 0, "price_avg": 30, "unit": "元/500g", "best_season": "全年", "suitable": ["火锅", "卤", "炒"], "tips": ["牛肚要煮到软烂"]},
        {"id": "lamb_shoulder", "name": "羊肩肉", "name_en": "Lamb Shoulder", "calories": 210, "protein": 16.0, "fat": 16.0, "carbs": 0, "price_avg": 55, "unit": "元/500g", "best_season": "秋冬", "suitable": ["炖", "烤"], "tips": ["羊肩肉适合慢炖"]},
        {"id": "lamb_chop", "name": "羊排", "name_en": "Lamb Chop", "calories": 250, "protein": 17.0, "fat": 20.0, "carbs": 0, "price_avg": 70, "unit": "元/500g", "best_season": "秋冬", "suitable": ["煎", "烤"], "tips": ["羊排要腌制后再烤"]},
        {"id": "chicken_wing", "name": "鸡翅", "name_en": "Chicken Wing", "calories": 222, "protein": 17.4, "fat": 16.7, "carbs": 0, "price_avg": 20, "unit": "元/500g", "best_season": "全年", "suitable": ["烤", "炸", "红烧", "可乐"], "tips": ["鸡翅要划刀更入味"]},
        {"id": "chicken_feet", "name": "鸡爪", "name_en": "Chicken Feet", "calories": 215, "protein": 19.4, "fat": 14.6, "carbs": 0, "price_avg": 15, "unit": "元/500g", "best_season": "全年", "suitable": ["卤", "泡椒", "炖汤"], "tips": ["鸡爪要剪指甲，卤到软烂"]},
        {"id": "chicken_gizzard", "name": "鸡胗", "name_en": "Chicken Gizzard", "calories": 118, "protein": 19.2, "fat": 2.8, "carbs": 4.0, "price_avg": 15, "unit": "元/500g", "best_season": "全年", "suitable": ["炒", "卤"], "tips": ["鸡胗要切花刀，大火快炒"]},
        {"id": "duck_blood", "name": "鸭血", "name_en": "Duck Blood", "calories": 55, "protein": 10.0, "fat": 0.3, "carbs": 1.0, "price_avg": 8, "unit": "元/盒", "best_season": "全年", "suitable": ["火锅", "毛血旺"], "tips": ["鸭血要煮熟，不能生吃"]},
        {"id": "goose", "name": "鹅肉", "name_en": "Goose", "calories": 161, "protein": 17.9, "fat": 9.8, "carbs": 0, "price_avg": 30, "unit": "元/500g", "best_season": "秋冬", "suitable": ["烧鹅", "炖汤"], "tips": ["鹅肉比鸭肉更嫩"]},
    ],
    "seafood": [
        {"id": "tilapia", "name": "罗非鱼", "name_en": "Tilapia", "calories": 96, "protein": 18.7, "fat": 1.5, "carbs": 0, "price_avg": 12, "unit": "元/条", "best_season": "全年", "suitable": ["红烧", "煎", "烤"], "tips": ["罗非鱼要去腥线"]},
        {"id": "carp", "name": "鲤鱼", "name_en": "Carp", "calories": 109, "protein": 17.6, "fat": 4.1, "carbs": 0, "price_avg": 10, "unit": "元/条", "best_season": "春季", "suitable": ["红烧", "糖醋", "炖汤"], "tips": ["鲤鱼要去腥线，两侧各一条"]},
        {"id": "catfish", "name": "鲶鱼", "name_en": "Catfish", "calories": 103, "protein": 16.0, "fat": 3.7, "carbs": 0, "price_avg": 15, "unit": "元/条", "best_season": "全年", "suitable": ["炖汤", "红烧"], "tips": ["鲶鱼炖豆腐是经典"]},
        {"id": "grass_carp", "name": "草鱼", "name_en": "Grass Carp", "calories": 113, "protein": 16.6, "fat": 5.2, "carbs": 0, "price_avg": 10, "unit": "元/斤", "best_season": "全年", "suitable": ["红烧", "水煮鱼", "酸菜鱼"], "tips": ["草鱼片要顺着纹理切"]},
        {"id": "mandarin_fish", "name": "鳜鱼", "name_en": "Mandarin Fish", "calories": 117, "protein": 19.9, "fat": 4.3, "carbs": 0, "price_avg": 45, "unit": "元/条", "best_season": "春季", "suitable": ["清蒸", "红烧"], "tips": ["鳜鱼肉质细嫩，适合清蒸"]},
        {"id": "yellow_croaker", "name": "黄花鱼", "name_en": "Yellow Croaker", "calories": 97, "protein": 17.7, "fat": 2.5, "carbs": 0, "price_avg": 25, "unit": "元/条", "best_season": "春季", "suitable": ["红烧", "煎", "炸"], "tips": ["黄花鱼要煎到两面金黄"]},
        {"id": "pomfret", "name": "鲳鱼", "name_en": "Pomfret", "calories": 140, "protein": 18.5, "fat": 7.3, "carbs": 0, "price_avg": 35, "unit": "元/条", "best_season": "秋季", "suitable": ["清蒸", "红烧"], "tips": ["鲳鱼要选新鲜的，眼睛明亮"]},
        {"id": "hairtail", "name": "带鱼", "name_en": "Hairtail", "calories": 127, "protein": 17.7, "fat": 4.9, "carbs": 3.1, "price_avg": 15, "unit": "元/斤", "best_season": "冬季", "suitable": ["红烧", "煎", "炸"], "tips": ["带鱼要去掉表面银色物质"]},
        {"id": "shrimp", "name": "基围虾", "name_en": "Shrimp", "calories": 101, "protein": 18.6, "fat": 1.3, "carbs": 3.9, "price_avg": 35, "unit": "元/斤", "best_season": "夏季", "suitable": ["白灼", "油焖", "椒盐"], "tips": ["虾要挑虾线，白灼要煮3分钟"]},
        {"id": "lobster", "name": "龙虾", "name_en": "Lobster", "calories": 90, "protein": 18.8, "fat": 0.9, "carbs": 0, "price_avg": 120, "unit": "元/只", "best_season": "夏季", "suitable": ["蒸", "烤", "芝士焗"], "tips": ["龙虾要蒸15分钟"]},
        {"id": "scallop", "name": "扇贝", "name_en": "Scallop", "calories": 69, "protein": 13.5, "fat": 0.6, "carbs": 2.5, "price_avg": 8, "unit": "元/个", "best_season": "冬季", "suitable": ["蒜蓉蒸", "烤"], "tips": ["蒜蓉粉丝蒸扇贝是经典"]},
        {"id": "clam", "name": "蛤蜊", "name_en": "Clam", "calories": 56, "protein": 10.1, "fat": 0.9, "carbs": 2.8, "price_avg": 10, "unit": "元/斤", "best_season": "夏季", "suitable": ["辣炒", "煮汤"], "tips": ["蛤蜊要吐沙后食用"]},
        {"id": "mussel", "name": "青口", "name_en": "Mussel", "calories": 86, "protein": 11.9, "fat": 2.9, "carbs": 3.7, "price_avg": 15, "unit": "元/斤", "best_season": "冬季", "suitable": ["蒜蓉蒸", "白酒煮"], "tips": ["青口要去除须丝"]},
        {"id": "octopus", "name": "章鱼", "name_en": "Octopus", "calories": 82, "protein": 14.9, "fat": 1.0, "carbs": 1.4, "price_avg": 25, "unit": "元/斤", "best_season": "全年", "suitable": ["烤", "炒", "刺身"], "tips": ["章鱼要煮到软烂"]},
        {"id": "sea_cucumber", "name": "海参", "name_en": "Sea Cucumber", "calories": 55, "protein": 16.5, "fat": 0.2, "carbs": 0, "price_avg": 200, "unit": "元/只", "best_season": "冬季", "suitable": ["葱烧", "炖汤"], "tips": ["干海参要泡发3-5天"]},
    ],
    "egg_bean": [
        {"id": "quail_egg", "name": "鹌鹑蛋", "name_en": "Quail Egg", "calories": 160, "protein": 12.8, "fat": 11.1, "carbs": 0.4, "price_avg": 15, "unit": "元/斤", "best_season": "全年", "suitable": ["卤", "红烧", "煮汤"], "tips": ["鹌鹑蛋要冷水下锅煮"]},
        {"id": "duck_egg", "name": "鸭蛋", "name_en": "Duck Egg", "calories": 180, "protein": 12.6, "fat": 13.0, "carbs": 3.1, "price_avg": 2, "unit": "元/个", "best_season": "全年", "suitable": ["腌制", "蒸"], "tips": ["咸鸭蛋要腌制20天"]},
        {"id": "salted_egg", "name": "咸蛋", "name_en": "Salted Egg", "calories": 190, "protein": 13.0, "fat": 14.0, "carbs": 2.0, "price_avg": 3, "unit": "元/个", "best_season": "全年", "suitable": ["蒸", "粽子", "月饼"], "tips": ["咸蛋黄要蒸熟后碾碎"]},
        {"id": "century_egg", "name": "皮蛋", "name_en": "Century Egg", "calories": 171, "protein": 13.1, "fat": 10.7, "carbs": 4.5, "price_avg": 2, "unit": "元/个", "best_season": "全年", "suitable": ["凉拌", "皮蛋瘦肉粥"], "tips": ["皮蛋要切块后蘸醋吃"]},
        {"id": "fermented_tofu", "name": "腐乳", "name_en": "Fermented Tofu", "calories": 133, "protein": 10.9, "fat": 8.2, "carbs": 4.8, "price_avg": 8, "unit": "元/瓶", "best_season": "全年", "suitable": ["调味", "下饭"], "tips": ["腐乳可以做蘸料和调味"]},
        {"id": "tempeh", "name": "豆豉", "name_en": "Tempeh", "calories": 200, "protein": 24.0, "fat": 8.0, "carbs": 18.0, "price_avg": 10, "unit": "元/袋", "best_season": "全年", "suitable": ["炒菜", "蒸排骨"], "tips": ["豆豉要剁碎使用"]},
        {"id": "soy_milk", "name": "豆浆", "name_en": "Soy Milk", "calories": 31, "protein": 2.9, "fat": 1.6, "carbs": 1.2, "price_avg": 3, "unit": "元/杯", "best_season": "全年", "suitable": ["直接饮用"], "tips": ["豆浆要煮熟，不能生喝"]},
        {"id": "bean_sprout", "name": "豆芽", "name_en": "Bean Sprout", "calories": 31, "protein": 3.0, "fat": 0.1, "carbs": 5.9, "price_avg": 3, "unit": "元/斤", "best_season": "全年", "suitable": ["炒", "凉拌"], "tips": ["豆芽要大火快炒，保持脆感"]},
    ],
    "staple": [
        {"id": "vermicelli", "name": "粉丝", "name_en": "Vermicelli", "calories": 335, "protein": 0.5, "fat": 0.1, "carbs": 83.0, "price_avg": 8, "unit": "元/袋", "best_season": "全年", "suitable": ["炒", "煮汤", "火锅"], "tips": ["粉丝要泡软后使用"]},
        {"id": "glass_noodle", "name": "粉条", "name_en": "Glass Noodle", "calories": 338, "protein": 0.3, "fat": 0.1, "carbs": 84.0, "price_avg": 8, "unit": "元/袋", "best_season": "全年", "suitable": ["炖菜", "酸辣粉"], "tips": ["粉条要泡软，炖菜时后放"]},
        {"id": "rice_noodle", "name": "米粉", "name_en": "Rice Noodle", "calories": 109, "protein": 2.6, "fat": 0.3, "carbs": 25.0, "price_avg": 6, "unit": "元/袋", "best_season": "全年", "suitable": ["炒", "煮汤"], "tips": ["米粉要泡软后炒，大火快炒"]},
        {"id": "flat_noodle", "name": "河粉", "name_en": "Flat Noodle", "calories": 110, "protein": 2.5, "fat": 0.4, "carbs": 24.0, "price_avg": 5, "unit": "元/斤", "best_season": "全年", "suitable": ["炒", "煮汤"], "tips": ["干炒牛河要大火快炒"]},
        {"id": "udon", "name": "乌冬面", "name_en": "Udon", "calories": 105, "protein": 2.5, "fat": 0.2, "carbs": 23.0, "price_avg": 8, "unit": "元/袋", "best_season": "全年", "suitable": ["煮汤", "炒"], "tips": ["乌冬面要煮到Q弹"]},
        {"id": "spaghetti", "name": "意面", "name_en": "Spaghetti", "calories": 131, "protein": 5.0, "fat": 0.6, "carbs": 27.0, "price_avg": 10, "unit": "元/袋", "best_season": "全年", "suitable": ["煮", "炒"], "tips": ["意面要煮到al dente（有嚼劲）"]},
        {"id": "mantou", "name": "馒头", "name_en": "Mantou", "calories": 221, "protein": 7.0, "fat": 1.1, "carbs": 47.0, "price_avg": 2, "unit": "元/个", "best_season": "全年", "suitable": ["蒸", "炸", "煎"], "tips": ["馒头要二次醒发才松软"]},
        {"id": "dumpling_wrapper", "name": "饺子皮", "name_en": "Dumpling Wrapper", "calories": 280, "protein": 8.0, "fat": 1.5, "carbs": 58.0, "price_avg": 5, "unit": "元/斤", "best_season": "全年", "suitable": ["包饺子", "包馄饨"], "tips": ["饺子皮要薄，馅要包紧"]},
        {"id": "wonton_wrapper", "name": "馄饨皮", "name_en": "Wonton Wrapper", "calories": 270, "protein": 7.5, "fat": 1.2, "carbs": 56.0, "price_avg": 5, "unit": "元/斤", "best_season": "全年", "suitable": ["包馄饨"], "tips": ["馄饨皮比饺子皮更薄"]},
        {"id": "spring_roll_wrapper", "name": "春卷皮", "name_en": "Spring Roll Wrapper", "calories": 290, "protein": 7.0, "fat": 2.0, "carbs": 60.0, "price_avg": 8, "unit": "元/袋", "best_season": "春季", "suitable": ["炸春卷"], "tips": ["春卷要包紧，炸到金黄"]},
        {"id": "glutinous_rice", "name": "糯米", "name_en": "Glutinous Rice", "calories": 345, "protein": 7.3, "fat": 1.0, "carbs": 78.0, "price_avg": 6, "unit": "元/斤", "best_season": "全年", "suitable": ["粽子", "糯米饭", "汤圆"], "tips": ["糯米要提前浸泡4小时"]},
        {"id": "brown_rice", "name": "糙米", "name_en": "Brown Rice", "calories": 348, "protein": 7.4, "fat": 2.7, "carbs": 72.9, "price_avg": 8, "unit": "元/斤", "best_season": "全年", "suitable": ["煮饭", "煮粥"], "tips": ["糙米要浸泡2小时，口感更好"]},
        {"id": "oat", "name": "燕麦", "name_en": "Oat", "calories": 367, "protein": 15.0, "fat": 6.7, "carbs": 61.6, "price_avg": 10, "unit": "元/袋", "best_season": "全年", "suitable": ["煮粥", "早餐"], "tips": ["燕麦要选纯燕麦，不要速溶的"]},
    ],
    "fruit": [
        {"id": "apple", "name": "苹果", "name_en": "Apple", "calories": 52, "protein": 0.3, "fat": 0.2, "carbs": 13.8, "price_avg": 6, "unit": "元/斤", "best_season": "秋季", "suitable": ["生吃", "沙拉", "甜点"], "tips": ["苹果要选红富士，又甜又脆"]},
        {"id": "pear", "name": "梨", "name_en": "Pear", "calories": 57, "protein": 0.4, "fat": 0.1, "carbs": 15.2, "price_avg": 5, "unit": "元/斤", "best_season": "秋季", "suitable": ["生吃", "炖汤", "甜品"], "tips": ["雪梨炖冰糖可以润肺"]},
        {"id": "orange", "name": "橙子", "name_en": "Orange", "calories": 47, "protein": 0.9, "fat": 0.1, "carbs": 11.8, "price_avg": 5, "unit": "元/斤", "best_season": "冬季", "suitable": ["生吃", "榨汁"], "tips": ["橙子要选重的，水分足"]},
        {"id": "lemon", "name": "柠檬", "name_en": "Lemon", "calories": 29, "protein": 1.1, "fat": 0.3, "carbs": 9.3, "price_avg": 3, "unit": "元/个", "best_season": "全年", "suitable": ["泡水", "调味", "甜点"], "tips": ["柠檬泡水要用温水"]},
        {"id": "mango", "name": "芒果", "name_en": "Mango", "calories": 60, "protein": 0.8, "fat": 0.4, "carbs": 15.0, "price_avg": 10, "unit": "元/个", "best_season": "夏季", "suitable": ["生吃", "甜品", "沙冰"], "tips": ["芒果要选软的，香气浓的"]},
        {"id": "strawberry", "name": "草莓", "name_en": "Strawberry", "calories": 32, "protein": 0.7, "fat": 0.3, "carbs": 7.1, "price_avg": 20, "unit": "元/斤", "best_season": "春季", "suitable": ["生吃", "甜品", "沙拉"], "tips": ["草莓要选红透的，不要洗太久"]},
        {"id": "grape", "name": "葡萄", "name_en": "Grape", "calories": 69, "protein": 0.7, "fat": 0.2, "carbs": 18.1, "price_avg": 10, "unit": "元/斤", "best_season": "秋季", "suitable": ["生吃", "酿葡萄酒"], "tips": ["葡萄要选紫黑色的，更甜"]},
        {"id": "watermelon", "name": "西瓜", "name_en": "Watermelon", "calories": 30, "protein": 0.6, "fat": 0.2, "carbs": 7.6, "price_avg": 3, "unit": "元/斤", "best_season": "夏季", "suitable": ["生吃", "榨汁", "沙冰"], "tips": ["西瓜要选声音清脆的"]},
        {"id": "kiwi", "name": "猕猴桃", "name_en": "Kiwi", "calories": 61, "protein": 1.1, "fat": 0.5, "carbs": 14.7, "price_avg": 5, "unit": "元/个", "best_season": "秋季", "suitable": ["生吃", "沙拉"], "tips": ["猕猴桃要选软的，硬的要催熟"]},
        {"id": "pineapple", "name": "菠萝", "name_en": "Pineapple", "calories": 50, "protein": 0.5, "fat": 0.1, "carbs": 13.1, "price_avg": 8, "unit": "元/个", "best_season": "夏季", "suitable": ["生吃", "炒饭", "甜品"], "tips": ["菠萝要用盐水泡30分钟"]},
    ],
    "dried": [
        {"id": "dried_shrimp", "name": "虾米", "name_en": "Dried Shrimp", "calories": 250, "protein": 50.0, "fat": 2.0, "carbs": 5.0, "price_avg": 40, "unit": "元/斤", "best_season": "全年", "suitable": ["炒菜", "煮汤", "馅料"], "tips": ["虾米要泡软后使用，泡的水可以当高汤"]},
        {"id": "dried_scallop", "name": "干贝", "name_en": "Dried Scallop", "calories": 290, "protein": 56.0, "fat": 2.0, "carbs": 10.0, "price_avg": 100, "unit": "元/斤", "best_season": "全年", "suitable": ["煮粥", "炖汤", "蒸蛋"], "tips": ["干贝要泡发后撕碎使用"]},
        {"id": "dried_mushroom", "name": "干香菇", "name_en": "Dried Mushroom", "calories": 290, "protein": 20.0, "fat": 3.0, "carbs": 50.0, "price_avg": 40, "unit": "元/斤", "best_season": "全年", "suitable": ["炖肉", "煮汤", "炒菜"], "tips": ["干香菇比鲜香菇更香，泡的水是高汤"]},
        {"id": "dried_lily", "name": "百合干", "name_en": "Dried Lily", "calories": 340, "protein": 8.0, "fat": 0.5, "carbs": 78.0, "price_avg": 30, "unit": "元/斤", "best_season": "全年", "suitable": ["煮粥", "甜品"], "tips": ["百合干要泡发后使用"]},
        {"id": "dried_red_date", "name": "红枣", "name_en": "Red Date", "calories": 264, "protein": 3.2, "fat": 0.5, "carbs": 67.0, "price_avg": 15, "unit": "元/斤", "best_season": "秋季", "suitable": ["煮粥", "炖汤", "泡水"], "tips": ["红枣要去核，否则会上火"]},
        {"id": "goji_berry", "name": "枸杞", "name_en": "Goji Berry", "calories": 349, "protein": 14.0, "fat": 1.5, "carbs": 64.0, "price_avg": 30, "unit": "元/斤", "best_season": "夏季", "suitable": ["泡水", "煮粥", "炖汤"], "tips": ["枸杞要最后放，不要煮太久"]},
        {"id": "dried_longan", "name": "桂圆干", "name_en": "Dried Longan", "calories": 280, "protein": 5.0, "fat": 0.5, "carbs": 65.0, "price_avg": 20, "unit": "元/斤", "best_season": "全年", "suitable": ["煮粥", "泡水", "炖汤"], "tips": ["桂圆干可以补气血"]},
        {"id": "walnut", "name": "核桃", "name_en": "Walnut", "calories": 654, "protein": 15.2, "fat": 65.2, "carbs": 13.7, "price_avg": 25, "unit": "元/斤", "best_season": "秋季", "suitable": ["生吃", "炒菜", "甜品"], "tips": ["核桃要选纸皮核桃，更容易剥"]},
        {"id": "peanut", "name": "花生", "name_en": "Peanut", "calories": 567, "protein": 25.8, "fat": 49.2, "carbs": 16.1, "price_avg": 8, "unit": "元/斤", "best_season": "秋季", "suitable": ["炒", "炸", "凉拌", "煮汤"], "tips": ["花生要炸到微黄捞出"]},
        {"id": "sesame", "name": "芝麻", "name_en": "Sesame", "calories": 573, "protein": 17.3, "fat": 49.0, "carbs": 23.0, "price_avg": 15, "unit": "元/斤", "best_season": "秋季", "suitable": ["调味", "甜品", "凉拌"], "tips": ["芝麻要炒香后使用"]},
        {"id": "cashew", "name": "腰果", "name_en": "Cashew", "calories": 553, "protein": 18.2, "fat": 43.9, "carbs": 30.2, "price_avg": 40, "unit": "元/斤", "best_season": "全年", "suitable": ["炒菜", "零食"], "tips": ["腰果要最后放，保持酥脆"]},
    ],
    "seasoning": [
        {"id": "sugar", "name": "白糖", "name_en": "Sugar", "calories": 400, "protein": 0, "fat": 0, "carbs": 100, "price_avg": 5, "unit": "元/斤", "best_season": "全年", "suitable": ["炒菜", "甜品", "腌制"], "tips": ["炒糖色要用冰糖，更容易操作"]},
        {"id": "salt", "name": "盐", "name_en": "Salt", "calories": 0, "protein": 0, "fat": 0, "carbs": 0, "price_avg": 2, "unit": "元/袋", "best_season": "全年", "suitable": ["所有菜肴"], "tips": ["盐要最后放，保持咸味"]},
        {"id": "msg", "name": "味精", "name_en": "MSG", "calories": 0, "protein": 0, "fat": 0, "carbs": 0, "price_avg": 5, "unit": "元/袋", "best_season": "全年", "suitable": ["炒菜", "汤"], "tips": ["味精要最后放，不要高温加热"]},
        {"id": "chicken_powder", "name": "鸡精", "name_en": "Chicken Powder", "calories": 100, "protein": 5.0, "fat": 1.0, "carbs": 15.0, "price_avg": 8, "unit": "元/袋", "best_season": "全年", "suitable": ["炒菜", "汤"], "tips": ["鸡精比味精更鲜"]},
        {"id": "dark_soy", "name": "老抽", "name_en": "Dark Soy Sauce", "calories": 53, "protein": 8.6, "fat": 0.1, "carbs": 4.9, "price_avg": 12, "unit": "元/瓶", "best_season": "全年", "suitable": ["红烧", "卤"], "tips": ["老抽用来上色，不要放太多"]},
        {"id": "fish_sauce", "name": "鱼露", "name_en": "Fish Sauce", "calories": 35, "protein": 5.0, "fat": 0, "carbs": 3.0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["东南亚菜", "凉拌"], "tips": ["鱼露很咸，要少放"]},
        {"id": "coconut_milk", "name": "椰浆", "name_en": "Coconut Milk", "calories": 197, "protein": 2.0, "fat": 20.0, "carbs": 3.0, "price_avg": 10, "unit": "元/盒", "best_season": "全年", "suitable": ["咖喱", "甜品"], "tips": ["椰浆要最后加，不要煮太久"]},
        {"id": "curry_powder", "name": "咖喱粉", "name_en": "Curry Powder", "calories": 325, "protein": 12.0, "fat": 14.0, "carbs": 58.0, "price_avg": 10, "unit": "元/盒", "best_season": "全年", "suitable": ["咖喱", "炒饭"], "tips": ["咖喱粉要炒香后使用"]},
        {"id": "five_spice", "name": "五香粉", "name_en": "Five Spice", "calories": 300, "protein": 10.0, "fat": 8.0, "carbs": 50.0, "price_avg": 8, "unit": "元/袋", "best_season": "全年", "suitable": ["卤肉", "腌制"], "tips": ["五香粉要少放，味道很浓"]},
        {"id": "cumin", "name": "孜然", "name_en": "Cumin", "calories": 375, "protein": 17.8, "fat": 22.3, "carbs": 44.2, "price_avg": 15, "unit": "元/袋", "best_season": "全年", "suitable": ["烧烤", "新疆菜"], "tips": ["孜然要炒香后使用"]},
        {"id": "star_anise", "name": "八角", "name_en": "Star Anise", "calories": 300, "protein": 5.0, "fat": 5.0, "carbs": 50.0, "price_avg": 15, "unit": "元/袋", "best_season": "全年", "suitable": ["卤肉", "炖肉"], "tips": ["八角要少放，1-2个就够"]},
        {"id": "cinnamon", "name": "桂皮", "name_en": "Cinnamon", "calories": 250, "protein": 4.0, "fat": 1.0, "carbs": 80.0, "price_avg": 10, "unit": "元/袋", "best_season": "全年", "suitable": ["卤肉", "炖肉", "甜品"], "tips": ["桂皮要少放，味道很浓"]},
        {"id": "bay_leaf", "name": "香叶", "name_en": "Bay Leaf", "calories": 250, "protein": 7.0, "fat": 8.0, "carbs": 75.0, "price_avg": 8, "unit": "元/袋", "best_season": "全年", "suitable": ["卤肉", "炖肉"], "tips": ["香叶要少放，2-3片就够"]},
        {"id": "sichuan_pepper_oil", "name": "花椒油", "name_en": "Sichuan Pepper Oil", "calories": 884, "protein": 0, "fat": 100, "carbs": 0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["凉拌", "麻辣菜"], "tips": ["花椒油要最后放，提麻味"]},
        {"id": "chili_oil", "name": "辣椒油", "name_en": "Chili Oil", "calories": 884, "protein": 0, "fat": 100, "carbs": 0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["凉拌", "拌面"], "tips": ["辣椒油要自制的更香"]},
        {"id": "peanut_butter", "name": "花生酱", "name_en": "Peanut Butter", "calories": 590, "protein": 25.0, "fat": 50.0, "carbs": 20.0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["拌面", "蘸料"], "tips": ["花生酱要用水调稀后使用"]},
        {"id": "sesame_paste", "name": "芝麻酱", "name_en": "Sesame Paste", "calories": 590, "protein": 17.0, "fat": 52.0, "carbs": 22.0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["凉拌", "火锅蘸料"], "tips": ["芝麻酱要用温水调开"]},
        {"id": "ketchup", "name": "番茄酱", "name_en": "Ketchup", "calories": 100, "protein": 1.0, "fat": 0.1, "carbs": 25.0, "price_avg": 10, "unit": "元/瓶", "best_season": "全年", "suitable": ["糖醋菜", "蘸料"], "tips": ["番茄酱要选纯番茄的"]},
        {"id": "mustard", "name": "芥末", "name_en": "Mustard", "calories": 60, "protein": 4.0, "fat": 4.0, "carbs": 5.0, "price_avg": 10, "unit": "元/管", "best_season": "全年", "suitable": ["日料", "蘸料"], "tips": ["芥末很呛，要少放"]},
        {"id": "wasabi", "name": "芥末酱", "name_en": "Wasabi", "calories": 109, "protein": 4.8, "fat": 0.6, "carbs": 24.0, "price_avg": 20, "unit": "元/管", "best_season": "全年", "suitable": ["日料", "刺身"], "tips": ["芥末酱要现磨的才新鲜"]},
        {"id": "mayonnaise", "name": "蛋黄酱", "name_en": "Mayonnaise", "calories": 680, "protein": 1.0, "fat": 75.0, "carbs": 1.0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["沙拉", "三明治"], "tips": ["蛋黄酱要冷藏保存"]},
        {"id": "salad_dressing", "name": "沙拉酱", "name_en": "Salad Dressing", "calories": 400, "protein": 1.0, "fat": 40.0, "carbs": 10.0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["沙拉"], "tips": ["沙拉酱要选低脂的更健康"]},
        {"id": "hoisin_sauce", "name": "海鲜酱", "name_en": "Hoisin Sauce", "calories": 220, "protein": 3.0, "fat": 3.0, "carbs": 45.0, "price_avg": 12, "unit": "元/瓶", "best_season": "全年", "suitable": ["烤肉", "炒菜"], "tips": ["海鲜酱可以做蘸料和调味"]},
        {"id": "teriyaki", "name": "照烧酱", "name_en": "Teriyaki Sauce", "calories": 150, "protein": 5.0, "fat": 0, "carbs": 30.0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["照烧鸡", "烤肉"], "tips": ["照烧酱要最后刷上"]},
        {"id": "sriracha", "name": "是拉差辣椒酱", "name_en": "Sriracha", "calories": 100, "protein": 2.0, "fat": 1.0, "carbs": 20.0, "price_avg": 15, "unit": "元/瓶", "best_season": "全年", "suitable": ["蘸料", "炒菜"], "tips": ["是拉差辣椒酱甜辣适中"]},
    ],
}

def create_ingredient_file(category, item):
    """创建单个食材文件"""
    category_dir = KNOWLEDGE_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = category_dir / f"{item['id']}.json"
    
    data = {
        "id": item["id"],
        "name": item["name"],
        "name_en": item["name_en"],
        "category": category,
        "subcategory": category,
        "nutrition_per_100g": {
            "calories": item["calories"],
            "protein": item["protein"],
            "fat": item["fat"],
            "carbs": item["carbs"],
            "fiber": 0
        },
        "price_range": {
            "min": int(item["price_avg"] * 0.7),
            "max": int(item["price_avg"] * 1.3),
            "average": item["price_avg"],
            "unit": item["unit"],
            "last_updated": "2024-01-15"
        },
        "seasonal_availability": {
            "全年": item["best_season"] == "全年",
            "best_season": item["best_season"] if item["best_season"] != "全年" else None
        },
        "storage": {
            "fresh": "冷藏3-5天",
            "tips": "按照食材特性保存"
        },
        "cuts": [],
        "pairing": {
            "classic": item["suitable"][:3],
            "usage": item["suitable"]
        },
        "tips": item["tips"]
    }
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    """主函数"""
    count = 0
    for category, items in ingredients.items():
        for item in items:
            create_ingredient_file(category, item)
            count += 1
    
    print(f"✅ Created {count} ingredient files")

if __name__ == "__main__":
    main()
