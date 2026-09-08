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
    for row in range(len(consts.BOARD_ROWS)):
        for col in range(len(consts.BOARD_COLS)):

            pygame.draw.rect(screen, consts.BLACK,
            pygame.Rect(r, c, consts.CELL_SIZE, consts.CELL_SIZE))

            if board[row][col] == MINE_CELL:
                mine = pygame.transform.scale(pygame.image.load(mine_img),
                (consts.CELL_SIZE * consts.MINE_ROWS, consts.CELL_SIZE* consts.MINE_COLS))
                rect = mine.get_rect(
                        center=(r, c))
                screen.blit(mine, rect)

            if board[row][col] == SOLDIER_CELL:
                soldier_night = pygame.transform.scale(pygame.image.load(soldier_night_img),
                (consts.CELL_SIZE * consts.MINE_ROWS, consts.CELL_SIZE* consts.MINE_COLS))
                rect = soldier_night.get_rect(
                        center=(r, c))
                screen.blit(soldier_night, rect)

#יצירת שחקן חדש
# לחישוב המשבצות של גוף הדמות
def cala_body():

# לחישוב המשבצות של רגלי הדמות
#מתודות לציור האובייקטים על המסך

