import sys
import platform
from PySide6 import __version__ as pyside6_version
class Asena:
    version = "1.0"
    author = "dotPEEKs"
    git_url = "https://www.github.com/dotPEEKs/Asena"


def create_credential_str(**extras) -> str:
    win_version = platform.platform()
    python_version = platform.python_version()
    pyside6version = pyside6_version
    sys_arch = platform.architecture()
    credential_str = """-*- Asena Version: %s -*-\nWin Version: %s\nPython Version: %s\nPySide6 Version: %s\nSys Arch: %s""" % (Asena.version,win_version,python_version,pyside6version,sys_arch)
    if extras:
        for value,item in extras.items():
            credential_str+= "%s: %s\n" % (value,item)
    credential_str+="\n-*- END -*-"
    return credential_str
