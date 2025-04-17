# this IntEnum has been created for better readability.

import winreg
from . import IntEnum
class HKEY(IntEnum):

    HKEY_CURRENT_USER = winreg.HKEY_CURRENT_USER
    HKEY_LOCAL_MACHINE = winreg.HKEY_LOCAL_MACHINE
    HKEY_USERS = winreg.HKEY_USERS
    HKEY_CLASSES_ROOT = winreg.HKEY_CLASSES_ROOT

class REGTYPES(IntEnum):
    REG_SZ = winreg.REG_SZ
    REG_DWORD = winreg.REG_DWORD
    REG_QWORD = winreg.REG_QWORD
    REG_BINARY = winreg.REG_BINARY


def is_valid_reg_path(hkey_path: int) -> bool:
    """
    it's checking given path valid path or invalid path returns True or False
    :param value:
    :return bool:
    """
    if isinstance(hkey_path,IntEnum):
        hkey_path = hkey_path.value
    return next((member for member in HKEY if member.value == hkey_path),False) != False

