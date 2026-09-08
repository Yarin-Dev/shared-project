import pygame
import consts
import Screen
import game_field


def main():
    # Set up the game display, clock and headline
    pygame.init()
    pygame.display.set_caption("Flag")
    clock = pygame.time.Clock()
    index = 0
    running = True
    grass = Screen.grass_location()
    board = game_field.create_board()
    n = Screen.night_location(board)
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())


        Screen.blit_grass(grass)
        Screen.blit_night(n)
        Screen.hidden_screen(board)

        # Update display - without input update everything
        if event.type == pygame.KEYDOWN:

            Screen.hidden_screen()

        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)


    pygame.quit()
    quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
