import pygame

from constants import *

pygame.init()

images_bullet_1_left = [pygame.image.load('res/Objects/Bullet_1_Left__000.png')]

images_bullet_1_right = [pygame.image.load('res/Objects/Bullet_1_Right__000.png')]

sound_projectile = pygame.mixer.Sound('res/bullet.mp3')

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
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
        self.vel = 8 * facing

        self.image_list_left = images_bullet_1_left
        self.image_list_right = images_bullet_1_right

        self.sound = sound_projectile

        # setup the hit box
        self.hit_box_left_indent = 2
        self.hit_box_right_indent = 2
        self.hit_box_top_indent = 2
        self.hit_box_bottom_indent = 2
        width = self.get_projectile_width()
        height = self.get_projectile_height()
        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent
        self.hit_box = (x, y, width, height)

    def draw(self, win):
        """Draws the projectile on the screen."""

        if self.is_left is True:
            image = self.image_list_left[0]
        else:
            image = self.image_list_right[0]

        win.blit(image, (self.x, self.y))

        # update the hit box
        width = self.get_projectile_width()
        height = self.get_projectile_height()
        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent
        self.hit_box = (x, y, width, height)

        # draw hit box
        if SHOW_PROJECTILE_HITBOX is True:
            '''
            width = self.get_projectile_width()
            height = self.get_projectile_height()
            self.hit_box = (self.x, self.y, width, height)
            '''
            pygame.draw.rect(win, COLOUR_PROJECTILE_HITBOX, self.hit_box,2)

        # draw the image outline box
        if SHOW_DIAGNOSTICS is True:
            width = self.get_projectile_width()
            height = self.get_projectile_height()
            image_rect = (self.x, self.y, width, height)
            pygame.draw.rect(win, COLOUR_PROJECTILE_PERIMETER, image_rect, 2)


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

    def projectile_sound(self):
        self.sound.play()
