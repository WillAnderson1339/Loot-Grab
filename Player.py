import pygame

from constants import *

hero_1_idle = [pygame.image.load('res/Hero - 1/Idle__000.png'), pygame.image.load('res/Hero - 1/Idle__001.png'),
               pygame.image.load('res/Hero - 1/Idle__002.png'), pygame.image.load('res/Hero - 1/Idle__003.png'),
               pygame.image.load('res/Hero - 1/Idle__004.png'), pygame.image.load('res/Hero - 1/Idle__005.png'),
               pygame.image.load('res/Hero - 1/Idle__006.png'), pygame.image.load('res/Hero - 1/Idle__007.png'),
               pygame.image.load('res/Hero - 1/Idle__008.png')]

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


class Player(object):
    IMAGES_WIDTH = 62
    IMAGES_HEIGHT = 76
    IMAGES_HIT_WIDTH = 48
    IMAGES_HIT_HEIGHT = 68

    def __init__(self, x, y, current_level, current_floor):
        self.x = x
        self.y = y
        self.current_level = current_level
        self.current_floor = current_floor

        self.width = self.IMAGES_WIDTH
        self.height = self.IMAGES_HEIGHT
        self.vel = PLAYER_VEL
        self.is_jumping = False
        self.is_in_ladder = False
        self.is_left = False
        self.is_right = False
        self.is_up = False
        self.is_down = False
        self.idleCount = 0
        self.walkCount = 0
        self.jumpCount = JUMP_HEIGHT
        self.is_standing = True
        self.target_floor = -1
        self.in_ladder_min_x = -1
        self.in_ladder_max_x = -1
        self.in_ladder_min_y = -1
        self.in_ladder_max_y = -1
        self.score = 0

        # set up the images lists
        self.images_idle = hero_1_idle
        self.images_walk_right = hero_1_walk_right
        self.images_walk_left = hero_1_walk_left

        # setup the hit box
        self.hit_box_left_indent = 9
        self.hit_box_right_indent = 7
        self.hit_box_top_indent = 2
        self.hit_box_bottom_indent = 2
        #idle_dims = self.get_image_idle_dims()
        width = self.get_player_width()
        height = self.get_player_height()
        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent

        self.hit_box = (x, y, width, height)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.is_standing):
            if self.is_left:
                win.blit(self.images_walk_left[self.walkCount//3], (self.x,self.y))
            elif self.is_right:
                win.blit(self.images_walk_right[self.walkCount//3], (self.x,self.y))
        else:
            '''
            if self.is_right:
                win.blit(self.images_walk_right[0], (self.x, self.y))
            else:
                win.blit(self.images_walk_left[0], (self.x, self.y))
            '''
            win.blit(self.images_idle[0], (self.x, self.y))

        # update the hit box
        width = self.get_player_width()
        height = self.get_player_height()
        x = self.x + self.hit_box_left_indent
        y = self.y + self.hit_box_top_indent
        width = width - self.hit_box_left_indent - self.hit_box_right_indent
        height = height - self.hit_box_top_indent - self.hit_box_bottom_indent
        self.hit_box = (x, y, width, height)


        # draw hit box
        if SHOW_PLAYER_HITBOX == True:
            '''
            # update the hit box
            idle_dims = self.get_image_idle_dims()
            x = self.x + self.hit_box_left_indent
            y = self.y + self.hit_box_top_indent
            width = idle_dims[0] - self.hit_box_left_indent - self.hit_box_right_indent
            height = idle_dims[1] - self.hit_box_top_indent - self.hit_box_bottom_indent
            self.hit_box = (x, y, width, height)
            #self.hitbox = (self.x + 0, self.y + 0, self.IMAGES_HIT_WIDTH, self.IMAGES_HEIGHT - 2)
            '''
            pygame.draw.rect(win, COLOUR_PLAYER_HITBOX, self.hit_box,1)

        if SHOW_DIAGNOSTICS == True:
            #width = 15  # default value just something recognizable if the standing/left/right etc does not work
            #height = 15
            width = self.get_player_width()
            height = self.get_player_height()
            '''
            if not (self.is_standing):
                if self.is_left:
                    width = self.images_walk_left[self.walkCount//3].get_width()
                    height = self.images_walk_left[self.walkCount//3].get_height()
                elif self.is_right:
                    width = self.images_walk_right[self.walkCount//3].get_width()
                    height = self.images_walk_right[self.walkCount//3].get_height()
            else:
                width = self.images_idle[0].get_width()
                height = self.images_idle[0].get_height()
            '''
            image_rect = (self.x, self.y, width, height)
            pygame.draw.rect(win, COLOUR_PLAYER_PERIMETER, image_rect,2)

        # increment the walkCount
        self.walkCount += 1

    def get_image_idle_dims(self):
        width = self.images_idle[0].get_width()
        height = self.images_idle[0].get_height()
        return (width, height)

    def get_image_run_dims(self):
        width = self.images_walk_right[0].get_width()
        height = self.images_walk_right[0].get_height()
        return (width, height)


    def get_player_width(self):
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

    def get_player_height(self):
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
