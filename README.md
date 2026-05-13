# 🍽️ Food Craft

> AI 驱动的智能菜谱生成系统 - 在约束条件下做出最好吃的菜

[![GitHub Pages](https://img.shields.io/badge/Demo-🌐%20在线预览-blue)](https://mrlmrml.github.io/food-craft/)
[![Recipes](https://img.shields.io/badge/菜谱-1744+-red)](https://github.com/MRLMRML/food-craft/tree/main/recipes)
[![Ingredients](https://img.shields.io/badge/食材-1025+-green)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/ingredients)
[![Cuisines](https://img.shields.io/badge/菜系-39+-orange)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/cuisines)

---

## 🎯 项目逻辑

```
用户需求 → Agent读取SKILL.md → LLM生成菜谱 → 文字输出 / 网页展示
```

**两种输出方式**：
1. **文字输出**：直接在对话中展示（默认）
2. **网页输出**：生成HTML文件，浏览器打开查看（美化版本）

---

## 🚀 使用方式

### 作为 AI Skill 使用

```bash
cp SKILL.md ~/.opencode/skills/food-craft/SKILL.md
```

然后在 Agent 中使用：
```
用户：帮我做个晚餐，4个人，预算200
AI：好的！给你安排...
```

### 查看网页展示 Demo

**👉 [在线 Demo](https://mrlmrml.github.io/food-craft/)**

这是 Skill 输出的美化展示版本，展示了一次完整的菜谱生成结果。

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

### 示例 2：输出网页版
```
用户：帮我做个晚餐，输出成网页版
AI：好的！[生成HTML内容]
    保存为 html 文件，用浏览器打开即可
```

---

## 🏗️ 项目结构

```
food-craft/
├── SKILL.md                    # AI Skill 文档（Agent读取）
├── README.md                   # 项目说明
├── frontend/
│   └── index.html              # 网页展示模板（输出美化版本）
├── knowledge/                  # 知识库
│   ├── ingredients/            # 1025 种食材
│   ├── cuisines/               # 39 种菜系
│   └── ...
├── recipes/                    # 菜谱库（1744+ 道）
├── scenes/                     # 5 种场景规则
└── scripts/                    # 数据生成脚本
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
