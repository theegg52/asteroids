import pygame
from constants import *

def main():
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill((0,0,0))
        pygame.display.flip()
if __name__ == "__main__":
    main()