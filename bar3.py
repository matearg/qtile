from colors import gruvbox, nord
from libqtile import widget
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
                        inactive = "#ffffff",
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[4],
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 16,
                        text = "[",
                        foreground = "#ffffff",
                        background = colors[1],
                        padding = 0,
                        ),
                widget.CurrentLayout(
                        font = "Hack NF Bold",
                        fontsize = 14,
                        foreground = "#ffffff",
                        background = colors[1]
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 16,
                        text = "]",
                        foreground = "#ffffff",
                        background = colors[1],
                        padding = 0,
                        ),
                widget.Spacer(background = colors[1]),
                widget.DF(
                        font = "Hack NF Bold",
                        fontsize = 12,
                        foreground = "#ffffff",
                        background = colors[1],
                        format = '{uf} {m}b',
                        visible_on_warn = False
                        ),
                widget.TextBox(
                        font = "FontAwesome",
                        text = "  ",
                        foreground = "#ffffff",
                        background = colors[1],
                        padding = 0,
                        fontsize = 16
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.Memory(
                        font = "Hack NF Bold",
                        format = '{MemUsed: .2f} Gb',
                        measure_mem = 'G',
                        update_interval = 1,
                        fontsize = 12,
                        foreground = "#ffffff",
                        background = colors[1],
                        ),
                widget.TextBox(
                        font = "FontAwesome",
                        text = "  ",
                        foreground = "#ffffff",
                        background = colors[1],
                        padding = 0,
                        fontsize = 16
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.KeyboardLayout(
                        font = "Hack NF Bold",
                        foreground = "#ffffff",
                        background = colors[1],
                        padding = 0,
                        fontsize = 12,
                        max_chars = 2,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': 'LA', 'us': 'US'}
                       ),
                widget.Sep(
                        font = "Hack NF Bold",
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.Clock(
                        font = "Hack NF Bold",
                        foreground = "#ffffff",
                        background = colors[1],
                        fontsize = 14,
                        format = "%a %d/%m %H:%M",
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.Systray(
                        background = colors[1],
                        icon_size = 20,
                        padding = 4
                        ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        text = prompt,
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
    del widgets_screen1[17:20]
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[17:20]
    return widgets_screen2
