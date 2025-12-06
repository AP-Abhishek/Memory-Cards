import pygame as pg
import sys
from utils import get_resource_path

class Game:
    def __init__(self):
        # Game Attributes
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.running = True
        self.is_game_started = False

        self.clock = pg.time.Clock()

        # Images
        self.logo = pg.image.load(get_resource_path(r"./assets/Logo.png"))
        self.bg = pg.transform.rotate(pg.transform.scale_by(pg.image.load(get_resource_path(r"./assets/Game-BG.png")), 0.5), 90.0)

        # Function calls
        self.create_window()
        self.mainloop()

    def create_window(self):
        self.window = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption("Memory Cards")
        pg.display.set_icon(self.logo)

    def handle_blit(self):
        self.window.blit(self.bg, (0,0))

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit_game()

    def mainloop(self):
        while self.running:
            self.clock.tick(60)
            self.handle_blit()
            self.handle_events()
            pg.display.update()

    def quit_game(self):
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    pg.init()
    Game()
    pg.quit()