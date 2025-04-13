from PySide6.QtCore import QPoint,Qt

class FramelessWindow:
    def __init__(self):
        self._drag_position = QPoint()
        self.setWindowFlags(Qt.FramelessWindowHint)
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