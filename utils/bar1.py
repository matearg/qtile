from libqtile import widget, bar
from libqtile.lazy import lazy
from .colors import catppuccin
from .spotify import Spotify

colors = catppuccin
regular_font = "Iosevka Nerd Font"
mono_font = "Iosevka Nerd Font Mono"
italic_font = "Iosevka Nerd Font Italic"
bold_font = "Iosevka Nerd Font Bold"

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
                fontsize = 12,
                padding = 2,
                background = colors[1])

def init_widgets_list():
    widgets_list = [
                widget.Image(
                        background=colors[0],
                        margin_x=14,
                        margin_y=3,
                        mouse_callbacks={"Button1": lazy.spawn("alacritty")},
                        filename="~/.config/qtile/icons/arch.png",
                        ),
                widget.GroupBox(
                        active = colors[0],
                        block_highlight_text_color = colors[0],
                        this_current_screen_border = colors[0],
                        this_screen_border = colors[0],
                        urgent_border = colors[3],
                        background = colors[12],  # background is [10-12]
                        other_current_screen_border = colors[12],
                        other_screen_border = colors[12],
                        highlight_color = colors[13],
                        inactive = colors[14],
                        foreground = colors[18],
                        borderwidth = 2,
                        disable_drag = True,
                        font = mono_font,
                        fontsize = 25,
                        highlight_method = "line",
                        padding_x = 10,
                        padding_y = 16,
                        rounded = False,
                        ),
                widget.Spacer(background = colors[13]),
                widget.TextBox(
                        text = " ",
                        foreground = "#ffffff",
                        background = colors[13],
                        font = regular_font,
                        ),
                widget.WindowName(
                        font = italic_font,
                        fontsize = 14,
                        foreground = "#ffffff",
                        background = colors[13],
                        width = bar.CALCULATED,
                        empty_group_string = "Desktop",
                        max_chars = 40,
                        parse_text = parse_window_name,
                        ),
                widget.Spacer(background = colors[13]),
                widget.OpenWeather(
                        font = mono_font,
                        fontsize = 20,
                        background = colors[3],
                        foreground = colors[13],
                        coordinates = {"longitude": "-57.5575", "latitude": "-38.0023"},
                        format = "{icon}",
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        ),
                widget.OpenWeather(
                        font = mono_font,
                        fontsize = 14,
                        background = colors[13],
                        foreground = colors[3],
                        coordinates = {"longitude": "-57.5575", "latitude": "-38.0023"},
                        format = "{main_temp:.0f}°{units_temperature}",
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        ),
                widget.TextBox(
                        text="阮",
                        font = mono_font,
                        fontsize=25,
                        foreground=colors[13],  # blue
                        background = colors[7],
                        filled = True,
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        mouse_callbacks={"Button1": lazy.spawn("spotify")},
                        ),
                Spotify(
                        font = regular_font,
                        fontsize = 14,
                        foreground = colors[7],
                        background = colors[13],
                        play_icon = "  ",
                        pause_icon = "  ",
                        format = "{icon} {artist} - {track} ",
                        # max_chars = 20,
                        ),
                widget.TextBox(
                        font = regular_font,
                        text = " ",
                        foreground = colors[13],
                        background = colors[4],
                        padding = 8,
                        padding_x = None,
                        padding_y = 4,
                        fontsize = 14
                        ),
                widget.KeyboardLayout(
                        font = mono_font,
                        foreground = colors[4],
                        background = colors[13],
                        padding = 8,
                        padding_x = 0,
                        padding_y = 4,
                        fontsize = 14,
                        max_chars = 2,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': 'LA', 'us': 'US'}
                       ),
                widget.TextBox(
                        text="",
                        font = mono_font,
                        fontsize=25,
                        foreground=colors[10],  # blue
                        background = colors[8],
                        radius = 4,
                        filled = True,
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        ),
                widget.Clock(
                        font = regular_font,
                        fontsize = 14,
                        format="%b %d, %H:%M",
                        foreground=colors[8],
                        background=colors[13],
                        padding=8,
                        ),
                widget.TextBox(
                        text="墳",
                        foreground=colors[10],
                        font=mono_font,
                        fontsize=25,
                        padding=8,
                        background=colors[6],
                        filled=True,
                        padding_x=None,
                        padding_y=4,
                        ),
                widget.PulseVolume(
                        font = mono_font,
                        fontsize = 14,
                        foreground=colors[6],
                        limit_max_volume="True",
                        padding=8,
                        step = 5,
                        background=colors[13],
                        filled=True,
                        padding_y=4,
                        padding_x=0,
                        ),
                widget.TextBox(
                        text="⏻",
                        background=colors[0],
                        foreground="#000000",
                        font=mono_font,
                        fontsize=20,
                        padding=16,
                        mouse_callbacks={"Button1": lazy.spawn("archlinux-logout")},
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
