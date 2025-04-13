from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt, QTimer
import sys


class LongPressLabel(QLabel):
    def __init__(self):
        super().__init__("Bana Uzun Bas")
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("font-size: 24px;")

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.on_long_press)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Mouse basıldı.")
            self.timer.start(500)  # 500ms içinde bırakmazsa uzun basma

    def mouseReleaseEvent(self, event):
        if self.timer.isActive():
            print("Kısa basıldı (zaman dolmadan bırakıldı).")
            self.timer.stop()
        else:
            print("Uzun basma zaten tetiklenmişti.")

    def on_long_press(self):
        print("⬆️ Uzun basma algılandı!")
        self.setText("Uzun basıldı!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LongPressLabel()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())