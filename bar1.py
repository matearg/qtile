from colors import gruvbox, nord
from libqtile import widget
from unicodes import left_arrow, right_arrow
import os

# COLORS FOR THE BAR
colors = nord()

def init_widgets_defaults():
    return dict(font = "Hack NF",
                fontsize = 12,
                padding = 2,
                background = colors[1])

def init_widgets_list():
    prompt = "{0}".format(os.environ["USER"])
    widgets_list = [
                widget.GroupBox(
                        font = "Hack NF",
                        fontsize = 25,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[6],
                        inactive = colors[1],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[4],
                        foreground = colors[2],
                        background = colors[7]
                        ),
                right_arrow(colors[4], colors[7]),
                widget.CurrentLayoutIcon(
                        custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons/wmicons")],
                        background = colors[4],
                        padding = 0,
                        scale = 0.7
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 16,
                        text = "[",
                        foreground = "#ffffff",
                        background = colors[4],
                        padding = 0,
                        ),
                widget.CurrentLayout(
                        font = "Hack NF Bold",
                        fontsize = 14,
                        foreground = "#ffffff",
                        background = colors[4]
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 16,
                        text = "]",
                        foreground = "#ffffff",
                        background = colors[4],
                        padding = 0,
                        ),
                right_arrow(colors[1], colors[4]),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 14,
                        text = " ",
                        background = colors[1],
                        padding = 0,
                        ),
                widget.WindowName(
                        font = "Hack NF Italic",
                        fontsize = 14,
                        foreground = colors[5],
                        background = colors[1],
                        ),
                left_arrow(colors[1], colors[4]),
                widget.DF(
                        font = "Hack NF Bold",
                        fontsize = 12,
                        foreground = "#ffffff",
                        background = colors[4],
                        format = '{uf} {m}b',
                        visible_on_warn = False
                        ),
                widget.TextBox(
                        font = "FontAwesome",
                        text = "  ",
                        foreground = "#ffffff",
                        background = colors[4],
                        padding = 0,
                        fontsize = 16
                        ),
                left_arrow(colors[4], colors [7]),
                widget.Memory(
                        font = "Hack NF Bold",
                        format = '{MemUsed: .2f} Gb',
                        measure_mem = 'G',
                        update_interval = 1,
                        fontsize = 12,
                        foreground = colors[1],
                        background = colors[7],
                        ),
                widget.TextBox(
                        font = "FontAwesome",
                        text = "  ",
                        foreground = colors[1],
                        background = colors[7],
                        padding = 0,
                        fontsize = 16
                        ),
                left_arrow(colors[7], colors[4]),
                widget.KeyboardLayout(
                        font = "Hack NF Bold",
                        foreground = "#ffffff",
                        background = colors[4],
                        padding = 0,
                        fontsize = 12,
                        max_chars = 2,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': 'LA', 'us': 'US'}
                       ),
                widget.TextBox(
                        font = "FontAwesome",
                        text = "  ",
                        foreground = "#ffffff",
                        background = colors[4],
                        padding = 0,
                        fontsize = 16
                        ),
                left_arrow(colors[4], colors[7]),
                widget.Clock(
                        font = "Hack NF Bold",
                        foreground = colors[1],
                        background = colors[7],
                        fontsize = 14,
                        format = "%a %d/%m %H:%M",
                        ),
                widget.TextBox(
                        font = "FontAwesome",
                        text = "  ",
                        foreground = colors[1],
                        background = colors[7],
                        padding = 0,
                        fontsize = 16
                        ),
                left_arrow(colors[7], colors[4]),
                widget.Systray(
                        background = colors[4],
                        icon_size = 20,
                        padding = 4
                        ),
                left_arrow(colors[7], colors[4]),
                left_arrow(colors[4], colors[1]),
                widget.TextBox(
                        font = "Hack NF Bold",
                        text = prompt,
                        foreground = colors[6],
                        background = colors[1],
                        padding = 0,
                        fontsize = 16
                        ),
                widget.TextBox(
                        font = "FontAwesome",
                        text = "  ",
                        foreground = colors[6],
                        background = colors[1],
                        padding = 0,
                        fontsize = 16
                        ),
    ]
    return widgets_list

widget_defaults = init_widgets_defaults()

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[23:27]
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[21:27]
    return widgets_screen2
