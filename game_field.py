from consts import *
import random



def get_solider_cells(x, y):
    cells = []
    for row in range(SOLDIER_ROWS):
        for col in range(SOLDIER_COLS):
            cells.append((x + row, y + col))
    return cells

def create_board():
    grid = []
    mine_counter = 0
    for i in range(BOARD_ROWS):
        row_to_add = []
        for j in range(BOARD_COLS):
            row_to_add.append(EMPTY_CELL)

        grid.append(row_to_add)

    for x, y in get_solider_cells(SOLIDER_POSITION[0], SOLIDER_POSITION[1]):
        grid[x][y] = SOLDIER_CELL

    # put flag
    for row in range(FLAG_ROWS):
        for col in range(FLAG_COLS):
            grid[flag_row + row][flag_col + col] = FLAG_CELL

    grid = insert_random_mines(grid)

    return grid


def insert_random_mines(grid):
    counter = 0
    while counter < MINES_COUNT:
        x = random.randint(0, BOARD_ROWS - 1)
        y = random.randint(0, BOARD_COLS - 1)
        if y + 3 >= BOARD_COLS:
            continue

        if all([grid[x][i] == EMPTY_CELL for i in range(y, y + 3)]):
            for i in range(y, y + 3):
                grid[x][i] = MINE_CELL
            counter += 1

    return grid


board = create_board()


def put_solider(x, y):
    for x, y in get_solider_cells(SOLIDER_POSITION[0], SOLIDER_POSITION[1]):
        board[x][y] = SOLDIER_CELL

def remove_solider(x, y):
    for x, y in get_solider_cells(SOLIDER_POSITION[0], SOLIDER_POSITION[1]):
        board[x][y] = EMPTY_CELL

