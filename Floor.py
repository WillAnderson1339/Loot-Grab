import pygame

from constants import *

class Floor(object):
    def __init__(self, floor_id, colour, rect, ladders):
        self.floor_id = floor_id
        self.colour = colour
        self.rect = rect
        self.ladders = ladders

    def draw(self, win):
        colour = self.colour
        rect = self.rect
        pygame.draw.rect(win, colour, rect)

        # draw the ladders
        for ladder in self.ladders:
            ladder.draw(win)
