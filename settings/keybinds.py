from os import path
from libqtile.lazy import lazy
from libqtile.config import Key
from .groups import groups
from .colors import *
from .traverse import *

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
terminal_var = "kitty"
terminal = "alacritty"
home = path.expanduser('~')
font = "CaskaydiaCove Nerd Font"


def dmenu_colors():
    if(theme == nord):
        scheme = "dmenu_run -i -nb '#3b4252' -nf '#81a1c1' -sb '#81a1c1' -sf '#3b4252' -fn '" + font + ":pixelsize=20'"
    elif(theme == catppuccin):
        scheme = "dmenu_run -i -nb '#302D41' -nf '#DDB6F2' -sb '#DDB6F2' -sf '#302D41' -fn '" + font + ":pixelsize=20'"
    elif(theme == monokai):
        scheme = "dmenu_run -i -nb '#2d2a2e' -nf '#ff6188' -sb '#ff6188' -sf '#2d2a2e' -fn '" + font + ":pixelsize=20'"
    elif(theme == rosepine):
        scheme = "dmenu_run -i -nb '#393552' -nf '#ea9a97' -sb '#ea9a97' -sf '#393552' -fn '" + font + ":pixelsize=20'"
    else:
        scheme = "dmenu_run -i -fn 'monospace:pixelsize=20'"

    return scheme
dmenu = dmenu_colors()


keys = [
# SUPER + NORMAL KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),

# QTILE LAYOUT KEYS
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift" ], "Tab", lazy.prev_layout()),
    Key([mod], "n", lazy.layout.normalize()),

# CHANGE FOCUS
    Key([mod], 'k', lazy.function(up)),
    Key([mod], 'j', lazy.function(down)),
    Key([mod], 'h', lazy.function(left)),
    Key([mod], 'l', lazy.function(right)),

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

# TOGGLE FLOATING LAYOUT
    Key([mod, "mod1"], "space", lazy.window.toggle_floating()),

# CHANGE KEYBOARD LAYOUT
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard()),

]

@lazy.function
def window_to_prev_group(qtile, switch_screen=False):
    i = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None and i != 0:
        qtile.current_window.togroup(qtile.groups[i - 1].name)
        if switch_screen == True:
            qtile.current_screen.toggle_group(qtile.groups[i - 1])

@lazy.function
def window_to_next_group(qtile, switch_screen=False):
    i = qtile.groups.index(qtile.current_group)
    if qtile.current_window is not None and i != 6:
        qtile.current_window.togroup(qtile.groups[i + 1].name)
        if switch_screen == True:
            qtile.current_screen.toggle_group(qtile.groups[i + 1])

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
    Key([mod, "mod1"], "Left", lazy.function(window_to_next_screen, switch_screen=False)),
    Key([mod, "mod1"], "Right", lazy.function(window_to_previous_screen, switch_screen=False)),
    Key([mod, "mod1"], "h", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod, "mod1"], "l", lazy.function(window_to_previous_screen, switch_screen=True)),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
])

for i in groups:
    keys.extend([
        #CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "mod1"], "j", lazy.screen.next_group()),
        Key([mod, "mod1"], "k", lazy.screen.prev_group()),

        # MOVE WINDOW TO NEXT/PREV GROUP
        Key(["mod1", "control"], "j", window_to_next_group(switch_screen=True)),
        Key(["mod1", "control"], "k", window_to_prev_group(switch_screen=True)),
        Key(["mod1", "control"], "Right", window_to_next_group(switch_screen=False)),
        Key(["mod1", "control"], "Left", window_to_prev_group(switch_screen=False)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])
