# Requires the Colorgram 1.2.0 package from https://pypi.org/project/colorgram.py/
import colorgram

# Pull 30 colors from the supplied image, and generate an empty list to insert processed colors into.
image_colors = colorgram.extract('image.jpg', 30)
colors = []

# For each color picked, pull its RGB values and save them cleanly as a tuple for the turtle to use.
for color in image_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors.append((r, g, b))

print(colors)