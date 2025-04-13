import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt,QPoint
from models.login_model import Ui_Form
from models.frameless_window import FramelessWindow
from apps.asena import AsenaMainWindow

class Login(QWidget,Ui_Form,FramelessWindow):
    def __init__(self,parent):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("ASENA - LOGIN")
        self.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.credentials = ["admin","alperen1"]
        self._drag_position = QPoint()
        self.counter = 4
        self.parent = parent
        self.login_btn.clicked.connect(self.check_credentials)
        self.minimize_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)

    def mousePressEvent(self, event):
        # Fare tıklama ile pencereyi hareket ettirmek için başlat
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        # Fare hareket ettiğinde pencereyi taşı
        if event.buttons() & Qt.LeftButton:
            delta = QPoint(event.globalPosition().toPoint() - self._drag_position)
            self.move(self.pos() + delta)
            self._drag_position = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        # Fareyi serbest bırakınca hareketi durdur
        self._drag_position = QPoint()

    def check_credentials(self):
        if len(self.username.text()) < 5:
            self.status_label.setText("Kullanıcı adı 5 karaktere eşit olmalı veya daha uzun olmalıdır !")
        elif len(self.passwd.text()) < 8:
            self.status_label.setText("Şifre 8 karaktere eşit olmalı veya daha uzun olmalıdır !")
        else:
            if self.username.text() != self.credentials[0] or self.passwd.text() != self.credentials[1]:
                self.counter -= 1
                self.status_label.setText("Yanlış giriş bilgileri kalan hak: %s" % (str(self.counter)))
            else:
                self.status_label.setText("Giriş başarılı hoşgeldiniz: %s" % (self.credentials[0]))
                self.parent.show()
                self.close()
        if self.counter == 0:
            print(self.counter)
            self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = AsenaMainWindow()
    window = Login(parent = main_window)
    window.show()
    app.exec()
