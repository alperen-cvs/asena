from collections import namedtuple
from dataclasses import dataclass
from typing import Any
@dataclass
class SignalContainer:
    msg: str
    status: bool

@dataclass
class RegistryWriteContainer:
    value_name: str
    value: Any
    data_type: int
@dataclass
class RegistryReadContainer:
    value: Any
    value_type: object
@dataclass
class SimpleSignalContainer:
    value: str

WinPosition = namedtuple("WinPosition",["x","y","width","height"])