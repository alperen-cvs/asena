from utils.reg_utils import Registry
from .winreg_enums import HKEY,REGTYPES


registry = Registry(HKEY.HKEY_CURRENT_USER,r"Software\Asena")

class SetupConstants:

    """
    It is a very critical class, you are kindly requested not to change it.
    It is the class that processes the installation path, database, image, application path after the installation is done.
    """

    DATABASE_PATH = registry.read_key("Asena_Database")
    IMAGE_PATH = registry.read_key("ItemImages")
    APP_PATH = registry.read_key("AsenaAppPath")

