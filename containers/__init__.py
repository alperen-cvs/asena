from collections import namedtuple
from dataclasses import dataclass
from ._card_widget import *
SignalContainer = namedtuple("SignalContainer",["msg","status"])
RegistryWriteContainer = namedtuple("RegistryWriteContainer",["value_name","value","data_type"])
RegistryReadContainer = namedtuple("RegistryReadContainer",["value","value_type"])


@dataclass
class WinPosition:
    x: int
    y: int
    width: int
    height: int