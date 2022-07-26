from libqtile import widget, bar
from .colors import nord, gruvbox

colors = nord()

def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        "Mozilla Firefox",
        "Visual Studio Code",
        "Discord",
    ]
    return next(filter(lambda name: name in text, target_names), text)

def init_widgets_defaults():
    return dict(font = "Hack NF",
                fontsize = 12,
                padding = 2,
                background = colors[10])

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(
                        font = "Hack NF",
                        fontsize = 20,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 8,
                        padding_x = 7,
                        borderwidth = 3,
                        center_aligned = True,
                        disable_drag = True,
                        active = "#ffffff",
                        inactive = "#ffffff",
                        rounded = False,
                        highlight_method = "line",
                        this_current_screen_border = "#ffffff",
                        other_current_screen_border = "#ffffff",
                        highlight_color = colors[10],
                        foreground = "#ffffff",
                        background = colors[10]
                        ),
                widget.Sep(
                    foreground = "#ffffff",
                    background = colors[10]
                    ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 12,
                        text = " ",
                        background = colors[10],
                        padding = 0,
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 16,
                        text = "[",
                        foreground = "#ffffff",
                        background = colors[10],
                        padding = 0,
                        ),
                widget.CurrentLayout(
                        font = "Hack NF Bold",
                        fontsize = 14,
                        foreground = "#ffffff",
                        background = colors[10],
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 16,
                        text = "]",
                        foreground = "#ffffff",
                        background = colors[10],
                        padding = 0,
                        ),
                widget.Spacer(
                        background = colors[10]
                        ),
                widget.WindowName(
                        font = "Hack NF Italic",
                        fontsize = 14,
                        foreground = "#ffffff",
                        background = colors[10],
                        width = bar.CALCULATED,
                        empty_group_string = "Desktop",
                        max_chars = 40,
                        parse_text = parse_window_name,
                        ),
                widget.Spacer(
                        background = colors[10]
                        ),
                widget.KeyboardLayout(
                        font = "Hack NF Bold",
                        foreground = "#ffffff",
                        background = colors[10],
                        padding = 3,
                        fontsize = 14,
                        max_chars = 4,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': ' LA ', 'us': ' US '}
                       ),
                widget.Sep(
                    foreground = "#ffffff",
                    background = colors[10]
                    ),
                widget.Clock(
                        font = "Hack NF Bold",
                        foreground = "#ffffff",
                        background = colors[10],
                        fontsize = 14,
                        format = " %a %d/%m %H:%M ",
                        ),
                widget.Sep(
                    foreground = "#ffffff",
                    background = colors[10]
                    ),
                widget.Systray(
                        background = colors[10],
                        icon_size = 20,
                        padding = 5
                        ),
                widget.TextBox(
                        font = "Hack NF Bold",
                        fontsize = 12,
                        text = " ",
                        background = colors[10],
                        padding = 0,
                        ),
    ]
    return widgets_list

widget_defaults = init_widgets_defaults()

widgets_list = init_widgets_list()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[24:27]
    return widgets_screen2
