"""
This table widget is no different from the original, it was created to avoid being configured over and over again.
"""
import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QHeaderView
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt
from animated_window import AnimatedWindow
from containers import CustomerContainer,OrderItemContainer
example_customer_container = CustomerContainer(
    name="Alperen",
    surname = "Çavuş",
    orders = [
        OrderItemContainer(
            item_name = "Supangle",
            item = "path/to"
        ),
        OrderItemContainer(
            item_name = "Supangle",
            item = "path/to/ex"
        ),
        OrderItemContainer(
            item_name = "Supangle",
            item = "path/to/ex"
        )
    ]
)
class OrderList(AnimatedWindow):
    def __init__(self,customer_container: CustomerContainer,parent = None):
        super(OrderList,self).__init__(parent=parent)
        self.customer_container = customer_container
        self.customer_container_item_size = len(customer_container.orders)
        self.vertical_layout = QVBoxLayout(self)
        self.table_widget = QTableWidget(self.customer_container_item_size,4)
        self.table_widget.setHorizontalHeaderLabels(["URUN ADI","SIPARİŞ TARİHİ","MUŞTERI İSMİ","ADET"])
        self.table_widget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.verticalHeader().setDefaultSectionSize(45) # vertical header cell size
        self.vertical_layout.addWidget(self.table_widget)
        self.set_all_items()
    def set_all_items(self):
        for index,items in enumerate(self.customer_container.orders):
            self.table_widget.setItem(index,0,self.create_aligned_text(items.item_name))
            self.table_widget.setItem(index,1,self.create_aligned_text(self.customer_container.name))
    def create_aligned_text(self,text: str) -> QTableWidgetItem:
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        return item
app = QApplication([])
window = OrderList(example_customer_container)
window.static_close = False
window.show()
app.exec()

