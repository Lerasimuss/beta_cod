import os
import pygame
import sys


def load_image(name):
    fullname = os.path.join(f'{name}')
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image