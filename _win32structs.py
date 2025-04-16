import ctypes
class RECT(ctypes.Structure):
    _fields_ = [
        ("left",ctypes.wintypes.LONG),
        ("top",ctypes.wintypes.LONG),
        ("right",ctypes.wintypes.LONG),
        ("bottom",ctypes.wintypes.LONG)
    ]

LRECT = PRECT = NPRECT = RECT

class BITMAP(ctypes.Structure):
    _fields_ = [
        ("bmType", ctypes.wintypes.LONG),
        ("bmWidth", ctypes.wintypes.LONG),
        ("bmHeight", ctypes.wintypes.LONG),
        ("bmWidthBytes", ctypes.wintypes.LONG),
        ("bmPlanes", ctypes.wintypes.WORD),
        ("bmBitsPixel", ctypes.wintypes.WORD),
        ("bmBits", ctypes.wintypes.LPVOID),
    ]



