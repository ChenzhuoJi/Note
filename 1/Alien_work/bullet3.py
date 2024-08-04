import pygame
from nm_bullet import Bullet
class Bullet3(Bullet):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)
        self.rect.midright=ai_game.ship.rect.midleft
    def update(self):
        """向上移动子弹"""
        #更新子弹的位置
        self.y-=5
        
        #更新表示子弹rect的位置
        self.rect.y=self.y
        self.rect.x=self.x