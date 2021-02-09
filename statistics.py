import pygame
import sys
from loadge_file import load_image
from prom import start_screen

WIDTH = 1280
HEIGHT = 720


def return_to_main_menu(mouse_pos):
    print(mouse_pos)
    x = mouse_pos[0]
    y = mouse_pos[1]
    if x in range(0, 75) and y in range(0, 85):
        start_screen()


def terminate():
    pygame.quit()
    sys.exit()


def statistics_window():
    fon = pygame.transform.scale(load_image('Statistics.png'), (WIDTH, HEIGHT))
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return_to_main_menu(event.pos)
        pygame.display.flip()
