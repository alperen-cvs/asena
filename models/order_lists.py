import os
import sys

from PyQt5.QtWidgets import QVBoxLayout, QFrame

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from widgets import AnimatedWindow
from PySide6.QtWidgets import QTableWidget,QApplication,QVBoxLayout,QHeaderView,QSizePolicy,QTableWidgetItem
from PySide6.QtCore import QRect,Qt
from utils.win32 import find_window_cordinates

class OrderTable(AnimatedWindow):
    def __init__(self):
        super().__init__()
        self.static_close = False
        self.vertical_layout = QVBoxLayout(self)
        self.data = list(range(70))
        self.table_widget = QTableWidget(len(self.data),2)
        self.vertical_layout.setContentsMargins(0,0,0,0)
        self.table_widget.setSelectionMode(QTableWidget.SelectionMode.NoSelection)
        self.table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_widget.setHorizontalHeaderLabels(["URUN ADI","MÜŞTERİ ADI"])
        self.table_widget.setStyleSheet("""
        
        
        QAbstractItemView {
            border: none;
            margin: 2px; 
        }
        
        QTableWidget {
            background-color: #1c1c30;
            border-radius: 15px;
            padding: 2px;
            border: 1px;
        }""")
        self.table_widget.horizontalHeader().setStyleSheet("""QHeaderView {\nbackground: transparent;\n}\nQHeaderView::section {
            background-color: cyan;
            font: 700 11pt Arial;
            color: white;
            border: none;
            border-radius: 15px;
            }""")

        self.table_widget.verticalHeader().setDefaultSectionSize(45)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) # We added this mode to prevent qtablewidget cells from overflowing
        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        """
        NOTE:if we want to set the width of the cells
        we should use the setDefaultSectionSize function
        
        we should make the size policy fixed
        """
        self.table_widget.horizontalHeader().setFixedHeight(45)
        self.table_widget.verticalHeader().hide()
        self.vertical_layout.addWidget(self.table_widget)
        for i in self.data[:]:
            self.table_widget.setItem(0,i,QTableWidgetItem(str(i)))
        self.setFixedSize(600,600)


app = QApplication()
window = OrderTable()
window.show()
app.exec()