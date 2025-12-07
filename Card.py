import pygame as pg

class Card:
    def __init__(self, name: str, path: str, back_path: str):
        self.card_name = name
        self.img = pg.transform.scale_by(pg.image.load(path), 0.09)
        self.back = pg.transform.scale_by(pg.image.load(back_path), 0.09)
        self.rect = None
        self.is_flipped = False

    def flip_card(self):
        self.is_flipped = not self.is_flipped

    def get_card_face(self) -> pg.Surface:
        if self.is_flipped:
            return self.img
        return self.back
