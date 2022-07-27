import os
import subprocess
from libqtile import layout, bar, hook
from libqtile.config import Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from utils import bar1, bar2

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


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

keys = [

# SUPER + NORMAL KEYS
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn('alacritty')),
    Key([mod], "e", lazy.spawn('thunar')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "i", lazy.spawn('archlinux-tweak-tool')),
    Key([mod], "p", lazy.spawn('rofi -show drun')),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "v", lazy.spawn('alacritty -e nvim')),
    Key([mod], "x", lazy.spawn('archlinux-logout')),

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
    Key(["mod1", "control"], "h", lazy.spawn('alacritty -e btm')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "s", lazy.spawn('spotify')),
    Key(["mod1", "control"], "t", lazy.spawn('alacritty')),
    Key(["mod1", "control"], "v", lazy.spawn('pavucontrol')),

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
    Key([mod, "mod1"], "h", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod, "mod1"], "l", lazy.function(window_to_previous_screen, switch_screen=True)),
])

groups = []

group_names = ["1", "2", "3", "4", "5",]

group_labels = ["", "", "", "阮", "",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

userBar = bar1

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

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

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
