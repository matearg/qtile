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
                background = colors[10])

def init_widgets_list():
    widgets_list = [
                widget.GroupBox(
                        active = colors[18],
                        block_highlight_text_color = colors[18],
                        this_current_screen_border = colors[18],
                        this_screen_border = colors[18],
                        urgent_border = colors[3],
                        background = colors[10],  # background is [10-12]
                        other_current_screen_border = colors[13],
                        other_screen_border = colors[13],
                        highlight_color = colors[13],
                        inactive = colors[14],
                        foreground = colors[18],
                        borderwidth = 2,
                        disable_drag = True,
                        font = mono_font,
                        fontsize = 16,
                        highlight_method = "line",
                        padding_x = 10,
                        padding_y = 16,
                        rounded = False,
                        ),
                widget.Sep(
                    foreground = colors[15],
                    background = colors[10]
                    ),
                widget.CurrentLayout(
                        font = regular_font,
                        fontsize = 14,
                        foreground = colors[18],
                        background = colors[10],
                        padding = 8,
                        padding_y = 4,
                        padding_x = 0,
                        ),
                widget.Sep(
                    foreground = colors[15],
                    background = colors[10]
                    ),
                widget.WindowName(
                        font = italic_font,
                        fontsize = 14,
                        foreground = colors[18],
                        background = colors[10],
                        width = bar.CALCULATED,
                        empty_group_string = "Desktop",
                        max_chars = 40,
                        parse_text = parse_window_name,
                        padding = 8,
                        padding_y = 4,
                        padding_x = 0,
                        ),
                widget.Spacer(background = colors[10]),
                widget.Memory(
                        background = colors[10],
                        foreground = colors[18],
                        font = mono_font,
                        fontsize = 14,
                        format = "{MemUsed:.1f}Gb/{MemTotal:.0f}Gb",
                        measure_mem = 'G',
                        padding = 8,
                        padding_y = 4,
                        padding_x = 0,
                        mouse_callbacks = {"Button1": lazy.spawn("alacritty -e htop")},
                        ),
                widget.Sep(
                    foreground = colors[15],
                    background = colors[10]
                    ),
                Spotify(
                        font = regular_font,
                        fontsize = 14,
                        foreground = colors[18],
                        background = colors[10],
                        play_icon = " ",
                        pause_icon = " ",
                        format = "{icon} {artist} - {track}",
                        padding = 8,
                        padding_y = 4,
                        padding_x = 0,
                        ),
                widget.Sep(
                    foreground = colors[15],
                    background = colors[10]
                    ),
                widget.KeyboardLayout(
                        font = regular_font,
                        foreground = colors[18],
                        background = colors[10],
                        padding = 3,
                        fontsize = 14,
                        max_chars = 4,
                        configured_keyboards = ['latam', 'us'],
                        display_map = {'latam': ' LA ', 'us': ' US '}
                       ),
                widget.Sep(
                    foreground = colors[15],
                    background = colors[10]
                    ),
                widget.Clock(
                        font = regular_font,
                        foreground = colors[18],
                        background = colors[10],
                        fontsize = 14,
                        format="%b %d, %H:%M",
                        padding = 8,
                        padding_y = 4,
                        padding_x = 0,
                        ),
                widget.Sep(
                    foreground = colors[15],
                    background = colors[10]
                    ),
                widget.PulseVolume(
                        font = mono_font,
                        fontsize = 14,
                        foreground=colors[18],
                        limit_max_volume="True",
                        padding=8,
                        step = 5,
                        background=colors[10],
                        filled=True,
                        padding_y=4,
                        padding_x=0,
                        ),
                widget.Sep(
                    foreground = colors[15],
                    background = colors[10]
                    ),
                widget.TextBox(
                        text="[X]",
                        background=colors[10],
                        foreground=colors[18],
                        font=bold_font,
                        fontsize=18,
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
    return widgets_screen2
