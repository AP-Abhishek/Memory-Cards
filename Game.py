import pygame as pg
import sys, random
from Card import Card
from utils import get_resource_path

class Game:
    def __init__(self):
        # Game Attributes
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600

        self.running = True
        self.is_game_started = False
        self.cards = []
        self.back_card = None

        self.clock = pg.time.Clock()
        self.primary_font = pg.font.Font(get_resource_path("./assets/Font/CaveatBrush.ttf"), 28)
        self.secondary_font = pg.font.Font(get_resource_path("./assets/Font/CaveatBrush.ttf"), 18)

        # Images
        self.logo = pg.image.load(get_resource_path("./assets/Images/Logo.png"))
        self.bg = pg.transform.rotate(pg.transform.scale_by(pg.image.load(get_resource_path("./assets/Images/Game-BG.png")), 0.5), 90.0)

        # Function calls
        self.create_window()
        self.mainloop()

    def create_window(self):
        self.window = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption("Memory Cards")
        pg.display.set_icon(self.logo)

    def handle_blit(self):
        self.window.blit(self.bg, (0,0))

        if self.is_game_started:
            row = 1
            col = 1
            for card in self.cards:
                card.rect = card.img.get_rect(center=(self.SCREEN_WIDTH // 5 * row, self.SCREEN_HEIGHT // 4 * col - 80 + (40 * col)))
                if card.is_flipped:
                    self.window.blit(card.img, card.rect)
                else:
                    self.window.blit(self.back_card.img, card.rect)
                col += 1
                if col == 4:
                    col = 1
                    row += 1
        else:
            # Logo
            logo = pg.transform.scale_by(self.logo, 0.5)
            self.window.blit(logo, ((self.SCREEN_WIDTH // 2) - (logo.get_width() // 2), (self.SCREEN_HEIGHT // 2) - (logo.get_height() // 2) - 130))

            # Menu Texts
            play_text = self.primary_font.render("Play", True, (0, 0, 0))
            exit_text = self.primary_font.render("Exit", True, (0, 0, 0))

            # Buttons Dimensions
            btn_width = 200
            btn_height = 50

            # Button Rects
            play_rect = pg.Rect(
                (self.SCREEN_WIDTH // 2) - (btn_width // 2),
                (self.SCREEN_HEIGHT // 2) - (btn_height // 2) + 20,
                btn_width,
                btn_height
            )
            exit_rect = pg.Rect(
                (self.SCREEN_WIDTH // 2) - (btn_width // 2),
                (self.SCREEN_HEIGHT // 2) - (btn_height // 2) + play_rect.height + 40,
                btn_width,
                btn_height
            )

            # Drawing Rects
            self.play_btn_rect = pg.draw.rect(self.window, (0, 225, 0), play_rect, border_radius=20)
            self.exit_btn_rect = pg.draw.rect(self.window, (225, 0, 0), exit_rect, border_radius=20)

            # Bliting Rects
            self.window.blit(play_text, play_text.get_rect(center=self.play_btn_rect.center))
            self.window.blit(exit_text, exit_text.get_rect(center=self.exit_btn_rect.center))

    def create_cards(self):
        cards = ["Apple", "Grape", "Lime", "Orange", "Strawberry", "Watermelon"]

        for card in cards:
            self.cards.append(Card(card, get_resource_path(f"./assets/Images/{card}.png")))
            self.cards.append(Card(card, get_resource_path(f"./assets/Images/{card}.png")))
        
        random.shuffle(self.cards)

        self.back_card = Card("Cover", get_resource_path("./assets/Images/Back-View.png"))

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit_game()
            elif self.is_game_started:
                if event.type == pg.MOUSEBUTTONDOWN:
                    click_point = pg.mouse.get_pos()
                    for card in self.cards:
                        if card.rect.collidepoint(click_point):
                            if not card.is_flipped:
                                card.flip_card()
            else:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.play_btn_rect.collidepoint(pg.mouse.get_pos()):
                        self.is_game_started = True
                        self.create_cards()
                        return
                    if self.exit_btn_rect.collidepoint(pg.mouse.get_pos()):
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