import pygame

from constants import *

class Ladder(object):
    def __init__(self, x, y, width, height, colour, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.direction = direction

        self.num_rungs = self.height // RUNG_HEIGHT
        if direction == UP:
            self.y_of_top_rung = self.y + (RUNG_HEIGHT * self.num_rungs * direction)
            self.y_of_2nd_top_rung = self.y_of_top_rung - (RUNG_HEIGHT * direction)
        else:
            self.y_of_top_rung = self.y + (RUNG_HEIGHT * self.num_rungs * direction)
            self.y_of_2nd_top_rung = self.y_of_top_rung - (RUNG_HEIGHT * direction)


    def draw(self, win):
        if self.direction == UP:
            # draw the vertical lines
            point_start = (self.x, self.y)
            point_end   = (self.x, self.y - self.height)
            #print(point_start, point_end)
            pygame.draw.line(win, self.colour,point_start, point_end, 3)
            point_start = (self.x + LADDER_WIDTH, self.y)
            point_end   = (self.x + LADDER_WIDTH, self.y - self.height)
            pygame.draw.line(win, self.colour,point_start, point_end, 3)

            # draw the rungs
            x_start = self.x
            y_start = self.y
            num_rungs = self.height // RUNG_HEIGHT
            for i in range(num_rungs):
                point_start = (x_start, y_start - (RUNG_HEIGHT * (i + 1)))
                point_end = (x_start + LADDER_WIDTH, y_start - (RUNG_HEIGHT * (i + 1)))
                pygame.draw.line(win, self.colour, point_start, point_end, 3)

