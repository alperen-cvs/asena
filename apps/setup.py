import os
import time
import sys
from typing import override

from PySide6.QtCore import QRunnable

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from PySide6.QtCore import QThreadPool
from PySide6.QtCore import Signal
from PySide6.QtCore import QObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QFileDialog

from models.setup_model import Ui_Form
from containers import RegistryWriteContainer

from enums.defaults import Defaults
from utils.fs import WriteOk
from utils.fs import ReadOk
from utils import  get_default_desktop
from utils.log_utils import create_new_logger_instance
from utils.log_utils import pack_log_files
from utils.reg_utils import Registry
from utils.reg_utils import HKEY
from utils.reg_utils import REGTYPES
from tempfile import NamedTemporaryFile
from utils import screenshot
from utils import  exe_mode_enabled
logger = create_new_logger_instance(Defaults.DEFAULT_LOG_FILE_PATH)

class Signals(QObject):
    msg_signal = Signal(str)
    progress_signal = Signal(bool)
class WorkerClass(QRunnable):
    def __init__(self,parent_class):
        super().__init__()
        self.parent_class = parent_class
    @override
    def run(self):
        self.parent_class.start_thread()
class SetupUI(QWidget,Ui_Form):
    """
    kod düzenlemesi yapılacak
    text_edit min'den max'e çekilecek
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signal = Signals()
        self.signal.msg_signal.connect(self.add_text)
        self.signal.progress_signal.connect(self.follow_progress_status)
        self.set_line_edit_path()
        self.set_all_signals()
        self.step = True
    def launch_file_dialog(self):
        file_dialog_window = QFileDialog()
        file_dialog_window.setWindowTitle("Patika seçin ")
        file_dialog_window.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        file_dialog_window.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog_window.exec()
        directory = file_dialog_window.selectedFiles()[0].replace("/","\\")
        if not WriteOk(directory) and not ReadOk(directory): # path has no write/read permission
            message_box = QMessageBox()
            message_box.setText("Uygun olmayan patika :/ seçilen patika uygun özellikleri taşımıyor :/ (R/W)")
            message_box.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            message_box.setWindowTitle("Hata")
            message_box.exec()
        else:
            self.path_line_edit.setText(directory)

    def setup(self):
        self.setup_btn.clicked.connect(lambda *_:None)
        self.status_line.setMaximumHeight(Defaults.DEFAULT_MAX_WINDOW_SIZE)
        self.qmain_thread = QThreadPool().globalInstance()
        self.worker = WorkerClass(self)
        self.qmain_thread.start(self.worker)

    def set_all_signals(self):
        self.file_dialog_btn.clicked.connect(self.launch_file_dialog)
        self.setup_btn.clicked.connect(self.setup)
    def set_line_edit_path(self):
        self.path_line_edit.mousePressEvent = self.reset_line_edit
        self.path_line_edit.setText(Defaults.DEFAULT_SETUP_PATH)
    def reset_line_edit(self,*args,**kwargs):
        self.path_line_edit.setText(Defaults.DEFAULT_SETUP_PATH)
    def create_registry_items(self):
        self.registry_items = (
            RegistryWriteContainer(
                value_name = "AsenaLoginBlock",
                value = 0,
                data_type = REGTYPES.REG_DWORD
            ),
        )
        self.registry = Registry(HKEY.HKEY_CURRENT_USER,r"Software\Asena")
        for registry_item in self.registry_items[:]:
            if not self.registry.write_key(registry_item.value_name,registry_item.value,data_type = registry_item.data_type):
                self.signal.progress_signal.emit(True)
                break
            else:
                self.signal.msg_signal.emit("Registry Ekleniyor: %s" % (registry_item.value_name))
        if self.persistance_btn.isChecked():

            self.registry.sub_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            path = "\"%s\" %s" %  (sys.executable,os.path.join(self.path_line_edit.text(),"asena.exe") if exe_mode_enabled() else os.path.join(sys.executable,os.path.dirname(__file__),"login.py"))
            if not self.registry.write_key("AsenaAutoStart",path):
                self.signal.progress_signal.emit(True)
                return
            self.signal.msg_signal.emit("Otomatik Başlatma: Açık")

    def follow_progress_status(self,status: bool):
        if status:
            self.step = False
            files_to_copy = [Defaults.DEFAULT_LOG_FILE_PATH]
            temp_fd = NamedTemporaryFile(mode = "wb+",delete=False,suffix=".bmp")
            screenshot(fd = temp_fd)
            Messagebox = QMessageBox()
            Messagebox.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
            Messagebox.setWindowTitle("-*- HATA -*-")
            Messagebox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            Messagebox.setText(Defaults.DEFAULT_CRASH_STR)
            MessageboxResult = Messagebox.exec()
            if MessageboxResult == QMessageBox.StandardButton.Yes:
                files_to_copy.append(temp_fd.name)
            print(files_to_copy)
            pack_log_files(os.path.join(get_default_desktop(),"crash_logs_%s.zip" % (time.strftime(Defaults.DEFAULT_TIME_FORMAT))),*files_to_copy)
            temp_fd.close()
            sys.exit(1)

    def add_text(self,msg: str):
        self.status_line.append(msg)
    def start_thread(self):
        functions = [self.create_registry_items, ]
        for function in functions[:]:
            if self.step:
                function()

if __name__ == "__main__":
    app = QApplication([])
    window = SetupUI()
    window.show()
    app.exec()