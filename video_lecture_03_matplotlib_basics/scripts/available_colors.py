import matplotlib.pyplot as plt
import matplotlib.colors as mc

# create plots from available matplotlib colors.
# The script creates three plots of available named
# matplotlib colors:
#
# 1. Base colors from the old and the new matplotlib
#    standard pallettes for line plots
# 2. standard colors sufficient for most applications
# 3. All currently available named colors within matplotlib

base_colors = dict(mc.BASE_COLORS, **mc.TABLEAU_COLORS)

standard_colors = dict(mc.BASE_COLORS, **mc.TABLEAU_COLORS,
                       **mc.CSS4_COLORS)

all_colors = dict(mc.BASE_COLORS, **mc.TABLEAU_COLORS,
                  **mc.CSS4_COLORS, **mc.XKCD_COLORS)

def plot_colors(colors, outfile=None):
    # Sort colors by hue, saturation, value and name.
    by_hsv = sorted((tuple(mc.rgb_to_hsv(mc.to_rgba(color)[:3])), name)
                    for name, color in colors.items())
    sorted_names = [name for hsv, name in by_hsv]

    n = len(sorted_names)
    
    if n < 50:
        ncols = 3
        fig, ax = plt.subplots(figsize=(8, 3), dpi=36)
    else:
        if n < 200:
            ncols = 4
            fig, ax = plt.subplots(figsize=(12, 10), dpi=36)
        else:
            ncols = 5
            fig, ax = plt.subplots(figsize=(30, 100), dpi=36)

    nrows = int(n / ncols) + 1
    
    # Get height and width
    X, Y = fig.get_dpi() * fig.get_size_inches()
    h = Y / (nrows + 1)
    w = X / ncols

    for i, name in enumerate(sorted_names):
        row = i % nrows
        col = i // nrows
        y = Y - (row * h) - h

        xi_line = w * (col + 0.05)
        xf_line = w * (col + 0.25)
        xi_text = w * (col + 0.3)

        ax.text(xi_text, y, name, fontsize=(h * 0.8),
                horizontalalignment='left',
                verticalalignment='center')

        ax.hlines(y + h * 0.1, xi_line, xf_line,
                  color=colors[name], linewidth=(h * 0.8))

    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    ax.set_axis_off()

    fig.subplots_adjust(left=0, right=1,
                        top=1, bottom=0,
                        hspace=0, wspace=0)
    if outfile != None:
        plt.savefig(outfile, dpi=100)
    else:
        plt.show()
        
plot_colors(base_colors, outfile="base_colors.png")
plot_colors(standard_colors, outfile="standard_colors.png")
plot_colors(all_colors, outfile="all_colors.png")
