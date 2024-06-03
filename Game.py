import pygame
from dataclasses import field

from diagnostics import *

from Level import *
from Character import *
from Projectile import *
from constants import *


class Game(object):
    def __init__(self):     # (self, pygame: object)
        self.pygame = pygame

        #self.levels = field(default_factory=list)
        # self.bullets = field(default_factory=list)
        # self.player = field(default_factory=object)
        self.levels = []
        self.bullets = []

        self.is_playing_music = False
        self.tumbleweed_hit_pause = False

        self.show_diagnostics = SHOW_DIAGNOSTICS
        self.show_portal_info = True

        self.show_message_count = 0
        self.show_message_text = ""

        self.pause = False

        self.total_loot = 0
        self.total_enemies = 0
        self.total_loot_grabbed = 0
        self.total_enemies_shot = 0

        self.pygame.init()

        self.clock = self.pygame.time.Clock()

        self.win = self.pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.pygame.display.set_caption("Loot Grab")

        # set up the various resources
        self.set_up_resources()

        # create the levels
        self.create_levels()

        # set the totals (for showing the score)
        for level in self.levels:
            self.total_loot += level.count_loot()
            self.total_enemies += level.count_enemies()

        # set up the player
        x = WINDOW_WIDTH - 100
        y = WINDOW_HEIGHT - (68 + FLOOR_HEIGHT + 4)
        current_level = 0
        level = self.levels[current_level]
        current_floor = len(level.floors) - 1
        player_type = CHARACTER_TYPE_HERO_1
        player_id = 1000
        num_lives = SCORE_START_NUM_LIVES
        num_bullets = SCORE_START_NUM_BULLETS
        self.player = Character(player_type, player_id, x, y, num_lives, num_bullets, current_level, current_floor)
        self.player.position_player_on_new_level()

        # for dev coding work - create sample loot
        # level = levels[current_level]
        # x = 100
        # y = level.get_floor_y(player.current_floor) - 30
        # loot_testing = Loot(1339, x, y, LOOT_DIAMOND, DIR_LEFT)
        # level.loots.append(loot_testing)


    def set_up_resources(self):
        """sets up the various resources like sounds, fonts, image arrays, etc."""

        self.font_stats = pygame.font.SysFont('comicsans', 25, True)
        self.font_diagnostics = pygame.font.SysFont('consolas', 15, False)
        self.font_pause = pygame.font.SysFont("comicsansms", 80)
        self.font_pause_stats = pygame.font.SysFont("comicsansms", 30)
        self.font_pause_neg_score_change = pygame.font.SysFont('comicsans', 25, True)

        self.sound_bullet = self.pygame.mixer.Sound('res/bullet.mp3')
        self.hitSound = self.pygame.mixer.Sound('res/hit.mp3')
        self.sound_portal = self.pygame.mixer.Sound('res/portal.mp3')
        self.sound_grunt = self.pygame.mixer.Sound('res/grunt-2.mp3')

        self.images_background = [
            pygame.image.load('res/Backgrounds/Mountains 5.png'),
            pygame.image.load('res/Backgrounds/Mountains 4.png'),
            pygame.image.load('res/Backgrounds/Mountains 7.png'),
            pygame.image.load('res/Backgrounds/Field 4.png'),
            pygame.image.load('res/Backgrounds/Field 3.png'),
            pygame.image.load('res/Backgrounds/Mountains 1.png'),
            pygame.image.load('res/Backgrounds/Mountains 6.png'),
            pygame.image.load('res/Backgrounds/Lava 1.png')]

        self.images_objects = [
            pygame.image.load('res/Objects/Heart_1__000.png'),
            pygame.image.load('res/Objects/Bullet_1__000.png')]

    def create_random_level(self, level_id):
        num_floors = random.randint(2, 5)
        num_enemies = random.randint(2, 8)
        num_up_portals = random.randint(1, 2)
        num_down_portals = random.randint(1, 2)
        background = level_id
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colour = (red, green, blue)
        difficulty_multiplier = 1.0 + (0.2 * level_id)
        level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour,
                      difficulty_multiplier)
        self.levels.append(level)

    def create_levels(self):
        """Creates the levels"""

        # create first level (the first level is special - it has no down portal)
        level_id = 0
        num_floors = 4
        num_enemies = 2
        num_up_portals = 1
        num_down_portals = 0
        background = 0
        colour = (90, 165, 120)
        difficulty_multiplier = 1.0
        level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour, difficulty_multiplier)
        self.levels.append(level)

        num_levels_to_create = 6
        # create random levels - could change this to planned levels with colours, backgrounds, enemies etc
        for i in range(num_levels_to_create):
            self.create_random_level(i + 1)

        # create last level (the last level is special - it has no up portal)
        level_id = len(self.levels)
        num_floors = 5
        num_enemies = 6
        num_up_portals = 0
        num_down_portals = 1
        background = 7
        colour = (150, 175, 75)
        difficulty_multiplier = 1.0 + (0.2 * level_id)
        level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour,
                      difficulty_multiplier)
        self.levels.append(level)

    def run(self):
        """Called to execute the running of the game"""

        level = self.levels[self.player.current_level]

        # move bullets
        for bullet in self.bullets:
            if bullet.x < WINDOW_WIDTH and bullet.x > 0:
                bullet.x += bullet.vel * level.difficulty_multiplier
            else:
                self.bullets.pop(self.bullets.index(bullet))

        # move enemies
        hit_box_list = level.auto_move_enemies(level.difficulty_multiplier)

        # update the tumbleweed pause timer (so tumbleweed passes player and does not continually decrement score)
        if self.tumbleweed_hit_pause > 0:
            self.tumbleweed_hit_pause += 1
        if self.tumbleweed_hit_pause > 20:
            self.tumbleweed_hit_pause = 0

        # check to see if anything is touching something
        for item in hit_box_list:
            rect_enemy = item[0]
            enemy_type = item[1]
            enemy_id = item[2]

            # bullets do not hit tumbleweeds
            bullets_ignore_types = [CHARACTER_TYPE_TUMBLEWEED_1, CHARACTER_TYPE_TUMBLEWEED_2, CHARACTER_TYPE_TUMBLEWEED_3, CHARACTER_TYPE_TUMBLEWEED_4]
            if enemy_type not in bullets_ignore_types:
                # check to see if an enemy is hit by a shot
                for bullet in self.bullets:
                    rect_projectile = bullet.get_hit_rect()
                    if do_rectangles_overlap(rect_enemy, rect_projectile) is True:
                        self.action_player_shot_enemy(enemy_id, bullet)

            # check to see if the enemy is touching the player
            rect_player = self.player.hit_box
            if do_rectangles_overlap(rect_enemy, rect_player) is True:
                self.action_enemy_touching_player(enemy_type)
                self.tumbleweed_hit_pause = 1

        # if below zero score -1 life
        if self.player.score < 0 and self.player.num_lives != -99:
            self.player.num_lives -= 1
            self.player.score = 0
            if self.player.num_lives == 0:
                print("Game Over!")
                self.player.num_lives = -99
                self.pause = True
                self.paused()
            else:
                current_floor = len(level.floors) - 1
                self.player.current_floor = current_floor
                self.player.position_player_on_new_level()

        """
        # if had pressed the slide key and now released it
        if (self.player.is_sliding is True or self.player.slide_ended is True) and not keys[pygame.K_s]:
            print("had pressed the slide key and now released it")
            self.player.slide_ended = False
            self.player.slide_move(False)
            self.player.play_sound(SOUND_TYPE_PLAYER_SLIDE, False)
        """

    def draw(self):

        level = self.levels[self.player.current_level]

        # draw background
        background = level.background
        self.win.blit(self.images_background[background], (0, 0))

        # draw level
        level.draw(self.win)

        # draw characters
        self.player.draw(self.win)

        # draw player message
        if self.show_message_count > 0:
            player_x, player_y = self.player.get_character_position()
            player_width = self.player.get_character_width()
            text = self.show_message_text
            colour = COLOUR_NEG_SCORE_TEXT
            print_text = self.font_pause_neg_score_change.render(text, 1, colour)

            # background for message
            width = print_text.get_width() + 20
            height = print_text.get_height() + 4
            x = player_x + (player_width // 2) - (width // 2)
            y = player_y - height - 2
            # width = 40
            # height = 20
            message_rect = (x, y, width, height)
            self.pygame.draw.rect(self.win, COLOUR_MESSAGE_BACKGROUND, message_rect, 0, 10)

            # message text
            x += 10
            y += 2
            self.win.blit(print_text, (x, y))

            self.show_message_count += 1
            if self.show_message_count >= MESSAGE_TEXT_TIMER_LIMIT:
                self.show_message_count = 0

        # draw bullets
        for bullet in self.bullets:
            bullet.draw(self.win)

        # show diagnostics (function will check for show/not show)
        if self.show_diagnostics is True:
            show_diagnotics(self.win, self.font_diagnostics, self.show_portal_info, self.levels, self.player)
        else:
            self.show_stats()

        self.pygame.display.update()

    def paused(self):
        """Used to pause the game. Triggered by Game Over or pressing the 'p' key"""

        # if music was playing turn stop it while paused
        if self.is_playing_music is True:
            self.pygame.mixer.music.stop()

        # background for message
        x = WINDOW_WIDTH * .25
        y = WINDOW_HEIGHT * .25
        width = WINDOW_WIDTH * .5
        height = WINDOW_HEIGHT * .4
        message_rect = (x, y, width, height)
        self.pygame.draw.rect(self.win, COLOUR_MESSAGE_BACKGROUND, message_rect, 0, 10)

        # message title
        if self.player.num_lives == -99:
            title = "Game Over! "
            colour = COLOUR_GAME_OVER
        else:
            title = "Paused"
            colour = COLOUR_PAUSE

        x = message_rect[0] + (message_rect[2] // 2)
        y = message_rect[1]

        print_title = self.font_pause.render(title, 1, colour)
        x -= print_title.get_width() // 2
        # y += print_title.get_height()
        self.win.blit(print_title, (x, y))

        text = "Stats:"
        print_text = self.font_pause_stats.render(text, 1, colour)
        x = message_rect[0] + (message_rect[2] // 2)
        x -= 200
        y += print_title.get_height()
        self.win.blit(print_text, (x, y))

        # x += 30

        text = "  Total Loot " + str(self.total_loot) + "  Grabbed " + str(self.total_loot_grabbed)
        print_text = self.font_pause_stats.render(text, 1, colour)
        x = message_rect[0] + (message_rect[2] // 2)
        x -= 190
        y += print_text.get_height()
        self.win.blit(print_text, (x, y))

        text = "  Total Enemies " + str(self.total_enemies) + "  Shot " + str(self.total_enemies_shot)
        print_text = self.font_pause_stats.render(text, 1, colour)
        # x = WINDOW_WIDTH // 2
        # x -= print_text.get_width() // 2
        y += print_text.get_height()
        self.win.blit(print_text, (x, y))

        # keep lines above in Game class. Remove lines below from Game class  - leave them in the main.py file
        while self.pause:
            for event in self.pygame.event.get():

                if event.type == pygame.QUIT:
                    self.pygame.quit()
                    quit()

                keys = self.pygame.key.get_pressed()

                # need ky_key_states from main...
                # pressing the 'p' key again will unpause the game
                #if keys[self.pygame.K_p] and kp_key_states[KP_p] == 0 and self.player.num_lives != -99:
                if keys[self.pygame.K_p] and self.player.num_lives != -99:
                    self.pause = False
                    # kp_key_states[KP_p] = 0

            self.pygame.display.update()
            self.clock.tick(15)

        # if music was playing turn it back on
        if self.is_playing_music is True:
            self.pygame.mixer.music.play(-1)

    def show_stats(self):
        """Displays the player game stats like lives, score, etc."""

        font = self.font_stats

        # show the player lives as hearts
        start_x = WINDOW_WIDTH - 200
        start_y = 10
        row_height = 30

        # show the hearts for lives
        object_index = IMAGE_OBJECT_LIFE_HEART
        width = self.images_objects[object_index].get_width()
        width += 4
        x = start_x - 15 - (self.player.num_lives * width)
        y = start_y + 10

        for num_lives in range(self.player.num_lives):
            self.win.blit(self.images_objects[object_index], (x, y))
            x += width

        # show the bullets for number of bullets left
        object_index = IMAGE_OBJECT_HERO_BULLET
        width = self.images_objects[object_index].get_width()
        width += 8
        x = start_x - 15 - (self.player.num_bullets * width)
        y = start_y + 10 + row_height
        for num_bullets in range(self.player.num_bullets):
            self.win.blit(self.images_objects[object_index], (x, y))
            x += width

        # show the player level and score info
        colour = COLOUR_STATS
        start_x = WINDOW_WIDTH - 200
        start_y = 10
        col_1_width = 170
        col_2_width = 325

        level = self.levels[self.player.current_level]

        x = start_x
        y = start_y

        text = "Level:  " + str(self.player.current_level +1)
        print_text = font.render(text, 1, colour)
        self.win.blit(print_text, (x, y))

        y += row_height
        text = "Score: " + str(self.player.score)
        print_text = font.render(text, 1, colour)
        self.win.blit(print_text, (x, y))

    def event_toggle_music(self):
        """Toggles the music from on to off and back again"""

        if self.is_playing_music is True:
            self.is_playing_music = False
            self.pygame.mixer.music.stop()
        else:
            self.is_playing_music = True
            self.pygame.mixer.music.play(-1)

        # for development sometimes need to clear all enemies (so they stop hitting the player!)
        # should move this to its own key but using 'm' just for ease
        if DEV_MODE == True:
            level = self.levels[self.player.current_level]
            level.remove_all_enemies()

    def event_toggle_diagnostics(self):
        """Toggles the diagnostics on and off"""

        if self.show_diagnostics is True:
            self.show_diagnostics = False
        else:
            self.show_diagnostics = True

            # toggle state of the portal or ladder info
            if self.show_portal_info:
                self.show_portal_info = False
            else:
                self.show_portal_info = True

    def event_spawn_enemy(self):
        """Spawns a new enemy - called on a timer event"""

        level = self.levels[self.player.current_level]
        spawned_enemy = level.check_if_spawning_enemy()
        if spawned_enemy is True:
            self.total_enemies += 1

    def event_move_left(self):
        """processes the move left event i.e. the left arrow key (or swipe left?)"""

        # calculate move so can compare for various results before moving
        level = self.levels[self.player.current_level]
        target_x, target_y, target_hit_box = self.player.calc_move_result(DIR_LEFT, level.difficulty_multiplier)
        # portal_id = level.is_location_in_portal(target_x, target_y)
        portal_id = level.is_player_in_portal(self.player)

        # if not in portal just allow move
        if portal_id == -1 or self.player.is_jumping is True or self.player.is_sliding is True:
            if portal_id != -1 and self.player.is_jumping is True:
                # print("in portal but jumping or sliding so moving instead!")
                pass

            # if in ladder restrict horizontal movement to within the ladder
            width = self.player.get_character_width()
            if self.player.is_in_ladder is False or target_x >= self.player.in_ladder_min_x - (width * 0.3):
                self.player.move(target_x, target_y, DIR_LEFT)

            # check to see if walked into any loot
            loot = level.is_player_in_loot(self.player)
            if loot.loot_id != -1:
                # level.action_player_touching_loot(loot, player)
                self.action_player_touching_loot(loot)

        else:
            # self.action_player_touching_portal(player)    # odd typo?  how did this work?
            self.action_player_touching_portal(portal_id)

    def event_move_right(self):
        """processes the move right event i.e. the left arrow key (or swipe right?)"""

        # calculate move so can compare for various results before moving
        level = self.levels[self.player.current_level]
        target_x, target_y, target_hit_box = self.player.calc_move_result(DIR_RIGHT, level.difficulty_multiplier)
        # portal_id = level.is_location_in_portal(target_x, target_y)
        portal_id = level.is_player_in_portal(self.player)

        # if not in portal just allow move
        if portal_id == -1 or self.player.is_jumping is True or self.player.is_sliding is True:
            if portal_id != -1 and self.player.is_jumping is True:
                # print("in portal but jumping or sliding so moving instead!")
                pass

            # if in ladder restrict horizontal movement to within the ladder
            width = self.player.get_character_width()
            if self.player.is_in_ladder is False or target_x <= self.player.in_ladder_max_x - (width * 0.5):
                self.player.move(target_x, target_y, DIR_RIGHT)

            # check to see if walked into any loot
            loot = level.is_player_in_loot(self.player)
            if loot.loot_id != -1:
                self.action_player_touching_loot(loot)

        else:
            # self.action_player_touching_portal(player)  # odd typo
            self.action_player_touching_portal(portal_id)

    def event_move_down(self):
        """Processes the down event"""

        # calculate move so can compare for various results before moving
        level = self.levels[self.player.current_level]
        target_x, target_y, target_hit_box = self.player.calc_move_result(DIR_DOWN, level.difficulty_multiplier)
        dims = self.player.get_image_idle_dims()
        # x_pos, y_pos = player.get_character_position()
        # x_pos += (dims[0] // 2)
        # y_pos += dims[1]
        # y_of_top_rung = level.get_ladder_top_rung_y(player.current_floor + 1)

        # normal going down (ladders are stored at the floor below and go up)
        if self.player.current_floor < self.player.target_floor or self.player.target_floor == -1:  # or player.is_up is True:
            floor_number = self.player.current_floor + 1
            # print("normal down floor_number =", floor_number)
        # switched from up to down
        # elif player.current_floor == player.target_floor and player.is_up is False:
        elif self.player.current_floor == self.player.target_floor:
            if self.player.is_up is False:
                floor_number = self.player.current_floor
            else:
                floor_number = self.player.current_floor + 1
            # print("switched from up to down AA floor_number =", floor_number)
        # switching from up to down
        else:
            floor_number = self.player.current_floor
            # print("switched from up to down BB floor_number =", floor_number)

        target_in_ladder, ladder_coords = level.is_player_move_in_ladder(target_hit_box, floor_number)
        # print("DOWN: floor with ladder =", floor_number, "target_in_ladder =", target_in_ladder)
        if target_in_ladder == True:
            # set ladder info
            if self.player.is_in_ladder is False:
                self.player.is_in_ladder = True
                # ladder_coords = level.get_ladder_coords(floor_number, x_pos, y_pos)  # changed to getting coords from call to is_player_move_in_ladder()
                if ladder_coords[0] != -1:
                    # player.in_ladder_min_x = ladder_coords[0]
                    # player.in_ladder_max_x = ladder_coords[2]
                    # player.in_ladder_min_y = ladder_coords[1]
                    # player.in_ladder_max_y = ladder_coords[3]
                    self.player.in_ladder_min_x = ladder_coords[0]
                    self.player.in_ladder_max_x = ladder_coords[0] + ladder_coords[2]
                    self.player.in_ladder_min_y = ladder_coords[1]
                    self.player.in_ladder_max_y = ladder_coords[1] + ladder_coords[3]
                    y_of_top_rung = level.get_ladder_top_rung_y(floor_number)
                    self.player.in_ladder_top_rung_y = y_of_top_rung

            # starting down set target to floor below
            if self.player.target_floor == -1:
                self.player.target_floor = self.player.current_floor + 1
            # if switching from up to down set to floor we just left (the one above)
            elif self.player.is_up is True:
                self.player.target_floor = self.player.target_floor + 1  # player.current_floor

            floor_y = level.get_floor_y(self.player.current_floor)

            # if this is the first step onto the ladder set y to the top rung
            dims = self.player.get_image_idle_dims()
            foot_y = self.player.y + dims[1]
            if foot_y == floor_y:
                # target_y = y_of_top_rung - dims[1]
                target_y = self.player.in_ladder_top_rung_y - dims[1]
            self.player.move(target_x, target_y, DIR_DOWN)

            # if reached bottom of ladder
            y_of_floor_below = level.get_floor_y(floor_number)
            # dims = player.get_image_idle_dims()
            # foot_y = player.y + dims[1]
            # normal down is to check the floor below
            if self.player.current_floor < self.player.target_floor or self.player.target_floor == -1:
                floor_number = self.player.current_floor + 1
            # if switching from up to down check the current floor
            else:
                floor_number = self.player.current_floor
            y_of_floor_below = level.get_floor_y(floor_number)
            dims = self.player.get_image_idle_dims()
            foot_y = self.player.y + dims[1]
            # print("DOWN: floor with ladder =", floor_number, "checking foot_y =", foot_y, " and y_of_floor_below =", y_of_floor_below)
            if foot_y >= y_of_floor_below:
                self.player.current_floor = self.player.target_floor
                # player.y = y_of_floor_below - dims[1]  # ensures the feet are exactly on the floor y
                target_y = y_of_floor_below - dims[1]
                self.player.move(target_x, target_y, DIR_NO_MOVE)  # ensures the feet are exactly on the floor y
                self.player.is_up = False
                self.player.is_standing = True
                self.player.is_in_ladder = False
                self.player.in_ladder_min_x = -1
                self.player.in_ladder_max_x = -1
                self.player.in_ladder_min_y = -1
                self.player.in_ladder_max_y = -1
                self.player.in_ladder_top_rung_y = -1
                self.player.target_floor = -1
                # print("bottom of ladder")

            self.player.is_left = False
            self.player.is_right = False
            # player.is_sliding = False
            self.player.walkCount = 0
    def event_move_up(self):
        """Processes the move up event"""

        level = self.levels[self.player.current_level]
        target_x, target_y, target_hit_box = self.player.calc_move_result(DIR_UP, level.difficulty_multiplier)
        dims = self.player.get_image_idle_dims()
        # x = player.x + (dims[0] // 2)
        # y = player.y + dims[1]
        # x_pos, y_pos = player.get_character_position()
        # x_pos += (dims[0] // 2)
        # y_pos += dims[1]

        # normal going up use the current floor (ladders are stored at the floor below and go up)
        if self.player.current_floor > self.player.target_floor or self.player.target_floor == -1:  # " or player.is_down is True:
            floor_number = self.player.current_floor
        # switched from down to up
        elif self.player.current_floor == self.player.target_floor and self.player.is_down is False:
            floor_number = self.player.current_floor + 1
        # switching from down to up
        else:
            floor_number =self. player.target_floor

        y_of_top_rung = level.get_ladder_top_rung_y(floor_number)
        if (self.player.y + dims[1] == y_of_top_rung):
            target_in_ladder = True
            # ladder_hit_box = (-1, -1, -1, -1)    # should replace this with the actual ladder coords
            ladder_hit_box = level.get_ladder_coords(floor_number, target_x,
                                                     target_y)  # returns the coords not hitbox but close enough
        else:
            target_in_ladder, ladder_hit_box = level.is_player_move_in_ladder(target_hit_box, floor_number)
            # print("UP: floor with ladder =", floor_number, "target_in_ladder =", target_in_ladder)

        if target_in_ladder is True or self.player.is_in_ladder is True:

            # if entering ladder set ladder info
            if self.player.is_in_ladder is False:
                self.player.is_in_ladder = True
                # ladder_coords = level.get_ladder_coords(floor_number, x_pos, y_pos)  # changed to getting coords from call to is_player_move_in_ladder()
                if ladder_hit_box[0] != -1:
                    # player.in_ladder_min_x = ladder_coords[0]
                    # player.in_ladder_max_x = ladder_coords[2]
                    # player.in_ladder_min_y = ladder_coords[1]
                    # player.in_ladder_max_y = ladder_coords[3]
                    self.player.in_ladder_min_x = ladder_hit_box[0]
                    self.player.in_ladder_max_x = ladder_hit_box[0] + ladder_hit_box[2]
                    self.player.in_ladder_min_y = ladder_hit_box[1]
                    self.player.in_ladder_max_y = ladder_hit_box[1] + ladder_hit_box[3]
                    y_of_top_rung = level.get_ladder_top_rung_y(floor_number)
                    self.player.in_ladder_top_rung_y = y_of_top_rung

            # starting up set target to floor above
            if self.player.target_floor == -1:
                self.player.target_floor = self.player.current_floor - 1
            # if switching from down to up so set to floor we just left (the one above)
            elif self.player.is_down == True:
                self.player.target_floor = self.player.target_floor - 1

            self.player.move(target_x, target_y, DIR_UP)

            # if reached top of ladder
            # normal up is to check the floor above
            if self.player.current_floor > self.player.target_floor:
                floor_number = self.player.current_floor - 1
                # print("normal up floor_number =", floor_number)
            # if switching from down to up check the current floor
            else:
                floor_number = self.player.current_floor
                # print("switched from Down to Up floor_number =", floor_number)

            # check if reached top of ladder
            y_of_floor_above = level.get_floor_y(floor_number)
            dims = self.player.get_image_idle_dims()
            foot_y = self.player.y + dims[1]
            # print("UP: floor with ladder =", floor_number, "checking foot_y =", foot_y, " and y_of_floor_above =", y_of_floor_above)
            if foot_y <= y_of_floor_above:
                self.player.current_floor = self.player.target_floor
                target_y = y_of_floor_above - dims[1]
                self.player.move(target_x, target_y, DIR_NO_MOVE)  # ensures the feet are exactly on the floor y
                self.player.is_up = False
                self.player.is_standing = True
                self.player.is_in_ladder = False
                self.player.in_ladder_min_x = -1
                self.player.in_ladder_max_x = -1
                self.player.in_ladder_min_y = -1
                self.player.in_ladder_max_y = -1
                self.player.in_ladder_top_rung_y = -1
                self.player.target_floor = -1
                # print("top of ladder")
        else:
            self.player.is_jumping = True

        self.player.is_left = False
        self.player.is_right = False
        # player.is_sliding = False
        self.player.walkCount = 0

    def event_move_set_to_standing(self):
        """Performs the set to standing action"""

        self.player.is_standing = True
        self.player.is_left = False
        self.player.is_right = False
        self.player.walkCount = 0

    def action_continue_jump(self):
        """Performs the continue jumping action"""

        if self.player.facing_direction == DIR_LEFT:
            direction = DIR_LEFT
        else:
            direction = DIR_RIGHT
        self.player.jump_move(direction)

    def action_enemy_touching_player(self, enemy_type):
        """Performs the enemy touching player action - changes score etc"""

        score_change = 0

        if self.tumbleweed_hit_pause == 0:
            match enemy_type:
                case constants.CHARACTER_TYPE_TUMBLEWEED_1:
                    score_change = SCORE_TUMBLEWEED_1
                case constants.CHARACTER_TYPE_TUMBLEWEED_2:
                    score_change = SCORE_TUMBLEWEED_2
                case constants.CHARACTER_TYPE_TUMBLEWEED_3:
                    score_change = SCORE_TUMBLEWEED_3
                case constants.CHARACTER_TYPE_TUMBLEWEED_4:
                    score_change = SCORE_TUMBLEWEED_4
                case constants.CHARACTER_TYPE_THUG_1:
                    score_change = SCORE_THUG_1
                case constants.CHARACTER_TYPE_SKELETON_1:
                    score_change = SCORE_SKELETON_1

            self.player.score += score_change

            self.sound_grunt.play()
            self.show_message_count = 1
            self.show_message_text = str(score_change)

    def action_player_touching_loot(self, loot):
        """Performs the player touching loot action - changes score etc"""

        level = self.levels[self.player.current_level]
        level.action_player_touching_loot(self.player, loot)
        self.total_loot_grabbed += 1

        sound_loot.play()

    def action_player_shot_enemy(self, enemy_id, projectile):
        """Performs the player shot enemy action - changes score etc"""

        # print("hit!")
        level = self.levels[self.player.current_level]
        level.remove_enemy(enemy_id)
        self.total_enemies_shot += 1
        self.bullets.pop(self.bullets.index(projectile))

        self.sound_grunt.play()

    def action_player_touching_portal(self, portal_id):
        """Performs the player using a portal action"""

        level = self.levels[self.player.current_level]
        new_level_id = level.get_portal_target(portal_id)
        print("Level change to ", new_level_id)
        self.player.current_level = new_level_id
        self.sound_portal.play()

        # setup player on new level
        new_level = self.levels[new_level_id]
        self.player.current_floor = new_level.get_num_floors()
        self.player.position_player_on_new_level()

    def action_shoot(self):
        """Performs the shoot action"""

        if self.player.shoot_dir == DIR_LEFT:
            facing = -1
        else:
            facing = 1

        if self.player.num_bullets > 0:
            width = self.player.get_character_width()
            height = self.player.get_character_width()
            projectile_id = 101
            # x = round(player.x + width // 2)
            # y = round(player.y + height // 2)
            x_pos, y_pos = self.player.get_character_position()
            x_pos = round(x_pos + width // 2)
            y_pos = round(y_pos + height // 2)
            bullet = Projectile(PROJECTILE_HERO_BULLET, projectile_id, x_pos, y_pos, 6, (0, 0, 0), facing)
            self.bullets.append(bullet)
            bullet.projectile_sound()
            self.player.num_bullets -= 1
            print("Shoot!")

    def action_create_enemy(self):
        """Creates an enemy - i.e. used for testing new enemies instead of waiting for random creation"""

        enemy_type = CHARACTER_TYPE_TUMBLEWEED_4
        level = self.levels[self.player.current_level]
        enemy_id = len(level.enemies)
        num_lives = 1
        num_bullets = 999
        floor_id = self.player.current_floor
        enemy = Character(enemy_type, enemy_id, -100, -100, num_lives, num_bullets, level.level_id, floor_id)
        height = enemy.get_character_height()
        x = 100
        y = level.get_floor_y(floor_id) - height
        direction = self.player.facing_direction
        enemy.move(x, y, direction)

        print("creating enemy type: ", enemy_type)
        level.enemies.append(enemy)

