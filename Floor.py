import pygame

from constants import *

class Floor(object):
    def __init__(self, floor_id, colour, rect, ladders, wind_direction):
        self.floor_id = floor_id
        self.colour = colour
        self.rect = rect
        self.ladders = ladders
        self.wind_direction = wind_direction

    def draw(self, win):
        colour = self.colour
        rect = self.rect
        pygame.draw.rect(win, colour, rect)

        # draw the ladders
        for ladder in self.ladders:
            ladder.draw(win)
