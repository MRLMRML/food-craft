# 🍽️ Food Craft

> AI 驱动的智能菜谱生成系统 - 在约束条件下做出最好吃的菜

[![GitHub Pages](https://img.shields.io/badge/Demo-🌐%20在线预览-blue)](https://mrlmrml.github.io/food-craft/)
[![Recipes](https://img.shields.io/badge/菜谱-1744+-red)](https://github.com/MRLMRML/food-craft/tree/main/recipes)
[![Ingredients](https://img.shields.io/badge/食材-1025+-green)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/ingredients)
[![Cuisines](https://img.shields.io/badge/菜系-39+-orange)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/cuisines)
[![Scenes](https://img.shields.io/badge/场景-5-purple)](https://github.com/MRLMRML/food-craft/tree/main/scenes)

---

## 🚀 两种使用方式

### 方式 1：作为 AI Skill 使用（文字交互）

将 SKILL.md 安装到你的 AI Agent 技能目录：

```bash
cp SKILL.md ~/.opencode/skills/food-craft/SKILL.md
```

然后在 Agent 中使用：
```
用户：帮我做个晚餐，4个人，预算200
AI：好的！给你安排...
```

### 方式 2：启动本地服务器（交互式网页）

```bash
git clone https://github.com/MRLMRML/food-craft.git
cd food-craft
python3 server.py
```

打开浏览器访问 `http://localhost:8080`

**在线 Demo**：https://mrlmrml.github.io/food-craft/

---

## ✨ 特性

- 🎯 **高度定制化** - 根据人数、场景、预算、热量等多维度需求生成菜谱
- 🌍 **全球菜系** - 涵盖 39 种菜系，从川菜到法餐，从日料到墨西哥菜
- 🥗 **1744+ 菜谱** - 覆盖中国菜、国际菜、场景菜谱
- 🥬 **1025+ 食材** - 全球食材数据库
- 🎯 **5 种场景** - 儿童餐、老人餐、减脂餐、增肌餐、素食餐
- 🔍 **智能搜索** - 按菜系、口味、关键词筛选

---

## 📖 使用示例

### 示例 1：日常晚餐
```
用户：帮我做个晚餐，2个人，想吃辣的
AI：给你安排川菜风格晚餐：
    - 宫保鸡丁
    - 回锅肉
    - 干煸四季豆
    - 紫菜蛋花汤
    预计：55分钟，¥90
```

### 示例 2：宴客场景
```
用户：周末请朋友吃饭，6个人，预算500
AI：给你安排有档次的菜单：
    - 口水鸡、拍黄瓜
    - 红烧肉、清蒸鲈鱼
    - 蒜蓉粉丝虾
    预计：90分钟，¥480
```

### 示例 3：健身餐
```
用户：健身增肌餐，一人份，高蛋白
AI：增肌餐安排：
    - 黑椒牛柳（250g）
    - 西兰花（150g）
    - 糙米饭（100g）
    热量：580大卡，蛋白质：42g
```

---

## 🏗️ 项目结构

```
food-craft/
├── SKILL.md                    # AI Skill 文档
├── README.md                   # 项目说明
├── server.py                   # 本地服务器
├── frontend/
│   ├── index.html              # 交互式前端
│   └── recipes.json            # 菜谱数据
├── knowledge/                  # 知识库
│   ├── cuisines/               # 39 种菜系
│   ├── ingredients/            # 1025 种食材
│   └── ...
├── recipes/                    # 菜谱库（1744+ 道）
├── scenes/                     # 5 种场景规则
├── scripts/                    # 数据生成脚本
└── .github/workflows/          # GitHub Actions
```

---

## 🍳 支持的菜系

**中国**：川菜 | 粤菜 | 鲁菜 | 苏菜 | 浙菜 | 闽菜 | 湘菜 | 徽菜 | 东北菜 | 新疆菜 | 云南菜 | 家常菜

**亚洲**：日本 | 韩国 | 泰国 | 越南 | 印度

**西方**：法国 | 意大利 | 西班牙 | 美国 | 英国 | 德国 | 地中海

**其他**：土耳其 | 墨西哥 | 巴西 | 秘鲁 | 埃塞俄比亚 | 摩洛哥

---

## 📊 统计

| 类别 | 数量 |
|------|------|
| 菜谱 | 1744+ |
| 食材 | 1025+ |
| 菜系 | 39+ |
| 场景 | 5 |

---

## 📄 License

MIT License
