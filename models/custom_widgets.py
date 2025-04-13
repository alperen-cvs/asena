import os.path

from PySide6.QtWidgets import (QHBoxLayout)
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QVBoxLayout,QSizePolicy

from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal
from PySide6.QtCore import QObject
class QClickAbleFrame(QFrame,QObject):
    mouse_long_press = Signal(bool)
    def __init__(self,*args,parent = None):
        super(QClickAbleFrame,self).__init__(*args,parent=parent)
        self.default_bg_color = 'gray'
        self.hover_bg_color = 'white'
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timer_slot)
        self.setStyleSheet("border: 1px solid #625fb8;\nborder-radius: 10px;")
    def set_bg_color(self,color: str):
        self.setStyleSheet(f"")
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
    def mouseDoubleClickEvent(self, event, /):
        print("Double clicked !")
    def timer_slot(self):
        self.mouse_long_press.emit(True)


class QCardWidget(QClickAbleFrame):
    def __init__(self,customer_name = "Example Customer Name",label_text = "This is a label text",image = None,parent = None):
        super(QCardWidget,self).__init__(parent=parent)
        self.vertical_layout = QVBoxLayout(self)
        self.count = 0
        self.text_label = QLabel(label_text)
        self.customer_label = QLabel(customer_name,alignment=Qt.AlignmentFlag.AlignCenter)
        self.customer_label.setStyleSheet("border: none;\ncolor: #625fb8;\nfont: 700 18pt \"Arial\";\nborder: none;")
        self.customer_label.setWordWrap(True)
        self.vertical_layout.addWidget(self.customer_label)
        self.text_label.setWordWrap(True)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setStyleSheet("border: none;")
        self.vertical_layout.addWidget(self.text_label)
        if not image is None and isinstance(image,str):
            self.image_label = QLabel()
            self.image_label.setFixedSize(QSize(16,16))
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.pixmap = QPixmap(image)
            if self.pixmap.width() > 400 and self.pixmap.height() > 400:
                raise ValueError("Image size overflow pictures must be maximum 400x400")
            self.image_label.setPixmap(self.pixmap.scaled(QSize(self.image_label.width(),self.image_label.height()),Qt.AspectRatioMode.KeepAspectRatio))
            self.vertical_layout.addWidget(self.image_label,alignment=Qt.AlignmentFlag.AlignCenter)


class QCounterLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.setStyleSheet("color: #625fb8;\nfont: 700 18pt \"Arial\";\nborder: none;")
        self.timer = QTimer()
        self.timer.timeout.connect(self.settext)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer.start(1000)
    def settext(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        elif self.minute == 60:
            self.minute = 0
            self.hour+=1
        self.setText("Geçen Süre: %s:%s:%s" % (self.hour,self.minute,self.second))

