import pygame
from bullet import Bullet

class NMBullet(Bullet):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)