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

    # map generation
    grass = Screen.grass_location()
    n = Screen.night_location(game_field.board)
    solider = Solider()

    # night vars
    night_mode = False
    night_start_time = 0
    hit_explosion = False

    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                # if clicked space, activate night mode for a second.
                if event.key == pygame.K_SPACE:
                    night_mode = True
                    night_start_time = pygame.time.get_ticks()

            # player movement
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

            # if player move, make the move on the board
            # additionally, we check if there was a win or lose during the move.
            if dr != 0 or dc != 0:
                solider.move(solider.x + dr, solider.y + dc)

                # lose, blit explosion
                if solider.check_touch_mine():
                    hit_explosion = True
                # win
                elif solider.check_touch_flag():
                    running = False


        if night_mode:
            # draw night mode map
            Screen.hidden_screen(game_field.board)
            Screen.blit_night(n)
            solider.change_image(consts.SOLDIER_NIGHT_IMG)

            # check if a second passed
            # if so, return to normal mode
            if pygame.time.get_ticks() - night_start_time >= 1000:
                night_mode = False
                solider.change_image(consts.SOLDIER_IMG)

        else:
            # normal mode
            Screen.draw_background()
            Screen.blit_grass(grass)
            Screen.draw_flag()

        # draw solider & welc message
        Screen.blit_solider(solider)
        Screen.draw_welcome_message()
        if hit_explosion:
            Screen.draw_explosion(solider.x, solider.y)
            running = False

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)


    pygame.quit()
    quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
