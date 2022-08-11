from libqtile import bar
from libqtile.config import Screen
from .widgetsvariant4 import widgets_screen1

def init_screens():
    return [
            # Screen(top=bar.Bar(widgets = widgets_screen1, opacity = 1, size = 30, margin = [10, 10, 0, 10])),
            Screen(top=bar.Bar(widgets = widgets_screen1, opacity = 1, size = 30, margin = 0)),
    ]

screens = init_screens()
