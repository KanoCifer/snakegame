from math import e
import pygame
import sys
from pygame.locals import QUIT, K_w, K_s, K_a, K_d, K_ESCAPE, K_SPACE
import random
import json
import time


class Direction:
    """表示蛇的移动方向的枚举类"""
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Board:
    """管理游戏板的类"""
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.highest_score = self.load_highest_score()
        self.lives_img = pygame.image.load('assets/lives.png').convert_alpha()
        self.lives_img = pygame.transform.scale(self.lives_img, (24, 24))
        self.lives_rect = self.lives_img.get_rect()
        self.lives_rect.center= (700, 10)

    def draw_lives(self, screen, lives):
        # 绘制剩余生命值，从外部传入生命值
        for i in range(lives):
            x = self.lives_rect.x + i * (self.lives_rect.width + 5)
            y = self.lives_rect.y
            screen.blit(self.lives_img, (x, y))

    def score_display(self, screen, snake):
        # 显示分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {snake.blocks_length - 2}", 
                                 True, (255, 255, 255))
        score_rect = score_text.get_rect(center =(self.width // 2, 20))
        screen.blit(score_text, score_rect)
    
    def highest_score_display(self, screen, highest_score):
        # 显示最高分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Highest Score: {highest_score}", 
                                 True, (255, 255, 255))
        score_rect = score_text.get_rect(center =(self.width // 2, 60))
        screen.blit(score_text, score_rect)

    def save_highest_score(self, score):
        # 保存最高分数到文件
        try:
            with open('highest_score.txt', 'r') as f:
                highest_score = int(f.read())
        except (FileNotFoundError, ValueError):
            highest_score = 0

        if score > highest_score:
            with open('highest_score.txt', 'w') as f:
                f.write(str(score))


    def load_highest_score(self):
        # 从文件加载最高分数
        try:
            with open('highest_score.txt', 'r') as f:
                highest_score = int(f.read())
        except (FileNotFoundError, ValueError):
            highest_score = 0
        return highest_score
    




class Snake:
    """管理蛇的类"""
    def __init__(self, block_size):
        self.block_size = block_size
        self.blocks = []
        self.blocks_length = 2
        self.blocks.append((19, 15))  # 蛇身
        self.blocks.append((20, 15))  # 蛇头
        self.current_direction = Direction.RIGHT
        self.right_image = pygame.image.load('assets/right_1.png').convert_alpha()
        self.left_image = pygame.image.load('assets/left_1.png').convert_alpha()
        self.up_image = pygame.image.load('assets/up_1.png').convert_alpha()
        self.down_image = pygame.image.load('assets/down_1.png').convert_alpha()
        self.body_image = pygame.image.load('assets/body.png').convert_alpha()
        # 动画图片
        self.right_image_2 = pygame.image.load('assets/right_2.png').convert_alpha()
        self.left_image_2 = pygame.image.load('assets/left_2.png').convert_alpha()
        self.up_image_2 = pygame.image.load('assets/up_2.png').convert_alpha()
        self.down_image_2 = pygame.image.load('assets/down_2.png').convert_alpha()
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
        self.image = pygame.image.load('assets/berry.png').convert_alpha()
        self.position = (x, y)

    def draw(self, surface):
        rect = self.image.get_rect()
        rect.left = self.position[0] * self.block_size
        rect.top = self.position[1] * self.block_size
        surface.blit(self.image, rect)


class Button:
    """按钮类，用于创建可点击的按钮"""
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
        # 先创建渲染窗口，再加载依赖 convert_alpha 的贴图
        self.block_size = 16
        self.bg_color = (0, 0, 0)
        self.screen_width = self.block_size * 50
        self.screen_height = self.block_size * 50
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.map_data = []
        pygame.display.set_caption("SNAKE贪吃蛇游戏")

        # 加载地图数据
        self.load_map('map.json')

        self.snake = Snake(block_size=16)
        self.berry = Berry(block_size=16, x=10, y=10)  # 食物对象
        self.board = Board(self.screen_width, self.screen_height, self.block_size)
        self.clock = pygame.time.Clock()

        # 初始化生命值
        self.lives = 3

        # 初始化其他游戏元素，如食物、音乐等
        self.turn = pygame.mixer.Sound('assets/step.wav')
        self.hit = pygame.mixer.Sound('assets/hit.wav')
        self.point = pygame.mixer.Sound('assets/point.wav')
        self.game_bg_music = pygame.mixer.Sound('assets/game_bgm.mp3')
        self.game_bg_music.set_volume(0.3)


        self.wall_image = pygame.image.load('assets/wall.png').convert_alpha()
        self.wall_rect = self.wall_image.get_rect()
        self.logic_fps = 10
        self.fps = 60
        # 将渲染帧率与逻辑帧率解耦：渲染 60 FPS，逻辑 10 FPS
        self.logic_interval_ms = 1000 // self.logic_fps
        self.last_logic_time = pygame.time.get_ticks()

        self.game_active = False  # 游戏是否进行中的标志
        self.active = True
        self.music_playing = False
        
        # 碰撞暂停相关
        self.collision_pause = False  # 是否处于碰撞暂停状态
        self.collision_pause_start = 0  # 碰撞暂停开始时间
        self.collision_pause_duration = 1000  # 暂停持续时间（毫秒）

        # 创建开始按钮
        self.play_button = Button(x=self.screen_width//2 - 50, y=self.screen_height//2 
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
                    self._start_game()
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
            self._start_game()

    def _start_game(self):
        # 重置游戏状态并启动背景音乐
        self.game_active = True
        self.snake = Snake(block_size=16)
        self.berry = Berry(block_size=16, x=10, y=10)
        self.last_logic_time = pygame.time.get_ticks()
        self._play_music_once()
    
    def _reset_game(self):
        # 完全重置游戏状态，包括生命值
        self.game_active = False
        self.lives = 3
        self.snake = Snake(block_size=16)
        self.berry = Berry(block_size=16, x=10, y=10)
        self._stop_music()
    
    def _current_score(self):
        # 当前得分（蛇身长度减去初始两节）
        return max(self.snake.blocks_length - 2, 0)
    
    def _update_high_score(self):
        score = self._current_score()
        if score > self.board.highest_score:
            self.board.highest_score = score
            self.board.save_highest_score(score)

    def _play_music_once(self):
        if not self.music_playing: # 仅当音乐未播放时启动
            channel = self.game_bg_music.play(-1, fade_ms=500) # 循环播放背景音乐
            if channel is not None: # 播放成功
                self.music_playing = True

    def _stop_music(self):
        if self.music_playing:
            self.game_bg_music.stop()
            self.music_playing = False

    def draw(self):
        # 绘制游戏元素
        self.snake.draw(self.screen)
        self.berry.draw(self.screen)

    def load_map(self, filename):
        """
        从文件中加载地图数据。
        """
        try:
            with open(filename, "r") as f:
                self.map_data = json.load(f)
        except Exception as e:
            print(f"加载地图失败: {e}")

    def draw_map(self):
        """
        绘制地图，将地图数据渲染到屏幕上。
        """
        # 检查地图数据是否已加载
        if not self.map_data:
            print("警告：地图数据未加载")
            return
            
        for row in range(50):
            for col in range(50):
                if self.map_data[row][col] == 1:
                    self.wall_rect.topleft = (col * self.block_size, row * self.block_size)
                    self.screen.blit(self.wall_image, self.wall_rect)

    def check_collisions(self):
        head = self.snake.blocks[-1]

        # 撞墙：减少生命值
        if self.map_data[head[1]][head[0]] == 1:
            self._handle_collision()
            return

        # 撞到自己：减少生命值
        if head in self.snake.blocks[:-1]:
            self._handle_collision()
            return

        # 吃到食物：加长并重新生成食物, 确保新位置不在蛇身或墙内
        if head == self.berry.position:
            self.snake.blocks_length += 1
            self.point.play()
            # 即时更新最高分
            self._update_high_score()
            while True:
                new_x = random.randint(2, (self.screen.get_width() // self.block_size) - 2)
                new_y = random.randint(2, (self.screen.get_height() // self.block_size) - 2)
                if (new_x, new_y) not in self.snake.blocks and self.map_data[new_y][new_x] == 0:
                        self.berry.position = (new_x, new_y)
                        break
                else:
                    continue

    def _handle_collision(self):
        """处理碰撞事件，开始暂停计时"""
        # 碰撞前先保存最高分（因为之后蛇会被重置）
        self._update_high_score()
        self.lives -= 1
        self.hit.play()
        self.collision_pause = True
        self.collision_pause_start = pygame.time.get_ticks()
    
    def _finish_collision_pause(self):
        """暂停结束后的处理"""
        self.collision_pause = False
        
        # 如果生命值耗尽，游戏结束
        if self.lives <= 0:
            self._update_high_score()
            self.game_active = False
            self._reset_game()
        else:
            # 如果还有生命值，重置蛇的位置但继续游戏
            self.snake = Snake(block_size=16)
            self.berry = Berry(block_size=16, x=10, y=10)
            self.last_logic_time = pygame.time.get_ticks()


    def score_display(self):
        font = pygame.font.Font(None, 32)
        score = self._current_score()
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        high_text = font.render(f"High: {self.board.highest_score}", True, (255, 215, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(high_text, (10, 42))


    def main_loop(self):
        # 主游戏循环
        while self.active:
            # 游戏未开始时显示开始按钮
            if not self.game_active:
                self.screen.fill(self.bg_color)
                self.play_button.draw(self.screen)
                self.check_events()
                self.draw_map()
                self.score_display()
                self.board.draw_lives(self.screen, self.lives)  # 传入生命值
                self._stop_music()
                pygame.display.update()
            else:
                # 游戏进行中
                self.check_events()
                current_time = pygame.time.get_ticks()
                
                # 检查是否处于碰撞暂停状态
                if self.collision_pause:
                    # 暂停期间仍然渲染画面，但不更新游戏逻辑
                    if current_time - self.collision_pause_start >= self.collision_pause_duration:
                        self._finish_collision_pause()
                else:
                    # 正常游戏逻辑
                    elapsed = current_time - self.last_logic_time
                    # 逻辑更新按固定间隔执行，可累积处理落后的逻辑帧
                    while elapsed >= self.logic_interval_ms:
                        self.snake.move()
                        self.check_collisions()
                        # 更新最后逻辑时间
                        self.last_logic_time += self.logic_interval_ms
                        elapsed -= self.logic_interval_ms

                self.screen.fill(self.bg_color)  # 清屏

                self._play_music_once()
                self.draw_map()
                self.score_display()
                self.board.draw_lives(self.screen, self.lives)  # 传入生命值
                self.draw()
                pygame.display.update()
                self.clock.tick(self.fps)

if __name__ == "__main__":
    game = Game()
    game.main_loop()