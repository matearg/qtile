from libqtile import bar
from libqtile.config import Screen
from .widgets import widgets_screen1

def init_screens():
    return [
            # Screen(top=bar.Bar(widgets = widgets_screen1, opacity = 1, size = 35, margin = 0)),
            Screen(top=bar.Bar(widgets = widgets_screen1, opacity = 1, size = 35, margin = [5, 5, 0, 5])),
    ]

screens = init_screens()
