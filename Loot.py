
import pygame

import constants
from constants import *

pygame.init()

coin_gold_1 = [pygame.image.load('res/Loot/Coin - 1__000.png'),
               pygame.image.load('res/Loot/Coin - 1__000.png'),
               pygame.image.load('res/Loot/Coin - 1__001.png'),
               pygame.image.load('res/Loot/Coin - 1__002.png'),
               pygame.image.load('res/Loot/Coin - 1__003.png'),
               pygame.image.load('res/Loot/Coin - 1__004.png'),
               pygame.image.load('res/Loot/Coin - 1__005.png'),
               pygame.image.load('res/Loot/Coin - 1__006.png'),
               pygame.image.load('res/Loot/Coin - 1__006.png')]

coin_silver_1 = [pygame.image.load('res/Loot/Coin - 2__000.png'),
               pygame.image.load('res/Loot/Coin - 2__001.png'),
               pygame.image.load('res/Loot/Coin - 2__002.png'),
               pygame.image.load('res/Loot/Coin - 2__003.png'),
               pygame.image.load('res/Loot/Coin - 2__004.png'),
               pygame.image.load('res/Loot/Coin - 2__005.png'),
               pygame.image.load('res/Loot/Coin - 2__006.png'),
               pygame.image.load('res/Loot/Coin - 2__007.png'),
               pygame.image.load('res/Loot/Coin - 2__008.png')]

heart_small = [pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png'),
               pygame.image.load('res/Loot/Heart - 1__000.png')]

heart_medium = [pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png'),
                pygame.image.load('res/Loot/Heart - 2__000.png')]

heart_large = [pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png'),
               pygame.image.load('res/Loot/Heart - 3__000.png')]

sound_loot = pygame.mixer.Sound('res/loot-1.mp3')
sound_ding = pygame.mixer.Sound('res/ding-1.mp3')
sound_miss = pygame.mixer.Sound('res/miss-1.mp3')

class Loot(object):
    def __init__(self, loot_id, x, y, loot_type, facing):
        self.loot_id = loot_id
        self.x = x
        self.y = y
        self.loot_type = loot_type
        self.facing = facing

        match self.loot_type:
            case constants.LOOT_COIN_BRONZE:
                # self.image_list = coin_bronze_1
                self.image_list = coin_silver_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_BRONZE
                self.sound_success = sound_loot
                self.sound_miss = sound_miss

            case constants.LOOT_COIN_SILVER:
                self.image_list = coin_silver_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_SILVER
                self.sound_success = sound_loot
                self.sound_miss = sound_miss

            case constants.LOOT_COIN_GOLD:
                self.image_list = coin_gold_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_GOLD
                self.sound_success = sound_loot
                self.sound_miss = sound_miss

            case constants.LOOT_HEART_SMALL:
                self.image_list = heart_small
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_HEART_SMALL
                self.sound_success = sound_ding
                self.sound_miss = sound_miss

            case constants.LOOT_HEART_MEDIUM:
                self.image_list = heart_medium
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_HEART_MEDIUM
                self.sound_success = sound_ding
                self.sound_miss = sound_miss

            case constants.LOOT_HEART_LARGE:
                self.image_list = heart_large
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_HEART_LARGE
                self.sound_success = sound_loot
                self.sound_miss = sound_miss

            # loot objects are created with this as an uninitialized loot object (i.e. function return when not found)
            case constants.LOOT_UNKNOWN:
                self.image_list = coin_gold_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_GOLD
                self.sound_success = sound_loot
                self.sound_miss = sound_miss

            case _:
                print("Loot Type", self.loot_type, "not yet coded!")
                self.image_list = coin_gold_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_GOLD
                self.sound_success = sound_loot
                self.sound_miss = sound_miss

        # setup the hit box
        self.hit_box_left_indent = 2
        self.hit_box_right_indent = 2
        self.hit_box_top_indent = 2
        self.hit_box_bottom_indent = 2
        width = self.get_loot_width()
        height = self.get_loot_height()
        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent
        self.hit_box = (x, y, width, height)

    def draw(self, win):
        """Draws the loot on the screen."""

        if self.spin_count + 1 >= 27:
            self.spin_count = 0

        win.blit(self.image_list[self.spin_count // 3], (self.x, self.y))

        # update the hit box
        # LOOT DOES NOT MOVE SO SHOULD NOT UPDATE THE HIT BOX!
        width = self.get_loot_width()
        height = self.get_loot_height()
        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent
        self.hit_box = (x, y, width, height)

        # draw hit box
        if SHOW_LOOT_HITBOX is True:
            pygame.draw.rect(win, COLOUR_LOOT_HITBOX, self.hit_box,1)

        # draw the image outline box
        if SHOW_DIAGNOSTICS is True:
            width = self.image_list[self.spin_count // 3].get_width()
            height = self.image_list[self.spin_count // 3].get_height()
            image_rect = (self.x, self.y, width, height)
            pygame.draw.rect(win, COLOUR_LOOT_PERIMETER, image_rect, 2)

        # increment the spinCount
        self.spin_count += 1

    def get_loot_width(self):
        """Returns the width of the loot"""

        width = self.image_list[0].get_width()
        return width

    def get_loot_height(self):
        """Returns the height of the loot"""

        height = self.image_list[0].get_height()
        return height

    def loot_sound(self, sound_type=0):
        if sound_type == 0:
            self.sound_success.play()
        else:
            self.sound_miss.play()
