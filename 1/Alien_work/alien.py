import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        """初始化外星人及其位置"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        #加载外星人的图形并设置其rect属性
        self.image=pygame.image.load('images/狗头JPEG.webp')
        self.rect=self.image.get_rect()
        
        #每个外星人都在最初的屏幕左上角附近
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        #存储外星人的实施坐标
        self.x=float(self.rect.x)
        
    def check_edges(self):
        """如果外星人位于屏幕边缘,返回ture"""   
        screen_rect=self.screen.get_rect()
        return(self.rect.right>=screen_rect.right) or (self.rect.left<=0)  
        
    def update(self):
        """向右移动外星人"""
        self.x+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x=self.x
        