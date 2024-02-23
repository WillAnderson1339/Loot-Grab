import pygame

from constants import *
from diagnostics import *
from Character import *
from Projectile import *
from Level import *

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



pygame.init()

clock = pygame.time.Clock()

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

# key press pause counts. use KP_ constants to access list
kp_key_states = [0, 0, 0, 0, 0, 0, 0, 0, 0]

font_stats = pygame.font.SysFont('comicsans', 25, True)
font_diagnostics = pygame.font.SysFont('consolas', 15, False)
font_pause = pygame.font.SysFont("comicsansms", 90)

show_diagnostics = SHOW_DIAGNOSTICS
show_portal_info = True


# num_player_lives_XXX = SCORE_START_NUM_LIVES
# num_player_bullets_XXX = SCORE_START_NUM_BULLETS

bullets = []

pause = False       # used for game over - but should implement a pause too?

def paused():
    colour = COLOUR_GAME_OVER

    x = WINDOW_WIDTH // 2
    y = WINDOW_HEIGHT // 2

    text = "Game Over! "
    print_text = font_pause.render(text, 1, colour)
    x -= print_text.get_width() // 2
    y -= print_text.get_height() // 2
    win.blit(print_text, (x, y))

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(15)


def show_stats(win, font, levels, player):
    """Displays the player game stats like lives, score, etc."""

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

    text = "Level:  " + str(player.current_level +1)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    text = "Score: " + str(player.score)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

def redraw_game_window(player):

    # draw background
    # pygame.draw.rect(win, (175,225,240), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
    level = levels[player.current_level]
    background = level.background
    win.blit(images_background[background], (0,0))

    # draw level
    level = levels[player.current_level]
    level.draw(win)
    '''
    for level in levels:
        if level.id == current_level:
            level.draw(win)
            break
    '''

    # draw characters
    player.draw(win)

    # draw bullets
    for bullet in bullets:
        bullet.draw(win)

    # show diagnostics (function will check for show/not show)
    if show_diagnostics is True:
        show_diagnotics(win, font_diagnostics, show_portal_info, levels, player, tumbleweed_hit_pause)


    else:
        show_stats(win, font_stats, levels, player)

    pygame.display.update()


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
    if kp_key_states[KP_foo] > max_pause_needed:
        kp_key_states[KP_foo] = 0
    if kp_key_states[KP_bar] > max_pause_needed:
        kp_key_states[KP_bar] = 0

def create_random_level(level_id):
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

def action_enemy_touching_player(enemy_type, player, tumbleweed_hit_pause):
    """Performs the enemy touching player action - changes score etc"""

    score_change = 0

    if tumbleweed_hit_pause == 0:
        match enemy_type:
            case constants.CHARACTER_TYPE_TUMBLEWEED_1:
                score_change = SCORE_TUMBLEWEED_1
            case constants.CHARACTER_TYPE_TUMBLEWEED_2:
                score_change = SCORE_TUMBLEWEED_2
            case constants.CHARACTER_TYPE_THUG_1:
                score_change = SCORE_THUG_1
            case constants.CHARACTER_TYPE_SKELETON_1:
                score_change = SCORE_SKELETON_1

        player.score += score_change

        sound_grunt.play()

def action_player_shot_enemy(enemy_id, projectile):
    """Performs the player shot enemy action - changes score etc"""

    # print("hit!")
    level = levels[player.current_level]
    level.remove_enemy(enemy_id)

    bullets.pop(bullets.index(projectile))

    sound_grunt.play()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # set up the levels
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
        create_random_level(i + 1)

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
                level = levels[player.current_level]
                level.check_if_spawning_enemy()


        if player.num_lives == -99:
            run = False

        # check if any key press pause counts are needed
        check_kp_pause_counts()

        # move bullets
        for bullet in bullets:
            if bullet.x < WINDOW_WIDTH and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        # move enemies
        level = levels[player.current_level]
        # level.check_if_spawning_enemy()
        hit_box_list = level.auto_move_enemies(level.difficulty_multiplier)

        # update the tumbleweed pause timer (so tumbleweed passes player and does not continually decrement score)
        if tumbleweed_hit_pause > 0:
            tumbleweed_hit_pause += 1
        if tumbleweed_hit_pause > 20:
            tumbleweed_hit_pause = 0

        # check to see if the enemy is touching the player
        for item in hit_box_list:
            rect_enemy = item[0]
            enemy_type = item[1]
            enemy_id = item[2]

            # check to see if the enemy is touching the player
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

        # shoot key
        if keys[pygame.K_SPACE] and kp_key_states[KP_SPACE] == 0:
            if player.shoot_dir == DIR_LEFT:
                facing = -1
            else:
                facing = 1

            if player.num_bullets > 0:
                width = player.get_character_width()
                height = player.get_character_width()
                projectile_id = 101
                x = round(player.x + width // 2)
                y = round(player.y + height // 2)
                bullet = Projectile(PROJECTILE_HERO_BULLET, projectile_id, x, y, 6, (0, 0, 0), facing)
                bullets.append(bullet)
                bullet.projectile_sound()
                player.num_bullets -= 1
                # sound_bullet.play()
                print("Shoot!")

            kp_key_states[KP_SPACE] = 1

        # toggle playing the music
        elif keys[pygame.K_m] and kp_key_states[KP_m] == 0:
            if playing_music is True:
                playing_music = False
                pygame.mixer.music.stop()
            else:
                playing_music = True
                pygame.mixer.music.play(-1)

            kp_key_states[KP_m] = 1

        # toggle showing the diagnostics
        elif keys[pygame.K_d] and kp_key_states[KP_d] == 0:
            if show_diagnostics is True:
                show_diagnostics = False
            else:
                show_diagnostics = True

                # toggle state of the portal or ladder info
                if show_portal_info:
                    show_portal_info = False
                else:
                    show_portal_info = True


            kp_key_states[KP_d] = 1

        #if keys[pygame.K_LEFT] and kp_key_states[KP_LEFT] == 0:
        if keys[pygame.K_LEFT]:
            # x = player.x - player.vel + 0     # -5 is to check if the player foot is in the portal (not his hat)
            # y = player.y

            # calculate move so can compare for various results before moving
            level = levels[player.current_level]
            target_x, target_y, target_hit_box = player.calc_move_result(DIR_LEFT, level.difficulty_multiplier)
            # portal_id = level.is_location_in_portal(x, y)
            portal_id = level.is_location_in_portal(target_x, target_y)

            # if not in portal just allow move
            if portal_id == -1 or player.is_jumping is True:
                if portal_id != -1 and player.is_jumping is True:
                    print("in portal but jumping so moving instead!")

                # if in ladder restrict horizontal movement to within the ladder
                width = player.get_character_width()
                if player.is_in_ladder is False or target_x >= player.in_ladder_min_x - (width * 0.3):
                    player.move(target_x, target_y, DIR_LEFT)

                # check to see if walked into any loot
                loot = level.is_player_in_loot(player)
                if loot.loot_id != -1:
                    level.action_player_touching_loot(loot, player)

            else:
                new_level_id = level.get_portal_target(portal_id)
                print("Level change to ", new_level_id)
                player.current_level = new_level_id
                sound_portal.play()

                # setup player on new level
                new_level = levels[new_level_id]
                player.current_floor = new_level.get_num_floors()
                player.position_player_on_new_level()

            kp_key_states[KP_LEFT] = 1


        #elif keys[pygame.K_RIGHT] and kp_key_states[KP_RIGHT] == 0:
        elif keys[pygame.K_RIGHT]:
            # calculate move so can compare for various results before moving
            level = levels[player.current_level]
            target_x, target_y, target_hit_box = player.calc_move_result(DIR_RIGHT, level.difficulty_multiplier)
            portal_id = level.is_location_in_portal(target_x, target_y)

            # if not in portal just allow move
            if portal_id == -1 or player.is_jumping is True:
                if portal_id != -1 and player.is_jumping is True:
                    print("in portal but jumping so moving instead!")

                # if in ladder restrict horizontal movement to within the ladder
                width = player.get_character_width()
                if player.is_in_ladder is False or target_x <= player.in_ladder_max_x - (width * 0.5):
                    player.move(target_x, target_y, DIR_RIGHT)

                # check to see if walked into any loot
                loot = level.is_player_in_loot(player)
                if loot.loot_id != -1:
                    level.action_player_touching_loot(loot, player)
                    sound_loot.play()

            else:
                new_level_id = level.get_portal_target(portal_id)
                print("Level change to ", new_level_id)
                player.current_level = new_level_id
                sound_portal.play()

                # setup player on new level
                level = levels[new_level_id]
                player.current_floor = len(level.floors) - 1
                player.position_player_on_new_level()

            kp_key_states[KP_RIGHT] = 1

        elif keys[pygame.K_DOWN] and kp_key_states[KP_DOWN] == 0:
            # calculate move so can compare for various results before moving
            level = levels[player.current_level]
            target_x, target_y, target_hit_box = player.calc_move_result(DIR_DOWN, level.difficulty_multiplier)
            dims = player.get_image_idle_dims()
            x = player.x + (dims[0] // 2)
            y = player.y + dims[1]
            y_of_top_rung = level.get_ladder_top_rung_y(player.current_floor + 1)

            # normal going down (ladders are stored at the floor below and go up)
            if player.current_floor < player.target_floor or player.target_floor == -1: # or player.is_up is True:
                floor_number = player.current_floor + 1
            # switched from up to down
            elif player.current_floor == player.target_floor and player.is_up is False:
                floor_number = player.current_floor
            # switching from up to down
            else:
                floor_number = player.current_floor

            # in_ladder = level.is_location_in_ladder(floor_number, x, y)
            in_ladder = level.is_player_move_in_ladder(target_hit_box, floor_number)
            if in_ladder == True:
                # set ladder info
                if player.is_in_ladder is False:
                    player.is_in_ladder = True
                    ladder_coords = level.get_ladder_coords(floor_number, x, y)
                    if ladder_coords[0] != -1:
                        player.in_ladder_min_x = ladder_coords[0]
                        player.in_ladder_max_x = ladder_coords[2]
                        player.in_ladder_min_y = ladder_coords[1]
                        player.in_ladder_max_y = ladder_coords[3]

                # starting down set target to floor below
                if player.target_floor == -1:
                    player.target_floor = player.current_floor + 1
                # if switching from up to down set to floor we just left (the one above)
                elif player.is_up is True:
                    player.target_floor = player.target_floor + 1 # player.current_floor

                floor_y = level.get_floor_y(player.current_floor)
                # if this is the first step set y to the top rung
                if player.y + dims[1] == floor_y:
                    # player.y = y_of_top_rung - dims[1]
                    target_y = y_of_top_rung - dims[1]
                # else:
                #     player.y += RUNG_HEIGHT
                player.move(target_x, target_y, DIR_DOWN)

                # set direction to down
                # player.is_up = False
                # player.is_down = True

                # if reached bottom of ladder
                y_of_floor_below = level.get_floor_y(floor_number)
                dims = player.get_image_idle_dims()
                foot_y = player.y + dims[1]
                # normal down is to check the floor below
                if player.current_floor < player.target_floor or player.target_floor == -1:
                    floor_number = player.current_floor + 1
                # if switching from up to down check the current floor
                else:
                    floor_number = player.current_floor
                y_of_floor_below = level.get_floor_y(floor_number)
                dims = player.get_image_idle_dims()
                foot_y = player.y + dims[1]
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
                    player.target_floor = -1

                player.is_right = False
                player.is_left = False
                player.walkCount = 0
                kp_key_states[KP_DOWN] = 1
        else:
            # if the left key press is being pressed but is being supressed don't set to standing
            #if keys[pygame.K_LEFT] and kp_key_states[KP_LEFT] == 0:
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                player.is_standing = True
                player.is_left = False
                player.is_right = False
                player.walkCount = 0

        if not player.is_jumping:
            if keys[pygame.K_UP] and kp_key_states[KP_UP] == 0:
                level = levels[player.current_level]
                target_x, target_y, target_hit_box = player.calc_move_result(DIR_UP, level.difficulty_multiplier)
                dims = player.get_image_idle_dims()
                x = player.x + (dims[0] // 2)
                y = player.y + dims[1]

                # normal going up use the current floor (ladders are stored at the floor below and go up)
                if player.current_floor > player.target_floor or player.target_floor == -1: #" or player.is_down is True:
                    floor_number = player.current_floor
                # switched from down to up
                elif player.current_floor == player.target_floor and player.is_down is False:
                    floor_number = player.current_floor + 1
                # switching from down to up
                else:
                    floor_number = player.target_floor

                # in_ladder = level.is_location_in_ladder(floor_number, x, y)
                y_of_top_rung = level.get_ladder_top_rung_y(floor_number)
                if (player.y + dims[1] == y_of_top_rung):
                    in_ladder = True
                else:
                    in_ladder = level.is_player_move_in_ladder(target_hit_box, floor_number)

                if in_ladder == True:
                    # set ladder info
                    if player.is_in_ladder is False:
                        player.is_in_ladder = True
                        ladder_coords = level.get_ladder_coords(floor_number, x, y)
                        if ladder_coords[0] != -1:
                            player.in_ladder_min_x = ladder_coords[0]
                            player.in_ladder_max_x = ladder_coords[2]
                            player.in_ladder_min_y = ladder_coords[1]
                            player.in_ladder_max_y = ladder_coords[3]

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
                    # if switching from down to up check the current floor
                    else:
                        floor_number = player.current_floor

                    # check if reached top of ladder
                    y_of_floor_above = level.get_floor_y(floor_number)
                    dims = player.get_image_idle_dims()
                    foot_y = player.y + dims[1]
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
                        player.target_floor = -1
                else:
                    player.is_jumping = True

                player.is_right = False
                player.is_left = False
                player.walkCount = 0
                kp_key_states[KP_UP] = 1
        else:
            if player.is_left:
                direction = DIR_LEFT
            else:
                direction = DIR_RIGHT
            player.jump_move(direction)

        redraw_game_window(player)
    
    pygame.quit()
