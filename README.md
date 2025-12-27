# 🐍 Snake Game 贪吃蛇游戏

一个使用 Python + Pygame 开发的经典贪吃蛇游戏，支持桌面端和 Web 端（通过 pygbag）。

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)

## ✨ 游戏特性

- 🎮 经典贪吃蛇玩法
- 🎨 精美的像素风格贴图
- 🎵 背景音乐和音效（转向、吃食物、碰撞）
- 🏆 最高分记录保存
- ❤️ 生命值系统
- 🌐 支持 Web 端运行（pygbag）

## 📁 项目结构

```
snake/
├── main.py              # Web 端入口（支持 pygbag）
├── main_desktop.py      # 桌面端入口
├── highest_score.txt    # 最高分存档
├── assets/              # 游戏资源
│   ├── berry.png        # 食物贴图
│   ├── body.png         # 蛇身贴图
│   ├── wall.png         # 墙壁贴图
│   ├── lives.png        # 生命值图标
│   ├── right_1/2.png    # 蛇头动画（右）
│   ├── left_1/2.png     # 蛇头动画（左）
│   ├── up_1/2.png       # 蛇头动画（上）
│   ├── down_1/2.png     # 蛇头动画（下）
│   ├── game_bgm.mp3     # 背景音乐
│   ├── step.wav         # 转向音效
│   ├── point.wav        # 得分音效
│   └── hit.wav          # 碰撞音效
└── build/               # Web 构建输出
    └── web/
        └── index.html
```

## 🚀 快速开始

### 环境要求

- Python 3.10+
- Pygame 2.0+

### 安装依赖

```bash
# 创建虚拟环境（可选）
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 安装依赖
pip install pygame
```

### 运行游戏

**桌面端：**
```bash
python main_desktop.py
```

**Web 端（需要 pygbag）：**
```bash
pip install pygbag
pygbag main.py
```

## 🎮 操作说明

| 按键 | 功能 |
|------|------|
| W | 向上移动 |
| S | 向下移动 |
| A | 向左移动 |
| D | 向右移动 |
| Space | 开始游戏 |
| ESC | 退出游戏 |

## 🎯 游戏规则

1. 控制蛇吃掉屏幕上的食物（浆果）
2. 每吃一个食物，蛇身增长一节，得分 +1
3. 撞到墙壁或自己的身体会失去生命
4. 生命值耗尽时游戏结束
5. 最高分会自动保存

## 📸 游戏截图

*游戏界面展示*

## 🛠️ 技术栈

- **Python** - 编程语言
- **Pygame** - 游戏开发库
- **pygbag** - Web 端打包工具

## 📝 License

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

Made with ❤️ by KanoCifer
