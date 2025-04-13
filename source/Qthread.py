from idlelib.editor import darwin
from typing import override

from PySide6.QtCore import QRunnable
from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import QThreadPool
from types import FunctionType
from containers import SignalContainer
from dataclasses import dataclass
from source.exceptions import BadSignalClass
from utils.log_utils import create_new_logger_instance
from .typing import Module

logger = create_new_logger_instance()

def create_new_thread_instance() -> QThreadPool:
    return QThreadPool.globalInstance()

class Signals:
    class SetupSignal(QObject):
        progress = Signal(object)

class QThreadWorker(QRunnable):
    def __init__(self,runnable: Module):
        super(QThreadWorker,self).__init__()
        self.runnable = runnable
        self.__toggle = False
        self.thread = create_new_thread_instance()
    @override
    def run(self): # QThreadPool calls this function
        if isinstance(self.runnable,Module) and self.__toggle:
           self.runnable.exec()
        else:
            logger.error("You cannot run this function directly !")
    def start(self):
        self.__toggle = True
        self.thread.start(self)
