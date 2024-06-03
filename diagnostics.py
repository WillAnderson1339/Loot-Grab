
from constants import *

def show_diagnotics(win, font, show_portal_info, levels, player):
    colour = COLOUR_DIAGNOSTICS
    start_x = 50
    start_y = 10
    row_height = 20
    col_1_width = 170
    col_2_width = 325
    col_3_width = 200

    level = levels[player.current_level]

    x = start_x
    y = start_y

    # column 1 shows Floor info
    num_levels = len(levels)
    text = "# of Levels: " + str(num_levels)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    text = "Current Info: "
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    num_floors = len(level.floors)
    text = "  # of Floors: " + str(num_floors)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    num_enemies = level.num_enemies # need to change to the len of the enemies list
    text = "  # of Enemies: " + str(num_enemies)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    y += row_height
    num_enemies = len(level.enemies) # need to change to the len of the enemies list
    text = "  Enemies Alive: " + str(num_enemies)
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    # column 2 shows either portal or ladder info
    if show_portal_info == True:
        # column 2 shows portal info
        x = start_x + col_1_width
        y = start_y
        num_portals = len(level.portals)
        for i in range(num_portals):
            portal = level.portals[i]
            portal_id = portal.portal_id
            portal_x = portal.x
            portal_y = portal.y
            if portal.direction == UP:
                direction_str = "Up"
            elif portal.direction == DOWN:
                direction_str = "Down"
            else:
                direction_str = "unknown"
            text = "Portal ID " + str(portal_id) + ": (" + str(portal_x) + ", " + str(portal_y) + ") direction " + direction_str
            print_text = font.render(text, 1, colour)
            win.blit(print_text, (x, y))
            y += row_height
    else:
        # column 2 shows ladder info
        x = start_x + col_1_width
        y = start_y
        num_floors = len(level.floors)
        for floor_id in range(num_floors):
            ladders = level.get_floor_ladder_coords(floor_id)
            for j in range(len(ladders)):
                ladder = ladders[j]

                ladder_x1 = ladder[0]
                ladder_y1 = ladder[1]
                ladder_x2 = ladder[2]
                ladder_y2 = ladder[3]

                wind_direction = level.get_floor_wind_direction(floor_id)
                if wind_direction == DIR_LEFT:
                    wind_direction_str = " L"
                elif wind_direction == DIR_RIGHT:
                    wind_direction_str = " R"
                else:
                    wind_direction_str = " ?"


                text = "Fl " + str(floor_id) + wind_direction_str + " ldr " + str(j) + ":  (" + str(ladder_x1) + ", " + str(
                    ladder_y1) + ")  (" + str(ladder_x2) + ", " + str(ladder_y2) + ")"
                print_text = font.render(text, 1, colour)
                win.blit(print_text, (x, y))
                y += row_height

    """
    """

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
    text = "P Top Left:  (" + str(player.x) + ", " + str(player.y) + ")"
    print_text = font.render(text, 1, (255, 127, 0))
    win.blit(print_text, (x, y))

    y += row_height
    dims = player.get_image_idle_dims()
    text = "P Bot Right: (" + str(player.x + dims[0]) + ", " + str(player.y + dims[1]) + ")"
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))

    # y += row_height
    # text = "E Top Left:  (" + str(enemy.x) + ", " + str(enemy.y) + ")"
    # print_text = font.render(text, 1, (255, 127, 0))
    # win.blit(print_text, (x, y))
    #
    # y += row_height
    # dims = player.get_image_idle_dims()
    # text = "E Bot Right: (" + str(enemy.x + dims[0]) + ", " + str(enemy.y + dims[1]) + ")"
    # print_text = font.render(text, 1, colour)
    # win.blit(print_text, (x, y))

    '''
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
    '''

    # column 4 shows misc info
    if show_portal_info == True:
        x += col_3_width
        y = start_y
        text = "is_sliding:  " + str(player.is_sliding)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))

        y += row_height
        text = "Diff Multiplier:  " + str(level.difficulty_multiplier)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))

        y += row_height
        text = "Speed:  " + str(level.difficulty_multiplier * player.vel)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))

        y += row_height
        text = "walk/step Count:  " + str(player.walkCount) + "/" + str(player.slideCount) + "/" + str(player.slide_ended)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))
    else:
        x += col_3_width
        y = start_y
        text = "is_jump/ladder:  " + str(player.is_jumping) + " / " + str(player.is_in_ladder)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))

        y += row_height
        text = "is_l/r:  " + str(player.is_left) + " / " + str(player.is_right)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))

        y += row_height
        text = "is_u/d:  " + str(player.is_up) + " / " + str(player.is_down)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))

        y += row_height
        text = "is_stand/slide:  " + str(player.is_standing) + " / "+ str(player.is_sliding)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))

        y += row_height
        text = "facing:  " + str(player.facing_direction)
        print_text = font.render(text, 1, colour)
        win.blit(print_text, (x, y))


'''
    y += row_height
    text = "KP_m:  " + str(kp_key_states[KP_m])
    print_text = font.render(text, 1, colour)
    win.blit(print_text, (x, y))
'''
