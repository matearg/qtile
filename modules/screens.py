from libqtile import bar
from libqtile.config import Screen
from .widgetsvariant2 import widgets_screen1, widgets_screen2

def init_screens():
    return [
            # Screen(top=bar.Bar(widgets = widgets_screen1, opacity = 1, size = 30, margin = [8, 8, 0, 8])),
            Screen(top=bar.Bar(widgets = widgets_screen1, opacity = 1, size = 28, margin = 0)),
            # Screen(top=bar.Bar(widgets = widgets_screen2, opacity = 1, size = 30, margin = [8, 8, 0, 8]))
    ]

screens = init_screens()
