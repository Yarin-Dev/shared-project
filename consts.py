"""

[2, 1, 0, 0]
[0, 0, 1, 0]
[0, 1, 0, 0]
[0, 0, 0, 3]


"""

EMPTY_CELL = 0
MINE_CELL = 1
SOLDIER_CELL = 2
FLAG_CELL = 3

BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

FLAG_POSITION = (BOARD_ROWS - 1, BOARD_COLS - 1)

# solider
SOLIDER_POSITION = (0, 0)
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part

FLAG_ROWS = 3
FLAG_COLS = 4
flag_row = BOARD_ROWS - FLAG_ROWS
flag_col = BOARD_COLS - FLAG_COLS
FLAG_POS = (FLAG_ROWS, FLAG_COLS)
FLAG_WIDTH = FLAG_COLS*CELL_SIZE
FLAG_HEIGHT = FLAG_ROWS*CELL_SIZE


BACKGROUND_COLOR = (0,100,0)
BLACK = (0,0,0)
MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3

GRASS_COUNT = 20
GRASS_ROWS = 3
GRASS_COLS = 3

GRASS_IMG = "C:/Users/User/Desktop/Nizanim Python/shared-project/images/grass.png"
GRASS_HEIGHT = GRASS_COLS * CELL_SIZE
GRASS_WIDTH = GRASS_ROWS * CELL_SIZE

SOLDIER_IMG = "C:/Users/User/Desktop/Nizanim Python/shared-project/images/soldier.png"
SOLDIER_NIGHT_IMG = "C:/Users/User/Desktop/Nizanim Python/shared-project/images/soldier_night.png"
MINE_IMG = "C:/Users/User/Desktop/Nizanim Python/shared-project/images/mine.png"
FLAG_IMG = "C:/Users/User/Desktop/Nizanim Python/shared-project/images/flag.png"

EXPLOSION_IMG = "explotion.png"
FONT_NAME = "Calibri"

LOSE_MESSAGE = "You Lost!"
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = (
    int(0.2 * WINDOW_WIDTH),
    int(WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2)),
)

WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = (
    int(0.2 * WINDOW_WIDTH),
    int(WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2)),
)
WELCOME_MESSAGE = "Welcome to The Flag game.\nHave Fun!"
WELCOME_FONT_SIZE = int(0.04 * WINDOW_WIDTH)  # או גודל קבוע לפי לבחירתך, למשל 24
WELCOME_COLOR = (255, 255, 255)  # WHITE
WELCOME_LOCATION = (10, 10)


