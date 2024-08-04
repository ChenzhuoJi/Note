import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from deceleration_bullet import DCLBullet
from bullet2 import Bullet2
from bullet3 import Bullet3
from bullet4 import Bullet4
from deceleration_bullet2 import DCLBullet2

class AlienInvasion:
    def __init__(self):#1
        """初始化"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        

        pygame.display.set_caption("AlienInvasion")
        #创建一个存储游戏数据的实例
        self.stats=GameStats(self)
        
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.alien=pygame.sprite.Group()
        self.dclbullets=pygame.sprite.Group()
        self.bullets2=pygame.sprite.Group()
        self.bullets3=pygame.sprite.Group()
        self.bullets4=pygame.sprite.Group()
        self.dclbullets2=pygame.sprite.Group()
        self._create_fleet()
        #设置背景色
        self.screen.fill(self.settings.bg_color)    
        
    def run_game(self):#主循环2
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_bullets()
            self._update_dclbullets()
            self._update_dclbullets2()
            self._update_bullets2()
            self._update_bullets3()
            self._update_bullets4()
            self._update_screen()
            self.ship.update()
            self._update_alien()
            self.clock.tick(60)
            
    def _check_events(self):    #辅助方法：检查事件发生3
        """侦听键盘和鼠标的事件"""
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=True
                elif event.key==pygame.K_LEFT:
                    self.ship.moving_left=True
                elif event.key==pygame.K_SPACE:
                    self._fire_bullet()
                    
                elif event.key==pygame.K_UP:
                    self._fire_dclbullet()
                    self._fire_dclbullet2()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
                elif event.key==pygame.K_LEFT:
                    self.ship.moving_left=False
            
    def _fire_bullet(self):#4
        """创建一颗子弹,并将其加入编组bukkets"""
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
            new_bullet2=Bullet2(self)
            self.bullets2.add(new_bullet2)
            new_bullet3=Bullet3(self)
            self.bullets3.add(new_bullet3)
            new_bullet4=Bullet4(self)
            self.bullets4.add(new_bullet4)
    def _fire_dclbullet(self):
        new_dclbullet=DCLBullet(self)
        self.dclbullets.add(new_dclbullet)
    def _fire_dclbullet2(self):
        new_dclbullet2=DCLBullet2(self)
        self.dclbullets2.add(new_dclbullet2)
        
    def _update_bullets(self):#5
        self.bullets.update()
        
        #s删除已消失的子弹/
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        #检查是否有子弹击中了外星人
        #如果是，删除相应的子弹和外星人
        
        a= pygame.sprite.groupcollide(self.bullets,self.alien,True,True)
        
    def _update_bullets2(self):#5
        self.bullets2.update()
        
        #s删除已消失的子弹/
        for bullet2 in self.bullets2.copy():
            if bullet2.rect.bottom<=0:
                self.bullets.remove(bullet2)
        #检查是否有子弹击中了外星人
        #如果是，删除相应的子弹和外星人
        
        a= pygame.sprite.groupcollide(self.bullets2,self.alien,True,True)
        
    def _update_bullets3(self):#5
        self.bullets3.update()
        
        #s删除已消失的子弹/
        for bullet3 in self.bullets3.copy():
            if bullet3.rect.bottom<=0:
                self.bullets.remove(bullet3)
        #检查是否有子弹击中了外星人
        #如果是，删除相应的子弹和外星人
        
        a= pygame.sprite.groupcollide(self.bullets3,self.alien,True,True)

    def _update_bullets4(self):#5
        self.bullets4.update()
        
        #s删除已消失的子弹/
        for bullet4 in self.bullets4.copy():
            if bullet4.rect.bottom<=0:
                self.bullets4.remove(bullet4)
        #检查是否有子弹击中了外星人
        #如果是，删除相应的子弹和外星人
        
        a= pygame.sprite.groupcollide(self.bullets4,self.alien,True,True)

        
    def _update_dclbullets(self):
        self.dclbullets.update()
        
        for dclbullt in self.dclbullets.copy():
            if dclbullt.rect.bottom<=0:
                self.dclbullets.remove(dclbullt)
        collisons=pygame.sprite.groupcollide(self.alien,self.dclbullets,True,True)
        
    def _update_dclbullets2(self):
        self.dclbullets2.update()
        
        for dclbullt2 in self.dclbullets2.copy():
            if dclbullt2.rect.bottom<=0:
                self.dclbullets2.remove(dclbullt2)
        collisons=pygame.sprite.groupcollide(self.alien,self.dclbullets2,True,True)
            
    def _create_alien(self,x_position,y_position):#7
        """创建一个外星人并把它存储在行中"""
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.alien.add(new_alien)
        
    def _create_fleet(self):#6
        """创建一个外星人舰队"""
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        init_position=15
        while current_y<(self.settings.screen_height-init_position*alien_height):
            while current_x<(self.settings.screen_width-2*alien_width):
                self._create_alien(current_x,current_y)
                current_x+=1.3*alien_width
            current_x=alien_width
            current_y+=1.5*alien_height
        
    def _update_alien(self):#8
        """更新外形舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.alien.update() 
        #检测碰撞
        if pygame.sprite.spritecollideany(self.ship,self.alien):
            print("ship hit!!!")
            self._ship_hit()
        if not self.alien:
            self._create_fleet()
            
            
    def _check_fleet_edges(self):#9
        """在有外星人到达边缘时采取相应措施"""
        for alien in self.alien.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):#10
        """将整个外形舰队向下移动，并改变他们的方向"""
        for alien in self.alien.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1
    
    def _ship_hit(self):
        """相应飞船与外星人的碰撞"""
        #将shios_left减一
        self.stats.ships_left-=1
        
        self.bullets.empty()
        self.alien.empty()
        
        self._create_fleet()
        self.ship.center_ship()
         
        #sleep
        sleep(1)
        
    def _check_alein_bottom(self):
        """检查是否有外星人到达屏幕的下边缘"""
        for alien in self.alien.sprites():
            if alien.rect.bottom>=self.settings.screen_height:
                #像碰到飞船一样处理
                self._ship_hit()
                break
    def _update_screen(self):#11
        """更新屏幕上的图像，并切换到新屏幕 """
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for dclbullet in self.dclbullets.sprites():
            dclbullet.draw_dclbullet()
        for dclbullet2 in self.dclbullets.sprites():
            dclbullet2.draw_dclbullet()
        for bullet2 in self.bullets2.sprites():
            bullet2.draw_bullet()
        for bullet3 in self.bullets3.sprites():
            bullet3.draw_bullet()
        for bullet4 in self.bullets4.sprites():
            bullet4.draw_bullet()

        self.ship.blitme()
        self.alien.draw(self.screen)
        
        pygame.display.flip()

if __name__=='__main__':
    #创建游戏并运行
    ai=AlienInvasion()
    ai.run_game()
    