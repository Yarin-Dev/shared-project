import consts
import pygame
import random

#מודול לניהול המסך הראשי, זה שיוצרים בעזרת pygame בתחילת המשחק.
# יחזיק את המשתנה של המסך הראשי, ואת כל המתודות לציור האובייקטים עליו.

#יצירת מסך pygame
screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

#מתודה לציור רקע רגיל
def draw_background():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()
#מיקומים רנדומלים לשיחים
def grass_location():
    b = {}
    for i in range(consts.GRASS_COUNT):
        grass = pygame.image.load(consts.GRASS_IMG)
        sized_grass = pygame.transform.scale(grass, (
            consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
        grass_x = random.randrange(consts.WINDOW_WIDTH)
        grass_y = random.randrange(consts.WINDOW_HEIGHT)
        rect = grass.get_rect(
                center=(grass_x, grass_y))
        b.update({sized_grass: rect})
    return b

#מתודה לציור רנדומלי של שיחים
def blit_grass(b):
    for k,v in b.items():
        screen.blit(k, v)

#מתודה לציור רשת המטריצה והמוקשים
def hidden_screen (board):
    screen.fill(consts.BACKGROUND_COLOR)
    gap = 1

    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            x_pos = col * consts.CELL_SIZE
            y_pos = row * consts.CELL_SIZE

            pygame.draw.rect(screen, consts.BLACK,
            pygame.Rect(x_pos- gap, y_pos- gap, consts.CELL_SIZE- gap, consts.CELL_SIZE- gap))

            if board[row][col] == consts.MINE_CELL:
                mine = pygame.transform.scale(pygame.image.load(consts.MINE_IMG),
                (consts.CELL_SIZE * consts.MINE_ROWS, consts.CELL_SIZE* consts.MINE_COLS))
                rect = mine.get_rect(
                        topleft=(x_pos, y_pos))
                screen.blit(mine, rect)

            if board[row][col] == consts.SOLDIER_CELL:
                soldier_night = pygame.transform.scale(pygame.image.load(consts.SOLDIER_IMG),
                (consts.CELL_SIZE * consts.MINE_ROWS, consts.CELL_SIZE* consts.MINE_COLS))
                rect = soldier_night.get_rect(topleft=(x_pos, y_pos))
                screen.blit(soldier_night, rect)
def night_location(board):
    b = {}
    did =False

    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            x_pos = col * consts.CELL_SIZE
            y_pos = row * consts.CELL_SIZE


            if board[row][col] == consts.MINE_CELL:
                mine = pygame.transform.scale(pygame.image.load(consts.MINE_IMG),
                (consts.CELL_SIZE * consts.MINE_ROWS, consts.CELL_SIZE* consts.MINE_COLS))
                rect = mine.get_rect(
                        topleft=(x_pos, y_pos))
                b.update({mine: rect})

            if not did and board[row][col] == consts.SOLDIER_CELL:
                soldier_night = pygame.transform.scale(pygame.image.load(consts.SOLDIER_IMG),
                (consts.CELL_SIZE * consts.MINE_ROWS, consts.CELL_SIZE* consts.MINE_COLS))
                rect = soldier_night.get_rect(topleft=(x_pos, y_pos))
                b.update({soldier_night: rect})
                did = True
    return b

def blit_night(b):
    for k,v in b.items():
        screen.blit(k, v)
#יצירת שחקן חדש
# לחישוב המשבצות של גוף הדמות


# לחישוב המשבצות של רגלי הדמות
#מתודות לציור האובייקטים על המסך

