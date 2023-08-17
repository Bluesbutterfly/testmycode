import sys
import pygame
from setting import settings
class AlienInvasion:
  def __init__(self):
    pygame.init()
    self.setting = settings()
    self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
    pygame.display.set_caption("Alien  Invasion")
  def run_game(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      self.screen.fill(self.setting.bg_color)
      pygame.display.flip()
if __name__ == '__main__':
  ai = AlienInvasion()
  ai.run_game()