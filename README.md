# 🍽️ Food Craft

> AI 驱动的智能菜谱生成系统 - 在约束条件下做出最好吃的菜

[![GitHub Pages](https://img.shields.io/badge/Demo-🌐%20在线预览-blue)](https://mrlmrml.github.io/food-craft/)
[![Update Knowledge Base](https://github.com/MRLMRML/food-craft/actions/workflows/update_weekly.yml/badge.svg)](https://github.com/MRLMRML/food-craft/actions/workflows/update_weekly.yml)
[![Ingredients](https://img.shields.io/badge/食材-1000+-green)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/ingredients)
[![Cuisines](https://img.shields.io/badge/菜系-25+-orange)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/cuisines)

---

## 🌐 在线 Demo

**👉 [点击查看 Demo](https://mrlmrml.github.io/food-craft/)**

Demo 展示了一个完整的菜谱输出示例，包括：
- 📋 菜单总览（人数、时长、成本、热量）
- 👨‍🍳 详细做法（食材、步骤、小贴士）
- 🛒 采购清单（分类、价格）
- ⏱️ 时间规划（并行烹饪安排）

---

## ✨ 特性

- 🎯 **高度定制化** - 根据人数、场景、预算、热量等多维度需求生成菜谱
- 🌍 **全球菜系** - 涵盖 25+ 菜系，从川菜到法餐，从日料到墨西哥菜
- 🥗 **1000+ 食材** - 全球食材数据库，涵盖蔬菜、肉类、海鲜、调味料等
- 💰 **预算控制** - 实时价格数据，人均成本精确到元
- ⏱️ **时间规划** - 多道菜并行烹饪的时间线
- 🛒 **采购清单** - 自动生成购物清单，不错过任何食材

---

## 🚀 快速开始

### 作为 AI Skill 使用

```bash
# 复制 SKILL.md 到你的 AI Agent 技能目录
cp SKILL.md ~/.opencode/skills/food-craft/SKILL.md
```

### 本地运行 Demo

```bash
# 克隆仓库
git clone https://github.com/MRLMRML/food-craft.git
cd food-craft

# 打开 Demo 页面
open frontend/index.html
```

---

## 📖 使用示例

### 示例 1：日常晚餐

```
用户：帮我做个晚餐
AI：好的！先了解几个基本情况：
    1. 几个人吃？
    2. 什么场景？日常还是有客人？
    3. 有特别想吃的吗？

用户：2个人，日常，想吃点辣的
AI：明白了！给你安排一个川菜风格的晚餐：
    - 主菜：宫保鸡丁
    - 荤菜：回锅肉
    - 素菜：干煸四季豆
    - 汤品：紫菜蛋花汤
    - 主食：米饭

    预计总时长：55分钟
    预计总成本：¥90（人均¥45）
```

### 示例 2：宴客场景

```
用户：周末请朋友吃饭，6个人，预算500
AI：请客吃饭，安排！给你安排一个有档次的菜单：
    - 凉菜：口水鸡、拍黄瓜
    - 主菜：红烧肉、清蒸鲈鱼
    - 荤菜：蒜蓉粉丝虾
    - 素菜：清炒时蔬
    - 汤品：玉米排骨汤
    - 主食：米饭

    预计总时长：90分钟
    预计总成本：¥480（人均¥80）
```

### 示例 3：健身餐

```
用户：健身增肌餐，一人份，高蛋白
AI：增肌餐安排！给你一份高蛋白低脂菜单：
    - 主菜：黑椒牛柳（250g）
    - 配菜：西兰花（150g）
    - 主食：糙米饭（100g）

    热量：580大卡
    蛋白质：42g
```

---

## 🏗️ 项目结构

```
food-craft/
├── SKILL.md                          # AI Skill 文档
├── README.md                         # 项目说明
├── frontend/
│   └── index.html                    # Demo 页面
├── knowledge/                        # 知识库
│   ├── cuisines/                     # 25+ 菜系
│   ├── ingredients/                  # 1000+ 食材
│   ├── techniques/                   # 烹饪技法
│   ├── pairing_rules.json            # 搭配规则
│   ├── nutrition_db.json             # 营养数据
│   ├── price_index.json              # 价格指数
│   └── seasonal_calendar.json        # 时令食材
├── scripts/                          # 更新脚本
│   ├── generate_*.py                 # 食材生成脚本
│   ├── update_*.py                   # 数据更新脚本
│   └── validate_knowledge.py         # 数据校验
└── .github/workflows/                # GitHub Actions
    ├── update_weekly.yml             # 每周更新
    └── update_monthly.yml            # 每月更新
```

---

## 🍳 支持的菜系

### 中国菜系
川菜 | 粤菜 | 鲁菜 | 苏菜 | 浙菜 | 闽菜 | 湘菜 | 徽菜 | 东北菜 | 新疆菜 | 云南菜 | 贵州菜 | 家常菜

### 亚洲菜系
日本（和食、拉面、寿司）| 韩国 | 泰国 | 越南 | 马来西亚 | 印尼 | 印度

### 西方菜系
法国 | 意大利 | 西班牙 | 美国 | 英国 | 德国 | 地中海

### 其他菜系
土耳其 | 黎巴嫩 | 波斯 | 墨西哥 | 巴西 | 秘鲁 | 阿根廷 | 埃塞俄比亚 | 摩洛哥

---

## 📊 知识库统计

| 类别 | 数量 |
|------|------|
| 菜系 | 25+ |
| 食材 | 1000+ |
| 烹饪技法 | 10+ |
| 调味料 | 50+ |
| 搭配规则 | 20+ |

---

## 🔄 自动更新

知识库通过 GitHub Actions 自动更新：

- **每周更新**：价格数据、时令食材
- **每月更新**：热门趋势、数据校验

---

## 🛠️ 开发

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/MRLMRML/food-craft.git
cd food-craft

# 校验数据
python3 scripts/validate_knowledge.py

# 生成食材
python3 scripts/generate_global_ingredients.py
```

### 添加新菜系

1. 在 `knowledge/cuisines/` 下创建新的 JSON 文件
2. 按照现有格式填写菜系信息
3. 运行 `python3 scripts/validate_knowledge.py` 校验

### 添加新食材

1. 在 `knowledge/ingredients/` 下创建新的 JSON 文件
2. 填写营养数据、价格区间、搭配建议
3. 运行校验脚本

---

## 📄 License

MIT License

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 🙏 致谢

- [下厨房](https://xiachufang.com/) - 菜谱数据参考
- [美食杰](https://www.meishij.net/) - 食材数据参考
