# from tkinter import W
import pygame
from sys import exit
import json

class MapEditor:
    def __init__(self, map_file):
        """
        MapEditor类的初始化方法，用于创建地图编辑器实例并加载地图数据。
        """
        pygame.init()
        self.filename = map_file
        self.map_data = [[0 for _ in range(50)] for _ in range(50)] # 创建一个50x50的二维列表，用于存储地图数据
        self.load_map()
        screen_width = 800
        screen_height = 800
        self.GRID_COLOR = (100, 100, 100)
        self.block_size = 16
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.wall_img = pygame.image.load("assets/wall.png").convert_alpha()
        self.wall_rect = self.wall_img.get_rect()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Map Editor")

    def check_events(self):
        """
        处理用户输入，并更新地图数据。
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save_map() # 保存地图数据
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标点击
                x, y = event.pos # 获取鼠标点击的位置
                row = y // self.block_size
                col = x // self.block_size
                self.map_data[row][col] = 1 # 将点击位置的地图数据设置为1，即添加墙壁
                self.draw_map() # 绘制地图，将地图数据渲染到屏幕上
            elif event.type == pygame.KEYDOWN: # 键盘按键
                if event.key == pygame.K_s: # 按下S键保存地图数据
                    self.save_map()
                elif event.key == pygame.K_c: # 按下C键清除所有墙壁
                    self.map_data = [[0 for _ in range(50)] for _ in range(50)]
                    self.draw_bound_wall() # 绘制地图边界墙壁
                    self.draw_map()

        if pygame.mouse.get_pressed()[2]: # 鼠标右键点击
            x, y = pygame.mouse.get_pos()
            row = y // self.block_size
            col = x // self.block_size
            self.map_data[row][col] = 0 # 将点击位置的地图数据设置为0，即删除墙壁
            self.draw_map() # 绘制地图，将地图数据渲染到屏幕上
        elif pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            row = y // self.block_size
            col = x // self.block_size
            self.map_data[row][col] = 1 # 将点击位置的地图数据设置为1，即添加墙壁 
            self.save_map() # 保存地图数据
    
    
    def add_grid(self):
        """
        绘制网格，用于辅助用户绘制地图。
        """
        for i in range(50):
            pygame.draw.line(self.screen, self.GRID_COLOR, (0, i * self.block_size), (800, i * self.block_size))
            pygame.draw.line(self.screen, self.GRID_COLOR, (i * self.block_size, 0), (i * self.block_size, 800))
    
    def draw_bound_wall(self):
        """
        绘制地图边界墙壁,并添加到地图数据中
        """
        for i in range(50):
            self.map_data[i][0] = 1
            self.map_data[i][49] = 1
            self.map_data[0][i] = 1
            self.map_data[49][i] = 1
            self.screen.blit(self.wall_img, (i * self.block_size, 0))
            self.screen.blit(self.wall_img, (i * self.block_size, 800 - self.block_size))
            self.screen.blit(self.wall_img, (0, i * self.block_size))
            self.screen.blit(self.wall_img, (800 - self.block_size, i * self.block_size))
            self.wall_rect.topleft = (i * self.block_size, 0)
            self.screen.blit(self.wall_img, self.wall_rect)
            self.wall_rect.topleft = (i * self.block_size, 800 - self.block_size)
            self.screen.blit(self.wall_img, self.wall_rect)
            self.wall_rect.topleft = (0, i * self.block_size)
            self.screen.blit(self.wall_img, self.wall_rect)
            self.wall_rect.topleft = (800 - self.block_size, i * self.block_size)
            self.screen.blit(self.wall_img, self.wall_rect)

    def draw_map(self):
        """
        绘制地图，将地图数据渲染到屏幕上。
        """
        for row in range(50):
            for col in range(50):
                if self.map_data[row][col] == 1:
                    self.screen.blit(self.wall_img, (col * self.block_size, row * self.block_size))

    def save_map(self):
        """
        保存地图数据到文件中。
        """
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.map_data, f)
            print(f"地图已保存到 {self.filename}")
        except Exception as e:
            print(f"保存失败: {e}")

    def load_map(self):
        """
        从文件中加载地图数据。
        """
        try:
            with open(self.filename, "r") as f:
                self.map_data = json.load(f)
        except Exception as e:
            print(f"加载地图失败: {e}")




    def run_map_editor(self):
        """
        运行地图编辑器的主循环，处理用户输入并更新地图数据。
        """
        while True:
            self.screen.fill((0, 0, 0))
            self.check_events()
            self.add_grid()
            self.draw_map() # 绘制地图，将地图数据渲染到屏幕上
            self.clock.tick(60) # 限制循环频率为60次/秒
            pygame.display.update()





if __name__ == "__main__":
    editor = MapEditor("map.json")
    editor.run_map_editor()

    