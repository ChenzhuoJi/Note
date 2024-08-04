import pygame
from bullet import Bullet
class DCLBullet(Bullet):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)
        self.color=self.settings.dclbullet_color
        
        self.rect=pygame.Rect(0,0,self.settings.dclbullet_width,
                                self.settings.dclbullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop
        self.rect_2=self.rect
        self.rect_2.midtop=self.rect.midtop
    def update(self):

        self.y-=self.settings.dclbullet_speed
        self.rect.y=self.y
        self.rect_2=self.y
    def draw_dclbullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
    