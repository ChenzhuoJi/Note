class GameStats:
    """跟踪游戏的统计数据"""
    
    def __init__(self,ai_game) -> None:
        """初始化游戏数据"""
        self.settings=ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        self.ships_left=self.settings.ship_limit
        
