from typing import Any
import pygame
from pygame.sprite import Sprite
#继承Sprite类
class Bullet(Sprite):
    """管理飞船所有子弹的类"""
    def __init__(self,ai_game) -> None:
        """在飞船但其那位置穿件衣鸽子蛋对象"""
        super().__init__()    
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color
        
        #在（0，0）出创建一个子弹矩形，并设置其正确位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,
                              self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop
        #用浮点数宝石子弹的位置 
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
    def update(self):
        """向上移动子弹"""
        #更新子弹的位置
        self.y-=self.settings.bullet_speed
        self.x-=5
        #更新表示子弹rect的位置
        self.rect.y=self.y
        self.rect.x=self.x
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        
        
        
        