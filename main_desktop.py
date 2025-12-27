import pygame
import sys
from pygame.locals import QUIT, K_w, K_s, K_a, K_d, K_ESCAPE, K_SPACE
import random


class Direction:
    """表示蛇的移动方向的枚举类"""
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Snake:
    """管理蛇的类"""
    def __init__(self, block_size):
        self.block_size = block_size
        self.blocks = []
        self.blocks_length = 2
        self.blocks.append((19, 15))  # 蛇身
        self.blocks.append((20, 15))  # 蛇头
        self.current_direction = Direction.RIGHT
        self.right_image = pygame.image.load('assets/right_1.png')
        self.left_image = pygame.image.load('assets/left_1.png')
        self.up_image = pygame.image.load('assets/up_1.png')
        self.down_image = pygame.image.load('assets/down_1.png')
        self.body_image = pygame.image.load('assets/body.png')
        # 动画图片
        self.right_image_2 = pygame.image.load('assets/right_2.png')
        self.left_image_2 = pygame.image.load('assets/left_2.png')
        self.up_image_2 = pygame.image.load('assets/up_2.png')
        self.down_image_2 = pygame.image.load('assets/down_2.png')
        self.current_head_image = self.right_image
        self.animation_frame = 10  # 每隔多少帧切换一次图片
        self.current_frame = 0

    def move(self):
        if self.current_direction == Direction.RIGHT:
            move = (1, 0)
        elif self.current_direction == Direction.LEFT:
            move = (-1, 0)
        elif self.current_direction == Direction.UP:
            move = (0, -1)
        else:
            move = (0, 1)
        head = self.blocks[-1]
        new_head = (head[0] + move[0], head[1] + move[1])
        self.blocks.append(new_head)
        if len(self.blocks) > self.blocks_length:
            del self.blocks[0]

    def draw(self, screen):
        for i, (x, y) in enumerate(self.blocks):
            pixel_x = x * self.block_size
            pixel_y = y * self.block_size
            if i == len(self.blocks) - 1:  # 蛇头
                self.current_frame += 1
                if self.current_frame >= self.animation_frame:
                    self.current_frame = 0
                    if self.current_direction == Direction.RIGHT:
                        self.current_head_image = (
                            self.right_image_2 if self.current_head_image == self.right_image else self.right_image
                        )
                    elif self.current_direction == Direction.LEFT:
                        self.current_head_image = (
                            self.left_image_2 if self.current_head_image == self.left_image else self.left_image
                        )
                    elif self.current_direction == Direction.UP:
                        self.current_head_image = (
                            self.up_image_2 if self.current_head_image == self.up_image else self.up_image
                        )
                    elif self.current_direction == Direction.DOWN:
                        self.current_head_image = (
                            self.down_image_2 if self.current_head_image == self.down_image else self.down_image
                        )
                screen.blit(self.current_head_image, (pixel_x, pixel_y))
            else:
                screen.blit(self.body_image, (pixel_x, pixel_y))


class Berry:
    """Berry类，表示游戏中的食物"""

    def __init__(self, block_size, x, y):
        self.block_size = block_size
        self.image = pygame.image.load('assets/berry.png')
        self.position = (x, y)

    def draw(self, surface):
        rect = self.image.get_rect()
        rect.left = self.position[0] * self.block_size
        rect.top = self.position[1] * self.block_size
        surface.blit(self.image, rect)


class Button:
    def __init__(self, x, y, width, height, text, font_size=32,
                 text_color=(255, 255, 255), color=(0, 160, 0), hover_color=(0, 190, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.color = color
        self.hover_color = hover_color

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        bg = self.hover_color if self.is_hovered(mouse_pos) else self.color
        pygame.draw.rect(surface, bg, self.rect, border_radius=6)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)


class Game:
    """管理游戏的类"""
    def __init__(self):
        pygame.init()
        self.snake = Snake(block_size=16)
        self.berry = Berry(block_size=16, x=10, y=10)  # 食物对象
        self.clock = pygame.time.Clock()
        # 设置屏幕尺寸
        self.block_size = 16
        self.bg_color = (0, 0, 0)
        screen_width = self.block_size * 50
        screen_height = self.block_size * 50
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("SNAKE贪吃蛇游戏")

        # 初始化其他游戏元素，如食物、音乐等
        self.turn = pygame.mixer.Sound('assets/step.wav')
        self.hit = pygame.mixer.Sound('assets/hit.wav')
        self.point = pygame.mixer.Sound('assets/point.wav')

        self.wall_image = pygame.image.load('assets/wall.png')
        self.logic_fps = 10
        self.fps = 60
        # 将渲染帧率与逻辑帧率解耦：渲染 60 FPS，逻辑 10 FPS
        self.logic_interval_ms = 1000 // self.logic_fps
        self.last_logic_time = pygame.time.get_ticks()

        self.game_active = False  # 游戏是否进行中的标志
        self.active = True

        # 创建开始按钮
        self.play_button = Button(x=screen_width//2 - 50, y=screen_height//2 
                                  - 25, width=100, height=50, text="PLAY", font_size=40)



    
    def check_events(self):
        # 事件处理：优先处理一次性事件（键按下、鼠标点击、退出等）
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                # 空格键：在未开始时启动游戏
                if event.key == K_SPACE and not self.game_active:
                    self.game_active = True
                    # 重置游戏状态
                    self.snake = Snake(block_size=16)
                    self.berry = Berry(block_size=16, x=10, y=10)
                    self.last_logic_time = pygame.time.get_ticks()
                elif event.key == K_ESCAPE:
                    # ESC：退出游戏
                    pygame.quit()
                else:
                    self._handle_input(event)

    def _handle_input(self, event):
            if event.key == K_d and self.snake.current_direction != Direction.LEFT:
                self.snake.current_direction = Direction.RIGHT
                self.turn.play()

            elif event.key == K_a and self.snake.current_direction != Direction.RIGHT:
                self.snake.current_direction = Direction.LEFT
                self.turn.play()
            elif event.key == K_w and self.snake.current_direction != Direction.DOWN:
                self.snake.current_direction = Direction.UP
                self.turn.play()

            elif event.key == K_s and self.snake.current_direction != Direction.UP:
                self.snake.current_direction = Direction.DOWN
                self.turn.play()

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.is_hovered(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True
            # 重置游戏状态
            self.snake = Snake(block_size=16)
            self.berry = Berry(block_size=16, x=10, y=10)
            self.last_logic_time = pygame.time.get_ticks()

    def draw(self):
        # 绘制游戏元素
        self.snake.draw(self.screen)
        self.berry.draw(self.screen)

    def draw_walls(self):
        # 绘制墙壁
        for x in range(0, self.screen.get_width(), self.block_size):
            self.screen.blit(self.wall_image, (x, 0))
            self.screen.blit(self.wall_image, (x, self.screen.get_height() - self.block_size))
        for y in range(0, self.screen.get_height(), self.block_size):
            self.screen.blit(self.wall_image, (0, y))
            self.screen.blit(self.wall_image, (self.screen.get_width() - self.block_size, y))

    def check_collisions(self):
        # 检查碰撞逻辑
        # 碰撞检测：撞到围墙即结束
        head = self.snake.blocks[-1]
        if head[0] <= 0 or head[0] >= (self.screen.get_width() // self.block_size) - 1 or \
              head[1] <= 0 or head[1] >= (self.screen.get_height() // self.block_size) - 1:
            game_over_message = "Game Over! You hit the wall."
            print(game_over_message)
            self.game_active = False
            # 碰撞检测：撞到自己即结束
        if head in self.snake.blocks[:-1]:
            print("Game Over! You ran into yourself.")
            self.game_active = False
            self.hit.play()
        # 碰撞检测：吃到食物
        if head == self.berry.position:
            self.snake.blocks_length += 1 # 增加蛇的长度
            self.point.play() # 播放得分音效
            # 重新生成食物位置
            while True:
                new_x = random.randint(2, (self.screen.get_width() // self.block_size) - 2)
                new_y = random.randint(2, (self.screen.get_height() // self.block_size) - 2)
                if (new_x, new_y) not in self.snake.blocks:
                    self.berry.position = (new_x, new_y)
                    break



    def main_loop(self):
        while self.active:
            if not self.game_active:
                self.screen.fill(self.bg_color)
                self.play_button.draw(self.screen)
                self.check_events()
                self.draw_walls()
                pygame.display.flip()
            else:
                self.check_events()
                current_time = pygame.time.get_ticks()
                elapsed = current_time - self.last_logic_time
                # 逻辑更新按固定间隔执行，可累积处理落后的逻辑帧
                while elapsed >= self.logic_interval_ms:
                    self.snake.move()
                    self.check_collisions()
                    self.last_logic_time += self.logic_interval_ms
                    elapsed -= self.logic_interval_ms

                self.screen.fill(self.bg_color)  # 清屏
                self.draw_walls()
                self.draw()
                pygame.display.flip()
                self.clock.tick(self.fps)

if __name__ == "__main__":
    game = Game()
    game.main_loop()
