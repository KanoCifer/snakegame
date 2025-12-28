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

## 10. Sprites（精灵）

Pygame 的 `sprite` 模块提供了对游戏对象的组织、更新和批量绘制的便利工具，适合管理角色、子弹、粒子、地块等。

### 常用类

- `pygame.sprite.Sprite`：基础类，继承后实现 `image`（Surface）和 `rect`（Rect）属性，并可实现 `update()` 方法。
- `pygame.sprite.Group`：管理一组精灵，支持统一 `update()`、`draw(surface)` 与碰撞查询。

### 基本用法（精灵类示例）

```python
import pygame

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image  # Surface
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, dt):
        # 根据 delta time 更新位置或动画
        self.rect.x += 100 * dt  # 每秒 100 px

# 创建组并使用
sprite_group = pygame.sprite.Group()
player = MySprite(pygame.image.load('assets/body.png').convert_alpha(), 100, 100)
sprite_group.add(player)

# 在主循环中
# dt = clock.tick(60) / 1000.0  # 秒为单位
# sprite_group.update(dt)
# sprite_group.draw(screen)
```

### 批量绘制与更新

使用 `Group.update()` 会调用组内每个精灵的 `update()`。
`Group.draw(surface)` 会把每个精灵的 `image` 按各自的 `rect` 绘制到目标 Surface 上（注意：精灵必须有 `image` 和 `rect` 属性）。

### 碰撞检测（与精灵组）

常用函数：
- `pygame.sprite.spritecollide(sprite, group, dokill, collided=None)`：检测单个精灵与组的碰撞。
- `pygame.sprite.groupcollide(groupa, groupb, dokilla, dokillb, collided=None)`：检测两个组之间的碰撞，返回碰撞映射。

示例（检测玩家与食物碰撞）：

```python
hits = pygame.sprite.spritecollide(player, food_group, dokill=True)
if hits:
    # 每次碰撞会把命中的食物从 food_group 中移除（dokill=True）
    player.grow()
```

### 动画精灵（多帧切换）

可以把多帧图片存在列表中，在 `update()` 中按帧或时间切换 `self.image`：

```python
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames, x, y, frame_time=100):
        super().__init__()
        self.frames = frames  # Surface 列表
        self.frame_time = frame_time  # 每帧持续毫秒
        self.current = 0
        self.image = self.frames[self.current]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_update = pygame.time.get_ticks()

    def update(self, dt=None):
        now = pygame.time.get_ticks()
        if now - self.last_update >= self.frame_time:
            self.last_update = now
            self.current = (self.current + 1) % len(self.frames)
            self.image = self.frames[self.current]
```

### 在 `main_desktop.py` 中集成建议

- 将游戏对象（玩家、食物、墙等）封装为 `Sprite`，把可移动对象放入 `moving_group`，不可移动的放 `static_group`（用于渲染或碰撞查询）。
- 使用 `sprite_group.update()` 替代在多个地方手动更新对象状态。
- 在暂停或碰撞等待时仍然可以调用 `group.draw(screen)` 来渲染当前帧。

### 小贴士

- `Group.draw()` 直接使用每个精灵的 `image` 和 `rect`，不要在 `draw()` 之外修改它们的类型。
- 若需更复杂的碰撞检测（像素级），可传入自定义 `collided` 函数给 `spritecollide`/`groupcollide`。
- 对于大量精灵，使用多个 `Group`（按用途分组）有助于优化更新和碰撞查询。

### Sprite 与普通 Rect 的区别

- 关注点：`Rect` 只存储位置尺寸并提供几何运算；`Sprite` 关注“对象”，需要 `image` + `rect`，可加入组、统一更新/绘制。
- 渲染：`Rect` 本身不绘制，需手动 `draw.rect` 或 `blit`；`Sprite` 通过 `Group.draw(surface)` 用 `image`+`rect` 自动批量绘制。
- 更新：`Rect` 没有生命周期方法；`Sprite` 可自定义 `update()`，`Group.update()` 会统一调用。
- 组织管理：`Sprite` 可被多个 `Group` 管理，便于批量碰撞、批量隐藏/显示；`Rect` 只是数据，需自己管理集合。
- 碰撞：`Rect` 提供 `colliderect`/`collidepoint` 等几何检测；`Sprite` 依然用 `rect` 做检测，但可直接用 `spritecollide`、`groupcollide` 针对组批量检测。

| 对比项 | Rect | Sprite + Group |
|--------|------|----------------|
| 数据 | 位置/尺寸 | image + rect + 其它状态 |
| 绘制 | 需手写 `draw.rect`/`blit` | `group.draw(surface)` 自动批量绘制 |
| 更新 | 无生命周期 | `update()` + `group.update()` 统一调用 |
| 组织 | 手工维护列表 | 可加入/移出多个 Group，便于分层分批 |
| 碰撞 | `colliderect` 等 | `spritecollide` / `groupcollide` 批量检测 |

#### 实战对比示例

- 只用 Rect（手动更新+绘制）：

```python
rects = [pygame.Rect(100, 100, 32, 32)]

for r in rects:
    r.x += 2  # 手动更新
    pygame.draw.rect(screen, (0, 200, 0), r)  # 手动绘制
```

- 用 Sprite + Group（统一更新+绘制）：

```python
class Block(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        self.rect.x += 2  # 统一由 group.update() 调用

blocks = pygame.sprite.Group()
blocks.add(Block(pygame.Surface((32, 32)), (100, 100)))

blocks.update()      # 批量更新
blocks.draw(screen)  # 批量绘制
```

选择原则：
- 只需要简单碰撞/定位且对象很少 → 用 `Rect` 即可。
- 需要批量绘制、统一更新、分层管理或大量对象 → 用 `Sprite` + `Group`。

## 11. Map Editor 使用笔记

基于 `mapeditor.py` 的 50×50 网格地图编辑器，方块大小 16px，保存到 `map.json`。

### 启动

```bash
python mapeditor.py
```

### 操作

| 操作 | 功能 |
|------|------|
| 左键（按住拖动） | 放置墙壁（值置为 1），同时自动保存 `map.json` |
| 右键（按住拖动） | 删除墙壁（值置为 0），实时刷新，但不自动保存 |
| S | 手动保存地图到 `map.json` |
| C | 清空全部墙壁并重绘边界（调用 `draw_bound_wall`） |
| ESC / 关闭窗口 | 退出并保存一次 |

### 显示与网格
- 画面尺寸 800×800，网格线用于定位；地图渲染使用 `assets/wall.png`。
- `draw_map()` 逐格绘制值为 1 的单元。

### 边界与清空
- `draw_bound_wall()` 会把四周一圈设为墙，并立即绘制（在按 C 清空后调用）。
- 默认加载已有 `map.json`；如文件缺失则使用全 0 地图。

### 保存/加载要点
- `save_map()` 使用 `json.dump` 覆盖写入；异常会打印“保存失败”。
- 退出（QUIT 事件）前会自动保存一次；右键删除后若需持久化请按 S。

### 与游戏联动
- 运行 `main_desktop.py` 时会从同一 `map.json` 读取；编辑后无需额外配置即可生效。
