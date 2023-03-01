from libqtile import hook
from os import path
import subprocess

from settings.groups import groups
from settings.keybinds import keys
from settings.mouse import mouse
from settings.screens import screens
from settings.layouts import *

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
auto_minimize = False
wmname = "Qtile"

@hook.subscribe.startup_once
def start_once():
    home = path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart'])

