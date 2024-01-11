import pygame
import random

from constants import *

class Ladder(object):
    def __init__(self, x, y, width, height, colour, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.direction = direction

    def draw(self, win):
        if self.direction == 1:
            pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 2)


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
            id = i
            ladders = []

            self.floors.append((id, colour, rect, ladders))

        self.init_ladders()

    def init_ladders(self):
        for item in self.floors:
            if (item[0] == 0):
                pass

            x = random. randint(10, WINDOW_WIDTH - 150)
            #x = item[2][0]
            y = item[2][1]
            width = 50
            height = 165

            ladder = Ladder(x, y, width, height, self.colour, 1)
            item[3].append(ladder)


    def draw(self, win):
        for item in self.floors:
            pygame.draw.rect(win, item[1], item[2])
            for ladder in item[3]:
                ladder.draw(win)

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

