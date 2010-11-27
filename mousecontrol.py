from Xlib import X, display

current_display = display.Display()
current_screen = current_display.screen()
current_root = current_screen.root

def sync_display():
    current_display.sync()

def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = current_root.query_pointer()._data
    return data["root_x"], data["root_y"]

def mouse_move_to(offset):
    current_root.warp_pointer(offset[0], offset[1])
    sync_display()
