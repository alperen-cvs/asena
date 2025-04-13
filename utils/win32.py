import os
import sys
import ctypes

from win32gui import GetForegroundWindow

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from ._win32structs import RECT
from containers import WinPosition

FindWindow = ctypes.windll.user32.FindWindowW
GetWindowRect = ctypes.windll.user32.GetWindowRect
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLen = ctypes.windll.user32.GetWindowTextLengthW
EnumWindows = ctypes.windll.user32.EnumWindows
GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow

def find_window_cordinates(window_name: str) -> WinPosition:
    """
    returns the x y width and height values of the given window in the system and returns WinPosition
    its usage is quite simple
    win_pos = find_window_cordinates("Example Window")
    print("width: ",winpos.width)
    print("height: ",winpos.height)
    print("x: ",winpos.x)
    print("y: ",winpos.y)
    :param window_name:
    :return WinPosition:
    """
    rectangle = RECT()
    hwnd = FindWindow(None,window_name)
    GetWindowRect(hwnd,ctypes.byref(rectangle))
    x = rectangle.left
    y = rectangle.top
    width = rectangle.right - rectangle.left
    height = rectangle.bottom - rectangle.top
    return WinPosition(x=x,y=y,width=width,height=height)


def get_window_text(hwnd: int) -> str:

    """
    It is used to get the hwnd information of the windows and get the window name. It requires an integer hwnd value as a parameter and returns a string as a return.
    :param hwnd:
    :return:
    """
    window_text_length = GetWindowTextLen(hwnd) + 1
    ctypes_buffer = ctypes.create_unicode_buffer(window_text_length)
    GetWindowText(hwnd,ctypes_buffer,window_text_length)
    return "" if ctypes_buffer.value is None else ctypes_buffer.value

def get_current_window_text() -> str:
    """
    Returns the name of the currently active window
    :return:
    """
    hwnd = GetForegroundWindow()
    return get_window_text(hwnd)
def enum_windows() -> list:
    """
    Gets all active windows with string values and returns a list as a return
    :return:
    """
    windows = []
    black_list_windows = ["Default IME","","MSCTFIME UI","BroadcastListenerWindow","DesktopWindowXamlSource"] # unnecessary and garbage window has no use
    hwnds_of_windows = []
    def enum_func(hwnd,_) -> bool:
        hwnds_of_windows.append(hwnd)
        return True
    win_enumerator = ctypes.WINFUNCTYPE(ctypes.c_bool,ctypes.c_int,ctypes.c_int)(enum_func)
    EnumWindows(win_enumerator,0)
    for window_hwnd in hwnds_of_windows[:]:
        window_text = get_window_text(window_hwnd)
        if not window_text in black_list_windows[:] and not window_text.isdigit():
            windows.append(window_text)
    return windows
