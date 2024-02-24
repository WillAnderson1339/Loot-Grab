import pygame

import constants
from constants import *

pygame.init()

images_bullet_1_left = [pygame.image.load('res/Objects/Bullet_1_Left__000.png')]

images_bullet_1_right = [pygame.image.load('res/Objects/Bullet_1_Right__000.png')]

sound_projectile = pygame.mixer.Sound('res/bullet.mp3')

class Projectile(object):
    def __init__(self, projectile_type, projectile_id, x, y, radius, color, facing):
        self.type = projectile_type
        self.projectile_id = projectile_id
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        if self.facing > 0:
            self.is_left = False
            self.is_right = True
        else:
            self.is_left = True
            self.is_right = False

        # set up the character specific data
        match projectile_type:
            case constants.PROJECTILE_HERO_BULLET:
                self.vel = VELOCITY_HERO_BULLET * facing

                self.image_list_left = images_bullet_1_left
                self.image_list_right = images_bullet_1_right

                self.sound = sound_projectile

                self.hit_box_left_indent = 0
                self.hit_box_right_indent = 0
                self.hit_box_top_indent = 0
                self.hit_box_bottom_indent = 0

            case _:
                print("ERROR: unknown projectile type", projectile_type)

        # setup the hit box
        self.hit_box = self.calc_hit_box(self.x, self.y)

    def draw(self, win):
        """Draws the projectile on the screen."""

        if self.is_left is True:
            image = self.image_list_left[0]
        else:
            image = self.image_list_right[0]

        win.blit(image, (self.x, self.y))

        # update the hit box
        self.hit_box = self.calc_hit_box(self.x, self.y)

        # draw hit box
        if SHOW_PROJECTILE_HITBOX is True:
            pygame.draw.rect(win, COLOUR_PROJECTILE_HITBOX, self.hit_box,2)

        # draw the image outline box
        if SHOW_DIAGNOSTICS is True:
            width = self.get_projectile_width()
            height = self.get_projectile_height()
            image_rect = (self.x, self.y, width, height)
            pygame.draw.rect(win, COLOUR_PROJECTILE_PERIMETER, image_rect, 2)


    def calc_hit_box(self, target_x, target_y):
        """Returns the hit box for the supplied x and y"""

        # update the hit box
        width = self.get_projectile_width()
        height = self.get_projectile_height()
        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent
        self.hit_box = (x, y, width, height)

        return self.hit_box
    def get_projectile_width(self):
        """Returns the width of the loot"""

        # always use left images (same as right)
        width = self.image_list_left[0].get_width()
        return width

    def get_projectile_height(self):
        """Returns the width of the loot"""

        # always use left images (same as right)
        width = self.image_list_left[0].get_height()
        return width

    def get_hit_rect(self):
        """Returns the hit_box rect"""

        return self.hit_box

    def projectile_sound(self):
        self.sound.play()
