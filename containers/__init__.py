from collections import namedtuple
from dataclasses import dataclass
################################ NAMED TUPLE CONTAİNERS ###############################

RegistryWriteContainer = namedtuple("RegistryWriteContainer",["value_name","value","data_type"])
RegistryReadContainer = namedtuple("RegistryReadContainer",["value","value_type"])
RegistryEnumeratedKeyContainer = namedtuple("RegistryEnumeratedContainer",["value_name"])
RegistryEnumeratedValueContainer = namedtuple("RegistryEnumeratedValueContainer",["value_name","value","data_type"])

OrderItemContainer = namedtuple("OrderItemContainer",["item_name","item_barcode","item_image_path","item_count"]) # This container is only for using table widget columns, the main container is below

ItemsContainer = namedtuple("ItemsContainer",["order_item_containers"]) # maybe you can change this container database module will process it

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


################################ DATACLASS CONTAİNERS ###############################


################################ Custom Containers  #################################

class GlobalOrderContainer:
    """
    This container holds general information about orders and is filled by the order screen

    With the push_back function, the CustomerContainer object is added to the list
    If CustomerContainer, it takes the parameters
    name
    surname
    orders

    if orders, it should be a list and it should have "OrderItemContainer" objects

    If OrderItemContainer object, it has 4 parameters in order:
    item_name - product name
    item_barcode - product barcode(Optional)
    item_image_path - product image(Optional) Product image should be maximum 400x400
    item_count - is the stock quantity of the product
    """
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
