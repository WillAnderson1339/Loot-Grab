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
        self.hit_box_left_indent = 2
        self.hit_box_right_indent = 2
        self.hit_box_top_indent = 2
        self.hit_box_bottom_indent = 2

        # setup the hit box
        target_x = self.x
        target_y = self.y

        self.hit_box = self.calc_hit_box(target_x, target_y)

    def draw(self, win):
        """Draws the portal"""

        light_width = PORTAL_LIGHT_WIDTH
        light_height = PORTAL_LIGHT_HEIGHT


        # draw frame
        x = self.x
        y = self.y
        portal_rect = (x, y, PORTAL_WIDTH, PORTAL_HEIGHT)
        width = 2
        pygame.draw.rect(win, PORTAL_COLOUR, portal_rect, width)

        # draw ellipse
        width = 0
        pygame.draw.ellipse(win, PORTAL_COLOUR, portal_rect, width)

        # draw top light
        if self.direction == UP:
            light_colour = PORTAL_UP_LIGHT_COLOUR
            light_x = self.x + (self.width // 2) - 16
            light_y = self.y - 8
            light_rect = (light_x, light_y, light_width, light_height)
        else:
            light_colour = PORTAL_DOWN_LIGHT_COLOUR
            light_x = self.x + (self.width // 2) - 16
            light_y = self.y - 8
            light_rect = (light_x, light_y, PORTAL_LIGHT_WIDTH, PORTAL_LIGHT_HEIGHT)

        width = 0
        pygame.draw.rect(win, light_colour, light_rect, width)

        # draw hit box
        if SHOW_PORTAL_HITBOX is True:
            pygame.draw.rect(win, COLOUR_LOOT_HITBOX, self.hit_box,1)

        # draw the image outline box
        # if SHOW_DIAGNOSTICS is True:
        #     width = self.image_list[self.spin_count // 3].get_width()
        #     height = self.image_list[self.spin_count // 3].get_height()
        #     image_rect = (self.x, self.y, width, height)
        #     pygame.draw.rect(win, COLOUR_LOOT_PERIMETER, image_rect, 2)

        # for development work
        # if DEV_MODE is True:
        #     pygame.draw.rect(win, (255,0,0), (x, y, 4, 4), 0)

    def calc_hit_box(self, target_x, target_y):
        """Returns the hit box for the supplied x and y"""

        # update the hit box
        width = self.width
        height = self.height

        x = target_x + self.hit_box_left_indent
        y = target_y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent

        hit_box = (x, y, width, height)

        return hit_box

