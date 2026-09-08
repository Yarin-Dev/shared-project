import pygame
import consts
import Screen


def main():
    # Set up the game display, clock and headline
    pygame.init()
    pygame.display.set_caption("Flag")
    clock = pygame.time.Clock()
    index = 0
    running = True
    grass = Screen.grass_location()
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        Screen.draw_background()
        Screen.blit_grass(grass)
        if event.type == pygame.MOUSEBUTTONDOWN:

        # Update display - without input update everything


        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)

    pygame.quit()
    quit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
