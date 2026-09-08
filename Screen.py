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
        grass_x = random.randrange(consts.GRASS_WIDTH, consts.WINDOW_WIDTH-consts.GRASS_WIDTH)
        grass_y = random.randrange(consts.GRASS_HEIGHT,consts.WINDOW_HEIGHT-consts.GRASS_HEIGHT)
        rect = grass.get_rect(
                topleft=(grass_x, grass_y))
        b.update({sized_grass: rect})
    return b

#מתודה לציור רנדומלי של שיחים
def blit_grass(b):
    for k,v in b.items():
        screen.blit(k, v)

#מתודה לציור רשת המטריצה
def hidden_screen (board):
    screen.fill(consts.BACKGROUND_COLOR)
    gap = 1

    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            x_pos = col * consts.CELL_SIZE
            y_pos = row * consts.CELL_SIZE
            pygame.draw.rect(screen, consts.BLACK,
                             pygame.Rect(x_pos - gap, y_pos - gap,
                                         consts.CELL_SIZE - gap,
                                         consts.CELL_SIZE - gap))



def night_location(board):
    b = {}
    for row in range(consts.BOARD_ROWS):
        for col in range(0,consts.BOARD_COLS,3):
            x_pos = col * consts.CELL_SIZE
            y_pos = row * consts.CELL_SIZE
            if board[row][col] == consts.MINE_CELL:
                mine = pygame.transform.scale(pygame.image.load(consts.MINE_IMG),
                (consts.CELL_SIZE * consts.MINE_COLS, consts.CELL_SIZE* consts.MINE_ROWS))
                rect = mine.get_rect(
                        topleft=(x_pos, y_pos))
                b.update({mine: rect})

    return b

def blit_night(b):
    for k,v in b.items():
        screen.blit(k, v)


#יצירת שחקן חדש
# לחישוב המשבצות של גוף הדמות


# לחישוב המשבצות של רגלי הדמות
#מתודות לציור האובייקטים על המסך

