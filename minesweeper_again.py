# By Mehmet Akdemir

import pygame
import sys
import random

# Set Constants

TV1989_1 = (72, 115, 152)
TV1989_2 = (101, 155, 187)
TV1989_3 = (139, 181, 210)
TV1989_4 = (175, 197, 212)
LOVER_1 = (118, 186, 224)
LOVER_2 = (140, 79, 102)
LOVER_3 = (184, 57, 107)
LOVER_4 = (235, 190, 211)
SPEAKNOW_1 = (82,49,107)

BOXSIZE = 30
GAPSIZE = 5
FIELDWIDTH = 20
FIELDHEIGHT = 20
TOTALMINES = 80

FONT_TYPE = 'Engravers Old English'
FONT_SIZE = 20


screen = pygame.display.set_mode((1000, 800), pygame.RESIZABLE)
pygame.display.set_caption('Minesweeper')

screen.fill(TV1989_2)

buttons = []

for m in range(60,660,20):
    for n in range(60,660,20):
        rect = pygame.Rect(m,n,FIELDWIDTH, FIELDHEIGHT)
        pygame.draw.rect(screen, LOVER_1, rect)
        pygame.draw.rect(screen, SPEAKNOW_1, rect, 2)
        buttons.append(rect)

places = [" " for n in range(320)]
places += ["*" for n in range(80)]

def shuffleMines(places):
    random.shuffle(places)
    places = ["".join(places[k * 20: (k + 1) * 20]) for k in range(20)]
    return places

def reveal(cor):
    pass

pygame.display.flip()

img = pygame.image.load("minesweepericon.png")
pygame.display.set_icon(img)


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for rect in buttons:
                    if rect.collidepoint(mouse_x, mouse_y):
                        reveal(rect.topleft)


if __name__ == '__main__':
    main()