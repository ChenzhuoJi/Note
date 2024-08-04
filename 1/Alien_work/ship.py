import pygame

class Ship:
    """manage the ship"""
    def __init__(self,ai_game):
        """initialize the ship and set its initial position"""
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        
        self.screen_rect=ai_game.screen.get_rect()
        
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        
        #每艘新飞船都放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom
        #在飞船的属性x中存储一个浮点数
        self.x=float(self.rect.x)
        
        #移动标志（飞船一开始不移动）
        self.moving_right=False
        self.moving_left=False
        
    def update(self):
        """根据移动标志调整飞船位置"""
        #更新飞船的属性x的值，而不是其外接矩形属性x的值
        #同时避免飞船出界
        if self.moving_right:
            self.x+=self.settings.ship_speed
        if self.moving_left:
            self.x-=self.settings.ship_speed
        if self.moving_right and self.rect.right>self.screen_rect.right:
            self.x-=self.settings.ship_speed
        if self.moving_left and self.rect.left<0:
            self.x+=self.settings.ship_speed
        self.rect.x=self.x
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        #在飞船的属性x中存储一个浮点数
        self.x=float(self.rect.x)