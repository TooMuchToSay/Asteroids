import pygame
import constants as c
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver }")
    print(f'Screen width: {c.SCREEN_WIDTH}')
    print(f'Screen height: {c.SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

    #call game loop#
    pygame.running = True
    while pygame.running:
        log_state()
        ##pygame quit stuff##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ##ends quit check##
        screen.fill('black')
        pygame.display.flip()

if __name__ == "__main__":
    main()
