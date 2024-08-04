import pygame
from nm_bullet import Bullet
class Bullet4(Bullet):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)
        self.rect=pygame.Rect(0,self.settings.screen_width,self.settings.bullet_width,
                              self.settings.bullet_height)
        self.rect.midtop=self.rect.midtop
    def update(self):
        """向上移动子弹"""
        #更新子弹的位置
        self.y-=5
        self.x+=5
        #更新表示子弹rect的位置
        self.rect.y=self.y
        self.rect.x=self.x