# 🍽️ Food Craft

> AI 驱动的智能菜谱生成系统 - 在约束条件下做出最好吃的菜

[![收录于 JerryKing's Trove](https://img.shields.io/badge/收录于-JerryKing's%20Trove-blue)](https://github.com/MRLMRML/JerryKing-s-Trove)

[![GitHub Pages](https://img.shields.io/badge/Demo-🌐%20在线预览-blue)](https://mrlmrml.github.io/food-craft/)
[![Recipes](https://img.shields.io/badge/菜谱-1744+-red)](https://github.com/MRLMRML/food-craft/tree/main/recipes)
[![Ingredients](https://img.shields.io/badge/食材-1025+-green)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/ingredients)
[![Cuisines](https://img.shields.io/badge/菜系-39+-orange)](https://github.com/MRLMRML/food-craft/tree/main/knowledge/cuisines)
[![Scenes](https://img.shields.io/badge/场景-7-purple)](https://github.com/MRLMRML/food-craft/tree/main/scenes)

---

## 🎯 项目是什么

Food Craft 是一个 AI Skill，帮用户生成菜谱。

**核心理念**：好吃第一，不懂就问，灵活迭代，实用输出。

**工作流程**：
```
用户告诉需求 → Agent 读取 SKILL.md → LLM 生成菜谱 → 输出
```

**两种输出方式**：
1. **文字输出**：直接在对话中展示（默认）
2. **网页输出**：生成 HTML，浏览器打开查看（美化版本）

**在线 Demo**：[https://mrlmrml.github.io/food-craft/](https://mrlmrml.github.io/food-craft/)

---

## ✨ 核心能力

### 🎯 高度定制化

根据多维度需求生成菜谱：
- 用餐人数
- 用餐场景（7种）
- 菜系偏好（39+种）
- 预算控制
- 热量要求
- 时间限制
- 口味偏好
- 忌口/过敏

### 🌍 全球菜系

涵盖 39+ 种菜系：

| 区域 | 菜系 |
|------|------|
| **中国** | 川菜、粤菜、鲁菜、苏菜、浙菜、闽菜、湘菜、徽菜、东北菜、新疆菜、云南菜、贵州菜、家常菜 |
| **亚洲** | 日本、韩国、泰国、越南、马来西亚、印尼、印度 |
| **西方** | 法国、意大利、西班牙、美国、英国、德国、地中海 |
| **其他** | 土耳其、黎巴嫩、波斯、墨西哥、巴西、秘鲁、阿根廷、埃塞俄比亚、摩洛哥 |

### 🎯 7 种场景

| 场景 | 说明 | 追问重点 |
|------|------|----------|
| 👶 **儿童餐** | 3-12岁营养餐 | 软烂易嚼，造型可爱 |
| 👴 **老人餐** | 65岁以上软烂餐 | 低盐低油，易消化 |
| 💪 **减脂餐** | 低卡高蛋白 | 热量控制，蛋白质目标 |
| 🏋️ **增肌餐** | 高蛋白高热量 | 蛋白质、碳水比例 |
| 🥬 **素食餐** | 纯素/蛋奶素 | 植物蛋白搭配 |
| 🎉 **聚餐** | 请客吃饭 | 预算、档次、忌口 |
| 🎁 **节日** | 节日聚餐 | 传统菜品、人数 |

### 🍽️ 1744+ 菜谱

- 中国菜系菜谱
- 国际菜系菜谱
- 场景专属菜谱（儿童、老人、减脂、增肌、素食）

### 🥬 1025+ 食材

- 蔬菜类
- 肉类
- 海鲜类
- 调味料
- 主食类
- 水果类
- 干货类
- 乳制品

---

## 🚀 使用方式

### 安装 Skill

```bash
cp SKILL.md ~/.opencode/skills/food-craft/SKILL.md
```

### 交互协议

**第一轮：基础需求（必问）**
```
1. 几个人吃？
2. 什么场景？（日常/聚餐/节日/约会/健身/便当/省钱）
3. 什么时候吃？（早餐/午餐/晚餐/下午茶/夜宵）
```

**第二轮：约束探索（场景化追问）**
```
- 有特别想吃的食材吗？
- 有偏好的菜系吗？
- 有忌口或过敏吗？
- [场景专属追问]
```

**第三轮：确认与迭代**
```
这是为你安排的菜单：
[菜单列表]

看看满意吗？可以：
- 换掉某道菜
- 调整成本/热量
- 查看某道菜的详细做法
```

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

### 示例 4：单一食材
```
用户：我只想吃茄子
AI：茄子可以做出很多美味！
    - 红烧茄子
    - 鱼香茄子
    - 蒜蓉烤茄子
    - 肉末茄子
    - 凉拌茄子
    ...
```

### 示例 5：输出网页版
```
用户：帮我做个晚餐，输出成网页版
AI：好的！[生成HTML内容]
    保存为 html 文件，用浏览器打开即可
```

---

## 🏗️ 项目结构

```
food-craft/
├── SKILL.md                    # AI Skill 文档（Agent 读取）
├── README.md                   # 项目说明
│
├── frontend/
│   └── index.html              # 网页展示模板（输出美化版本）
│
├── knowledge/                  # 知识库
│   ├── ingredients/            # 1025 种食材（营养、价格、搭配）
│   ├── cuisines/               # 39 种菜系（口味特征、招牌菜）
│   ├── techniques/             # 烹饪技法
│   ├── pairing_rules.json      # 食材搭配规则
│   ├── nutrition_db.json       # 营养数据库
│   ├── price_index.json        # 价格指数
│   └── seasonal_calendar.json  # 时令食材
│
├── recipes/                    # 菜谱库（1744+ 道）
│   ├── chinese/                # 中国菜系菜谱
│   ├── japanese/               # 日本料理
│   ├── korean/                 # 韩国料理
│   ├── thai/                   # 泰国菜
│   ├── french/                 # 法国菜
│   ├── italian/                # 意大利菜
│   ├── ...                     # 更多菜系
│   ├── children/               # 儿童餐
│   ├── elderly/                # 老人餐
│   ├── weight_loss/            # 减脂餐
│   ├── muscle_gain/            # 增肌餐
│   └── vegetarian/             # 素食餐
│
├── scenes/                     # 场景规则
│   ├── children.json           # 儿童餐规则
│   ├── elderly.json            # 老人餐规则
│   ├── weight_loss.json        # 减脂餐规则
│   ├── muscle_gain.json        # 增肌餐规则
│   └── vegetarian.json         # 素食餐规则
│
└── scripts/                    # 数据生成脚本
    ├── generate_*.py           # 食材/菜谱生成
    ├── export_recipes_json.py  # 导出JSON
    └── validate_knowledge.py   # 数据校验
```

---

## 📊 数据统计

| 类别 | 数量 | 说明 |
|------|------|------|
| 菜谱 | 1744+ | 中国菜 + 国际菜 + 场景菜 |
| 食材 | 1025+ | 蔬菜、肉类、海鲜、调味料等 |
| 菜系 | 39+ | 覆盖全球主要菜系 |
| 场景 | 7 | 儿童、老人、减脂、增肌、素食、聚餐、节日 |

---

## 🔧 约束求解规则

### 优先级（从高到低）

1. **安全**（过敏、忌口）→ 必须满足，不可妥协
2. **预算** → 尽量满足，超出时推荐替代方案
3. **热量** → 尽量满足，超出时调整份量或推荐替代
4. **时间** → 尽量满足，超出时简化步骤或换菜
5. **口味** → 灵活调整，根据场景平衡

### 冲突处理

| 冲突场景 | 处理方式 | 示例 |
|----------|----------|------|
| 食材超出预算 | 降级替代 | 龙虾→虾仁 |
| 热量超标 | 改良做法 | 红烧肉→清蒸肉 |
| 时间不足 | 简化或换菜 | 佛跳墙→快手汤 |
| 口味冲突 | 推荐兼容方案 | 又想辣又想清淡→微辣菜系 |

---

## 📄 License

MIT License
