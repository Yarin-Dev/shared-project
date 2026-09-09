import game_field
import Screen

import consts
from consts import SOLIDER_POSITION

class Solider:
    """ Represents a solider on the screen. """
    def __init__(self):
        self.x = SOLIDER_POSITION[0]
        self.y = SOLIDER_POSITION[1]
        self.image_path = consts.SOLDIER_IMG

    def move(self, new_x, new_y):

        # make sure solider doesn't go out of screen.
        if new_x + consts.SOLDIER_ROWS > consts.BOARD_ROWS or new_y + consts.SOLDIER_COLS > consts.BOARD_COLS or new_x < 0 or new_y < 0:
            return

        self.x = new_x
        self.y = new_y

    def change_image(self, new_path):
        self.image_path = new_path

    def check_touch_mine(self):
        cells = game_field.get_solider_cells(self.x, self.y)
        for row in range(len(game_field.board)):
            for col in range(len(game_field.board[row])):
                if game_field.board[row][col] == consts.MINE_CELL and (row, col) in cells:
                    return True
        return False

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