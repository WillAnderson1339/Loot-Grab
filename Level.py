
import pygame

from constants import *

class Level(object):
    def __init__(self, num_floors, num_enemies, colour):
        self.num_floors = num_floors
        self.num_enemies = num_enemies
        self.colour = colour

        self.floors = []

        for i in range(self.num_floors):
            colour = self.colour
            x = 0
            y = (WINDOW_HEIGHT // (self.num_floors + 1)) * (i + 1)
            # y = 200 * i
            width = WINDOW_WIDTH
            height = 10
            rect = (x, y, width, height)

            self.floors.append((colour, rect))


    def draw(self, win):
        for item in self.floors:
            pygame.draw.rect(win, item[0], item[1])

    def foo(self):
        if self.num_floors == -1:
            pass

        for item in self.floors:
            bar = 12

            if bar == 10:
                something = 3
            else:
                something = 5

            mystring = "hello world"

