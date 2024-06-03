import pygame

from constants import *
from diagnostics import *
from Character import *
from Projectile import *
from Level import *

from Game import *

pygame.init()
clock = pygame.time.Clock()

"""1 - done
images_background = [
    pygame.image.load('res/Backgrounds/Mountains 5.png'),
    pygame.image.load('res/Backgrounds/Mountains 4.png'),
    pygame.image.load('res/Backgrounds/Mountains 7.png'),
    pygame.image.load('res/Backgrounds/Field 4.png'),
    pygame.image.load('res/Backgrounds/Field 3.png'),
    pygame.image.load('res/Backgrounds/Mountains 1.png'),
    pygame.image.load('res/Backgrounds/Mountains 6.png'),
    pygame.image.load('res/Backgrounds/Lava 1.png')]

images_objects = [
    pygame.image.load('res/Objects/Heart_1__000.png'),
    pygame.image.load('res/Objects/Bullet_1__000.png')]


sound_bullet = pygame.mixer.Sound('res/bullet.mp3')
hitSound = pygame.mixer.Sound('res/hit.mp3')
sound_portal = pygame.mixer.Sound('res/portal.mp3')
sound_grunt = pygame.mixer.Sound('res/grunt-2.mp3')

# setup music
music = pygame.mixer.music.load('res/music.mp3')
playing_music = False
if playing_music is True:
    pygame.mixer.music.play(-1)
else:
    pygame.mixer.music.stop()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Loot Grab")

levels = []
"""

# key press pause counts. use KP_ constants to access list
kp_key_states = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""1 - done
font_stats = pygame.font.SysFont('comicsans', 25, True)
font_diagnostics = pygame.font.SysFont('consolas', 15, False)
font_pause = pygame.font.SysFont("comicsansms", 80)
font_pause_stats = pygame.font.SysFont("comicsansms", 30)
font_pause_neg_score_change = pygame.font.SysFont('comicsans', 25, True)

show_diagnostics = SHOW_DIAGNOSTICS
show_portal_info = True

show_message_count = 0
show_message_text = ""

# num_player_lives_XXX = SCORE_START_NUM_LIVES
# num_player_bullets_XXX = SCORE_START_NUM_BULLETS

bullets = []

total_loot = 0
total_enemies = 0
total_loot_grabbed = 0
total_enemies_shot = 0
"""
pause = False       # used for game over - but should implement a pause too?

def paused():
    """Used to pause the game. Triggered by Game Over or pressing the 'p' key"""

    game.paused()
    """ 2 - done
    global playing_music
    global pygame
    # if music was playing turn stop it while paused
    if playing_music is True:
        pygame.mixer.music.stop()

    # background for message
    x = WINDOW_WIDTH * .25
    y = WINDOW_HEIGHT * .25
    width = WINDOW_WIDTH * .5
    height = WINDOW_HEIGHT * .4
    message_rect = (x, y, width, height)
    pygame.draw.rect(win, COLOUR_MESSAGE_BACKGROUND, message_rect, 0, 10)

    # message title
    if player.num_lives == -99:
        title = "Game Over! "
        colour = COLOUR_GAME_OVER
    else:
        title = "Paused"
        colour = COLOUR_PAUSE

    x = message_rect[0] + (message_rect[2] // 2)
    y = message_rect[1]

    print_title = font_pause.render(title, 1, colour)
    x -= print_title.get_width() // 2
    # y += print_title.get_height()
    win.blit(print_title, (x, y))

    global total_enemies
    global total_enemies_shot
    global total_loot
    global total_loot_grabbed

    text = "Stats:"
    print_text = font_pause_stats.render(text, 1, colour)
    x = message_rect[0] + (message_rect[2] // 2)
    x -= 200
    y += print_title.get_height()
    win.blit(print_text, (x, y))

    # x += 30

    text = "  Total Loot " + str(total_loot) + "  Grabbed " + str(total_loot_grabbed)
    print_text = font_pause_stats.render(text, 1, colour)
    x = message_rect[0] + (message_rect[2] // 2)
    x -= 190
    y += print_text.get_height()
    win.blit(print_text, (x, y))

    text = "  Total Enemies " + str(total_enemies) + "  Shot " + str(total_enemies_shot)
    print_text = font_pause_stats.render(text, 1, colour)
    # x = WINDOW_WIDTH // 2
    # x -= print_text.get_width() // 2
    y += print_text.get_height()
    win.blit(print_text, (x, y))

    """

    global pause

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()

            # pressing the 'p' key again will unpause the game
            if keys[pygame.K_p] and kp_key_states[KP_p] == 0 and game.player.num_lives != -99:
                pause = False
                kp_key_states[KP_p] = 0

        pygame.display.update()
        clock.tick(15)

    # if music was playing turn it back on
    if game.is_playing_music is True:
        pygame.mixer.music.play(-1)

"""1 - done

def show_stats(win, font, levels, player):
    #Displays the player game stats like lives, score, etc.

    # show the player lives as hearts
    start_x = WINDOW_WIDTH - 200
    start_y = 10
    row_height = 30

    # show the hearts for lives
    object_index = IMAGE_OBJECT_LIFE_HEART
    width = images_objects[object_index].get_width()
    width += 4
    x = start_x - 15 - (player.num_lives * width)
    y = start_y + 10

    for num_lives in range(player.num_lives):
        win.blit(images_objects[object_index], (x, y))
        x += width

    # show the bullets for number of bullets left
    object_index = IMAGE_OBJECT_HERO_BULLET
    width = images_objects[object_index].get_width()
    width += 8
    x = start_x - 15 - (player.num_bullets * width)
    y = start_y + 10 + row_height
    for num_bullets in range(player.num_bullets):
        win.blit(images_objects[object_index], (x, y))
        x += width

    # show the player level and score info
    colour = COLOUR_STATS
    start_x = WINDOW_WIDTH - 200
    start_y = 10
    col_1_width = 170
    col_2_width = 325

    level = levels[player.current_level]

    x = start_x
    y = start_y

    text = "Level:  " + str(player.current_level + 1)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    text = "Score: " + str(player.score)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

def redraw_game_window(player):

    level = levels[player.current_level]

    # draw background
    background = level.background
    win.blit(images_background[background], (0, 0))

    # draw level
    level.draw(win)

    # draw characters
    player.draw(win)

    # draw player message
    global show_message_count
    global show_message_text
    global font_pause_neg_score_change
    if show_message_count > 0:
        player_x, player_y = player.get_character_position()
        player_width = player.get_character_width()
        text = show_message_text
        colour = COLOUR_NEG_SCORE_TEXT
        print_text = font_pause_neg_score_change.render(text, 1, colour)

        # background for message
        width = print_text.get_width() + 20
        height = print_text.get_height() + 4
        x = player_x + (player_width // 2) - (width // 2)
        y = player_y - height - 2
        # width = 40
        # height = 20
        message_rect = (x, y, width, height)
        pygame.draw.rect(win, COLOUR_MESSAGE_BACKGROUND, message_rect, 0, 10)

        # message text
        x += 10
        y += 2
        win.blit(print_text, (x, y))

        show_message_count += 1
        if show_message_count >= MESSAGE_TEXT_TIMER_LIMIT:
            show_message_count = 0

    # draw bullets
    for bullet in bullets:
        bullet.draw(win)

    # show diagnostics (function will check for show/not show)
    if show_diagnostics is True:
        show_diagnotics(win, font_diagnostics, show_portal_info, levels, player)
    else:
        show_stats(win, font_stats, levels, player)

    pygame.display.update()

"""

def check_kp_pause_counts():
    '''
    NOTE:
        need to look into another method for this. Consider pygame.key.get_repeat()
        https://www.pygame.org/docs/ref/key.html#pygame.key.get_repeat
    '''

    # uses a count to pause so multiple key press events are not processed when the user only intended a single press
    max_pause_needed = 3

    # if pausing key increment by 1
    if kp_key_states[KP_UP] > 0:
        kp_key_states[KP_UP] += 1
    if kp_key_states[KP_DOWN] > 0:
        kp_key_states[KP_DOWN] += 1
    if kp_key_states[KP_LEFT] > 0:
        kp_key_states[KP_LEFT] += 1
    if kp_key_states[KP_RIGHT] > 0:
        kp_key_states[KP_RIGHT] += 1
    if kp_key_states[KP_SPACE] > 0:
        kp_key_states[KP_SPACE] += 1
    if kp_key_states[KP_m] > 0:
        kp_key_states[KP_m] += 1
    if kp_key_states[KP_d] > 0:
        kp_key_states[KP_d] += 1
    if kp_key_states[KP_s] > 0:
        kp_key_states[KP_s] += 1
    if kp_key_states[KP_p] > 0:
        kp_key_states[KP_p] += 1
    if kp_key_states[KP_e] > 0:
        kp_key_states[KP_e] += 1
        # print("key e state = ", str(kp_key_states[KP_e]))
    if kp_key_states[KP_foo] > 0:
        kp_key_states[KP_foo] += 1
    if kp_key_states[KP_bar] > 0:
        kp_key_states[KP_bar] += 1

    # if reached max pause rest to 0
    if kp_key_states[KP_UP] > max_pause_needed:
        kp_key_states[KP_UP] = 0
    if kp_key_states[KP_DOWN] > max_pause_needed:
        kp_key_states[KP_DOWN] = 0
    if kp_key_states[KP_LEFT] > max_pause_needed:
        kp_key_states[KP_LEFT] = 0
    if kp_key_states[KP_RIGHT] > max_pause_needed:
        kp_key_states[KP_RIGHT] = 0
    if kp_key_states[KP_SPACE] > max_pause_needed:
        kp_key_states[KP_SPACE] = 0
    if kp_key_states[KP_m] > max_pause_needed:
        kp_key_states[KP_m] = 0
    if kp_key_states[KP_d] > max_pause_needed:
        kp_key_states[KP_d] = 0
    if kp_key_states[KP_s] > max_pause_needed:
        kp_key_states[KP_s] = 0
    if kp_key_states[KP_p] > max_pause_needed:
        kp_key_states[KP_p] = 0
    if kp_key_states[KP_e] > max_pause_needed:
        kp_key_states[KP_e] = 0
    if kp_key_states[KP_foo] > max_pause_needed:
        kp_key_states[KP_foo] = 0
    if kp_key_states[KP_bar] > max_pause_needed:
        kp_key_states[KP_bar] = 0

"""1 - done

def create_random_level(levels, level_id):
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
    level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour, difficulty_multiplier)
    levels.append(level)
"""
"""1 - done

def create_levels(levels):
    #Creates the levels

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
    levels.append(level)

    num_levels_to_create = 6
    # create random levels - could change this to planned levels with colours, backgrounds, enemies etc
    for i in range(num_levels_to_create):
        create_random_level(levels, i + 1)

    # create last level (the last level is special - it has no up portal)
    level_id = len(levels)
    num_floors = 5
    num_enemies = 6
    num_up_portals = 0
    num_down_portals = 1
    background = 7
    colour = (150, 175, 75)
    difficulty_multiplier = 1.0 + (0.2 * level_id)
    level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour, difficulty_multiplier)
    levels.append(level)

def action_enemy_touching_player(enemy_type, player, tumbleweed_hit_pause):
    #Performs the enemy touching player action - changes score etc

    score_change = 0

    if tumbleweed_hit_pause == 0:
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

        player.score += score_change

        sound_grunt.play()
        global show_message_count
        global show_message_text
        show_message_count = 1
        show_message_text = str(score_change)

def action_player_touching_loot(player, loot):
    #Performs the player touching loot action - changes score etc

    global total_loot_grabbed

    level = levels[player.current_level]

    level.action_player_touching_loot(player, loot)

    sound_loot.play()

    total_loot_grabbed += 1


def action_player_shot_enemy(enemy_id, projectile):
    #Performs the player shot enemy action - changes score etc

    global total_enemies_shot

    # print("hit!")
    level = levels[player.current_level]
    level.remove_enemy(enemy_id)

    total_enemies_shot += 1

    bullets.pop(bullets.index(projectile))

    sound_grunt.play()

def action_player_touching_portal(player):
    #Performs the player using a portal action

    new_level_id = level.get_portal_target(portal_id)
    print("Level change to ", new_level_id)
    player.current_level = new_level_id
    sound_portal.play()

    # setup player on new level
    new_level = levels[new_level_id]
    player.current_floor = new_level.get_num_floors()
    player.position_player_on_new_level()

"""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """ main function """

    # create the game object
    game = Game()

    """2 - done
    
    # create the levels
    create_levels(levels)

    # set the totals (for showing the score)
    for level in levels:
        total_loot += level.count_loot()
        total_enemies += level.count_enemies()

    # set up the player
    x = WINDOW_WIDTH - 100
    y = WINDOW_HEIGHT - (68 + FLOOR_HEIGHT + 4)
    current_level = 0
    level = levels[current_level]
    current_floor = len(level.floors) - 1
    player_type = CHARACTER_TYPE_HERO_1
    player_id = 1000
    num_lives = SCORE_START_NUM_LIVES
    num_bullets = SCORE_START_NUM_BULLETS
    player = Character(player_type, player_id, x, y, num_lives, num_bullets, current_level, current_floor)
    player.position_player_on_new_level()

    # for dev coding work - create sample loot
    # level = levels[current_level]
    # x = 100
    # y = level.get_floor_y(player.current_floor) - 30
    # loot_testing = Loot(1339, x, y, LOOT_DIAMOND, DIR_LEFT)
    # level.loots.append(loot_testing)
    """

    tumbleweed_hit_pause = 0

    print("Hellow World!")

    # set timer to spawn enemies
    pygame.time.set_timer(TIMER_EVENT_ENEMY_SPAWN_CHECK, TIMER_INTERVAL_ENEMY_SPAWN_CHECK)

    run = True
    while run:
        clock.tick(27)

        # check events
        for event in pygame.event.get():

            # check if they are quitting
            if event.type == pygame.QUIT:
                run = False

            # timer event
            elif event.type == TIMER_EVENT_ENEMY_SPAWN_CHECK:
                game.event_spawn_enemy()
                """4 need  - done
                level = levels[player.current_level]
                spawned_enemy = level.check_if_spawning_enemy()
                if spawned_enemy is True:
                    total_enemies += 1
                """

        """4 need - pending
        if player.num_lives == -99:
            run = False
        """

        # check if any key press pause counts are needed
        check_kp_pause_counts()

        """4 need - done
        level = levels[player.current_level]
        
        # move bullets
        for bullet in bullets:
            if bullet.x < WINDOW_WIDTH and bullet.x > 0:
                bullet.x += bullet.vel * level.difficulty_multiplier
            else:
                bullets.pop(bullets.index(bullet))
        """

        keys = pygame.key.get_pressed()

        game.run()

        """4 need - done
        
        # move enemies
        hit_box_list = level.auto_move_enemies(level.difficulty_multiplier)

        # update the tumbleweed pause timer (so tumbleweed passes player and does not continually decrement score)
        if tumbleweed_hit_pause > 0:
            tumbleweed_hit_pause += 1
        if tumbleweed_hit_pause > 20:
            tumbleweed_hit_pause = 0

        # check to see if anything is touching something
        for item in hit_box_list:
            rect_enemy = item[0]
            enemy_type = item[1]
            enemy_id = item[2]

            # bullets do not hit tumbleweeds
            bullets_ignore_types = [CHARACTER_TYPE_TUMBLEWEED_1, CHARACTER_TYPE_TUMBLEWEED_2, CHARACTER_TYPE_TUMBLEWEED_3, CHARACTER_TYPE_TUMBLEWEED_4]
            if enemy_type not in bullets_ignore_types:
                # check to see if an enemy is hit by a shot
                for bullet in bullets:
                    rect_projectile = bullet.get_hit_rect()
                    if do_rectangles_overlap(rect_enemy, rect_projectile) is True:
                        action_player_shot_enemy(enemy_id, bullet)

            # check to see if the enemy is touching the player
            rect_player = player.hit_box
            if do_rectangles_overlap(rect_enemy, rect_player) is True:
                action_enemy_touching_player(enemy_type, player, tumbleweed_hit_pause)
                tumbleweed_hit_pause = 1

        # if below zero score -1 life
        if player.score < 0 and player.num_lives != -99:
            player.num_lives -= 1
            player.score = 0
            if player.num_lives == 0:
                print("Game Over!")
                player.num_lives = -99
                pause = True
                paused()
            else:
                current_floor = len(level.floors) - 1
                player.current_floor = current_floor
                player.position_player_on_new_level()

        """
        # if had pressed the slide key and now released it
        if (game.player.is_sliding is True or game.player.slide_ended is True) and not keys[pygame.K_s]:
            print("had pressed the slide key and now released it")
            game.player.slide_ended = False
            game.player.slide_move(False)
            game.player.play_sound(SOUND_TYPE_PLAYER_SLIDE, False)

        # shoot key
        if keys[pygame.K_SPACE] and kp_key_states[KP_SPACE] == 0:
            game.action_shoot()
            """3 added to game
            if player.shoot_dir == DIR_LEFT:
                facing = -1
            else:
                facing = 1

            if player.num_bullets > 0:
                width = player.get_character_width()
                height = player.get_character_width()
                projectile_id = 101
                # x = round(player.x + width // 2)
                # y = round(player.y + height // 2)
                x_pos, y_pos = player.get_character_position()
                x_pos = round(x_pos + width // 2)
                y_pos = round(y_pos + height // 2)
                bullet = Projectile(PROJECTILE_HERO_BULLET, projectile_id, x_pos, y_pos, 6, (0, 0, 0), facing)
                bullets.append(bullet)
                bullet.projectile_sound()
                player.num_bullets -= 1
                print("Shoot!")
            """

            kp_key_states[KP_SPACE] = 1

        # sliding
        elif keys[pygame.K_s] and kp_key_states[KP_s] == 0 and game.player.slide_ended == False:
            """2
            player.slide_move()
            """
            game.player.slide_move()

            kp_key_states[KP_s] = 1

        # pausing
        elif keys[pygame.K_p] and kp_key_states[KP_p] == 0:
            game.pause = True
            game.paused()

            kp_key_states[KP_p] = 1

        # creating a new enemy (for testing)
        elif keys[pygame.K_e] and kp_key_states[KP_e] == 0:
            if DEV_MODE == True:
                game.action_create_enemy()
                """3 added to game - done
                enemy_type = CHARACTER_TYPE_TUMBLEWEED_4
                level = levels[player.current_level]
                enemy_id = len(level.enemies)
                num_lives = 1
                num_bullets = 999
                floor_id = player.current_floor
                enemy = Character(enemy_type, enemy_id, -100, -100, num_lives, num_bullets, level.level_id, floor_id)
                height = enemy.get_character_height()
                x = 100
                y = level.get_floor_y(floor_id) - height
                direction = player.facing_direction
                enemy.move(x, y, direction)

                print("creating enemy type: ", enemy_type)
                level.enemies.append(enemy)
                """

                kp_key_states[KP_e] = 1

        # toggle playing the music
        elif keys[pygame.K_m] and kp_key_states[KP_m] == 0:
            game.event_toggle_music()
            """4 need - done
            if playing_music is True:
                playing_music = False
                pygame.mixer.music.stop()
            else:
                playing_music = True
                pygame.mixer.music.play(-1)

            # for development sometimes need to clear all enemies (so they stop hitting the player!)
            # should move this to its own key but using 'm' just for ease
            if DEV_MODE == True:
                level = levels[player.current_level]
                level.remove_all_enemies()
            """

            kp_key_states[KP_m] = 1

        # toggle showing the diagnostics
        elif keys[pygame.K_d] and kp_key_states[KP_d] == 0:
            game.event_toggle_diagnostics()
            """4 need - done
            if show_diagnostics is True:
                show_diagnostics = False
            else:
                show_diagnostics = True

                # toggle state of the portal or ladder info
                if show_portal_info:
                    show_portal_info = False
                else:
                    show_portal_info = True
            """

            kp_key_states[KP_d] = 1

        #if keys[pygame.K_LEFT] and kp_key_states[KP_LEFT] == 0:
        if keys[pygame.K_LEFT]:
            game.event_move_left()
            """2 - done
            # calculate move so can compare for various results before moving
            level = levels[player.current_level]
            target_x, target_y, target_hit_box = player.calc_move_result(DIR_LEFT, level.difficulty_multiplier)
            # portal_id = level.is_location_in_portal(target_x, target_y)
            portal_id = level.is_player_in_portal(player)

            # if not in portal just allow move
            if portal_id == -1 or player.is_jumping is True or player.is_sliding is True:
                if portal_id != -1 and player.is_jumping is True:
                    # print("in portal but jumping or sliding so moving instead!")
                    pass

                # if in ladder restrict horizontal movement to within the ladder
                width = player.get_character_width()
                if player.is_in_ladder is False or target_x >= player.in_ladder_min_x - (width * 0.3):
                    player.move(target_x, target_y, DIR_LEFT)

                # check to see if walked into any loot
                loot = level.is_player_in_loot(player)
                if loot.loot_id != -1:
                    # level.action_player_touching_loot(loot, player)
                    action_player_touching_loot(player, loot)

            else:
                action_player_touching_portal(player)
            """

            kp_key_states[KP_LEFT] = 1


        #elif keys[pygame.K_RIGHT] and kp_key_states[KP_RIGHT] == 0:
        elif keys[pygame.K_RIGHT]:
            game.event_move_right()
            """2 - done
            # calculate move so can compare for various results before moving
            level = levels[player.current_level]
            target_x, target_y, target_hit_box = player.calc_move_result(DIR_RIGHT, level.difficulty_multiplier)
            # portal_id = level.is_location_in_portal(target_x, target_y)
            portal_id = level.is_player_in_portal(player)

            # if not in portal just allow move
            if portal_id == -1 or player.is_jumping is True or player.is_sliding is True:
                if portal_id != -1 and player.is_jumping is True:
                    # print("in portal but jumping or sliding so moving instead!")
                    pass

                # if in ladder restrict horizontal movement to within the ladder
                width = player.get_character_width()
                if player.is_in_ladder is False or target_x <= player.in_ladder_max_x - (width * 0.5):
                    player.move(target_x, target_y, DIR_RIGHT)

                # check to see if walked into any loot
                loot = level.is_player_in_loot(player)
                if loot.loot_id != -1:
                    action_player_touching_loot(player, loot)

            else:
                action_player_touching_portal(player)
            """

            kp_key_states[KP_RIGHT] = 1

        elif keys[pygame.K_DOWN] and kp_key_states[KP_DOWN] == 0:
            game.event_move_down()
            """2 - done
            # calculate move so can compare for various results before moving
            level = levels[player.current_level]
            target_x, target_y, target_hit_box = player.calc_move_result(DIR_DOWN, level.difficulty_multiplier)
            dims = player.get_image_idle_dims()
            # x_pos, y_pos = player.get_character_position()
            # x_pos += (dims[0] // 2)
            # y_pos += dims[1]
            # y_of_top_rung = level.get_ladder_top_rung_y(player.current_floor + 1)

            # normal going down (ladders are stored at the floor below and go up)
            if player.current_floor < player.target_floor or player.target_floor == -1: # or player.is_up is True:
                floor_number = player.current_floor + 1
                # print("normal down floor_number =", floor_number)
            # switched from up to down
            # elif player.current_floor == player.target_floor and player.is_up is False:
            elif player.current_floor == player.target_floor:
                if player.is_up is False:
                    floor_number = player.current_floor
                else:
                    floor_number = player.current_floor + 1
                # print("switched from up to down AA floor_number =", floor_number)
            # switching from up to down
            else:
                floor_number = player.current_floor
                # print("switched from up to down BB floor_number =", floor_number)

            target_in_ladder, ladder_coords = level.is_player_move_in_ladder(target_hit_box, floor_number)
            # print("DOWN: floor with ladder =", floor_number, "target_in_ladder =", target_in_ladder)
            if target_in_ladder == True:
                # set ladder info
                if player.is_in_ladder is False:
                    player.is_in_ladder = True
                    # ladder_coords = level.get_ladder_coords(floor_number, x_pos, y_pos)  # changed to getting coords from call to is_player_move_in_ladder()
                    if ladder_coords[0] != -1:
                        # player.in_ladder_min_x = ladder_coords[0]
                        # player.in_ladder_max_x = ladder_coords[2]
                        # player.in_ladder_min_y = ladder_coords[1]
                        # player.in_ladder_max_y = ladder_coords[3]
                        player.in_ladder_min_x = ladder_coords[0]
                        player.in_ladder_max_x = ladder_coords[0] + ladder_coords[2]
                        player.in_ladder_min_y = ladder_coords[1]
                        player.in_ladder_max_y = ladder_coords[1] + ladder_coords[3]
                        y_of_top_rung = level.get_ladder_top_rung_y(floor_number)
                        player.in_ladder_top_rung_y = y_of_top_rung

                # starting down set target to floor below
                if player.target_floor == -1:
                    player.target_floor = player.current_floor + 1
                # if switching from up to down set to floor we just left (the one above)
                elif player.is_up is True:
                    player.target_floor = player.target_floor + 1 # player.current_floor

                floor_y = level.get_floor_y(player.current_floor)

                # if this is the first step onto the ladder set y to the top rung
                dims = player.get_image_idle_dims()
                foot_y = player.y + dims[1]
                if foot_y == floor_y:
                    # target_y = y_of_top_rung - dims[1]
                    target_y = player.in_ladder_top_rung_y - dims[1]
                player.move(target_x, target_y, DIR_DOWN)

                # if reached bottom of ladder
                y_of_floor_below = level.get_floor_y(floor_number)
                # dims = player.get_image_idle_dims()
                # foot_y = player.y + dims[1]
                # normal down is to check the floor below
                if player.current_floor < player.target_floor or player.target_floor == -1:
                    floor_number = player.current_floor + 1
                # if switching from up to down check the current floor
                else:
                    floor_number = player.current_floor
                y_of_floor_below = level.get_floor_y(floor_number)
                dims = player.get_image_idle_dims()
                foot_y = player.y + dims[1]
                # print("DOWN: floor with ladder =", floor_number, "checking foot_y =", foot_y, " and y_of_floor_below =", y_of_floor_below)
                if foot_y >= y_of_floor_below:
                    player.current_floor = player.target_floor
                    # player.y = y_of_floor_below - dims[1]  # ensures the feet are exactly on the floor y
                    target_y = y_of_floor_below - dims[1]
                    player.move(target_x, target_y, DIR_NO_MOVE)  # ensures the feet are exactly on the floor y
                    player.is_up = False
                    player.is_standing = True
                    player.is_in_ladder = False
                    player.in_ladder_min_x = -1
                    player.in_ladder_max_x = -1
                    player.in_ladder_min_y = -1
                    player.in_ladder_max_y = -1
                    player.in_ladder_top_rung_y = -1
                    player.target_floor = -1
                    # print("bottom of ladder")

                player.is_left = False
                player.is_right = False
                # player.is_sliding = False
                player.walkCount = 0
            """
            kp_key_states[KP_DOWN] = 1

        else:
            # if the left key press is being pressed but is being suppressed don't set to standing
            #if keys[pygame.K_LEFT] and kp_key_states[KP_LEFT] == 0:
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                game.event_move_set_to_standing()
                """ added to game - done
                player.is_standing = True
                player.is_left = False
                player.is_right = False
                player.walkCount = 0
                """

        if not game.player.is_jumping:
            if keys[pygame.K_UP] and kp_key_states[KP_UP] == 0:
                game.event_move_up()
                """2 - done
                level = levels[player.current_level]
                target_x, target_y, target_hit_box = player.calc_move_result(DIR_UP, level.difficulty_multiplier)
                dims = player.get_image_idle_dims()
                # x = player.x + (dims[0] // 2)
                # y = player.y + dims[1]
                # x_pos, y_pos = player.get_character_position()
                # x_pos += (dims[0] // 2)
                # y_pos += dims[1]

                # normal going up use the current floor (ladders are stored at the floor below and go up)
                if player.current_floor > player.target_floor or player.target_floor == -1: #" or player.is_down is True:
                    floor_number = player.current_floor
                # switched from down to up
                elif player.current_floor == player.target_floor and player.is_down is False:
                    floor_number = player.current_floor + 1
                # switching from down to up
                else:
                    floor_number = player.target_floor

                y_of_top_rung = level.get_ladder_top_rung_y(floor_number)
                if (player.y + dims[1] == y_of_top_rung):
                    target_in_ladder = True
                    # ladder_hit_box = (-1, -1, -1, -1)    # should replace this with the actual ladder coords
                    ladder_hit_box = level.get_ladder_coords(floor_number, target_x, target_y)    # returns the coords not hitbox but close enough
                else:
                    target_in_ladder, ladder_hit_box = level.is_player_move_in_ladder(target_hit_box, floor_number)
                    # print("UP: floor with ladder =", floor_number, "target_in_ladder =", target_in_ladder)

                if target_in_ladder is True or player.is_in_ladder is True:

                    # if entering ladder set ladder info
                    if player.is_in_ladder is False:
                        player.is_in_ladder = True
                        # ladder_coords = level.get_ladder_coords(floor_number, x_pos, y_pos)  # changed to getting coords from call to is_player_move_in_ladder()
                        if ladder_hit_box[0] != -1:
                            # player.in_ladder_min_x = ladder_coords[0]
                            # player.in_ladder_max_x = ladder_coords[2]
                            # player.in_ladder_min_y = ladder_coords[1]
                            # player.in_ladder_max_y = ladder_coords[3]
                            player.in_ladder_min_x = ladder_hit_box[0]
                            player.in_ladder_max_x = ladder_hit_box[0] + ladder_hit_box[2]
                            player.in_ladder_min_y = ladder_hit_box[1]
                            player.in_ladder_max_y = ladder_hit_box[1] + ladder_hit_box[3]
                            y_of_top_rung = level.get_ladder_top_rung_y(floor_number)
                            player.in_ladder_top_rung_y = y_of_top_rung


                    # starting up set target to floor above
                    if player.target_floor == -1:
                        player.target_floor = player.current_floor - 1
                    # if switching from down to up so set to floor we just left (the one above)
                    elif player.is_down == True:
                        player.target_floor = player.target_floor - 1

                    player.move(target_x, target_y, DIR_UP)

                    # if reached top of ladder
                    # normal up is to check the floor above
                    if player.current_floor > player.target_floor:
                        floor_number = player.current_floor - 1
                        # print("normal up floor_number =", floor_number)
                    # if switching from down to up check the current floor
                    else:
                        floor_number = player.current_floor
                        # print("switched from Down to Up floor_number =", floor_number)

                    # check if reached top of ladder
                    y_of_floor_above = level.get_floor_y(floor_number)
                    dims = player.get_image_idle_dims()
                    foot_y = player.y + dims[1]
                    # print("UP: floor with ladder =", floor_number, "checking foot_y =", foot_y, " and y_of_floor_above =", y_of_floor_above)
                    if foot_y <= y_of_floor_above:
                        player.current_floor = player.target_floor
                        target_y = y_of_floor_above - dims[1]
                        player.move(target_x, target_y, DIR_NO_MOVE) # ensures the feet are exactly on the floor y
                        player.is_up = False
                        player.is_standing = True
                        player.is_in_ladder = False
                        player.in_ladder_min_x = -1
                        player.in_ladder_max_x = -1
                        player.in_ladder_min_y = -1
                        player.in_ladder_max_y = -1
                        player.in_ladder_top_rung_y = -1
                        player.target_floor = -1
                        # print("top of ladder")
                else:
                    player.is_jumping = True

                player.is_left = False
                player.is_right = False
                # player.is_sliding = False
                player.walkCount = 0
                """
                kp_key_states[KP_UP] = 1
        else:
            game.action_continue_jump()
            """2 - done
            if game.player.facing_direction == DIR_LEFT:
                direction = DIR_LEFT
            else:
                direction = DIR_RIGHT
            game.player.jump_move(direction)
            #player.jump_move(direction)
            """

        game.draw()
        """2 - done
        redraw_game_window(player)
        """

    pygame.quit()

