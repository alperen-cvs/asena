from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QTimer

from source.signal import ClickAbleFrameSignal

class QClickAbleFrame(QFrame):

    def __init__(self,*args,parent = None):
        super(QClickAbleFrame,self).__init__(*args,parent=parent)
        self.setStyleSheet("border: 1px solid #625fb8;")
        self.signal = ClickAbleFrameSignal()
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timer_slot)
    def set_hover_color(self,color: str):
        self.hover_bg_color = color
    """
    def enterEvent(self, event):
        self.set_bg_color(self.hover_bg_color)
    def leaveEvent(self, event):
        self.set_bg_color(self.default_bg_color)
    """
    """
    NOT:Enter ve Leave event hover efekti için eklendi
    """
    def mousePressEvent(self, event):
        if event.button() & Qt.MouseButton.LeftButton:
            self.timer.start(500)
    def mouseReleaseEvent(self, event):
        if self.timer.isActive():
            self.timer.stop()
    def timer_slot(self):

        self.signal.mouse_long_press.emit(True)
    def autoBlur(self) -> bool:
        pass