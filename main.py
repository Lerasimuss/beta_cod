import pygame
from random import randint
import sys
import os

pygame.init()

score = 0
total = 0

font = pygame.font.SysFont('f', 50)
all_sprites = pygame.sprite.Group
player_image = load_image("dash.png")
# Jumping Variables
yVel = 0
jumping = 0
# if ghoul)
is_dead = False


display = {
    "width": 1280,
    "height": 720
}

character = {
    "width": 20,
    "height": 20,
    "x": 200,
    "y": 580,
    "velocity": 50
}

platform = {
    'y': 580,
    "x": 700,
    "pass": 0,
    "length": 20,
    "amount": 2,
    "distanceApart": 50
}
spike = {
    "height": -15,
    "y": 600,
    "x": 700,
    "pass": 0,
    "length": 20,
    "amount": 2,
    "distanceApart": 50
}


def load_image(name):
    fullname = os.path.join(f'data/{name}')
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Dash(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            -spike["height"] * pos_x + 15, -spike["height"] * pos_y + 5)


screen = pygame.display.set_mode((display["width"], display["height"]))
displ = pygame.display.set_mode((display["width"], display["height"]))


def get_pos(pos):
    return pos[0], pos[1]


def terminate():
    pygame.quit()
    sys.exit()


def nextSection():
    spike["x"] = 700
    spike['pass'] += spike['amount']
    spike['amount'] = randint(1, 4)
    spike['distanceApart'] = randint(2, 4) * 10
    return


def triangleDraw(num):  # Draws the triangles
    pygame.draw.polygon(displ,
                        (0, 0, 0),
                        ((spike["x"] + spike['distanceApart'] * num, spike["y"]),
                         (spike['x'] + spike['distanceApart'] * num + spike["length"], spike['y']),
                         (spike['x'] + spike['length'] / 2 + spike['distanceApart'] * num,
                          spike['y'] + spike['height'])))


def jump():  # Start Jumping
    global yVel
    global jumping
    if jumping == 0:
        jumping = 1
        yVel = 10
        character['y'] = character['y'] - yVel
        if character['y'] > platform['y']:
            jumping = 0
        yVel -= 0.5


def cJump():  # Continue Jump
    global yVel
    global jumping
    if jumping == 0:
        if character['y'] > platform['y']:
            pass
        else:
            jumping = 1
    if jumping == 1:
        character['y'] = character['y'] - yVel
        if character['y'] > platform['y']:
            jumping = 2
        yVel -= 0.5
    elif 2 <= jumping < 5:
        jumping += 1
    else:
        jumping = 0


def print_progress():
    if spike['pass'] < 100:  # Win Statement
        text_surface_2 = font.render("Percentage {0}%".format(spike['pass']), False, (0, 0, 0))
        displ.blit(text_surface_2, (300, 10))
    else:
        text_surface_2 = font.render("YOU WIN", False, (255, 0, 0))
        displ.blit(text_surface_2, (300, 10))


def next_step():
    cJump()
    pygame.draw.rect(displ, (255, 0, 0),
                     (character["x"],
                      character["y"],
                      character["width"],
                      character["height"]))
    pygame.display.update()
    spike['x'] -= 5


def check_next_ses(charar_x):
    if spike['x'] + spike['distanceApart'] * spike['amount'] < charar_x:
        return True
    return False


bg = load_image('fon.jpg')

while True:  # Main Game Loop
    pygame.time.delay(10)
    screen.blit(bg, (0, 0))
    for i in range(spike['amount']):  # Spike Drawing
        triangleDraw(i)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:  # Checks Jump
            jump()
    if check_next_ses(character['x']):
        nextSection()
    print_progress()
    for i in range(spike['amount']):  # Checks if death occurs
        if spike['x'] + spike['distanceApart'] * i <= character['x'] <= spike['x'] \
                + spike['distanceApart'] * i + spike['length']:

            posOnSpike = abs(character['x'] - (spike['x'] + spike['length'] / 2))
            if posOnSpike * 2 + spike['y'] > character['y'] > spike['y'] \
                    or posOnSpike * 2 + spike['y'] > character['y'] + character['height'] > spike['y']:
                text_surface2 = font.render("YOU LOSE", False, (255, 0, 0))
                displ.blit(text_surface2, (300, 60))
                is_dead = True

        else:
            pass
    # Drawing Stuff
    next_step()
    if is_dead:
        break