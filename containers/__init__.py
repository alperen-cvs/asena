from collections import namedtuple
from dataclasses import dataclass
SignalContainer = namedtuple("SignalContainer",["msg","status"]) # Gereksiz SignalContainer'i sil !
RegistryWriteContainer = namedtuple("RegistryWriteContainer",["value_name","value","data_type"])
RegistryReadContainer = namedtuple("RegistryReadContainer",["value","value_type"])


@dataclass
class WinPosition:
    x: int
    y: int
    width: int
    height: int
