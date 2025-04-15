from collections import namedtuple
from ._card_widget import *
SignalContainer = namedtuple("SignalContainer",["msg","status"])
RegistryWriteContainer = namedtuple("RegistryWriteContainer",["value_name","value","data_type"])
RegistryReadContainer = namedtuple("RegistryReadContainer",["value","value_type"])
WinPosition = namedtuple("WinPosition",["x","y","width","height"])