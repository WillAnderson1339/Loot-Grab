import pygame

import constants
from constants import *

pygame.init()

sound_yee_haw_hero = pygame.mixer.Sound('res/yeehaw-1.mp3')
sound_yee_haw_heroess = pygame.mixer.Sound('res/yeehaw-2.mp3')
sound_slide_1 = pygame.mixer.Sound('res/slide-1.mp3')

tumbleweed_1_idle = [pygame.image.load('res/Tumbleweed - 1/Idle__000.png')]

tumbleweed_1_right = [pygame.image.load('res/Tumbleweed - 1/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__008.png')]

tumbleweed_1_left = [pygame.image.load('res/Tumbleweed - 1/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 1/Right__008.png')]

tumbleweed_2_idle = [pygame.image.load('res/Tumbleweed - 2/Idle__000.png')]

tumbleweed_2_right = [pygame.image.load('res/Tumbleweed - 2/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__008.png')]

tumbleweed_2_left = [pygame.image.load('res/Tumbleweed - 2/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 2/Right__008.png')]

tumbleweed_3_idle = [pygame.image.load('res/Tumbleweed - 1/Idle__000.png')]

tumbleweed_3_right = [pygame.image.load('res/Tumbleweed - 3/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__008.png')]

tumbleweed_3_left = [pygame.image.load('res/Tumbleweed - 3/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 3/Right__008.png')]

tumbleweed_4_idle = [pygame.image.load('res/Tumbleweed - 4/Idle__000.png')]

tumbleweed_4_right = [pygame.image.load('res/Tumbleweed - 4/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__008.png')]

tumbleweed_4_left = [pygame.image.load('res/Tumbleweed - 4/Right__000.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__001.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__002.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__003.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__004.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__005.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__006.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__007.png'),
                     pygame.image.load('res/Tumbleweed - 4/Right__008.png')]

thug_1_idle = [pygame.image.load('res/Thug - 1/Idle__000.png')]

thug_1_right = [pygame.image.load('res/Thug - 1/Run_Right__000.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__001.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__002.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__003.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__004.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__005.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__006.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__007.png'),
                     pygame.image.load('res/Thug - 1/Run_Right__008.png')]

thug_1_left = [pygame.image.load('res/Thug - 1/Run_Left__000.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__001.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__002.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__003.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__004.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__005.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__006.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__007.png'),
                     pygame.image.load('res/Thug - 1/Run_Left__008.png')]

skeleton_1_idle = [pygame.image.load('res/Skeleton/Idle__001.png'), pygame.image.load('res/Skeleton/Idle__001.png'),
               pygame.image.load('res/Skeleton/Idle__002.png'), pygame.image.load('res/Skeleton/Idle__003.png'),
               pygame.image.load('res/Skeleton/Idle__004.png'), pygame.image.load('res/Skeleton/Idle__005.png'),
               pygame.image.load('res/Skeleton/Idle__006.png'), pygame.image.load('res/Skeleton/Idle__007.png'),
               pygame.image.load('res/Skeleton/Idle__007.png')]


skeleton_1_walk_right = [pygame.image.load('res/Skeleton/Walk_Right__001.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__001.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__002.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__003.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__004.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__005.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__006.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__007.png'),
                     pygame.image.load('res/Skeleton/Walk_Right__008.png')]

skeleton_1_walk_left = [pygame.image.load('res/Skeleton/Walk_Left__001.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__001.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__002.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__003.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__004.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__005.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__006.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__007.png'),
                    pygame.image.load('res/Skeleton/Walk_Left__008.png')]


# hero idle image list not setup for animation. First image is left. Second image is right
hero_1_idle = [pygame.image.load('res/Hero - 1/Idle__000.png'), pygame.image.load('res/Hero - 1/Idle__001.png')]

hero_1_walk_right = [pygame.image.load('res/Hero - 1/Run_Right__000.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__001.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__002.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__003.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__004.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__005.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__006.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__007.png'),
                     pygame.image.load('res/Hero - 1/Run_Right__008.png')]

hero_1_walk_left = [pygame.image.load('res/Hero - 1/Run_Left__000.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__001.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__002.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__003.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__004.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__005.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__006.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__007.png'),
                    pygame.image.load('res/Hero - 1/Run_Left__008.png')]

hero_1_slide_right = [pygame.image.load('res/Hero - 1/Slide_Right__000.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__001.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__002.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__003.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__004.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__005.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__006.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__007.png'),
                     pygame.image.load('res/Hero - 1/Slide_Right__008.png')]

hero_1_slide_left = [pygame.image.load('res/Hero - 1/Slide_Left__000.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__001.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__002.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__003.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__004.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__005.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__006.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__007.png'),
                    pygame.image.load('res/Hero - 1/Slide_Left__008.png')]


class Character(object):
    IMAGES_WIDTH = 62
    IMAGES_HEIGHT = 76
    IMAGES_HIT_WIDTH = 48
    IMAGES_HIT_HEIGHT = 68

    def __init__(self, character_type, character_id, x, y, num_lives, num_bullets, current_level, current_floor):
        self.character_type = character_type
        self.character_id = character_id
        self.x = x
        self.y = y
        self.num_lives = num_lives
        self.num_bullets = num_bullets
        self.current_level = current_level
        self.current_floor = current_floor

        # self.width = self.IMAGES_WIDTH
        # self.height = self.IMAGES_HEIGHT
        self.score = 0
        self.slide_sound = sound_slide_1
        self.reset_movement_vars()

        # set up the character specific data
        match self.character_type:
            case constants.CHARACTER_TYPE_HERO_1:
                self.vel = VELOCITY_HERO
                self.jumpCount = JUMP_HEIGHT_HERO
                self.jump_height = JUMP_HEIGHT_HERO
                self.images_idle = hero_1_idle
                self.images_walk_right = hero_1_walk_right
                self.images_walk_left = hero_1_walk_left
                self.images_slide_right = hero_1_slide_right
                self.images_slide_left = hero_1_slide_left
                self.hit_box_left_indent = 9
                self.hit_box_right_indent = 10
                self.hit_box_top_indent = 2
                self.hit_box_bottom_indent = 2

            case constants.CHARACTER_TYPE_TUMBLEWEED_1:
                self.vel = VELOCITY_TUMBLEWEED_1
                self.jumpCount = JUMP_HEIGHT_TUMBLEWEED_1
                self.jump_height = JUMP_HEIGHT_TUMBLEWEED_1
                self.images_idle = tumbleweed_1_idle
                self.images_walk_right = tumbleweed_1_right
                self.images_walk_left = tumbleweed_1_left
                self.hit_box_left_indent = 21
                self.hit_box_right_indent = 21
                self.hit_box_top_indent = 25
                self.hit_box_bottom_indent = 10

            case constants.CHARACTER_TYPE_TUMBLEWEED_2:
                self.vel = VELOCITY_TUMBLEWEED_2
                self.jumpCount = JUMP_HEIGHT_TUMBLEWEED_2
                self.jump_height = JUMP_HEIGHT_TUMBLEWEED_2
                self.images_idle = tumbleweed_2_idle
                self.images_walk_right = tumbleweed_2_right
                self.images_walk_left = tumbleweed_2_left
                self.hit_box_left_indent = 15
                self.hit_box_right_indent = 16
                self.hit_box_top_indent = 24
                self.hit_box_bottom_indent = 4
                
            case constants.CHARACTER_TYPE_TUMBLEWEED_3:
                self.vel = VELOCITY_TUMBLEWEED_3
                self.jumpCount = JUMP_HEIGHT_TUMBLEWEED_3
                self.jump_height = JUMP_HEIGHT_TUMBLEWEED_3
                self.images_idle = tumbleweed_3_idle
                self.images_walk_right = tumbleweed_3_right
                self.images_walk_left = tumbleweed_3_left
                self.hit_box_left_indent = 21
                self.hit_box_right_indent = 21
                self.hit_box_top_indent = 18
                self.hit_box_bottom_indent = 15

            case constants.CHARACTER_TYPE_TUMBLEWEED_4:
                self.vel = VELOCITY_TUMBLEWEED_4
                self.jumpCount = JUMP_HEIGHT_TUMBLEWEED_4
                self.jump_height = JUMP_HEIGHT_TUMBLEWEED_4
                self.images_idle = tumbleweed_4_idle
                self.images_walk_right = tumbleweed_4_right
                self.images_walk_left = tumbleweed_4_left
                self.hit_box_left_indent = 13
                self.hit_box_right_indent = 12
                self.hit_box_top_indent = 12
                self.hit_box_bottom_indent = 9

            case constants.CHARACTER_TYPE_THUG_1:
                self.vel = VELOCITY_THUG
                self.jumpCount = JUMP_HEIGHT_THUG
                self.jump_height = JUMP_HEIGHT_THUG
                self.images_idle = thug_1_idle
                self.images_walk_right = thug_1_right
                self.images_walk_left = thug_1_left
                self.hit_box_left_indent = 14
                self.hit_box_right_indent = 14
                self.hit_box_top_indent = 14
                self.hit_box_bottom_indent = 2

            case constants.CHARACTER_TYPE_SKELETON_1:
                self.vel = VELOCITY_SKELETON
                self.jumpCount = JUMP_HEIGHT_SKELETON
                self.jump_height = JUMP_HEIGHT_SKELETON
                self.images_idle = skeleton_1_idle
                self.images_walk_right = skeleton_1_walk_right
                self.images_walk_left = skeleton_1_walk_left
                self.hit_box_left_indent = 12
                self.hit_box_right_indent = 24
                self.hit_box_top_indent = 12
                self.hit_box_bottom_indent = 2

            case _:
                print("ERROR: unknown character type", character_type)

        # setup the hit box
        self.hit_box = self.calc_hit_box(self.x, self.y)

    def reset_movement_vars(self):
        self.is_jumping = False
        self.is_in_ladder = False
        self.is_left = False
        self.is_right = False
        self.is_up = False
        self.is_down = False
        self.idleCount = 0
        self.walkCount = 0
        self.jumpCount = 0
        self.slideCount = 0
        self.slide_ended = False
        self.is_standing = True
        self.is_sliding = False
        self.facing_direction = DIR_LEFT
        self.shoot_dir = DIR_LEFT  # TO DO replace this with using self.is_facing
        self.target_floor = -1
        self.in_ladder_min_x = -1   # to do  change to new way to implement in ladder
        self.in_ladder_max_x = -1
        self.in_ladder_min_y = -1
        self.in_ladder_max_y = -1

    def draw(self, win):
        # character_type = self.character_type
        # if character_type == CHARACTER_TYPE_SKELETON_1:
        #     print("drawing skeleton!")

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        # if sliding
        if self.is_sliding == True:
            y_change = self.calc_slide_y_change()

            if self.facing_direction == DIR_LEFT:
                win.blit(self.images_slide_left[self.walkCount//3], (self.x,self.y + y_change))
            elif self.facing_direction == DIR_RIGHT:
                win.blit(self.images_slide_right[self.walkCount//3], (self.x,self.y + y_change))

        # if moving
        elif self.is_standing == False:
            if self.facing_direction == DIR_LEFT:
                win.blit(self.images_walk_left[self.walkCount//3], (self.x,self.y))
            elif self.facing_direction == DIR_RIGHT:
                win.blit(self.images_walk_right[self.walkCount//3], (self.x,self.y))

        # else standing
        else:
            if self.facing_direction == DIR_LEFT:
                win.blit(self.images_idle[0], (self.x, self.y))
            else:
                win.blit(self.images_idle[1], (self.x, self.y))

        # draw hit box
        if SHOW_PLAYER_HITBOX == True:
            pygame.draw.rect(win, COLOUR_PLAYER_HITBOX, self.hit_box,1)

        if SHOW_DIAGNOSTICS == True:
            width = self.get_character_width()
            height = self.get_character_height()
            image_rect = (self.x, self.y, width, height)
            pygame.draw.rect(win, COLOUR_PLAYER_PERIMETER, image_rect,2)

        # increment the walkCount
        self.walkCount += 1
        if self.is_sliding == True: # and self.walkCount % 3 == 0:
            self.slideCount += 1
            if self.slideCount >= 100:
                self.slideCount = 0

    def move(self, target_x, target_y, direction):
        """Performs the move action. difficulty_multiplier is inc speed. Call calc_move_result for target x,y"""

        # this if statement is used for debugging only
        if self.character_type == CHARACTER_TYPE_TUMBLEWEED_2:
            foo = 5
            if foo == 4:
                print("foobar")

        match direction:
            case constants.DIR_UP:
                self.is_up = True
                self.is_down = False
            case constants.DIR_DOWN:
                self.is_up = False
                self.is_down = True
            case constants.DIR_LEFT:
                self.is_left = True
                self.is_right = False
                self.is_standing = False
                self.facing_direction = DIR_LEFT
                self.shoot_dir = DIR_LEFT
            case constants.DIR_RIGHT:
                self.is_left = False
                self.is_right = True
                self.is_standing = False
                self.facing_direction = DIR_RIGHT
                self.shoot_dir = DIR_RIGHT
            case constants.DIR_NO_MOVE:
                pass
            case _:
                print("ERROR: unknown move direction", direction)

        # if called with a y value too low adjust to lowest possible y value
        width, height = self.get_image_idle_dims()
        max_y = WINDOW_HEIGHT - (height + FLOOR_HEIGHT)
        if target_y > max_y:
            target_y = max_y

        self.x = target_x
        self.y = target_y

        self.hit_box = self.calc_hit_box(self.x, self.y)

    def auto_move(self, difficulty_multiplier):
        """actions the move for non-player characters"""

        if self.is_left:
            direction = DIR_LEFT
        else:
            direction = DIR_RIGHT
        target_x, target_y, hit_box = self.calc_move_result(direction, difficulty_multiplier)

        if self.is_left:
            self.move(target_x, target_y, direction)
        else:
            self.move(target_x, target_y, direction)

        if (self.character_type == CHARACTER_TYPE_TUMBLEWEED_1 or
                self.character_type == CHARACTER_TYPE_TUMBLEWEED_2 or
                self.character_type == CHARACTER_TYPE_TUMBLEWEED_3 or
                self.character_type == CHARACTER_TYPE_TUMBLEWEED_4):
            y_change = self.jump_move(direction)
            new_y = hit_box[1] - y_change
            new_hit_box = (hit_box[0], new_y, hit_box[2], hit_box[3])
            hit_box = new_hit_box

        return hit_box, self.character_type, self.character_id

    def jump_move(self, direction):
        """Performs the jump move by adjusting the y value"""

        x, y = self.get_character_position()
        y_change = 0

        if self.jumpCount >= (self.jump_height * -1):
            neg = 1
            if self.jumpCount < 0:
                neg = -1
            y_change = int((self.jumpCount ** 2) * 0.5 * neg)
            y -= y_change
            self.jumpCount -= 1
        else:
            self.is_jumping = False
            self.jumpCount = self.jump_height

        self.move(x, y, direction)

        return y_change

    def slide_move(self, start_sliding=True):
        """Performs the sliding move. call with False to end sliding move"""


        print("slide_move called with", str(start_sliding))

        if start_sliding == True and self.slide_ended == False:
            self.is_sliding = True
            # play slide sound
            self.play_sound()

        elif start_sliding == False:
            self.is_sliding = False
            # self.slide_ended = False
            self.slideCount = 0

        self.hit_box = self.calc_hit_box(self.x, self.y)

    def calc_hit_box(self, target_x, target_y):
        """Returns the hit box for the supplied x and y"""

        # update the hit box
        if self.is_sliding == False:
            width = self.get_character_width()
            height = self.get_character_height()
            x = target_x + self.hit_box_left_indent
            y = target_y + self.hit_box_top_indent

            width = width - self.hit_box_left_indent - self.hit_box_right_indent
            height = height - self.hit_box_top_indent - self.hit_box_bottom_indent

        else:
            width, height = self.get_image_slide_dims()
            y_change = self.calc_slide_y_change()
            slide_left_indent, slide_right_indent, slide_top_indent, slide_bottom_indent = self.get_slide_hit_box_indents()
            x = target_x + slide_left_indent
            y = target_y + slide_top_indent + y_change

            width = width - slide_left_indent - slide_right_indent
            height = height - slide_top_indent - slide_bottom_indent

        hit_box = (x, y, width, height)

        return hit_box

    def calc_move_result(self, direction, difficulty_multiplier):
        """Returns the resulting x, y, hit box of a move. difficulty_multiplier is used to make the speed faster"""

        # print("calc move result", direction, difficulty_multiplier)

        target_x = self.x
        target_y = self.y

        match direction:
            case constants.DIR_UP:
                x_change = 0
                y_change = int(RUNG_HEIGHT * -1)
            case constants.DIR_DOWN:
                x_change = 0
                y_change = int(RUNG_HEIGHT)
            case constants.DIR_LEFT:
                slide_reduction = self.get_move_reduction()
                # slide_reduction = 0
                x_change = int(self.vel * difficulty_multiplier - slide_reduction)
                if x_change < 0:
                    print("slide ground to a halt!")
                    x_change = 0
                    self.slide_ended = True
                    self.slide_move(False)
                    self.play_sound(SOUND_TYPE_PLAYER_SLIDE, False)
                x_change *= -1
                y_change = 0
            case constants.DIR_RIGHT:
                slide_reduction = self.get_move_reduction()
                x_change = int(self.vel * difficulty_multiplier - slide_reduction)
                if x_change < 0:
                    print("slide ground to a halt!")
                    x_change = 0
                    self.slide_ended = True
                    self.slide_move(False)
                    self.play_sound(SOUND_TYPE_PLAYER_SLIDE, False)
                y_change = 0
            case constants.DIR_NO_MOVE:
                x_change = 0
                y_change = 0
            case _:
                print("ERROR: unknown move direction", direction)
                x_change = 0
                y_change = 0

        # print("x_change = ", x_change)

        target_x += x_change
        target_y += y_change

        # if going off-screen left reposition to the right side
        width, height = self.get_image_run_dims()
        if self.is_in_ladder is False and target_x <= width * -1:
            target_x = WINDOW_WIDTH - width

        # if going off-screen right reposition to the left side
        if self.is_in_ladder is False and target_x >= WINDOW_WIDTH:
            target_x = 0

        # calculate the hit box
        hit_box = self.calc_hit_box(target_x, target_y)

        return target_x, target_y, hit_box

    def position_player_on_new_level(self, portal_id = -1):
        """Positions on new level at portal_id. If portal_id = -1 (default) player is positioned in bottom right."""

        self.reset_movement_vars()

        width, height = self.get_image_idle_dims()

        target_x = WINDOW_WIDTH - 100
        # target_y = WINDOW_HEIGHT - (68 + FLOOR_HEIGHT + 4)
        target_y = WINDOW_HEIGHT - (height + FLOOR_HEIGHT)

        self.move(target_x, target_y, DIR_NO_MOVE)


    def get_image_idle_dims(self):
        width = self.images_idle[0].get_width()
        height = self.images_idle[0].get_height()
        return (width, height)

    def get_image_run_dims(self):
        width = self.images_walk_right[0].get_width()
        height = self.images_walk_right[0].get_height()
        return (width, height)

    def get_image_slide_dims(self):
        width = self.images_slide_right[0].get_width()
        height = self.images_slide_right[0].get_height()
        return (width, height)

    def calc_slide_y_change(self):
        """Returns the y change value when sliding - the x,y of the character position does not change while sliding"""
        idle_dims = self.get_image_idle_dims()
        slide_dims = self.get_image_slide_dims()
        y_change = idle_dims[1] - slide_dims[1] + 5

        return y_change

    def get_slide_hit_box_indents(self):
        """Returns the hit box indents when sliding (did not want to create class level vars for this)"""
        slide_hit_box_left_indent = 3
        slide_hit_box_right_indent = 10
        slide_hit_box_top_indent = 7
        slide_hit_box_bottom_indent = 2

        return slide_hit_box_left_indent, slide_hit_box_right_indent, slide_hit_box_top_indent, slide_hit_box_bottom_indent

    def get_move_reduction(self):
        """Returns the move reduction (if any)"""

        reduction = 0

        level_one = 50
        level_two = 75
        level_three = 100

        # Sliding has an increasing slide reduction to halt slide progress
        if self.is_sliding == True:
            # method 1
            # if 0 <= self.slideCount < level_one:
            #     reduction = 0
            # elif level_one <= self.slideCount < level_two:
            #     reduction = 3
            # elif level_two <= self.slideCount < level_three:
            #     reduction = 6

            # method 2
            # reduction = (2 ** self.slideCount) / 5

            # method 3
            reduction = (1.06 ** self.slideCount) / 2

            print("slideCount =", self.slideCount, "slide reduction =", reduction)

        return reduction

    def get_character_width(self):
        """Returns the width of the player"""

        '''
        if self.is_standing is True:
            width = self.images_idle[0].get_width()
        else:
            if self.is_left is True:
                width = self.images_walk_left[self.walkCount // 3].get_width()
            elif self.is_right:
                width = self.images_walk_right[self.walkCount // 3].get_width()
        '''
        width = self.images_idle[0].get_width()

        if self.is_left is True:
            width = self.images_walk_left[self.walkCount // 3].get_width()
        elif self.is_right:
            width = self.images_walk_right[self.walkCount // 3].get_width()

        return width

    def get_character_height(self):
        """Returns the height of the player"""

        '''
        if self.is_standing is True:
            height = self.images_idle[0].get_height()
        else:
            if self.is_left is True:
                height = self.images_walk_left[self.walkCount // 3].get_height()
            elif self.is_right:
                height = self.images_walk_right[self.walkCount // 3].get_height()
        '''
        height = self.images_idle[0].get_height()

        if self.is_left is True:
            height = self.images_walk_left[self.walkCount // 3].get_height()
        elif self.is_right:
            height = self.images_walk_right[self.walkCount // 3].get_height()

        return height

    def get_character_position(self):
        """Returns the character position.  Used to determine if the position is in contact with another object"""

        return self.x, self.y

    def play_sound(self, sound = SOUND_TYPE_PLAYER_SLIDE, repeating=False):
        """Plays a sound. Default is the slide"""

        if sound == SOUND_TYPE_PLAYER_SLIDE:
            if repeating:
                self.slide_sound.play()
            else:
                self.slide_sound.stop()
