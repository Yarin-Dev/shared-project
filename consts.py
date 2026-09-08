"""

[2, 1, 0, 0]
[0, 0, 1, 0]
[0, 1, 0, 0]
[0, 0, 0, 3]


"""

# cells
EMPTY_CELL = 0
MINE_CELL = 1
SOLDIER_CELL = 2
FLAG_CELL = 3

# board
BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell

# windows
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

# solider
SOLIDER_POSITION = (0, 0)
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part

# flag
FLAG_ROWS = 3
FLAG_COLS = 4
flag_row = BOARD_ROWS - FLAG_ROWS
flag_col = BOARD_COLS - FLAG_COLS


# mines
MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3