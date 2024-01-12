import pygame
import random

from constants import *

LADDER_WIDTH = 50

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

        # create the floor objects and append them to the floor List
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

        # Once all the floors are create the ladders can be added
        self.init_ladders()

    def init_ladders(self):
        ladder_locations = []

        num = len(ladder_locations)

        for item in self.floors:
            num_ladders = random.randint(1,2)
            num_ladders = 2

            # find an x co-ordinate for this ladder
            for i in range(num_ladders):
                x = random.randint(10, WINDOW_WIDTH - 150)

                found_dupe = False
                keep_looking = True
                counter = 0
                while keep_looking == True and len(ladder_locations) > 0:
                    # ensure this ladder X location is not too close to any existing ladder locations on this floor
                    for ladder_location in ladder_locations:
                        if x > ladder_location[0] and x < ladder_location[1]:
                            found_dupe = True
                            break
                    if found_dupe == True:
                            x = random.randint(10, WINDOW_WIDTH - 150)
                    counter += 1
                    if (counter == len(ladder_locations)):
                        keep_looking = False

                y = item[2][1]
                width = LADDER_WIDTH
                height = 165

                ladder = Ladder(x, y, width, height, self.colour, 1)
                item[3].append(ladder)
                ladder_locations.append((x - LADDER_WIDTH - 20, x + LADDER_WIDTH + 20))  # 20 padding so not too close


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

