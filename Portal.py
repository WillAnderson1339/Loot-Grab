import pygame

from constants import *

class Portal(object):
    def __init__(self, portal_id, x, y, width, height, colour, direction):
        self.portal_id = portal_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.direction = direction

    def draw(self, win):
        # draw frame
        x = self.x
        y = self.y
        portal_rect = (x, y, PORTAL_WIDTH, PORTAL_HEIGHT)

        # draw ellipse
        width = 2
        pygame.draw.rect(win, PORTAL_COLOUR, portal_rect, width)
        width = 0
        pygame.draw.ellipse(win, PORTAL_COLOUR, portal_rect, width)

        # draw top light
        if self.direction == UP:
            colour = (50,200,50)
            x = self.x + (self.width // 2) - 16
            y = self.y - 8
            top_light_rect = (x, y, 32, 8)
            width = 0
            pygame.draw.rect(win, colour, top_light_rect, width)
        else:
            colour = (200,25,25)
            x = self.x + (self.width // 2) - 16
            y = self.y - 8
            top_light_rect = (x, y, 32, 8)
            width = 0
            pygame.draw.rect(win, colour, top_light_rect, width)


