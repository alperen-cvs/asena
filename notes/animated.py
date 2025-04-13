from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFrame
from PySide6.QtCore import QPropertyAnimation, Property, QObject
from PySide6.QtGui import QPainter, QPen, QColor


class AnimatedFrame(QFrame):
    def __init__(self):
        super().__init__()
        self._border_color = QColor("black")
    def getBorderColor(self):
        return self._border_color

    def setBorderColor(self, color):
        self._border_color = color
        self.update()  # repaint frame

    borderColor = Property(QColor, getBorderColor, setBorderColor)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pen = QPen(self._border_color, 4)
        painter.setPen(pen)
        painter.drawRect(self.rect().adjusted(2, 2, -2, -2))  # hafif içeriden çiz


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Border Renk Animasyonu")
        layout = QVBoxLayout(self)

        self.frame = AnimatedFrame()
        layout.addWidget(self.frame)

        button = QPushButton("Kırmızıya Geçiş Yap")
        layout.addWidget(button)
        button.clicked.connect(self.animateBorder)

    def animateBorder(self):
        self.anim = QPropertyAnimation(self.frame, b"borderColor")
        self.anim.setDuration(2000)
        self.anim.setStartValue(QColor("black"))
        self.anim.setEndValue(QColor("#625fb8"))
        self.anim.start()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()