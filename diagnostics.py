
from constants import *

def show_diagnotics(win, font, levels, player):
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
