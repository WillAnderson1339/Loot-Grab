import pygame

from constants import *

coin_gold_1 = [pygame.image.load('res/Loot/Coin - 1__000.png'),
               pygame.image.load('res/Loot/Coin - 1__000.png'),
               pygame.image.load('res/Loot/Coin - 1__001.png'),
               pygame.image.load('res/Loot/Coin - 1__002.png'),
               pygame.image.load('res/Loot/Coin - 1__003.png'),
               pygame.image.load('res/Loot/Coin - 1__004.png'),
               pygame.image.load('res/Loot/Coin - 1__005.png'),
               pygame.image.load('res/Loot/Coin - 1__006.png'),
               pygame.image.load('res/Loot/Coin - 1__006.png')]

class Loot(object):
    def __init__(self, loot_id, x, y, loot_type, facing):
        self.loot_id = loot_id
        self.x = x
        self.y = y
        self.loot_type = loot_type
        self.facing = facing

        self.image_list = coin_gold_1

        width = self.image_list[0].get_width()
        height = self.image_list[0].get_height()
        self.hit_box = (self.x, self.y, self.x + width, self.y + height)
        self.spinCount = self.facing

    def draw(self, win):
        if self.spinCount + 1 >= 27:
            self.spinCount = 0

        #pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        win.blit(self.image_list[self.spinCount // 3], (self.x, self.y))

        # draw hit box
        if SHOW_LOOT_HITBOX == True:
            width = self.get_loot_width()
            height = self.get_loot_height()
            self.hit_box = (self.x, self.y, width, height)
            pygame.draw.rect(win, COLOUR_LOOT_HITBOX, self.hit_box,2)

        # increment the spinCount
        self.spinCount += 1

    def get_loot_width(self):
        """Returns the width of the loot"""
        width = self.image_list[0].get_width()
        return width

    def get_loot_height(self):
        """Returns the width of the loot"""
        width = self.image_list[0].get_height()
        return width

