import pygame

from constants import *
from diagnostics import *
from Player import *
from Projectile import *
from Level import *

images_background = [pygame.image.load('res/Backgrounds/Field 3.png'), pygame.image.load('res/Backgrounds/Field 4.png'),
                     pygame.image.load('res/Backgrounds/Mountains 1.png'), pygame.image.load('res/Backgrounds/Mountains 4.png'),
                     pygame.image.load('res/Backgrounds/Mountains 5.png'), pygame.image.load('res/Backgrounds/Mountains 6.png'),
                     pygame.image.load('res/Backgrounds/Mountains 7.png'),
                     pygame.image.load('res/Backgrounds/Lava 1.png')]

clock = pygame.time.Clock()

pygame.init()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Loot Grab")

levels = []

font = pygame.font.SysFont('consolas', 15, False)

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
    # goblin.draw(win)

    # draw bullets
    for bullet in bullets:
        bullet.draw(win)

    # show diagnostics (function will check for show/not show)
    if SHOW_DIAGNOSTICS is True:
        show_diagnotics(win, font, levels, player)

    pygame.display.update()


def check_kp_pause_counts():
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

def create_random_level(level_id):
    num_floors = random.randint(2, 2)
    num_enemies = random.randint(2, 8)
    num_up_portals = random.randint(1, 1)
    num_down_portals = random.randint(1, 1)
    background = level_id
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colour = (red, green, blue)
    level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour)
    levels.append(level)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # set up the levels
    # create first level (the first level is special - it has no down portal)
    level_id = 0
    num_floors = 2
    num_enemies = 2
    num_up_portals = 1
    num_down_portals = 0
    background = 0
    colour = (25, 125, 150)
    level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour)
    levels.append(level)

    num_levels_to_create = 2
    # create random levels - could change this to planned levels with colours, backgrounds, enemies etc
    for i in range(num_levels_to_create):
        create_random_level(i + 1)

    # create last level (the last level is special - it has no up portal)
    level_id = len(levels)
    num_floors = 2
    num_enemies = 6
    num_up_portals = 0
    num_down_portals = 1
    background = 2
    colour = (150, 175, 75)
    level = Level(level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour)
    levels.append(level)

    '''
    level_id = 0
    num_floors = 2 #4
    num_enemies = 5
    num_up_portals = 1
    num_down_portals = 0
    background = 0
    colour = (100, 150, 200)
    level = Level(portal_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour)
    levels.append(level)

    portal_id = 1
    num_floors = 3
    num_enemies = 8
    num_up_portals = 1
    num_down_portals = 2
    background = 1
    colour = (50, 75, 175)
    level = Level(portal_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour)
    levels.append(level)

    portal_id = 2
    num_floors = 2
    num_enemies = 8
    num_up_portals = 2
    num_down_portals = 2
    background = 2
    colour = (100, 50, 200)
    level = Level(portal_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour)
    levels.append(level)

    portal_id = 3
    num_floors = 2
    num_enemies = 6
    num_up_portals = 0
    num_down_portals = 2
    background = 2
    colour = (150, 175, 75)
    level = Level(portal_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour)
    levels.append(level)
    '''

    # set up the player
    x = WINDOW_WIDTH - 100
    y = WINDOW_HEIGHT - (68 + FLOOR_HEIGHT + 4)
    current_level = 0
    level = levels[current_level]
    current_floor = len(level.floors) - 1
    player = Player(x, y, current_level, current_floor)

    bullets = []

    # key press pause counts. use KP_ constants to access list
    kp_key_states = [0, 0, 0, 0, 0]

    print("Hellow World!")

    run = True
    while run:
        clock.tick(27)

        # check if they are quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        if keys[pygame.K_SPACE] and kp_key_states[KP_SPACE] == 0:
            if player.is_left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append(
                    Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 6, (0, 0, 0), facing))

            kp_key_states[KP_SPACE] = 1
            print("Shoot!")

        if keys[pygame.K_LEFT] and player.x > player.vel:
            x = player.x - player.vel
            y = player.y
            level = levels[player.current_level]
            portal_id = level.is_location_in_portal(x, y)

            # if not in portal just allow move
            if portal_id == -1:
                player.x -= player.vel
                player.is_left = True
                player.is_right = False
                player.is_standing = False
            else:
                new_level_id = level.get_portal_target(portal_id)
                print("Level change to ", new_level_id)
                player.current_level = new_level_id

                # setup player on new level
                player.x = WINDOW_WIDTH - 100
                player.y = WINDOW_HEIGHT - (68 + FLOOR_HEIGHT + 4)
                level = levels[new_level_id]
                player.current_floor = len(level.floors) - 1

        elif keys[pygame.K_RIGHT] and player.x < WINDOW_WIDTH:  # - player.width - player.vel:
            x = player.x + player.vel
            y = player.y
            level = levels[player.current_level]
            portal_id = level.is_location_in_portal(x, y)

            # if not in portal just allow move
            if portal_id == -1:
                player.x += player.vel
                player.is_right = True
                player.is_left = False
                player.is_standing = False
            else:
                new_level_id = level.get_portal_target(portal_id)
                print("Level change to ", new_level_id)
                player.current_level = new_level_id

                # setup player on new level
                player.x = WINDOW_WIDTH - 100
                player.y = WINDOW_HEIGHT - (68 + FLOOR_HEIGHT + 4)
                level = levels[new_level_id]
                player.current_floor = len(level.floors) - 1

        elif keys[pygame.K_DOWN] and kp_key_states[KP_DOWN] == 0:
            level = levels[player.current_level]
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
            in_ladder = level.is_location_in_ladder(floor_number, x, y)
            if in_ladder == True:
                floor_y = level.get_floor_y(player.current_floor)
                # if this is the first step set y to the top rung
                if player.y + dims[1] == floor_y:
                    player.y = y_of_top_rung - dims[1]
                else:
                    player.y += RUNG_HEIGHT

                # starting down set target to floor below
                if player.target_floor == -1:
                    player.target_floor = player.current_floor + 1
                # if switching from up to down set to floor we just left (the one above)
                elif player.is_up is True:
                    player.target_floor = player.target_floor + 1 # player.current_floor

                # set direction to down
                player.is_up = False
                player.is_down = True

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
                    player.y = y_of_floor_below - dims[1]  # ensures the feet are exactly on the floor y
                    player.is_up = False
                    player.is_standing = True
                    player.is_in_ladder = False
                    player.target_floor = -1

                player.is_right = False
                player.is_left = False
                player.walkCount = 0
                kp_key_states[KP_DOWN] = 1
        else:
            player.is_standing = True
            player.walkCount = 0

        if not player.is_jumping:
            if keys[pygame.K_UP] and kp_key_states[KP_UP] == 0:
                level = levels[player.current_level]
                dims = player.get_image_idle_dims()
                x = player.x + (dims[0] // 2)
                y = player.y + dims[1]

                # normal going up use the current floor (ladders are stored at the floor below and go up)
                if player.current_floor > player.target_floor or player.target_floor == -1 or player.is_down is True:
                    floor_number = player.current_floor
                # switched from down to up
                elif player.current_floor == player.target_floor and player.is_down is False:
                    floor_number = player.current_floor + 1
                # switching from down to up
                else:
                    floor_number = player.target_floor
                in_ladder = level.is_location_in_ladder(floor_number, x, y)
                if in_ladder == True:
                    player.y -= RUNG_HEIGHT
                    # starting up set target to floor above
                    if player.target_floor == -1:
                        player.target_floor = player.current_floor - 1
                    # if switching from down to up so set to floor we just left (the one above)
                    elif player.is_down == True:
                        player.target_floor = player.target_floor - 1

                    # set direction to up
                    player.is_up = True
                    player.is_down = False

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
                        player.y = y_of_floor_above - dims[1]   # ensures the feet are exactly on the floor y
                        player.is_up = False
                        player.is_standing = True
                        player.is_in_ladder = False
                        player.target_floor = -1
                else:
                    player.is_jumping = True

                player.is_right = False
                player.is_left = False
                player.walkCount = 0
                kp_key_states[KP_UP] = 1
        else:
            if player.jumpCount >= (JUMP_HEIGHT * -1):
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= (player.jumpCount ** 2) * 0.5 * neg
                player.jumpCount -= 1
            else:
                player.is_jumping = False
                player.jumpCount = JUMP_HEIGHT

        redraw_game_window(player)
    
    pygame.quit()
