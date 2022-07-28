import os
import subprocess
from libqtile import layout, bar, hook
from libqtile.config import Drag, Match, Screen
from libqtile.lazy import lazy
from utils import bar1, bar2, keybinds

mod = "mod4"
keys = keybinds.keys
groups = keybinds.groups
userBar = bar2

def border_colors(bar):
    if bar == bar1:
        color = 0
    else:
        color = 18
    return color

def if_bar(bar):
    if bar == bar1:
        margin_val = [8, 8, 0, 8]
    else:
        margin_val = 0
    return margin_val

def init_layout_theme():
    return {"margin": 8,
            "border_width": 2,
            "border_focus": userBar.colors[border_colors(userBar)],
            "border_normal": userBar.colors[13] 
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]

widgets_screen1 = userBar.init_widgets_screen1()
widgets_screen2 = userBar.init_widgets_screen2()

def init_screens():
    return [
            Screen(top=bar.Bar(widgets = widgets_screen1, opacity = 1, size = 30, margin = if_bar(userBar))),
            # Screen(top=bar.Bar(widgets = widgets_screen2, opacity = 1, size = 30, margin = if_bar(userBar)))
            ]
screens = init_screens()

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='nitrogen'),
    Match(wm_class='ristretto'),
    Match(wm_class='pavucontrol'),

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True
focus_on_window_activation = "smart" # or smart
wmname = "qtile"
