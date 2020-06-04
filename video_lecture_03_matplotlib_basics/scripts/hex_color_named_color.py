import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mc

# for a given colour HEX-code such as '#ff0000'. print out
# the closest 'named color' available in matplotlib.
# The 'closest color' is defined as the minimum squared
# difference between the RGB-values of the HEX-color and
# the predefined named colors.

# The HEX-code needs to be provided on the command line:
if len(sys.argv) != 2:
    print(f"SYNOPSIS: {sys.argv[0]} HEX-CODE", file=sys.stderr)
    print("", file=sys.stderr)
    print(f"Example: {sys.argv[0]} \#FFd8c0", file=sys.stderr)
    print("", file=sys.stderr)
    print("NOTE: On a Linux shell, you must quote the hast (#)",
          file=sys.stderr)
    print("in the HEX-CODE.", file=sys.stderr)
    sys.exit(1)

hex_code = sys.argv[1]

try:
    hex_code_rgb = mc.hex2color(hex_code)
except ValueError:
    print(f"{sys.argv[1]} is not a valid color HEX code.",
          file=sys.stderr)
    sys.exit(1)
    
# currently the named colors are BASE (old standard matplotlib
# pallette), TABLEAU (current matplotlib standard palette), CSS4
# color palette and XKCD colors:
avail_colors = dict(mc.BASE_COLORS, **mc.TABLEAU_COLORS,
              **mc.CSS4_COLORS, **mc.XKCD_COLORS)

# we isolate color names and RGB values from a dictionary
# to ordered lists so that we can determine and access the
# 'optimal' color with an index below:
avail_colors_names = list(avail_colors.keys())

r = np.array([mc.to_rgb(c)[0] for c in avail_colors.values()])
g = np.array([mc.to_rgb(c)[1] for c in avail_colors.values()])
b = np.array([mc.to_rgb(c)[2] for c in avail_colors.values()])

rgb = np.vstack((r, g, b)).T

dist_rgb = (rgb[:,0] - hex_code_rgb[0])**2 + \
           (rgb[:,1] - hex_code_rgb[1])**2 + \
           (rgb[:,2] - hex_code_rgb[2])**2

min_index = dist_rgb.argmin()
min_name = avail_colors_names[min_index]
min_hex = list(avail_colors.values())[min_index]

print(f"The best matching named matplotlib color is '{min_name}'.")
print(f"This best match named color has the HEX-code {min_hex}.")
