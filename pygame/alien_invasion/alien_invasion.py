import sys     # 加载模块
import pygame  # 加载模块
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    while True:
        gf.check_events(ship)
        ship.update()
run_game()
