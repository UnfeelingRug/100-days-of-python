# A simple function to calculate how many cans of paint one would need to cover a given wall.
# Assume the height and width of the wall are given in meters, and that the "coverage" is defined in square meters.
import math

# Calculate the area needing to be covered, and how many cans it will take to cover it.
# Rounds up, since you obviously can't purchase partial cans.
def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f'You will need {cans} cans of paint.')

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)