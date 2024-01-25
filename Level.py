import pygame
import random

from constants import *
from utils import *
from Floor import *
from Ladder import *
from Portal import *
from Loot import *


class Level(object):
    def __init__(self, level_id, num_floors, num_enemies, num_up_portals, num_down_portals, background, colour):
        self.level_id = level_id
        self.num_floors = num_floors
        self.num_enemies = num_enemies
        self.num_up_portals = num_up_portals
        self.num_down_portals = num_down_portals
        self.background = background
        self.colour = colour

        self.floors = []
        self.portals = []
        self.loots = []

        self.create_floors()
        self.create_portals()
        self.create_loot()

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

            #self.floors.append((floor_id, colour, rect, ladders))
            floor = Floor(floor_id, colour, rect, ladders)
            self.floors.append(floor)

        # add the bottom floor
        colour = (20, 115, 80)
        x = 0
        y = WINDOW_HEIGHT - 10
        width = WINDOW_WIDTH
        height = FLOOR_HEIGHT
        rect = (x, y, width, height)
        floor_id = self.num_floors
        ladders = []

        #self.floors.append((floor_id, colour, rect, ladders))
        floor = Floor(floor_id, colour, rect, ladders)
        self.floors.append(floor)

        # Once all the floors are create the ladders can be added
        self.init_ladders()

    def init_ladders(self):
        ladder_locations = []

        num = len(ladder_locations)

        for floor in self.floors:
            # don't add ladders to the top floor
            if floor.floor_id == 0:
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

                #y = item[2][1]
                rect = floor.rect
                y = rect[1]
                width = LADDER_WIDTH
                #id = item[0]
                id = floor.floor_id
                id_floor_above = id - 1
                #row_above = self.floors[id_floor_above]
                #y_row_above = row_above[2][1]
                #row_above = self.floors[id_floor_above]
                #height = y - y_row_above
                floor_above = self.floors[id_floor_above]
                y_floor_above = floor_above.rect[1]
                height = y - y_floor_above
                # height = 165
                colour = self.colour
                # colour = (255, 0, 0)

                ladder = Ladder(x, y, width, height, colour, UP)
                #item[3].append(ladder)
                #floor.append(ladder)
                floor.ladders.append(ladder)
                ladder_locations.append((x - LADDER_WIDTH - 20, x + LADDER_WIDTH + 20))  # 20 padding so not too close

    def create_portals(self):
        # create the up portals
        width = PORTAL_WIDTH
        height = PORTAL_HEIGHT
        colour = PORTAL_COLOUR
        direction = UP
        portal_id = 0

        for i in range(self.num_up_portals):
            # if only 1 up portal place it on the top floor at the left most edge
            if self.num_up_portals == 1:
                x = PORTAL_WIDTH // 2 * -1
                y = self.get_floor_y(0) - PORTAL_HEIGHT
            # else randomize floor and location
            else:
                # find the y coord
                num_floors = len(self.floors)
                floor_id = random.randint(0, num_floors)
                y = self.get_floor_y(floor_id) - PORTAL_HEIGHT

                # find the x coord
                x = 0
                while x == 0:
                    min_x = PORTAL_WIDTH // 2 * -1
                    max_x = WINDOW_WIDTH + (PORTAL_WIDTH // 2)
                    x = random.randint(min_x, max_x)
                    in_ladder = self.is_location_in_ladder(floor_id, x + PORTAL_WIDTH // 2, y)

                    # portal would have been in a ladder so regenerate x value
                    if in_ladder is True:
                        x = 0

            portal = Portal(portal_id, x, y, width, height, colour, direction)
            self.portals.append(portal)

            portal_id += 1

        # create the down portals
        width = PORTAL_WIDTH
        height = PORTAL_HEIGHT
        colour = PORTAL_COLOUR
        direction = DOWN
        for i in range(self.num_down_portals):
            # if only 1 up portal place it on the bottom floor at the right most edge
            if self.num_down_portals == 1:
                x = WINDOW_WIDTH - (PORTAL_WIDTH // 2)
                num_floors = len(self.floors)
                y = self.get_floor_y(num_floors - 1) - PORTAL_HEIGHT
            # else randomize floor and location
            else:
                # find the y coord
                num_floors = len(self.floors)
                floor_id = random.randint(0, num_floors)
                y = self.get_floor_y(floor_id) - PORTAL_HEIGHT

                # find the x coord
                x = 0
                while x == 0:
                    min_x = PORTAL_WIDTH // 2 * -1
                    max_x = WINDOW_WIDTH + (PORTAL_WIDTH // 2) + 10
                    x = random.randint(min_x, max_x)
                    in_ladder = self.is_location_in_ladder(floor_id, x + PORTAL_WIDTH // 2, y)

                    # portal would have been in a ladder so regenerate x value
                    if in_ladder is True:
                        x = 0

            portal = Portal(portal_id, x, y, width, height, colour, direction)
            self.portals.append(portal)

            portal_id += 1

    def create_loot(self):
        """Creates the loot on each level."""
        loot_id = 1
        facing = random.randint(0, 9)
        start_x = 50
        loot_interval = 50
        loot_type = LOOT_COIN_GOLD
        for floor in self.floors:
            sizing_loot = Loot(-1, 0,0,loot_type, 0)
            width = sizing_loot.get_loot_width()
            height = sizing_loot.get_loot_height()
            num_loot = WINDOW_WIDTH // (loot_interval + width) - 1
            x = start_x
            y = self.get_floor_y(floor.floor_id) - height - LOOT_FLOAT
            for i in range(num_loot):
                okay_to_place = True
                if (self.is_location_in_ladder(floor.floor_id, x, y) is True or self.is_location_in_ladder(floor.floor_id, x + width, y) is True):
                    okay_to_place = False
                if self.is_location_in_portal(x, y) is True or self.is_location_in_portal(x + width, y) is True:
                    okay_to_place = False

                if okay_to_place is True:
                    loot = Loot(loot_id, x, y, loot_type, facing)
                    self.loots.append(loot)
                    loot_id += 1

                x += loot_interval + sizing_loot.get_loot_width()

    def draw(self, win):
        # draw the floors
        for floor in self.floors:
            floor.draw(win)

        # draw the portals
        for portal in self.portals:
            portal.draw(win)

        # draw the loots
        for loot in self.loots:
            loot.draw(win)

    def get_floor(self, floor_id):
        """Returns the floor with the matching ID. Returns an empty floor if ID not found."""
        ladders = []
        found_floor = Floor(-1, (0,0,0), (0,0,0,0), ladders)
        found = False
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor.floor_id == floor_id:
                    found_floor = floor
        return found_floor

    def get_num_floor_ladders(self, floor_id):
        """Returns the number of ladders for the floor ID. Returns -1 if ID not found."""
        num_ladders = -1
        floor = self.get_floor(floor_id)
        if floor.floor_id != -1:
            num_ladders = len(floor.ladders)
        '''    
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    num_ladders = len(floor[3])
        '''
        return num_ladders

    def get_ladder_top_rung_y(self, floor_id):
        """Returns the y of the top rung of the ladders for the floor ID. Returns -1 if ID not found."""
        top_rung_y = -1
        floor = self.get_floor(floor_id)
        if floor.floor_id != -1:
            ladder = floor.ladders[0]   # all ladders on this floor have the same y coord for the top rung
            top_rung_y = ladder.y_of_top_rung
        '''
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    for ladder in floor[3]:
                        top_rung_y = ladder.y_of_top_rung
        '''
        return top_rung_y

    def get_ladder_2nd_top_rung_y(self, floor_id):
        """Returns the y of the 2nd top rung of the ladders for the floor ID. Returns -1 if ID not found."""
        top_2nd_rung_y = -1
        floor = self.get_floor(floor_id)
        if floor.floor_id != -1:
            ladder = floor.ladders[0]  # all ladders on this floor have the same y coord for the top rung
            top_2nd_rung_y = ladder.y_of_2nd_top_rung
        '''
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    for ladder in floor[3]:
                        top_2nd_rung_y = ladder.y_of_2nd_top_rung
        '''
        return top_2nd_rung_y

    def get_floor_y(self, floor_id):
        """Returns the y of the floor for the floor ID. Returns -1 if ID not found."""
        y = -1

        '''
        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                if floor[0] == floor_id:
                    rect = floor[2]
                    y = rect[1]
                    break
        '''
        floor = self.get_floor(floor_id)
        if floor.floor_id != -1:
            rect = floor.rect
            y = rect[1]
            y = floor.rect[1]
        return y

    def get_floor_id(self, y):
        """Returns the ID of the floor for the floor y. Returns -1 if ID not found."""
        floor_id = -1

        if (y >= 0 and y <= WINDOW_HEIGHT):
            for floor in self.floors:
                rect = floor.rect
                if rect[1] == y:
                    floor_id = floor.floor_id
                    break

        '''
        if (y >= 0 and y <= WINDOW_HEIGHT):
            for floor in self.floors:
                rect = floor[2]
                if rect[1] == y:
                    floor_id = floor[0]
                    break
        '''

        return floor_id

    def get_floor_ladder_coords(self, floor_id):
        """Returns a list of coords of ladder(s) for the floor with ID. Returns an empty list if ID not found."""
        ladder_coords = []

        if (floor_id >= 0 and floor_id < len(self.floors)):
            for floor in self.floors:
                #if floor[0] == floor_id:
                if floor.floor_id == floor_id:
                    #for ladder in floor[3]:
                    for ladder in floor.ladders:
                        x1 = ladder.x
                        y1 = ladder.y
                        x2 = ladder.x + ladder.width
                        y2 = ladder.y + (ladder.height * ladder.direction)
                        ladder_coords.append((x1, y1, x2, y2))
        return ladder_coords

    def is_location_in_ladder(self, floor_id, x, y):
        """Returns True if the x,y point is in a ladder on floor with ID. Returns False if not."""
        in_ladder = False

        ladder_coords = self.get_floor_ladder_coords(floor_id)
        for coord in ladder_coords:
            # print("Checking (", x, ",", y, ") with coord (", coord[0], ",", coord[1], ",", coord[2], ",", coord[3], ")")
            if x >= coord[0] and x <= coord[2] and y <= coord[1] and y >= coord[3]:
                in_ladder = True
                break
        return in_ladder

    def get_ladder_coords(self, floor_id, x, y):
        """Returns the rect of the ladder the point (x,y) is in on floor with ID. Returns a rect of -1 if ID not found."""
        #in_ladder = False
        rect = (-1, -1, -1, -1)

        ladder_coords = self.get_floor_ladder_coords(floor_id)
        for coord in ladder_coords:
            # print("Checking (", x, ",", y, ") with coord (", coord[0], ",", coord[1], ",", coord[2], ",", coord[3], ")")
            if x >= coord[0] and x <= coord[2] and y <= coord[1] and y >= coord[3]:
                rect = (coord[0], coord[1], coord[2], coord[3])
                break
        return rect

    def get_portal_coords(self):
        """Returns a list of coords of portal(s). Returns an empty list if no portals found."""
        portal_coords = []

        for portal in self.portals:
            x1 = portal.x
            y1 = portal.y
            x2 = portal.x + portal.width
            y2 = portal.y + portal.height
            portal_coords.append((x1, y1, x2, y2))
        return portal_coords

    def is_location_in_portal(self, x, y):
        """Returns the ID of the portal the x,y point is in if in a portal. Returns -1 if not."""
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
        """Returns the target level of a portal. Returns -1 if portal direction is not known"""
        target_level = -1

        for portal in self.portals:
            if portal_id == portal.portal_id:
                if portal.direction == UP:
                    target_level = self.level_id + 1
                else:
                    target_level = self.level_id - 1
                break

        return target_level

    def is_player_in_loot(self, player):
        """Returns the loot object that the player is intersecting. The loot_id is -1 if not interacting with any loot"""

        found_loot = Loot(-1, 0, 0, 0, 0)
        found = False

        player_hit_box = player.hit_box

        for loot in self.loots:
            loot_hit_box = loot.hit_box

            found = do_rectangles_overlap(player_hit_box, loot_hit_box)
            if found is True:
                found_loot = loot

            '''
            width = loot.get_loot_width()
            height = loot.get_loot_height()
            rect_1 = (loot.x, loot.y, width, height)

            player_dims = player.get_image_run_dims()
            width = player_dims[0]
            height = player_dims[1]
            body_indent = 5
            if player.is_left is True:
                #body_indent *= 1
                rect_2 = (player.x + body_indent, player.y, width, height)
            elif player.is_right is True:
                #body_indent *= -1
                rect_2 = (player.x, player.y, width - body_indent - 20, height)
            found = do_rectangles_overlap(rect_1, rect_2)
            if found is True:
                found_loot = loot
                break
            '''

        return found_loot



