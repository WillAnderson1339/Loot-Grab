"""
collection of useful utility functions
"""

def do_rectangles_overlap(rect_1, rect_2):
    """Determines if 2 rectangles overlap. Rect are (x, y, width, height)"""

    overlap = False

    # points for 1st rectangle
    x1 = rect_1[0]
    y1 = rect_1[1]
    x2 = rect_1[0] + rect_1[2]
    y2 = rect_1[1] + rect_1[3]

    # points for 2nd rectangle
    x3 = rect_2[0]
    y3 = rect_2[1]
    x4 = rect_2[0] + rect_2[2]
    y4 = rect_2[1] + rect_2[3]

    # check points for overlap
    for y in range(y1, y2):
        for x in range(x1, x2):
            # if (y > y3 and y < y4) and (x > x3 and x < x4):
            if (y3 < y < y4) and (x3 < x < x4):
                overlap = True

    return overlap

