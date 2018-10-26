import sys     # 加载模块
import pygame  # 加载模块
from settings import Settings
from ship import Ship
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()
