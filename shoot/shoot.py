import sys
from time import sleep
import pygame

from setting import Settings

class Shoot:
    def __init__(self):#1
        """初始化"""
        pygame.init()
        #clock:时钟刻
        self.clock=pygame.time.Clock()
        
        #游戏中参与的对象
        self.settings=Settings()
        
        #display:创建屏幕
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        #屏幕颜色
        self.screen.fill(self.settings.bg_color) 
        
        
    def run_game(self):
        while True:
            self.clock.tick(60)
            
    
    
    def car(self):
        self.car()
        
        
        
if __name__=='__main__':
    #创建游戏并运行
    ai=Shoot()
    ai.run_game()