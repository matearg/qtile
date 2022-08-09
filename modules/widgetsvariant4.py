from libqtile import widget
from libqtile.lazy import lazy
from .colors import catppuccin

regular_font = "Hack Nerd Font"
font_size = 15

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
                foreground = catppuccin[18],
                background = catppuccin[13],
                )

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(
                        active = catppuccin[0],
                        block_highlight_text_color = catppuccin[0],
                        this_current_screen_border = catppuccin[0],
                        this_screen_border = catppuccin[0],
                        urgent_border = catppuccin[3],
                        background = catppuccin[13],  # background is [10-12]
                        other_current_screen_border = catppuccin[13],
                        other_screen_border = catppuccin[13],
                        highlight_color = catppuccin[13],
                        inactive = catppuccin[18],
                        foreground = catppuccin[18],
                        borderwidth = 2,
                        disable_drag = True,
                        font = regular_font,
                        fontsize = font_size,
                        highlight_method = "text",
                        ),
                widget.Spacer(**widget_defaults),
                widget.TextBox(
                        **widget_defaults,
                        text="墳",
                        ),
                widget.Volume(
                        **widget_defaults,
                        step = 5,
                        ),
                widget.Spacer(**widget_defaults, length = 6),
                widget.TextBox(
                        **widget_defaults,
                        text = "ﮮ",
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e sudo paru")},
                        padding = 6,
                        ),
                widget.CheckUpdates(
                        **widget_defaults,
                        no_update_string = "N/A",
                        colour_no_updates = catppuccin[18],
                        colour_have_updates = catppuccin[18],
                        display_format = "{updates}",
                        update_interval = 10,
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e sudo paru")},
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
                widget.TextBox(
                        **widget_defaults,
                        text="",
                        padding = 6,
                        ),
                widget.Clock(
                        **widget_defaults,
                        format="%a %d %b %H:%M",
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

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()
