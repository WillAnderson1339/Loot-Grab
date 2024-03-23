
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

coin_bronze_1 = [pygame.image.load('res/Loot/Coin - 3__000.png'),
               pygame.image.load('res/Loot/Coin - 3__001.png'),
               pygame.image.load('res/Loot/Coin - 3__002.png'),
               pygame.image.load('res/Loot/Coin - 3__003.png'),
               pygame.image.load('res/Loot/Coin - 3__004.png'),
               pygame.image.load('res/Loot/Coin - 3__005.png'),
               pygame.image.load('res/Loot/Coin - 3__006.png'),
               pygame.image.load('res/Loot/Coin - 3__007.png'),
               pygame.image.load('res/Loot/Coin - 3__008.png')]

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

bullet_small = [pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png'),
               pygame.image.load('res/Loot/Bullet - 1__000.png')]

bullet_large = [pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png'),
               pygame.image.load('res/Loot/Bullet - 2__000.png')]

diamond = [pygame.image.load('res/Loot/Diamond - 1__000.png'),
               pygame.image.load('res/Loot/Diamond - 1__001.png'),
               pygame.image.load('res/Loot/Diamond - 1__002.png'),
               pygame.image.load('res/Loot/Diamond - 1__003.png'),
               pygame.image.load('res/Loot/Diamond - 1__004.png'),
               pygame.image.load('res/Loot/Diamond - 1__005.png'),
               pygame.image.load('res/Loot/Diamond - 1__006.png'),
               pygame.image.load('res/Loot/Diamond - 1__007.png'),
               pygame.image.load('res/Loot/Diamond - 1__008.png')]

sound_loot = pygame.mixer.Sound('res/loot-1.mp3')
sound_ding = pygame.mixer.Sound('res/ding-1.mp3')
sound_miss = pygame.mixer.Sound('res/loot-miss-1.mp3')

class Loot(object):
    """
    When adding new Loot types do the following:
      - add the image list with the png file(s)
      - add the constants
      - add the case statement to the init function
      - add the elif statement to create_loots function in the level class
      - add the action_player_touching_loot function in the level class
      - add the code to count_loot function in the level class
    """

    def __init__(self, loot_id, x, y, loot_type, facing):
        self.loot_id = loot_id
        self.x = x
        self.y = y
        self.loot_type = loot_type
        self.facing = facing

        match self.loot_type:
            case constants.LOOT_COIN_BRONZE:
                self.image_list = coin_bronze_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_BRONZE
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 4
                self.hit_box_right_indent = 4
                self.hit_box_top_indent = 3
                self.hit_box_bottom_indent = 4

            case constants.LOOT_COIN_SILVER:
                self.image_list = coin_silver_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_SILVER
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 4
                self.hit_box_right_indent = 4
                self.hit_box_top_indent = 3
                self.hit_box_bottom_indent = 4

            case constants.LOOT_COIN_GOLD:
                self.image_list = coin_gold_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_GOLD
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 4
                self.hit_box_right_indent = 4
                self.hit_box_top_indent = 3
                self.hit_box_bottom_indent = 4

            case constants.LOOT_HEART_SMALL:
                self.image_list = heart_small
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_HEART_SMALL
                self.sound_success = sound_ding
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 5
                self.hit_box_right_indent = 5
                self.hit_box_top_indent = 5
                self.hit_box_bottom_indent = 5

            case constants.LOOT_HEART_MEDIUM:
                self.image_list = heart_medium
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_HEART_MEDIUM
                self.sound_success = sound_ding
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 2
                self.hit_box_right_indent = 2
                self.hit_box_top_indent = 2
                self.hit_box_bottom_indent = 3

            case constants.LOOT_HEART_LARGE:
                self.image_list = heart_large
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_HEART_LARGE
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 2
                self.hit_box_right_indent = 2
                self.hit_box_top_indent = 2
                self.hit_box_bottom_indent = 3

            case constants.LOOT_BULLET_SMALL:
                self.image_list = bullet_small
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_BULLET_SMALL
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 7
                self.hit_box_right_indent = 7
                self.hit_box_top_indent = 3
                self.hit_box_bottom_indent = 3

            case constants.LOOT_BULLET_LARGE:
                self.image_list = bullet_large
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_BULLET_LARGE
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 7
                self.hit_box_right_indent = 7
                self.hit_box_top_indent = 3
                self.hit_box_bottom_indent = 3

            case constants.LOOT_DIAMOND:
                self.image_list = diamond
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_DIAMOND
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 7
                self.hit_box_right_indent = 7
                self.hit_box_top_indent = 12
                self.hit_box_bottom_indent = 3

            # loot objects are created with this as an uninitialized loot object (i.e. function return when not found)
            case constants.LOOT_UNKNOWN:
                self.image_list = coin_gold_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_GOLD
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 0
                self.hit_box_right_indent = 0
                self.hit_box_top_indent = 0
                self.hit_box_bottom_indent = 0

            case _:
                print("Loot Type", self.loot_type, "not yet coded!")
                self.image_list = coin_gold_1
                self.spin_count = self.facing
                self.loot_value = LOOT_VALUE_COIN_GOLD
                self.sound_success = sound_loot
                self.sound_miss = sound_miss
                self.hit_box_left_indent = 0
                self.hit_box_right_indent = 0
                self.hit_box_top_indent = 0
                self.hit_box_bottom_indent = 0

        # setup the hit box
        self.hit_box = self.calc_hit_box(self.x, self.y)

    def draw(self, win):
        """Draws the loot on the screen."""

        if self.spin_count + 1 >= 27:
            self.spin_count = 0

        win.blit(self.image_list[self.spin_count // 3], (self.x, self.y))

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

    def calc_hit_box(self, target_x, target_y):
        """Returns the hit box for the supplied x and y"""

        # update the hit box
        width = self.get_loot_width()
        height = self.get_loot_height()

        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent

        hit_box = (x, y, width, height)

        return hit_box

    def get_loot_width(self):
        """Returns the width of the loot"""

        width = self.image_list[0].get_width()
        return width

    def get_loot_height(self):
        """Returns the height of the loot"""

        height = self.image_list[0].get_height()
        return height

    def loot_sound(self, sound_type=SOUND_TYPE_LOOT_SUCCESS):
        if sound_type == SOUND_TYPE_LOOT_SUCCESS:
            self.sound_success.play()
        else:
            self.sound_miss.play()
