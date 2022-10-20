from qtile_extras import widget
from libqtile.lazy import lazy
from .colors import theme
from .spotify import Spotify

terminal = "kitty"

regular_font = "FiraCode Nerd Font"
font_size = 17

def parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = [
        "Mozilla Firefox",
        "Visual Studio Code",
        "Discord",
    ]
    return next(filter(lambda name: name in text, target_names), text)

def init_widgets_defaults():
    return dict(font = regular_font,
                fontsize = font_size,
                foreground = theme[10],
                background = theme[8],
                )

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(
                        **widget_defaults,
                        active = theme[0],
                        block_highlight_text_color = theme[0],
                        this_current_screen_border = theme[0],
                        this_screen_border = theme[0],
                        urgent_border = theme[1],
                        other_current_screen_border = theme[8],
                        other_screen_border = theme[8],
                        highlight_color = theme[8],
                        inactive = theme[10],
                        borderwidth = 2,
                        disable_drag = True,
                        highlight_method = "text",
                        ),
                widget.Spacer(**widget_defaults, length = 6),
                widget.TextBox(
                        **widget_defaults,
                        text=" ",
                        mouse_callbacks={"Button1": lazy.spawn("spotify")},
                        ),
                Spotify(
                    **widget_defaults,
                    format = '{track}',
                    ),
                widget.Spacer(**widget_defaults),
                widget.TextBox(
                        **widget_defaults,
                        text="",
                        padding = 6,
                        ),
                widget.Clock(
                        **widget_defaults,
                        format="%a %b %d - %H:%M",
                        ),
                widget.Spacer(**widget_defaults),
                widget.Systray(
                        **widget_defaults
                        ),
                widget.Spacer(**widget_defaults, length = 6),
                widget.TextBox(
                        **widget_defaults,
                        text="墳",
                        mouse_callbacks = {"Button1": lazy.spawn(terminal + " -e alsamixer")},
                        ),
                widget.Volume(
                        **widget_defaults,
                        step = 5,
                        ),
                widget.Spacer(**widget_defaults, length = 6),
                widget.UPowerWidget(
                        **widget_defaults,
                        ),
                widget.Battery(
                        **widget_defaults,
                        format = '{percent:2.0%}',
                        charge_char = '',
                        discharge_char = '',
                        full_char = '',
                        update_interval = 10,
                        show_short_text = False,
                        ),
                widget.Spacer(**widget_defaults, length = 4),
                widget.TextBox(
                        **widget_defaults,
                        text = "ﮮ",
                        mouse_callbacks = {"Button1": lazy.spawn(terminal + " -e sudo paru -Syyu --color=auto")},
                        padding = 6,
                        ),
                widget.CheckUpdates(
                        **widget_defaults,
                        no_update_string = "N/A",
                        colour_no_updates = theme[10],
                        colour_have_updates = theme[10],
                        display_format = "{updates}",
                        update_interval = 10,
                        mouse_callbacks = {"Button1": lazy.spawn(terminal + " -e sudo paru -Syyu --color=auto")},
                        ),
                widget.Spacer(**widget_defaults, length = 4),
                widget.TextBox(
                        **widget_defaults,
                        text = "",
                        padding = 8,
                        mouse_callbacks = {"Button1": lazy.widget["keyboardlayout"].next_keyboard()}
                        ),
                widget.KeyboardLayout(
                        **widget_defaults,
                        max_chars = 2,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': 'LA', 'us': 'US'}
                       ),
                widget.Spacer(**widget_defaults, length = 6),
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

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()
