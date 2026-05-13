# Food Craft

> 🍽️ AI 驱动的智能菜谱生成系统 - 在约束条件下做出最好吃的菜

[![Update Knowledge Base](https://github.com/YOUR_USERNAME/food-craft/actions/workflows/update_weekly.yml/badge.svg)](https://github.com/YOUR_USERNAME/food-craft/actions/workflows/update_weekly.yml)

## ✨ 特性

- 🎯 **高度定制化** - 根据人数、场景、预算、热量等多维度需求生成菜谱
- 🌍 **世界菜系** - 涵盖 25+ 菜系，从川菜到法餐，从日料到墨西哥菜
- 🥗 **营养均衡** - 精确的热量、蛋白质、脂肪、碳水计算
- 💰 **预算控制** - 实时价格数据，人均成本精确到元
- ⏱️ **时间规划** - 多道菜并行烹饪的时间线
- 🛒 **采购清单** - 自动生成购物清单，不错过任何食材

## 🚀 快速开始

### 作为 AI Skill 使用

```bash
# 复制 SKILL.md 到你的 AI Agent 技能目录
cp SKILL.md ~/.opencode/skills/food-craft/SKILL.md
```

### 作为前端网站使用

```bash
# 直接打开前端页面
open frontend/index.html
```

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

## 🏗️ 项目结构

```
food-craft/
├── SKILL.md                          # AI Skill 文档
├── README.md                         # 项目说明
├── knowledge/                        # 知识库
│   ├── cuisines/                     # 菜系库（25+ 菜系）
│   │   ├── chinese/                  # 中国菜系
│   │   ├── japanese/                 # 日本料理
│   │   ├── korean/                   # 韩国料理
│   │   ├── southeast_asian/          # 东南亚菜系
│   │   ├── western/                  # 西方菜系
│   │   └── ...
│   ├── ingredients/                  # 食材库（50+ 食材）
│   │   ├── meat/                     # 肉类
│   │   ├── seafood/                  # 海鲜
│   │   ├── vegetables/               # 蔬菜
│   │   └── ...
│   ├── techniques/                   # 烹饪技法库
│   ├── pairing_rules.json            # 食材搭配规则
│   ├── nutrition_db.json             # 营养数据库
│   ├── price_index.json              # 价格指数
│   └── seasonal_calendar.json        # 时令食材日历
├── scripts/                          # 更新脚本
│   ├── update_prices.py              # 更新价格
│   ├── update_seasonal.py            # 更新时令
│   ├── update_trending.py            # 更新趋势
│   └── validate_knowledge.py         # 数据校验
├── frontend/                         # 前端页面
│   └── index.html                    # 单页应用
└── .github/workflows/                # GitHub Actions
    ├── update_weekly.yml             # 每周更新
    └── update_monthly.yml            # 每月更新
```

## 🍳 支持的菜系

### 中国菜系
川菜 | 粤菜 | 鲁菜 | 苏菜 | 浙菜 | 闽菜 | 湘菜 | 徽菜 | 东北菜 | 新疆菜 | 云南菜 | 贵州菜 | 家常菜

### 亚洲菜系
日本（和食、拉面、寿司）| 韩国 | 泰国 | 越南 | 马来西亚 | 印尼 | 印度

### 西方菜系
法国 | 意大利 | 西班牙 | 美国 | 英国 | 德国 | 地中海

### 其他菜系
土耳其 | 黎巴嫩 | 波斯 | 墨西哥 | 巴西 | 秘鲁 | 阿根廷 | 埃塞俄比亚 | 摩洛哥

## 📊 知识库统计

| 类别 | 数量 |
|------|------|
| 菜系 | 25+ |
| 食材 | 50+ |
| 烹饪技法 | 10+ |
| 搭配规则 | 20+ |

## 🔄 自动更新

知识库通过 GitHub Actions 自动更新：

- **每周更新**：价格数据、时令食材
- **每月更新**：热门趋势、数据校验

## 🛠️ 开发

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/food-craft.git
cd food-craft

# 校验数据
python scripts/validate_knowledge.py

# 更新价格
python scripts/update_prices.py
```

### 添加新菜系

1. 在 `knowledge/cuisines/` 下创建新的 JSON 文件
2. 按照现有格式填写菜系信息
3. 运行 `python scripts/validate_knowledge.py` 校验

### 添加新食材

1. 在 `knowledge/ingredients/` 下创建新的 JSON 文件
2. 填写营养数据、价格区间、搭配建议
3. 运行校验脚本

## 📄 License

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 🙏 致谢

- [下厨房](https://xiachufang.com/) - 菜谱数据参考
- [美食杰](https://www.meishij.net/) - 食材数据参考
