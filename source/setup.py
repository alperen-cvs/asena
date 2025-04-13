import os
import sys
import glob
from types import FunctionType
from PySide6.QtCore import QThreadPool
from PySide6.QtCore import QRunnable
from PySide6.QtCore import Signal
from PySide6.QtCore import QObject
from typing import override

from utils.reg_utils import HKEY
from utils.reg_utils import Registry
from utils.reg_utils import REGTYPES
from utils import exe_mode_enabled
from utils.log_utils import create_new_logger_instance
from utils.fs import create_file
from utils.fs import copyfile2dst
from enums.defaults import Defaults


class Signals(QObject):
    progress = Signal(tuple)

class ThreadWorker(QRunnable):
    def __init__(self,setup_handler):
        super(ThreadWorker,self).__init__()
        self.setup_handler = setup_handler
    @override
    def run(self):
        self.setup_handler.handle_setup_progress()

class SetupModule:
    def __init__(self,entry_path: str,auto_start: bool,setup_path: str):
        self.base_registry_path = r"Software\Asena"
        self.entry_path = entry_path # This variable will be replaced with the current path when the exe file is run, so the exe files will be placed in the target folder.
        self.signal_function = lambda *_:None # daha iyi bir isim bul
        self.setup_path = setup_path
        self.auto_start = auto_start
        self.registry = Registry(HKEY.HKEY_CURRENT_USER,self.base_registry_path)
        self.log = create_new_logger_instance("setup_module")
        self.step = True
    def callback_function(self,label_str: str,step: bool):
        self.step = step
        self.signal_function((label_str,step))
    def create_registry_items(self):
        self.callback_function("Registry değişkenleri atanıyor ...",True)
        registry_items = [
            (
                "AsenaSetupPath",
                self.setup_path,
                REGTYPES.REG_SZ
            ),
            (
                "AsenaLoginBlock",
                0,
                REGTYPES.REG_DWORD
            ),
            (
                "AutoBackupToDriveCloud",
                0,
                REGTYPES.REG_DWORD
            ),
            (
                "AutoBackupTimeRange",
                0,
                REGTYPES.REG_DWORD
            )
        ]
        for registry_item in registry_items[:]:
            registry_key_name = registry_item[0]
            registry_key_item = registry_item[1]
            registry_key_item_type = registry_item[2]
            if not self.registry.write_key(registry_key_name,registry_key_item,data_type = registry_key_item_type):
                self.callback_function(Defaults.DEFAULT_CRASH_STR,False)
        if self.auto_start:
            print("God damn mannn")
            self.registry.regpath = HKEY.HKEY_CURRENT_USER
            self.registry.sub_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            self.registry.write_key("AsenaAutoStart","\"%s\"" % (sys.executable))
    def copy_files(self):
        """
        Dosyalar exe dosyasının konumundan kurulum patikasına atılacak
        :return:
        """
        """
        exe_files = ["ab",",","b"] # bunu exe_mode_enabled fonksiyonuna göre ayarla !
        for exe_file in exe_files[:]:
            base_name_of_exe_file = os.path.basename(exe_file)
            target_path = os.path.join(self.setup_path,base_name_of_exe_file)
            if copyfile2dst(exe_file,target_path):
                self.callback_function("Kopyalandı - %s" % (target_path),True)
            else:
                self.callback_function(Defaults.DEFAULT_CRASH_STR,False)
        """
    def handle_setup_progress(self):
        self.callback_function("Kurulum işlemi başlıyor ...",True)
        for function in [self.create_registry_items,self.copy_files]:
            function()
        if self.step:
            self.finish_setup_progress()
    def finish_setup_progress(self):
        pass