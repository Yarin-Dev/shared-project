import random
import pygame
import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_background():
    screen.fill(consts.BACKGROUND_COLOR)

def grass_location():
    grass_rect_list = []

    grass_img = pygame.image.load(consts.GRASS_IMG)
    sized_grass = pygame.transform.scale(
        grass_img, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT)
    )

    while len(grass_rect_list) < consts.GRASS_COUNT:
        x_pos = random.randrange(
            consts.GRASS_WIDTH, consts.WINDOW_WIDTH - consts.GRASS_WIDTH
        )
        y_pos = random.randrange(
            consts.GRASS_HEIGHT, consts.WINDOW_HEIGHT - consts.GRASS_HEIGHT
        )
        new_rect = sized_grass.get_rect(topleft=(x_pos, y_pos))

        if new_rect not in  grass_rect_list:
            grass_rect_list.append(new_rect)

    return grass_rect_list

def blit_grass(grass_rect_list):
    grass_img = pygame.image.load(consts.GRASS_IMG)
    sized_grass = pygame.transform.scale(
        grass_img, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT)
    )

    for rect in grass_rect_list:
        screen.blit(sized_grass, rect)


def hidden_screen(board):
    screen.fill(consts.BACKGROUND_COLOR)
    gap = 1

    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            x_pos = col * consts.CELL_SIZE
            y_pos = row * consts.CELL_SIZE
            pygame.draw.rect(
                screen,
                consts.BLACK,
                pygame.Rect(
                    x_pos - gap,
                    y_pos - gap,
                    consts.CELL_SIZE - gap,
                    consts.CELL_SIZE - gap,
                ),
            )

def night_location(board):
    mines_rect_list = []

    mine_w = consts.CELL_SIZE * consts.MINE_COLS
    mine_h = consts.CELL_SIZE * consts.MINE_ROWS

    for row in range(consts.BOARD_ROWS):
        for col in range(0, consts.BOARD_COLS, 3):
            x_pos = col * consts.CELL_SIZE
            y_pos = row * consts.CELL_SIZE

            if board[row][col] == consts.MINE_CELL:
                mine_rect = pygame.Rect(x_pos, y_pos, mine_w, mine_h)
                mines_rect_list.append(mine_rect)

    return mines_rect_list

def blit_night(mines_rect_list):
    mine_img = pygame.image.load(consts.MINE_IMG)
    sized_mine = pygame.transform.scale(
        mine_img,
        (
            consts.CELL_SIZE * consts.MINE_COLS,
            consts.CELL_SIZE * consts.MINE_ROWS,
        ),
    )

    for rect in mines_rect_list:
        screen.blit(sized_mine, rect)


def draw_lose_message():
    draw_message(
        consts.LOSE_MESSAGE,
        consts.LOSE_FONT_SIZE,
        consts.LOSE_COLOR,
        consts.LOSE_LOCATION,
    )


def draw_win_message():
    draw_message(
        consts.WIN_MESSAGE,
        consts.WIN_FONT_SIZE,
        consts.WIN_COLOR,
        consts.WIN_LOCATION,
    )


def draw_welcome_message():
    font = pygame.font.SysFont(consts.FONT_NAME, consts.WELCOME_FONT_SIZE)

    line1 = font.render(consts.WELCOME_LINE1, True, consts.WELCOME_COLOR)
    line2 = font.render(consts.WELCOME_LINE2, True, consts.WELCOME_COLOR)

    screen.blit(line1, consts.WELCOME_LOCATION_LINE1)
    screen.blit(line2, consts.WELCOME_LOCATION_LINE2)


# ציור פיצוץ בלחיצה/דריכה על מוקש
def draw_explosion():
    exp_img = pygame.image.load(consts.EXPLOSION_IMG)
    sized_exp = pygame.transform.scale(
        exp_img,
        (
            consts.CELL_SIZE * consts.MINE_COLS,
            consts.CELL_SIZE * consts.MINE_ROWS,
        )
    )
    screen.blit(sized_exp, mine_rect)

def blit_solider(solider):
    image = pygame.image.load(solider.image_path)

    image = pygame.transform.scale(
        image,
        (
            consts.CELL_SIZE * consts.SOLDIER_COLS,
            consts.CELL_SIZE * consts.SOLDIER_ROWS
        )
    )

    x = solider.y * consts.CELL_SIZE
    y = solider.x * consts.CELL_SIZE

    screen.blit(image, (x, y))

def get_soldier_body_cells(x, y):
    body_cells = []
    for r in range(x, x + consts.SOLDIER_BODY_ROWS):
        for c in range(y, y + consts.SOLDIER_FEET_ROWS):
            body_cells.append((r, c))
    return body_cells


def get_soldier_feet_cells(x, y):
    feet_cells = []
    feet_row = x + consts.SOLDIER_BODY_ROWS
    for c in range(y, y + consts.SOLDIER_FEET_ROWS):
        feet_cells.append((feet_row, c))
    return feet_cells


def draw_flag():
    flag_img = pygame.image.load(consts.FLAG_IMG)
    sized_flag = pygame.transform.scale(
        flag_img, (consts.FLAG_WIDTH, consts.FLAG_HEIGHT)
    )

    flag_x = consts.WINDOW_WIDTH - consts.FLAG_WIDTH
    flag_y = consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT - 5

    flag_rect = sized_flag.get_rect(topleft=(flag_x, flag_y))
    screen.blit(sized_flag, flag_rect)
