from PySide6.QtCore import QRect, QAbstractAnimation
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtCore import QEasingCurve
from PySide6.QtCore import Signal
from containers import WinPosition
class TableInfo(QWidget):
    close = Signal(bool)
    def __init__(self,parent = None,items = (),winpos = None):
        super(TableInfo,self).__init__(parent = parent)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setContentsMargins(0,0,0,0)
        self.setStyleSheet("background-color: '#1c1c30';\nborder: 1px solid gray;\nborder-radius: 10px;")
        for item in items:
            label = QLabel(item,alignment = Qt.AlignmentFlag.AlignCenter)
            self.vertical_layout.addWidget(label)
        self.setLayout(self.vertical_layout)
        self.start_anim = QPropertyAnimation(self,b"geometry")
        self.start_anim.setDuration(300)
        self.start_anim.setStartValue(QRect(winpos.x,winpos.y,winpos.width,0))
        self.start_anim.setEndValue(QRect(winpos.x,winpos.y,winpos.width,winpos.height))

        self.close_anim = QPropertyAnimation(self,b"geometry")
        self.close_anim.setDuration(300)
        self.close_anim.setStartValue(QRect(winpos.x, winpos.y, winpos.width, winpos.height))
        self.close_anim.setEndValue(QRect(winpos.x, winpos.y, winpos.width,0))
    def closeEvent(self,event,/):
        """
        The close signal will be triggered when the window is closed.
        :param event:
        :return:
        """
        self.close_anim.start(QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)
        self.close.emit(True)
    def showEvent(self, event, /):
        self.start_anim.start(QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)