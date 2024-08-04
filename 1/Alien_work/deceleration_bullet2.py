from typing import Any
import pygame
from pygame.sprite import Sprite
class DCLBullet2(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.dclbullet_color
        
        #在（0，0）出创建一个子弹矩形，并设置其正确位置
        self.rect=pygame.Rect(0,0,self.settings.dclbullet_width,
                                self.settings.dclbullet_height)
        self.rect.midbottom=ai_game.ship.rect.midtop
        
        
        #用浮点数宝石子弹的位置
        self.y=float(self.rect.y)
            
    def update(self):
        """向上移动子弹"""
        #更新子弹的位置
        self.y-=self.settings.dclbullet_speed
        #更新表示子弹rect的位置
        self.rect.y=self.y
        
    def draw_dclbullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)