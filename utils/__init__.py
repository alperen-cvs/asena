import os
import string
import random
import ctypes.wintypes

from utils.reg_utils import Registry
from utils.reg_utils import HKEY

from ._win32structs import BITMAP
def get_assets_rc_path() -> str:
    return os.path.join(
        os.path.dirname(__file__),
        "..",
        "image_src"
    )
def exe_mode_enabled() -> bool:
    """
    ito find out if the program is running in exe mode
    NOTE: Please remember that this is only valid for nuitka, other compilers may have different methods, so methods like sys.frozen are invalid
    :return:
    """
    return globals().get("__compiled__",False)

def get_default_desktop() -> str:
    """
    Returns the user's current desktop path
    :return:
    """
    registry = Registry(HKEY.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
    desktop_path = registry.read_key("Desktop").value
    if desktop_path.startswith("%"):
        desktop_path = desktop_path[1:desktop_path.index("%",1).replace("%")] # SOMETIMES registry items returns %USERPROFILE%\Desktop
    return desktop_path
def create_desktop_shortcut(exe_path):
    lnk_path = os.path.basename(os.path.splitext(exe_path)[0]) + ".lnk"
    lnk_path = os.path.join(get_user_desktop(), lnk_path)
    win32_client = Dispatch("WScript.Shell")
    shortcut = win32_client.CreateShortcut(lnk_path)
    shortcut.TargetPath = exe_path
    shortcut.Save()


create_rand_char = lambda len:"".join(random.sample(string.ascii_letters,len))

def screenshot(save_to = ".",fd = None):
    user32 = ctypes.windll.user32
    gdi32 = ctypes.windll.gdi32


    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)


    hdc_screen = user32.GetDC(0)
    hdc_mem = gdi32.CreateCompatibleDC(hdc_screen)
    hbitmap = gdi32.CreateCompatibleBitmap(hdc_screen, screen_width, screen_height)
    gdi32.SelectObject(hdc_mem, hbitmap)

    gdi32.BitBlt(hdc_mem, 0, 0, screen_width, screen_height, hdc_screen, 0, 0, 0x00CC0020)


    bmp_info = BITMAP()
    gdi32.GetObjectW(hbitmap, ctypes.sizeof(bmp_info), ctypes.byref(bmp_info))

    bmp_header = b"BM" + (14 + 40 + bmp_info.bmWidth * bmp_info.bmHeight * 4).to_bytes(4, "little")
    bmp_header += (0).to_bytes(4, "little")  # Reserved
    bmp_header += (14 + 40).to_bytes(4, "little")

    bmp_info_header = (40).to_bytes(4, "little")
    bmp_info_header += bmp_info.bmWidth.to_bytes(4, "little")
    bmp_info_header += (-bmp_info.bmHeight).to_bytes(4, "little", signed=True)
    bmp_info_header += (1).to_bytes(2, "little")  # Planes
    bmp_info_header += (32).to_bytes(2, "little")  # Bit count
    bmp_info_header += (0).to_bytes(4, "little")  # Compression
    bmp_info_header += (bmp_info.bmWidth * bmp_info.bmHeight * 4).to_bytes(4, "little")
    bmp_info_header += (2835).to_bytes(4, "little") * 2  # PPM X, Y
    bmp_info_header += (0).to_bytes(4, "little") * 2  # Color tables

    buffer_size = bmp_info.bmWidth * bmp_info.bmHeight * 4
    bmp_data = ctypes.create_string_buffer(buffer_size)
    gdi32.GetBitmapBits(hbitmap, buffer_size, bmp_data)
    bmp_data = bmp_header + bmp_info_header + bmp_data.raw

    try:
        if fd is None:
            with open(os.path.join(save_to,f"screenshot_{create_rand_char(12)}.bmp"), "wb") as f:
                f.write(bmp_data)
        else:
            fd.write(bmp_data)
    except:
        return False
    return True

    user32.ReleaseDC(0, hdc_screen)
    gdi32.DeleteDC(hdc_mem)
    gdi32.DeleteObject(hbitmap)
