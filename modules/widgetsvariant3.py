from libqtile import widget, bar
from libqtile.lazy import lazy
from .colors import theme
from .spotify import Spotify

regular_font = "JetBrainsMono Nerd Font"
mono_font = regular_font + " Mono"
italic_font = regular_font + " Italic"
bold_font = regular_font + " Bold"
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
                padding = 8,
                padding_y = 4,
                padding_x = 0,
                foreground = theme[10],
                background = theme[8],
                )

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(
                        active = theme[0],
                        block_highlight_text_color = theme[0],
                        this_current_screen_border = theme[0],
                        this_screen_border = theme[0],
                        urgent_border = theme[1],
                        background = theme[8],  # background is [10-12]
                        other_current_screen_border = theme[8],
                        other_screen_border = theme[8],
                        highlight_color = theme[8],
                        inactive = theme[9],
                        foreground = theme[10],
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
                        foreground = theme[10],
                        background = theme[8],
                        font = mono_font,
                        fontsize = 20,
                        ),
                widget.WindowName(
                        font = italic_font,
                        fontsize = font_size,
                        foreground = theme[10],
                        background = theme[8],
                        width = bar.CALCULATED,
                        empty_group_string = "Desktop",
                        max_chars = 40,
                        parse_text = parse_window_name,
                        ),
                widget.Spacer(background = theme[8]),
                widget.TextBox(
                        text="阮",
                        font = mono_font,
                        fontsize=25,
                        foreground=theme[5],  # blue
                        background = theme[8],
                        filled = True,
                        padding_y=4,
                        padding_x=0,
                        padding=8,
                        mouse_callbacks={"Button1": lazy.spawn("spotify")},
                        ),
                Spotify(
                        font = regular_font,
                        fontsize = font_size,
                        foreground = theme[5],
                        background = theme[8],
                        play_icon = "  ",
                        pause_icon = "  ",
                        format = "{icon} {artist} - {track} ",
                        max_chars = 30,
                        ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        font = mono_font,
                        text = "",
                        foreground = theme[1],
                        background = theme[8],
                        padding = 8,
                        padding_x = None,
                        padding_y = 4,
                        fontsize = 25,
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e sudo paru")},
                        ),
                widget.CheckUpdates(
                        no_update_string = "N/A",
                        colour_no_updates = theme[1],
                        colour_have_updates = theme[1],
                        font = regular_font,
                        fontsize = font_size,
                        padding = 8,
                        padding_y = 4,
                        padding_x = 0,
                        background = theme[8],
                        display_format = "{updates}",
                        update_interval = 10,
                        mouse_callbacks = {"Button1": lazy.spawn("kitty -e sudo paru")},
                        ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        font = mono_font,
                        text = "",
                        foreground = theme[2],
                        background = theme[8],
                        padding = 8,
                        padding_x = None,
                        padding_y = 4,
                        fontsize = 25,
                        mouse_callbacks = {"Button1": lazy.widget["keyboardlayout"].next_keyboard()}
                        ),
                widget.KeyboardLayout(
                        font = regular_font,
                        foreground = theme[2],
                        background = theme[8],
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
                        foreground=theme[6],  # blue
                        background = theme[8],
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
                        foreground=theme[6],
                        background=theme[8],
                        padding=8,
                        ),
                widget.Sep(**widget_defaults),
                widget.TextBox(
                        text="墳",
                        font=mono_font,
                        fontsize=25,
                        padding=8,
                        foreground=theme[4],
                        background=theme[8],
                        filled=True,
                        padding_x=None,
                        padding_y=4,
                        ),
                widget.Volume(
                        font = regular_font,
                        fontsize = font_size,
                        foreground=theme[4],
                        background=theme[8],
                        padding = 8,
                        padding_x = 0,
                        padding_y = 4,
                        step = 5,
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
