from libqtile import widget, bar
from libqtile.lazy import lazy
from .colors import catppuccin
from .spotify import Spotify

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
                        inactive = catppuccin[15],
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
                widget.Sep(**widget_defaults),
                widget.CurrentLayout(**widget_defaults),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        text = "",
                        foreground = catppuccin[18],
                        background = catppuccin[13],
                        font = mono_font,
                        fontsize = 20,
                        ),
                widget.WindowName(
                        font = italic_font,
                        fontsize = font_size,
                        foreground = catppuccin[18],
                        background = catppuccin[13],
                        width = bar.CALCULATED,
                        empty_group_string = "Desktop",
                        max_chars = 40,
                        parse_text = parse_window_name,
                        ),
                widget.Spacer(background = catppuccin[13]),
                widget.OpenWeather(
                        font = mono_font,
                        fontsize = 30,
                        background = catppuccin[13],
                        foreground = catppuccin[5],
                        coordinates = {"longitude": "-57.5575", "latitude": "-38.0023"},
                        format = "{icon}",
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        weather_symbols = {
                            "Unknown": "✨",
                            "01d": "滛",
                            "01n": "望",
                            "02d": "杖",
                            "02n": "杖",
                            "03d": "摒",
                            "03n": "摒",
                            "04d": "敖",
                            "04n": "敖",
                            "09d": "歹",
                            "09n": "歹",
                            "10d": "滋",
                            "10n": "滋",
                            "11d": "朗",
                            "11n": "朗",
                            "13d": "流",
                            "13n": "流",
                            "50d": "煮",
                            "50n": "煮",
                        }
                        ),
                widget.OpenWeather(
                        font = regular_font,
                        fontsize = font_size,
                        background = catppuccin[13],
                        foreground = catppuccin[5],
                        coordinates = {"longitude": "-57.5575", "latitude": "-38.0023"},
                        format = "{main_temp:.0f}°{units_temperature}",
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        text="阮",
                        font = mono_font,
                        fontsize=25,
                        foreground=catppuccin[7],  # blue
                        background = catppuccin[13],
                        filled = True,
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        mouse_callbacks={"Button1": lazy.spawn("spotify")},
                        ),
                Spotify(
                        font = regular_font,
                        fontsize = font_size,
                        foreground = catppuccin[7],
                        background = catppuccin[13],
                        play_icon = "  ",
                        pause_icon = "  ",
                        format = "{icon} {artist} - {track} ",
                        max_chars = 30,
                        ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        font = mono_font,
                        text = "",
                        foreground = catppuccin[3],
                        background = catppuccin[13],
                        padding = 8,
                        padding_x = None,
                        padding_y = 4,
                        fontsize = 25,
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e yay")},
                        ),
                widget.CheckUpdates(
                        no_update_string = "N/A",
                        colour_no_updates = catppuccin[3],
                        colour_have_updates = catppuccin[3],
                        font = regular_font,
                        fontsize = font_size,
                        padding = 8,
                        padding_y = 4,
                        padding_x = 0,
                        background = catppuccin[13],
                        display_format = "{updates}",
                        update_interval = 10,
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e yay")},
                        ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        font = mono_font,
                        text = "",
                        foreground = catppuccin[4],
                        background = catppuccin[13],
                        padding = 8,
                        padding_x = None,
                        padding_y = 4,
                        fontsize = 25,
                        mouse_callbacks = {"Button1": lazy.widget["keyboardlayout"].next_keyboard()}
                        ),
                widget.KeyboardLayout(
                        font = regular_font,
                        foreground = catppuccin[4],
                        background = catppuccin[13],
                        padding = 8,
                        padding_x = 0,
                        padding_y = 4,
                        fontsize = font_size,
                        max_chars = 2,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': 'LA', 'us': 'US'}
                       ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        text="",
                        font = mono_font,
                        fontsize=25,
                        foreground=catppuccin[8],  # blue
                        background = catppuccin[13],
                        radius = 4,
                        filled = True,
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        ),
                widget.Clock(
                        font = regular_font,
                        fontsize = font_size,
                        format="%b %d, %H:%M",
                        foreground=catppuccin[8],
                        background=catppuccin[13],
                        padding=8,
                        ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        text="墳",
                        font=mono_font,
                        fontsize=25,
                        padding=8,
                        foreground=catppuccin[6],
                        background=catppuccin[13],
                        filled=True,
                        padding_x=None,
                        padding_y=4,
                        ),
                widget.PulseVolume(
                        font = regular_font,
                        fontsize = font_size,
                        limit_max_volume="True",
                        padding=8,
                        step = 5,
                        foreground=catppuccin[6],
                        background=catppuccin[13],
                        filled=True,
                        padding_y=4,
                        padding_x=0,
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