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
        self.hit_box_left_indent = 0
        self.hit_box_right_indent = 0
        self.hit_box_top_indent = 0
        self.hit_box_bottom_indent = 0

        self.num_rungs = self.height // RUNG_HEIGHT
        if direction == UP:
            self.y_of_top_rung = self.y + (RUNG_HEIGHT * self.num_rungs * direction)
            self.y_of_2nd_top_rung = self.y_of_top_rung - (RUNG_HEIGHT * direction)
        else:
            self.y_of_top_rung = self.y + (RUNG_HEIGHT * self.num_rungs * direction)
            self.y_of_2nd_top_rung = self.y_of_top_rung - (RUNG_HEIGHT * direction)

        # setup the hit box
        target_x = self.x
        target_y = self.y - self.height

        # self.hit_box = (target_x, target_y, self.width, self.height)
        self.hit_box = self.calc_hit_box(target_x, target_y)


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
        else:
            print("ERROR not yet coded direction ", self.direction)

        # draw hit box
        if SHOW_LADDER_HITBOX is True:
            pygame.draw.rect(win, COLOUR_LADDER_HITBOX, self.hit_box,1)

    def calc_hit_box(self, target_x, target_y):
        """Returns the hit box for the supplied x and y"""

        # calc the hit box
        width = self.width
        height = self.height

        x = target_x + self.hit_box_left_indent
        y = target_y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent

        hit_box = (x, y, width, height)

        return hit_box

    def get_rung_width(self):
        """Returns the width of the rung on this ladder"""

        width = LADDER_WIDTH
        return width

    def get_rung_height(self):
        """Returns the height of rung on this ladder"""

        height = RUNG_HEIGHT
        return height
