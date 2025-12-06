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
        self.is_game_ended = False
        self.cards = []
        self.back_card = None
        self.flip_count = 0
        self.cards_fipped = 0

        self.clock = pg.time.Clock()
        self.font = pg.font.Font(get_resource_path("./assets/Font/CaveatBrush.ttf"), 28)

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

            if self.is_game_ended:
                dialog_width = 300
                dialog_height = 200
                dialog_rect = pg.Rect(
                    (self.SCREEN_WIDTH // 2) - (dialog_width // 2),
                    (self.SCREEN_HEIGHT // 2) - (dialog_height // 2),
                    dialog_width,
                    dialog_height
                )
                dialog_box_rect = pg.draw.rect(
                    self.window,
                    (200, 200, 225),
                    dialog_rect,
                    border_radius=5
                )
                
                won_text = self.font.render("You Won", True, (0, 180, 0))
                play_again_text = self.font.render("Play Again", True, (0, 0, 0))
                home_text = self.font.render("Back", True, (0, 0, 0))
                
                btn_width = 200
                btn_height = 50
                
                play_again_rect = pg.Rect(
                    (self.SCREEN_WIDTH // 2) - (btn_width // 2),
                    (self.SCREEN_HEIGHT // 2) - (btn_height // 2),
                    btn_width,
                    btn_height
                )
                home_rect = pg.Rect(
                    (self.SCREEN_WIDTH // 2) - (btn_width // 2),
                    (self.SCREEN_HEIGHT // 2) - (btn_height // 2) + play_again_rect.height + 10,
                    btn_width,
                    btn_height
                )

                self.play_again_btn_rect = pg.draw.rect(
                    self.window,
                    (0, 255, 0),
                    play_again_rect,
                    border_radius=20
                )
                self.home_btn_rect = pg.draw.rect(
                    self.window,
                    (255, 0, 0),
                    home_rect,
                    border_radius=20
                )

                self.window.blit(won_text, (dialog_box_rect.x + dialog_box_rect.width // 2 - won_text.get_width() // 2, dialog_box_rect.y + 20))
                self.window.blit(play_again_text, play_again_text.get_rect(center=self.play_again_btn_rect.center))
                self.window.blit(home_text, home_text.get_rect(center=self.home_btn_rect.center))

        else:
            # Logo
            logo = pg.transform.scale_by(self.logo, 0.5)
            self.window.blit(logo, ((self.SCREEN_WIDTH // 2) - (logo.get_width() // 2), (self.SCREEN_HEIGHT // 2) - (logo.get_height() // 2) - 130))

            # Menu Texts
            play_text = self.font.render("Play", True, (0, 0, 0))
            exit_text = self.font.render("Exit", True, (0, 0, 0))

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

    def check_flips(self):
        if self.flip_count == 2:
            if self.card1.card_name == self.card2.card_name:
                self.flip_count = 0
                self.flip_timer = None
                self.cards_fipped += 2
                self.check_win()
                return
            elif pg.time.get_ticks() - self.flip_timer >= 500:
                self.card1.flip_card()
                self.card2.flip_card()
                self.flip_count = 0

    def check_win(self):
        if not self.cards_fipped == len(self.cards):
            return
        self.is_game_ended = True

    def reset_game(self):
        self.is_game_started = True
        self.is_game_ended = False
        self.cards = []
        self.back_card = None
        self.flip_count = 0
        self.cards_fipped = 0
        self.create_cards()

    def back_home(self):
        self.is_game_started = False
        self.is_game_ended = False
        self.cards = []
        self.back_card = None
        self.flip_count = 0
        self.cards_fipped = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit_game()
            elif self.is_game_started:
                if event.type == pg.MOUSEBUTTONDOWN:
                    click_point = pg.mouse.get_pos()
                    for card in self.cards:
                        if card.rect.collidepoint(click_point):
                            if not card.is_flipped and self.flip_count < 2:
                                card.flip_card()
                                self.flip_count += 1
                                if self.flip_count == 1:
                                    self.card1 = card
                                if self.flip_count == 2:
                                    self.card2 = card
                                    self.flip_timer = pg.time.get_ticks()
                if self.is_game_ended:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if self.play_again_btn_rect.collidepoint(pg.mouse.get_pos()):
                            self.reset_game()
                            return
                        if self.home_btn_rect.collidepoint(pg.mouse.get_pos()):
                            self.back_home()
                            return
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
            self.check_flips()
            pg.display.update()

    def quit_game(self):
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    pg.init()
    Game()
    pg.quit()