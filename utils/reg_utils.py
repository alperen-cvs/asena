import winreg
import logging
from enums.winreg_enums import HKEY
from enums.winreg_enums import REGTYPES
from source.exceptions import InvalidHKEYPath
from enums.winreg_enums import is_valid_reg_path
from utils.log_utils import create_new_logger_instance
from containers import RegistryReadContainer
class Registry:
    def __init__(self,
        reg_path: int | HKEY,
        sub_path: str
                 ):
        """
        :param reg_path main path of registry e.g HKCU,HKEY,HKLU
        :param sub_path: sub path of registry e.g Software\\Microsoft .etc
        """
        self.reg_path = reg_path
        self.sub_path = sub_path
        self.log = create_new_logger_instance(__name__)
    def write_key(self,value_name: str,value,*,data_type = REGTYPES.REG_SZ) -> bool:
        """
        it's write specified key
        but you should check type param otherwise returns false
        :param value_name:
        :param value:
        :param data_type:
        :return:
        """
        try:
            hReg = winreg.CreateKey(self.reg_path,self.sub_path)
            winreg.SetValueEx(hReg,value_name,0,data_type,value)
            winreg.CloseKey(hReg)
        except Exception as fault:
            self.log.critical("Write Error: %s - Path: %s Value: %s Value Name: %s Data Type: %s" % (fault,repr(self.reg_path),value,value_name,repr(data_type)))
            return False
        return True
    def read_key(self,value_name: str) -> RegistryReadContainer:
        """
        it's read key given value name
        :param value_name:
        :returns: tuple[value,value_type]
        """
        try:
            hReg = winreg.OpenKey(self.reg_path,self.sub_path,0,winreg.KEY_READ)
            value,regtype = winreg.QueryValueEx(hReg,value_name)
            winreg.CloseKey(hReg)
            return RegistryReadContainer(value = value,value_type = regtype)
        except Exception as fault:
            self.log.critical("Read Error: %s Value Name: %s - Base Path: %s" % (fault,value_name,repr(self.reg_path)))
            return False
    @property
    def regpath(self) -> int:
        return self.reg_path
    @regpath.setter
    def regpath(self,value: int or HKEY) -> None:
        if not is_valid_reg_path(value):
            raise InvalidHKEYPath("Invalid Hkey path :/ see winreg_enums module")
        self.reg_path = value
    def key_exists(self,value_name: str) -> bool:
        """
        checks key exists
        :param value_name:
        :return:
        """
        return self.read_key(value_name) != False
