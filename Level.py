import pygame
import random

from constants import *
from Portal import *

class Ladder(object):
    def __init__(self, x, y, width, height, colour, direction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.direction = direction

        self.num_rungs = self.height // RUNG_HEIGHT
        if direction == UP:
            self.y_of_top_rung = self.y + (RUNG_HEIGHT * self.num_rungs * direction)
            self.y_of_2nd_top_rung = self.y_of_top_rung - (RUNG_HEIGHT * direction)
        else:
            self.y_of_top_rung = self.y + (RUNG_HEIGHT * self.num_rungs * direction)
            self.y_of_2nd_top_rung = self.y_of_top_rung - (RUNG_HEIGHT * direction)


    def draw(self, win):
        if self.direction == UP:
            # draw the vertical lines
            point_start = (self.x, self.y)
            point_end   = (self.x, self.y - self.height)
            #print(point_start, point_end)
            pygame.draw.line(win, self.colour,point_start, point_end, 3)
            point_start = (self.x + LADDER_WIDTH, self.y)
            point_end   = (self.x + LADDER_WIDTH, self.y - self.height)
            pygame.draw.line(win, self.colour,point_start, point_end, 3)

            # draw the rungs
            x_start = self.x
            y_start = self.y
            num_rungs = self.height // RUNG_HEIGHT
            for i in range(num_rungs):
                point_start = (x_start, y_start - (RUNG_HEIGHT * (i + 1)))
                point_end = (x_start + LADDER_WIDTH, y_start - (RUNG_HEIGHT * (i + 1)))
                pygame.draw.line(win, self.colour, point_start, point_end, 3)



class Level(object):
    def __init__(self, level_id, num_floors, num_enemies, num_up_portals, num_down_portals, colour):
        self.level_id = level_id
        self.num_floors = num_floors
        self.num_enemies = num_enemies
        self.num_up_portals = num_up_portals
        self.num_down_portals = num_down_portals
        self.colour = colour

        self.floors = []
        self.portals = []

        self.create_floors()
        self.create_portals()

    def create_floors(self):
        # create the floor objects and append them to the floor List
        for i in range(self.num_floors):
            colour = self.colour
            x = 0
            y = (WINDOW_HEIGHT // (self.num_floors + 1)) * (i + 1)
            width = WINDOW_WIDTH
            height = FLOOR_HEIGHT
            rect = (x, y, width, height)
            floor_id = i
            ladders = []

            self.floors.append((floor_id, colour, rect, ladders))

        # add the bottom floor
        colour = (20, 115, 80)
        x = 0
        y = WINDOW_HEIGHT - 10
        width = WINDOW_WIDTH
        height = FLOOR_HEIGHT
        rect = (x, y, width, height)
        id = self.num_floors
        ladders = []

        self.floors.append((id, colour, rect, ladders))

        # Once all the floors are create the ladders can be added
        self.init_ladders()

    def init_ladders(self):
        ladder_locations = []

        num = len(ladder_locations)

        for item in self.floors:
            # don't add ladders to the top floor
            if item[0] == 0:
                continue

            num_ladders = random.randint(1,2)
            #num_ladders = 3
            ladder_locations.clear()

            # find an x co-ordinate for this ladder
            for i in range(num_ladders):
                x = random.randint(10, WINDOW_WIDTH - 150)

                found_dupe = False
                keep_looking = True
                counter = 0
                while keep_looking == True and len(ladder_locations) > 0:
                    # ensure this ladder X location is not too close to any existing ladder locations on this floor
                    for ladder_location in ladder_locations:
                        if x > ladder_location[0] and x < ladder_location[1]:
                            found_dupe = True
                            break
                    if found_dupe == True:
                        x = random.randint(10, WINDOW_WIDTH - 150)
                    else:
                        counter += 1
                    found_dupe = False

                    if (counter == len(ladder_locations)):
                        keep_looking = False

                y = item[2][1]
                width = LADDER_WIDTH
                id = item[0]
                id_floor_above = id - 1
                row_above = self.floors[id_floor_above]
                y_row_above = row_above[2][1]
                height = y - y_row_above
                # height = 165
                colour = self.colour
                # colour = (255, 0, 0)

                ladder = Ladder(x, y, width, height, colour, UP)
                item[3].append(ladder)
                ladder_locations.append((x - LADDER_WIDTH - 20, x + LADDER_WIDTH + 20))  # 20 padding so not too close

    def create_portals(self):
        # create the up portals
        width = PORTAL_WIDTH
        height = PORTAL_HEIGHT
        colour = PORTAL_COLOUR
        direction = UP
        for portal_id in range(self.num_up_portals):
            # if only 1 up portal place it on the top floor at the left most edge
            if self.num_up_portals == 1:
                x = PORTAL_WIDTH // 2 * -1
                y = self.get_floor_y(0) - PORTAL_HEIGHT
            # else randomize floor and location
            else:
                min_x = PORTAL_WIDTH // 2 * -1
                max_x = WINDOW_WIDTH + (PORTAL_WIDTH // 2) + 10
                x = random.randint(min_x, max_x)
                num_floors = len(self.floors)
                floor_id = random.randint(0, num_floors)
                y = self.get_floor_y(floor_id) - PORTAL_HEIGHT

            portal = Portal(portal_id, x, y, width, height, colour, direction)
            self.portals.append(portal)

        # create the down portals
        width = PORTAL_WIDTH
        height = PORTAL_HEIGHT
        colour = PORTAL_COLOUR
        direction = DOWN
        for portal_id in range(self.num_down_portals):
            # if only 1 up portal place it on the bottom floor at the right most edge
            if self.num_down_portals == 1:
                x = WINDOW_WIDTH - (PORTAL_WIDTH // 2) + 10
                num_floors = len(self.floors)
                y = self.get_floor_y(num_floors - 1) - PORTAL_HEIGHT
            # else randomize floor and location
            else:
                min_x = PORTAL_WIDTH // 2 * -1
                max_x = WINDOW_WIDTH + (PORTAL_WIDTH // 2) + 10
                x = random.randint(min_x, max_x)
                num_floors = len(self.floors)
                floor_id = random.randint(0, num_floors)
                y = self.get_floor_y(floor_id) - PORTAL_HEIGHT

            portal = Portal(portal_id, x, y, width, height, colour, direction)
            self.portals.append(portal)

    def draw(self, win):
        # draw the floors
        for floor in self.floors:
            colour = floor[1]
            rect = floor[2]
            pygame.draw.rect(win, colour, rect)

            # draw the ladders
            ladders = floor[3]
            for ladder in ladders:
                ladder.draw(win)

        # draw the portals
        for portal in self.portals:
            portal.draw(win)

    def foo(self):
        if self.num_floors == -1:
            pass

        for item in self.floors:
            bar = 12

            if bar == 10:
                something = 3
            else:
                something = 5

            mystring = "hello world"

    def get_num_floor_ladders(self, floor_id):
        num_ladders = -1
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    num_ladders = len(floor[3])
        return num_ladders

    def get_ladder_top_rung_y(self, floor_id):
        top_rung_y = -1
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    for ladder in floor[3]:
                        top_rung_y = ladder.y_of_top_rung
        return top_rung_y

    def get_ladder_2nd_top_rung_y(self, floor_id):
        top_2nd_rung_y = -1
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    for ladder in floor[3]:
                        top_2nd_rung_y = ladder.y_of_2nd_top_rung
        return top_2nd_rung_y

    def get_floor_y(self, floor_id):
        y = -1

        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    rect = floor[2]
                    y = rect[1]
                    break

        return y
    def get_floor_id(self, y):
        floor_id = -1

        if (y >= 0 and y <= WINDOW_HEIGHT):
            for floor in self.floors:
                rect = floor[2]
                if rect[1] == y:
                    floor_id = floor[0]
                    break

        return floor_id

    def get_floor_ladder_coords(self, floor_id):
        ladder_coords = []

        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    for ladder in floor[3]:
                        x1 = ladder.x
                        y1 = ladder.y
                        x2 = ladder.x + ladder.width
                        y2 = ladder.y + (ladder.height * ladder.direction)
                        ladder_coords.append((x1, y1, x2, y2))
        return ladder_coords

    def is_location_in_ladder(self, floor_id, x, y):
        in_ladder = False

        ladder_coords = self.get_floor_ladder_coords(floor_id)
        for coord in ladder_coords:
            # print("Checking (", x, ",", y, ") with coord (", coord[0], ",", coord[1], ",", coord[2], ",", coord[3], ")")
            if x >= coord[0] and x <= coord[2] and y <= coord[1] and y >= coord[3]:
                in_ladder = True
                break
        return in_ladder
    def get_portal_coords(self):
        portal_coords = []

        for portal in self.portals:
            x1 = portal.x
            y1 = portal.y
            x2 = portal.x + portal.width
            y2 = portal.y + portal.height
            portal_coords.append((x1, y1, x2, y2))
        return portal_coords

    def is_location_in_portal(self, x, y):
        portal_id = -1

        i = 0
        portal_coords = self.get_portal_coords()
        for coord in portal_coords:
            if x >= coord[0] and x <= coord[2] and y >= coord[1] and y <= coord[3]:
                portal_id = i
                break
            i += 1

        return portal_id

    def get_portal_target(self, portal_id):
        target_level = -1

        for portal in self.portals:
            if portal_id == portal.portal_id:
                if portal.direction == UP:
                    target_level = self.level_id + 1
                else:
                    target_level = self.level_id - 1
                break

        return target_level