import pygame

import consts
import Screen
from consts import SOLIDER_POSITION

class Solider:
    """ Represents a solider on the screen. """
    def __init__(self):
        self.x = SOLIDER_POSITION[0]
        self.y = SOLIDER_POSITION[1]
        self.image_path = consts.SOLDIER_IMG

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def change_image(self, new_path):
        self.image_path = new_path

    def check_touch_flag(self):
        body_cells = Screen.get_soldier_body_cells(self.x, self.y)
        flag_cells = []
        for row in range(consts.flag_row,consts.BOARD_ROWS):
            for col in range(consts.flag_col,consts.BOARD_COLS):
                flag_cells.append((row,col))


        for cell in body_cells:
            if cell in flag_cells:
                return True

        return False

