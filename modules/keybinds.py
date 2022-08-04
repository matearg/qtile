import os
from libqtile.lazy import lazy
from libqtile.config import Key
from .groups import groups

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
terminal_var = "alacritty"
terminal = "kitty"
home = os.path.expanduser('~')

keys = [
# SUPER + NORMAL KEYS
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "e", lazy.spawn('thunar')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "i", lazy.spawn('lxappearance')),
    Key([mod], "p", lazy.spawn('rofi -show drun')),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "v", lazy.spawn(terminal + ' -e nvim')),
    Key([mod], "x", lazy.spawn('rofi -show power-menu -modi power-menu:/home/mateo/github/dotfiles/linux/rofi/rofi-power-menu')),

# SUPER + SHIFT KEYS
    Key([mod, "shift"], "c", lazy.window.kill()),
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#302D41' -nf '#DDB6F2' -sb '#DDB6F2' -sf '#302D41' -fn 'Iosevka Nerd Font Mono:pixelsize=18'")),
    Key([mod, "shift"], "f", lazy.spawn('firefox')),
    Key([mod, "shift"], "r", lazy.restart()),

# SUPER + FUNCTION KEYS
    Key([mod], "F1", lazy.spawn('amixer set Master 5%+')),
    Key([mod], "F2", lazy.spawn('amixer set Master 5%-')),
    Key([mod], "F11", lazy.spawn('rofi-theme-selector')),

# CONTROL + ALT KEYS
    Key(["mod1", "control"], "h", lazy.spawn(terminal + ' -e btm')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "s", lazy.spawn('spotify')),
    Key(["mod1", "control"], "t", lazy.spawn(terminal_var)),
    Key(["mod1", "control"], "v", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "q", lazy.shutdown()),
    Key(["mod1", "control"], "l", lazy.spawn('xflock4')),

# QTILE LAYOUT KEYS
    Key([mod, "shift"], "space", lazy.next_layout()),
    Key([mod], "n", lazy.layout.normalize()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

# SHUFLE WINDOWS ORDER
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "mod1"], "f", lazy.layout.flip()),

# TOGGLE FLOATIN LAYOUT
    Key([mod, "mod1"], "space", lazy.window.toggle_floating()),

# CHANGE KEYBOARD LAYOUT
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard()),

]

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod, "mod1"], "Left", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod, "mod1"], "Right", lazy.function(window_to_previous_screen, switch_screen=True)),
    Key([mod, "mod1"], "h", lazy.function(window_to_next_screen, switch_screen=False)),
    Key([mod, "mod1"], "l", lazy.function(window_to_previous_screen, switch_screen=False)),
])

for i in groups:
    keys.extend([
#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key([mod, "mod1"], "k", lazy.screen.next_group()),
        Key([mod, "mod1" ], "j", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
