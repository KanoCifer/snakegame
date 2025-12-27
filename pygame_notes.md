# 🎮 Pygame 学习笔记

基于贪吃蛇项目 `main_desktop.py` 整理的 Pygame 常用函数和方法。

---

## 目录

- [1. 初始化与退出](#1-初始化与退出)
- [2. 显示与窗口](#2-显示与窗口)
- [3. 图像加载与处理](#3-图像加载与处理)
- [4. 绘制图形](#4-绘制图形)
- [5. 事件处理](#5-事件处理)
- [6. 音频播放](#6-音频播放)
- [7. 时间控制](#7-时间控制)
- [8. 字体与文本](#8-字体与文本)
- [9. 矩形操作](#9-矩形操作)

---

## 1. 初始化与退出

### `pygame.init()`
初始化所有 Pygame 模块，**必须在使用其他 Pygame 功能之前调用**。

```python
pygame.init()
```

### `pygame.quit()`
退出并清理所有 Pygame 模块，通常在程序结束时调用。

```python
pygame.quit()
sys.exit()  # 配合 sys.exit() 完全退出程序
```

---

## 2. 显示与窗口

### `pygame.display.set_mode((width, height))`
创建游戏窗口，返回一个 Surface 对象用于绑定绘制内容。

```python
screen = pygame.display.set_mode((800, 800))
```

### `pygame.display.set_caption(title)`
设置窗口标题栏文字。

```python
pygame.display.set_caption("SNAKE贪吃蛇游戏")
```

### `pygame.display.update()` / `pygame.display.flip()`
刷新屏幕显示。两者功能类似：
- `update()` - 可以只更新部分区域
- `flip()` - 更新整个屏幕

```python
pygame.display.update()  # 推荐使用
```

---

## 3. 图像加载与处理

### `pygame.image.load(path)`
加载图片文件，返回 Surface 对象。

```python
image = pygame.image.load('assets/berry.png')
```

### `.convert_alpha()`
优化带透明通道（Alpha）的图片，**提升渲染性能**。

```python
image = pygame.image.load('assets/berry.png').convert_alpha()
```

> ⚠️ **注意**：必须在 `pygame.display.set_mode()` 之后调用，否则会报错 "No video mode has been set"

### `pygame.transform.scale(surface, (width, height))`
缩放图片到指定尺寸。

```python
lives_img = pygame.image.load('assets/lives.png').convert_alpha()
lives_img = pygame.transform.scale(lives_img, (24, 24))
```

### `surface.blit(source, dest)`
将一个 Surface 绘制到另一个 Surface 上。

```python
# 将图片绘制到屏幕的指定位置
screen.blit(image, (x, y))

# 使用 Rect 定位
screen.blit(image, rect)
```

### `surface.fill(color)`
用指定颜色填充整个 Surface（常用于清屏）。

```python
screen.fill((0, 0, 0))  # 黑色背景
```

### `surface.get_width()` / `surface.get_height()`
获取 Surface 的宽度和高度。

```python
width = screen.get_width()   # 800
height = screen.get_height() # 800
```

---

## 4. 绘制图形

### `pygame.draw.rect(surface, color, rect, border_radius=0)`
绘制矩形。

```python
# 绘制填充矩形
pygame.draw.rect(screen, (0, 160, 0), rect)

# 绘制圆角矩形
pygame.draw.rect(screen, (0, 160, 0), rect, border_radius=6)
```

---

## 5. 事件处理

### `pygame.event.get()`
获取事件队列中的所有事件，返回事件列表。

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
```

### 常用事件类型

| 事件类型 | 说明 | 示例 |
|----------|------|------|
| `QUIT` | 点击窗口关闭按钮 | `event.type == QUIT` |
| `KEYDOWN` | 键盘按下 | `event.type == pygame.KEYDOWN` |
| `KEYUP` | 键盘释放 | `event.type == pygame.KEYUP` |
| `MOUSEBUTTONDOWN` | 鼠标按下 | `event.type == pygame.MOUSEBUTTONDOWN` |

### 键盘按键常量

```python
from pygame.locals import K_w, K_s, K_a, K_d, K_ESCAPE, K_SPACE

if event.key == K_w:      # W 键
    pass
if event.key == K_SPACE:  # 空格键
    pass
if event.key == K_ESCAPE: # ESC 键
    pass
```

### `pygame.mouse.get_pos()`
获取鼠标当前位置。

```python
mouse_pos = pygame.mouse.get_pos()  # 返回 (x, y) 元组
```

---

## 6. 音频播放

### `pygame.mixer.Sound(path)`
加载音效文件（支持 WAV、MP3、OGG）。

```python
sound = pygame.mixer.Sound('assets/hit.wav')
music = pygame.mixer.Sound('assets/game_bgm.mp3')
```

### `.play(loops=0, fade_ms=0)`
播放音效。
- `loops`: 循环次数，`-1` 表示无限循环
- `fade_ms`: 淡入时间（毫秒）

```python
sound.play()           # 播放一次
music.play(-1)         # 无限循环
music.play(-1, fade_ms=500)  # 0.5秒淡入，无限循环
```

### `.stop()`
停止播放。

```python
music.stop()
```

### `.set_volume(value)`
设置音量，范围 0.0 ~ 1.0。

```python
music.set_volume(0.3)  # 30% 音量
```

---

## 7. 时间控制

### `pygame.time.Clock()`
创建时钟对象，用于控制帧率。

```python
clock = pygame.time.Clock()
```

### `clock.tick(fps)`
控制游戏循环的帧率，返回上一帧到现在的时间（毫秒）。

```python
clock.tick(60)  # 限制最高 60 FPS
```

### `pygame.time.get_ticks()`
获取从 `pygame.init()` 开始到现在的毫秒数。

```python
current_time = pygame.time.get_ticks()

# 常用于实现固定时间间隔的逻辑
elapsed = current_time - last_logic_time
if elapsed >= 100:  # 每 100ms 执行一次
    # 执行逻辑
    last_logic_time = current_time
```

---

## 8. 字体与文本

### `pygame.font.Font(name, size)`
创建字体对象。
- `name`: 字体文件路径，`None` 使用默认字体
- `size`: 字体大小

```python
font = pygame.font.Font(None, 36)  # 默认字体，36号
```

### `font.render(text, antialias, color)`
渲染文本为 Surface。
- `text`: 要渲染的文字
- `antialias`: 是否抗锯齿（通常用 `True`）
- `color`: 文字颜色

```python
text_surface = font.render("Score: 10", True, (255, 255, 255))
screen.blit(text_surface, (10, 10))
```

---

## 9. 矩形操作

### `pygame.Rect(x, y, width, height)`
创建矩形对象，常用于碰撞检测和定位。

```python
rect = pygame.Rect(100, 100, 50, 30)
```

### `surface.get_rect()`
获取 Surface 的矩形，用于定位。

```python
image = pygame.image.load('assets/berry.png')
rect = image.get_rect()

# 设置中心点位置
rect.center = (400, 400)

# 设置左上角位置
rect.left = 100
rect.top = 200
```

### `rect.collidepoint(pos)`
检测点是否在矩形内（常用于按钮点击检测）。

```python
if rect.collidepoint(mouse_pos):
    print("鼠标在矩形内！")
```

### 矩形常用属性

| 属性 | 说明 |
|------|------|
| `rect.x`, `rect.y` | 左上角坐标 |
| `rect.left`, `rect.right` | 左边/右边 x 坐标 |
| `rect.top`, `rect.bottom` | 顶部/底部 y 坐标 |
| `rect.center` | 中心点 (x, y) |
| `rect.width`, `rect.height` | 宽度和高度 |

---

## 📌 常用代码模板

### 基本游戏框架

```python
import pygame
import sys

pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    # 1. 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 2. 更新游戏逻辑
    # ...
    
    # 3. 绘制
    screen.fill((0, 0, 0))  # 清屏
    # 绘制游戏元素...
    
    # 4. 刷新显示
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
```

---

## 📚 参考资源

- [Pygame 官方文档](https://www.pygame.org/docs/)
- [Pygame 教程](https://pygame.readthedocs.io/)

---

*整理自贪吃蛇项目 main_desktop.py*
