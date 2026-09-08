from consts import *
import random


def create_board():
    grid = []
    mine_counter = 0
    for i in range(BOARD_ROWS):
        row_to_add = []
        for j in range(BOARD_COLS):
            if len(row_to_add) >= BOARD_COLS:
                break

            if mine_counter < MINES_COUNT and j < BOARD_COLS - 3:
                if random.random() < 0.01:
                    mine_counter += 1
                    for _ in range(MINE_COLS):
                        row_to_add.append(MINE_CELL)
                else:
                    row_to_add.append(EMPTY_CELL)
            else:
                row_to_add.append(EMPTY_CELL)

        grid.append(row_to_add)

    # put solider
    for row in range(SOLDIER_ROWS):
        for col in range(SOLDIER_COLS):
            grid[SOLIDER_POSITION[0] + row][SOLIDER_POSITION[1] + col] = SOLDIER_CELL

    # put flag
    for row in range(FLAG_ROWS):
        for col in range(FLAG_COLS):
            grid[flag_row + row][flag_col + col] = FLAG_CELL

    return grid

board = create_board()