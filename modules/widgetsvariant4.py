from libqtile import widget, bar
from libqtile.lazy import lazy
from .colors import catppuccin

regular_font = "Hack Nerd Font"
mono_font = regular_font + " Mono"
italic_font = regular_font + " Italic"
bold_font = regular_font + " Bold"
font_size = 14

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
                padding = 8,
                padding_y = 4,
                padding_x = 0,
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
                        font = mono_font,
                        fontsize = 15,
                        highlight_method = "text",
                        padding_x = 10,
                        padding_y = 16,
                        rounded = False,
                        ),
                widget.CurrentLayoutIcon(**widget_defaults, scale = 0.7),
                widget.Spacer(background = catppuccin[13]),
                widget.TextBox(
                        **widget_defaults,
                        text="墳",
                        ),
                widget.PulseVolume(
                        **widget_defaults,
                        limit_max_volume="True",
                        step = 5,
                        ),
                widget.TextBox(
                        **widget_defaults,
                        text = "",
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e yay")},
                        ),
                widget.CheckUpdates(
                        **widget_defaults,
                        no_update_string = "N/A",
                        colour_no_updates = catppuccin[18],
                        colour_have_updates = catppuccin[18],
                        display_format = "{updates}",
                        update_interval = 10,
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e yay")},
                        ),
                widget.TextBox(
                        **widget_defaults,
                        text = "",
                        mouse_callbacks = {"Button1": lazy.widget["keyboardlayout"].next_keyboard()}
                        ),
                widget.KeyboardLayout(
                        **widget_defaults,
                        max_chars = 2,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': 'LA', 'us': 'US'}
                       ),
                widget.TextBox(
                        **widget_defaults,
                        text="",
                        ),
                widget.Clock(
                        **widget_defaults,
                        format="%H:%M",
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
