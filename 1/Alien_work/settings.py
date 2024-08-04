class Settings:
    #存储设置的类
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=800
        self.screen_height=800
        self.bg_color=(239,230,230)
        
        #飞船速度
        self.ship_speed=10
        self.ship_limit=3
        
        #子弹设置
        self.bullet_width=4
        self.bullet_height=5
        self.bullet_speed=10
        self.bullet_color=(60,60,60)
        self.bullets_allowed=100
        self.dclbullet_color=(0,0,100)
        self.dclbullet_speed=10
        self.dclbullet_width=4
        self.dclbullet_height=20
        #外星人设置
        self.alien_speed=2
        self.fleet_drop_speed=45
        self.fleet_direction=1
        
        