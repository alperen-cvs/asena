import ctypes
from ctypes.wintypes import LONG

class RECT(ctypes.Structure):
    _fields_ = [
        ("left",LONG),
        ("top",LONG),
        ("right",LONG),
        ("bottom",LONG)
    ]

LRECT = PRECT = NPRECT = RECT

