import sys,os

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap
from PyQt6.QtGui import QIcon, QImage
from PySide6.QtCore import QUrl
from PySide6.QtCore import QTimer,Signal
from PySide6.QtWidgets import QHBoxLayout,QVBoxLayout,QLabel
from PySide6.QtWidgets import QFrame,QWidget,QMainWindow
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class ClickableFrame(QFrame):
    def __init__(self,text = "Hello"):
        super().__init__()
        self.count = 0
    def mousePressEvent(self, event):
        if event.button() & Qt.MouseButton.LeftButton:
            ftimer = QTimer()
            ftimer.timeout.connect(self.show_msgbox)
            ftimer.start(30)
            print("Sol click tıklandı !")
    def enterEvent(self, event, /):
        self.setStyleSheet("background-color: 'blue';\nborder-radius: 5px;")
    def leaveEvent(self, event, /):
        self.setStyleSheet("background-color: 'red';\nborder-radius: 5px;")
    def show_msgbox(self,index):
        qms = QMessageBox()
        qms.setText(index)
        qms.exec()
class CardWidget(QWidget):
    def __init__(self,label = "Hello",image = None):
        super().__init__()
        self.v_layout = QVBoxLayout(self)
        self.v_layout.setContentsMargins(5,0,5,0)
        if image is not None:
            self.image_label = QLabel()
            self.image_label.setFixedSize(QSize(32,32))
            self.pixmap = QPixmap("resim.png")
            print(self.pixmap.width(),self.pixmap.height())
            self.image_label.setPixmap(self.pixmap.scaled(self.image_label.width(),self.image_label.height(),Qt.AspectRatioMode.KeepAspectRatio))
            self.v_layout.addWidget(self.image_label)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.frame = QFrame(self)
        self.setContentsMargins(10,10,10,10)
        self.hlayout = QVBoxLayout(self.frame)
        self.t = QTimer()

        self.t.start(1000)
        self.setMinimumSize(QSize(500,500))
        for _ in range(5):
            self.clicable_frame = ClickableFrame()
            self.clicable_frame.setStyleSheet("background-color: 'red';\nborder-radius: 5px;")
            self.v_lf = QVBoxLayout(self.clicable_frame)
            self.f = CardWidget(image="resim.png")
            self.v_lf.addWidget(self.f)
            self.hlayout.addWidget(self.clicable_frame)
        self.setCentralWidget(self.frame)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()