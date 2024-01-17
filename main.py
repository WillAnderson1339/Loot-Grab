import pygame

from constants import *
from Player import *
from Projectile import *
from Level import *



clock = pygame.time.Clock()

pygame.init()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Loot Grab")

font = pygame.font.SysFont('consolas', 15, False)

levels = []


def redraw_game_window():

    # draw background
    pygame.draw.rect(win, (175,225,240), (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))

    # draw level
    for level in levels:
        level.draw(win)

    # draw characters
    player.draw(win)
    # goblin.draw(win)

    # draw bullets
    for bullet in bullets:
        bullet.draw(win)

    if SHOW_DIAGNOSTICS == True:
        show_diagnotics()

    pygame.display.update()

def show_diagnotics():
    colour = COLOUR_DIAGNOSTICS
    start_x = 50
    start_y = 10
    row_height = 20
    col_1_width = 170
    col_2_width = 325

    x = start_x
    y = start_y

    # column 1 shows Floor info
    num_levels = len(levels)
    text = "# of Levels: " + str(num_levels)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    level = levels[player.current_level]
    num_floors = len(level.floors)
    text = "# of Floors: " + str(num_floors)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    num_enemies = level.num_enemies # need to change to the len of the enemies list
    text = "# of Enemies: " + str(num_enemies)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    num_enemies = 0 # need to change to the len of the enemies list
    text = "Enemies Alive: " + str(num_enemies)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    # column 2 shows ladder info
    x = start_x + col_1_width
    y = start_y
    for i in range(num_floors):
        ladders = level.get_floor_ladder_coords(i)
        for j in range(len(ladders)):
            foo = ladders[j]

            ladder_x1 = foo[0]
            ladder_y1 = foo[1]
            ladder_x2 = foo[2]
            ladder_y2 = foo[3]
            text = "Fl " + str(i) + " ldr " + str(j) + ":  (" + str(ladder_x1) + ", " + str(ladder_y1) + ")  (" + str(ladder_x2) + ", " + str(ladder_y2) + ")"
            print_text = font.render(text, 1, colour)
            win.blit(print_text, (x, y))
            y += row_height

    # column 3 shows current player info
    x = start_x + col_1_width + col_2_width
    y = start_y
    text = "Level: " + str(player.current_level)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    text = "Floor: " + str(player.current_floor) + "  Target: " + str(player.target_floor)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    text = "Top Left:  (" + str(player.x) + ", " + str(player.y) + ")"
    print_text = font.render(text, 1, (255, 127, 0))
    win.blit(print_text, (x, y))

    y += row_height
    dims = player.get_image_idle_dims()
    text = "Bot Right: (" + str(player.x + dims[0]) + ", " + str(player.y + dims[1]) + ")"
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    idle = player.get_image_idle_dims()
    text = "Idle: (" + str(idle[0]) + ", " + str(idle[1]) + ")"
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    idle = player.get_image_run_dims()
    text = "Run:  (" + str(idle[0]) + ", " + str(idle[1]) + ")"
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # set up the levels

    num_floors = 4
    num_enemies = 5
    #colour = (50, 75, 175)
    colour = (100, 150, 200)
    level = Level(num_floors, num_enemies, colour)
    levels.append(level)

    # set up the player
    current_level = 0
    current_floor = num_floors
    player = Player(WINDOW_WIDTH - 100, WINDOW_HEIGHT - (68 + FLOOR_HEIGHT + 4), current_level, current_floor)

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
            player.x -= player.vel
            player.is_left = True
            player.is_right = False
            player.is_standing = False
        elif keys[pygame.K_RIGHT] and player.x < WINDOW_WIDTH - player.width - player.vel:
            player.x += player.vel
            player.is_right = True
            player.is_left = False
            player.is_standing = False
        elif keys[pygame.K_DOWN] and kp_key_states[KP_DOWN] == 0:
            level = levels[player.current_level]
            dims = player.get_image_idle_dims()
            x = player.x + (dims[0] // 2)
            y = player.y + dims[1]
            y_of_top_rung = level.get_ladder_top_rung_y(player.current_floor + 1)
            y_of_2nd_top_rung = level.get_ladder_2nd_top_rung_y(player.current_floor + 1)
            y_of_current_floor = level.get_floor_y(player.current_floor)
            if player.is_up == True:
                floor_number = player.current_floor
            else:
                floor_number = player.current_floor + 1
            in_ladder = level.is_location_in_ladder(floor_number, x, y)
            #print("Position (", x, ",", y, ") In Ladder:", in_ladder, " top rung", y_of_top_rung, " 2nd top rung", y_of_2nd_top_rung, "  floor =", player.current_floor)
            if in_ladder == True:
                floor_y = level.get_floor_y(player.current_floor)
                #print("y = ", player.y + dims[1], " floor_y = ", floor_y)
                # if this is the first step set y to the top rung
                if player.y + dims[1] == floor_y:
                    player.y = y_of_top_rung - dims[1]
                else:
                    player.y += RUNG_HEIGHT
                player.is_in_ladder = True
                player.is_up = False
                player.is_down = True
                player.target_floor = player.current_floor + 1

                # if reached bottom of ladder
                #coords = level.get_floor_ladder_coords(player.current_floor)
                y_of_floor_below = level.get_floor_y(floor_number)
                dims = player.get_image_idle_dims()
                foot_y = player.y + dims[1]
                print("checking foot y", foot_y, "and floor below y", y_of_floor_below)
                if foot_y >= y_of_floor_below:
                    player.current_floor = level.get_floor_id(y_of_floor_below)
                    player.y = y_of_floor_below - dims[1]
                    player.is_down = False
                    player.is_standing = True
                    player.is_in_ladder = False
                    player.target_floor = -1
                    print("Reached bottom of floor! New current floor is", player.current_floor)
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

                if player.current_floor > player.target_floor:      # normal going up
                    floor_number = player.current_floor
                elif player.current_floor == player.target_floor:   # switched from down to up
                    floor_number = player.current_floor + 1
                else:                                               # switching from down to up
                    floor_number = player.target_floor
                in_ladder = level.is_location_in_ladder(floor_number, x, y)
                if in_ladder == True:
                    player.y -= RUNG_HEIGHT
                    # starting up set target to floor above
                    if player.target_floor == -1:
                        player.target_floor = player.current_floor - 1
                    # if switching from down to up set floor we just left (the one above)
                    elif player.is_down == True:
                        player.target_floor = player.current_floor

                    # change direction to up
                    player.is_up = True
                    player.is_down = False

                    # if reached top of ladder
                    # normal up is to check the floor above
                    if player.current_floor > player.target_floor:
                        floor_number = player.current_floor - 1
                    # if switching from down to up check the current floor
                    else:
                        floor_number = player.current_floor
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

        redraw_game_window()
    
    pygame.quit()
