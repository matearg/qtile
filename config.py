from libqtile import hook
import os
import subprocess

from modules.groups import groups
from modules.keybinds import keys
from modules.mouse import mouse
from modules.screens import screens
from modules.layouts import layouts, floating_layout

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
auto_minimize = False
wmname = "qtile"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

