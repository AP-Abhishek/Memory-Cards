import pygame as pg

class Card:
    def __init__(self, name, path):
        self.card_name = name
        self.img = pg.transform.scale_by(pg.image.load(path), 0.09)
        self.rect = None
        self.is_flipped = False

    def flip_card(self):
        self.is_flipped = True
