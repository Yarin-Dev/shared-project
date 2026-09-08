import pygame

from consts import SOLIDER_POSITION

class Solider:
    """ Represents a solider on the screen. """
    def __init__(self):
        self.x = SOLIDER_POSITION[0]
        self.y = SOLIDER_POSITION[1]
        self.image_path = 'images/solider.png'

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def change_image(self, new_path):
        self.image_path = new_path
