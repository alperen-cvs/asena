from collections import namedtuple
from dataclasses import dataclass
################################ NAMED TUPLE CONTAİNERS ###############################

RegistryWriteContainer = namedtuple("RegistryWriteContainer",["value_name","value","data_type"])
RegistryReadContainer = namedtuple("RegistryReadContainer",["value","value_type"])
RegistryEnumeratedKeyContainer = namedtuple("RegistryEnumeratedContainer",["value_name"])
RegistryEnumeratedValueContainer = namedtuple("RegistryEnumeratedValueContainer",["value_name","value","data_type"])

OrderItemContainer = namedtuple("OrderItemContainer",["item_name","item"]) # This container is only for using table widget columns, the main container is below
################################ NAMED TUPLE CONTAİNERS ###############################

################################ DATACLASS CONTAİNERS ###############################
@dataclass
class WinPosition:
    x: int
    y: int
    width: int
    height: int

@dataclass
class CustomerContainer:
    name: str
    surname: str
    orders: list[OrderItemContainer]
class GlobalOrderContainer:
    def __init__(self):
        self._data = []
    def push_back(self,item_container: CustomerContainer):
        self._data.append(item_container)
    def pop_back(self,item_container: CustomerContainer):
        self._data.remove(item_container)
    def __iter__(self):
        for data in self._data: yield data
    def __contains__(self,input: CustomerContainer):
        return input in self._data


################################ DATACLASS CONTAİNERS ###############################
