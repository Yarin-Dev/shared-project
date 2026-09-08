import pygame
import consts
import Screen
import game_field
from solider import Solider


def main():
    # Set up the game display, clock and headline
    pygame.init()
    pygame.display.set_caption("Flag")
    clock = pygame.time.Clock()
    running = True
    grass = Screen.grass_location()
    board = game_field.create_board()
    n = Screen.night_location(board)
    solider = Solider()

    night_mode = False
    night_start_time = 0

    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    night_mode = True
                    night_start_time = pygame.time.get_ticks()

            dr, dc = 0, 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                dr = -1
            elif keys[pygame.K_DOWN]:
                dr = 1

            elif keys[pygame.K_LEFT]:
                dc = -1

            elif keys[pygame.K_RIGHT]:
                dc = 1

            if dr != 0 or dc != 0:
                solider.move(solider.x + dr, solider.y + dc)


        if night_mode:
            Screen.hidden_screen(board)
            Screen.blit_night(n)
            solider.change_image(consts.SOLDIER_NIGHT_IMG)

            if pygame.time.get_ticks() - night_start_time >= 1000:
                night_mode = False
                solider.change_image(consts.SOLDIER_IMG)
        else:
            Screen.draw_background()
            Screen.blit_grass(grass)

        Screen.blit_solider(solider)
        Screen.draw_flag()

        # Update display - without input update everything

        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)


    pygame.quit()
    quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
