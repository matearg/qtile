from libqtile.widget.textbox import TextBox

def left_half_circle(bg_color, fg_color):
    return TextBox(
        text='\uE0B6',
        fontsize=28,
        background = bg_color,
        foreground=fg_color,
        padding=0)

def right_half_circle(bg_color, fg_color):
    return TextBox(
        text='\uE0B4',
        fontsize=28,
        background=bg_color,
        foreground=fg_color,
        padding=0)

def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=24,
        background=bg_color,
        foreground=fg_color)

def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=24,
        background=bg_color,
        foreground=fg_color)