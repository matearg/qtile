from libqtile import widget, bar
from .colors import catppuccin
from .spotify import Spotify

colors = catppuccin

def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        "Mozilla Firefox",
        "Visual Studio Code",
        "Discord",
    ]
    return next(filter(lambda name: name in text, target_names), text)

def init_widgets_defaults():
    return dict(font = "Hack Nerd Font",
                fontsize = 12,
                padding = 2,
                background = colors[10])

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(
                        font = "Hack Nerd Font",
                        fontsize = 15,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 9,
                        padding_x = 9,
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
                        font = "Hack Nerd Font",
                        fontsize = 12,
                        text = " ",
                        background = colors[10],
                        padding = 0,
                        ),
                widget.TextBox(
                        font = "Hack Nerd Font",
                        fontsize = 16,
                        text = "[",
                        foreground = "#ffffff",
                        background = colors[10],
                        padding = 0,
                        ),
                widget.CurrentLayout(
                        font = "Hack Nerd Font",
                        fontsize = 14,
                        foreground = "#ffffff",
                        background = colors[10],
                        ),
                widget.TextBox(
                        font = "Hack Nerd Font",
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
                        font = "Hack Nerd Font Italic",
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
                Spotify(
                        font = "Hack Nerd Font",
                        fontsize = 14,
                        foreground = "#ffffff",
                        background = colors[10],
                        play_icon = " ",
                        pause_icon = " ",
                        format = "{icon} {artist} - {track} ",
                        max_chars = 25,
                        ),
                widget.Sep(
                    foreground = "#ffffff",
                    background = colors[10]
                    ),
                widget.KeyboardLayout(
                        font = "Hack Nerd Font",
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
                        font = "Hack Nerd Font",
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
                        font = "Hack Nerd Font",
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
    return widgets_screen2
