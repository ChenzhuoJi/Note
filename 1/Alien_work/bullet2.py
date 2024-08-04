import pygame
from nm_bullet import Bullet
class Bullet2(Bullet):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)
        
    def update(self):
        """向上移动子弹"""
        #更新子弹的位置
        self.y-=self.settings.bullet_speed
        self.x+=5
        #更新表示子弹rect的位置
        self.rect.y=self.y
        self.rect.x=self.x