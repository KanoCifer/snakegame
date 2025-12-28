# 🐍 Snake Game 贪吃蛇游戏

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

A classic Snake game developed with Python + Pygame, supporting both desktop and web (via pygbag).

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)

### ✨ Features

- 🎮 Classic Snake gameplay
- 🎨 Beautiful pixel-style graphics
- 🎵 Background music and sound effects (turn, eat, collision)
- 🏆 High score saving
- ❤️ Lives system
- 🌐 Web support (via pygbag)
- 🗺️ **Map Editor** - Create custom maps
- 🍓 Huge Berry - Spawns every 10s, 2x2 size, length +3
- ⚙️ Settings Button - Click on start screen to open map editor and return

### 📁 Project Structure

```
snake/
├── main.py              # Web entry (pygbag support)
├── main_desktop.py      # Desktop entry
├── mapeditor.py         # Map editor tool
├── map.json             # Map data file
├── highest_score.txt    # High score save file
├── assets/              # Game assets
│   ├── berry.png        # Food sprite
│   ├── body.png         # Snake body sprite
│   ├── wall.png         # Wall sprite
│   ├── lives.png        # Lives icon
│   ├── right_1/2.png    # Snake head animation (right)
│   ├── left_1/2.png     # Snake head animation (left)
│   ├── up_1/2.png       # Snake head animation (up)
│   ├── down_1/2.png     # Snake head animation (down)
│   ├── game_bgm.mp3     # Background music
│   ├── step.wav         # Turn sound effect
│   ├── point.wav        # Score sound effect
│   └── hit.wav          # Collision sound effect
└── build/               # Web build output
    └── web/
        └── index.html
```

### 🚀 Quick Start

#### Requirements

- Python 3.10+
- Pygame 2.0+

#### Install Dependencies

```bash
# Create virtual environment (optional)
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install pygame
```

#### Run the Game

**Desktop:**
```bash
python main_desktop.py
```

**Web (requires pygbag):**
```bash
pip install pygbag
pygbag main.py
```

### 🎮 Controls

| Key | Action |
|-----|--------|
| W | Move Up |
| S | Move Down |
| A | Move Left |
| D | Move Right |
| Space | Start Game |
| ESC | Quit Game |

### 🎯 Game Rules

1. Control the snake to eat food (berries) — length +1
2. Huge berry (spawns ~every 10s, 2x2) — length +3
3. Hitting walls or yourself loses a life; lives reach 0 → game over
4. High score saves automatically

### 📸 Screenshots

<p align="center">
  <img src="screenshot/Screenshot%202025-12-27%20at%2021.06.15.png" alt="Start Screen" width="400">
  <img src="screenshot/Screenshot%202025-12-27%20at%2021.07.13.png" alt="Gameplay" width="400">
</p>

### 🎨 Game Assets

| Head (Right) | Head (Left) | Head (Up) | Head (Down) |
|:------------:|:-----------:|:---------:|:-----------:|
| <img src="assets/right_1.png" width="32"> <img src="assets/right_2.png" width="32"> | <img src="assets/left_1.png" width="32"> <img src="assets/left_2.png" width="32"> | <img src="assets/up_1.png" width="32"> <img src="assets/up_2.png" width="32"> | <img src="assets/down_1.png" width="32"> <img src="assets/down_2.png" width="32"> |

| Body | Food | Wall | Lives |
|:----:|:----:|:----:|:-----:|
| <img src="assets/body.png" width="32"> | <img src="assets/berry.png" width="32"> | <img src="assets/wall.png" width="32"> | <img src="assets/lives.png" width="32"> |

### 🛠️ Tech Stack

- **Python** - Programming Language
- **Pygame** - Game Development Library
- **pygbag** - Web Packaging Tool

### 🗺️ Map Editor

Create custom maps with the built-in map editor:

```bash
python mapeditor.py
```

Shortcut: click the ⚙️ settings icon on the start screen to launch the editor; closing it returns to the game and reloads `map.json`.

| Key | Action |
|-----|--------|
| Left Click | Place wall |
| Right Click | Remove wall |
| S | Save map |
| C | Clear all walls |
| ESC | Quit editor |

Maps are saved to `map.json` and will be loaded automatically when you start the game.

### 📝 Changelog

#### v1.2.0 (2025-12-28)
- ✨ Huge berry added (2x2, length +3, spawns every 10s)
- ✨ Start-screen settings button launches map editor and reloads map on exit
- ✨ Start-screen tips now show controls and rules
- 🐛 Fixed score inflation after length ≥12 (rate no longer mutates per call)

#### v1.1.0 (2025-12-28)
- ✨ Added Map Editor - Create and edit custom maps
- 🐛 Fixed high score not saving immediately
- 🐛 Fixed high score not updating in real-time
- 🐛 Improved collision pause (non-blocking, 1 second pause after collision)

#### v1.0.0
- 🎉 Initial release

### 🛠️ TODO

1. ~~Map Editor~~ ✅
2. Multiple map selection
3. Difficulty levels
4. ...

---

<a name="中文"></a>
## 中文

一个使用 Python + Pygame 开发的经典贪吃蛇游戏，支持桌面端和 Web 端（通过 pygbag）。

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)

### ✨ 游戏特性

- 🎮 经典贪吃蛇玩法
- 🎨 精美的像素风格贴图
- 🎵 背景音乐和音效（转向、吃食物、碰撞）
- 🏆 最高分记录保存
- ❤️ 生命值系统
- 🌐 支持 Web 端运行（pygbag）
- 🗺️ **地图编辑器** - 创建自定义地图
- 🍓 巨型食物 - 每约 10 秒刷新一次，2x2 占位，长度 +3
- ⚙️ 设置按钮 - 开始界面点击可打开地图编辑器，退出后返回游戏

### 📁 项目结构

```
snake/
├── main.py              # Web 端入口（支持 pygbag）
├── main_desktop.py      # 桌面端入口
├── mapeditor.py         # 地图编辑器
├── map.json             # 地图数据文件
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

### 🚀 快速开始

#### 环境要求

- Python 3.10+
- Pygame 2.0+

#### 安装依赖

```bash
# 创建虚拟环境（可选）
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 安装依赖
pip install pygame
```

#### 运行游戏

**桌面端：**
```bash
python main_desktop.py
```

**Web 端（需要 pygbag）：**
```bash
pip install pygbag
pygbag main.py
```

### 🎮 操作说明

| 按键 | 功能 |
|------|------|
| W | 向上移动 |
| S | 向下移动 |
| A | 向左移动 |
| D | 向右移动 |
| Space | 开始游戏 |
| ESC | 退出游戏 |

### 🎯 游戏规则

1. 吃普通食物：长度 +1
2. 吃巨型食物（约每 10 秒刷新，2x2）：长度 +3
3. 撞墙或撞自己：生命 -1；生命为 0 游戏结束
4. 最高分自动保存

### 📸 游戏截图

<p align="center">
  <img src="screenshot/Screenshot%202025-12-27%20at%2021.06.15.png" alt="游戏开始界面" width="400">
  <img src="screenshot/Screenshot%202025-12-27%20at%2021.07.13.png" alt="游戏进行中" width="400">
</p>

### 🎨 游戏素材

| 蛇头（右） | 蛇头（左） | 蛇头（上） | 蛇头（下） |
|:----------:|:----------:|:----------:|:----------:|
| <img src="assets/right_1.png" width="32"> <img src="assets/right_2.png" width="32"> | <img src="assets/left_1.png" width="32"> <img src="assets/left_2.png" width="32"> | <img src="assets/up_1.png" width="32"> <img src="assets/up_2.png" width="32"> | <img src="assets/down_1.png" width="32"> <img src="assets/down_2.png" width="32"> |

| 蛇身 | 食物 | 墙壁 | 生命值 |
|:----:|:----:|:----:|:------:|
| <img src="assets/body.png" width="32"> | <img src="assets/berry.png" width="32"> | <img src="assets/wall.png" width="32"> | <img src="assets/lives.png" width="32"> |

### 🛠️ 技术栈

- **Python** - 编程语言
- **Pygame** - 游戏开发库
- **pygbag** - Web 端打包工具

### 🗺️ 地图编辑器

使用内置的地图编辑器创建自定义地图：

```bash
python mapeditor.py
```

快捷方式：在开始界面点击 ⚙️ 设置按钮即可启动编辑器，关闭后自动返回游戏并重新加载 `map.json`。

| 按键 | 功能 |
|------|------|
| 鼠标左键 | 放置墙壁 |
| 鼠标右键 | 删除墙壁 |
| S | 保存地图 |
| C | 清除所有墙壁 |
| ESC | 退出编辑器 |

地图保存到 `map.json`，启动游戏时会自动加载。

### 📝 更新日志

#### v1.2.0 (2025-12-28)
- ✨ 新增巨型食物（2x2，占位，长度 +3，每 10 秒刷新一次）
- ✨ 开始界面增加 ⚙️ 设置按钮，点击可打开地图编辑器并返回后自动加载新地图
- ✨ 开始界面展示操作指南与规则
- 🐛 修复长度 ≥12 后分数异常增长（倍率不再被反复累加）

#### v1.1.0 (2025-12-28)
- ✨ 新增地图编辑器 - 可创建和编辑自定义地图
- 🐛 修复最高分未即时保存的问题
- 🐛 修复最高分未实时更新显示的问题
- 🐛 改进碰撞暂停机制（非阻塞式，碰撞后暂停1秒）

#### v1.0.0
- 🎉 初始版本发布

### 🛠️ 待完善

1. ~~地图编辑器~~ ✅
2. 多地图选择
3. 难度等级
4. ...

---

## 📝 License

MIT License

## 🤝 Contributing / 贡献

Welcome to submit Issues and Pull Requests!

欢迎提交 Issue 和 Pull Request！

---

Made with ❤️ by KanoCifer
