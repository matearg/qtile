from libqtile import layout
from . import bar1

def init_layout_theme():
    return {"margin": 8,
            "border_width": 2,
            "border_focus": bar1.colors[0],
            "border_normal": bar1.colors[13] 
            }

layout_theme = init_layout_theme()

layouts_list = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
]
