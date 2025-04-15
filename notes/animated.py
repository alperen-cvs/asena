from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QMessageBox
from PySide6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget Örneği")
        self.resize(300, 250)

        # Ana layout
        layout = QVBoxLayout(self)

        # QListWidget oluştur
        self.list_widget = QListWidget()

        # Öğe ekle
        self.list_widget.addItems([
            "Elma",
            "Armut",
            "Muz",
            "Karpuz",
            "Çilek"
        ])

        # Seçildiğinde uyarı göster
        self.list_widget.itemClicked.connect(self.on_item_clicked)

        # Stil ekleyelim
        self.list_widget.setStyleSheet("""
            QListWidget {
                background-color: #f0f0f0;
                border: 1px solid #aaa;
                border-radius: 10px;
                padding: 5px;
            }

            QListWidget::item {
                padding: 10px;
                border-radius: 5px;
            }

            QListWidget::item:selected {
                background-color: #3498db;
                color: white;
            }

            QListWidget::item:hover {
                background-color: #d0e6f8;
            }
        """)

        # Listeyi layout'a ekle
        layout.addWidget(self.list_widget)

    def on_item_clicked(self, item):
        QMessageBox.information(self, "Seçilen", f"Seçtiğin meyve: {item.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
