from consts import *

board = []

def create_board():
    for row in range(BOARD_ROWS):
        row_to_add = []
        for col in range(BOARD_COLS):
            if (row, col) == SOLIDER_POSITION:
                row_to_add.append(SOLDIER_CELL)

            elif RO == :
            row_to_add.append(EMPTY_CELL)