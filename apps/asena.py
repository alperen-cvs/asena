import os
import random
import sys

from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QGridLayout
from PySide6.QtWidgets import QScrollArea
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QHeaderView,QTabWidget
from PySide6.QtWidgets import QStackedWidget,QWidget
from PySide6.QtWidgets import QTableWidget
from PySide6.QtWidgets import QFrame
from PySide6.QtWidgets import QGraphicsBlurEffect
from PySide6.QtWidgets import QStackedWidget
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtCore import QRect
from PySide6.QtCore import QFile
from PySide6.QtCore import Qt,QEasingCurve
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPropertyAnimation


path = os.path.join(
    os.path.dirname(__file__),
    ".."
)
sys.path.append(path)

from enums.frame_constants import calculate_animated_order_window_position

from utils.win32 import find_window_cordinates
from utils.win32 import enum_windows
from utils.log_utils import create_new_logger_instance

from models.main_window import Ui_MainWindow

from widgets import QCardWidget
from widgets import AnimatedWindow

from containers import WinPosition

logger = create_new_logger_instance()


class AsenaMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__() # initialize all class
        self.setupUi(self)
        self.setWindowTitle("ASENA")
        self.main_container.setStyleSheet("border-radius: 10px;")
        self.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        self.set_all_signals()
        #self.setWindowFlags(Qt.FramelessWindowHint)


        self.inside_container_animation_handler = self.create_animation_object(self.inside_container)
        self.slide_sidebar_animation_handler = self.create_animation_object(self.slide_sidebar)
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurHints(QGraphicsBlurEffect.BlurHint.PerformanceHint)
        self.blur_effect_toggle = True

        self.stretch_all_table_widgets()
        self.orders_history_btn.setCheckable(False)
        self.append_tables_to_scrollbar_area()
    def handle_sidebar(self):
        sidebar_width = 153
        collapsed_width = 0
        # <>
        main_width = self.width()
        print(self.slide_sidebar.width())
        if self.slide_sidebar.width() == 0:
            # sidebar is opening

            self.slide_sidebar_animation_handler.setStartValue(QRect(61, 1, collapsed_width, self.height()))
            self.slide_sidebar_animation_handler.setEndValue(QRect(61, 1, sidebar_width, self.height()))

            self.inside_container_animation_handler.setStartValue(
                QRect(61, 1, self.inside_container.width(), self.height()))
            self.inside_container_animation_handler.setEndValue(
                QRect(61 + sidebar_width, 1, main_width - (61 + sidebar_width), self.height()))
        else:

            # sidebar is closing
            self.slide_sidebar_animation_handler.setStartValue(QRect(61, 1, sidebar_width, self.height()))
            self.slide_sidebar_animation_handler.setEndValue(QRect(61, 1, collapsed_width, self.height()))

            self.inside_container_animation_handler.setStartValue(
                QRect(61 + sidebar_width, 1, self.inside_container.width(), self.height()))
            self.inside_container_animation_handler.setEndValue(QRect(61, 1, main_width - 61, self.height()))

        self.slide_sidebar_animation_handler.start()
        self.inside_container_animation_handler.start()
    def create_animation_object(self,input_frame: QFrame,duration = 300,animation_type = b"geometry") -> QPropertyAnimation:
        qproperty_animation_object = QPropertyAnimation(
            input_frame,
            animation_type
        )
        qproperty_animation_object.setDuration(duration)
        return qproperty_animation_object
    def set_all_signals(self):
       self.active_orders_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
       self.orders_history_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
       self.orders_screen_btn.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
       self.endorsement_btn.clicked.connect(lambda *_:None)
       self.sidebar_toggle_btn.clicked.connect(self.handle_sidebar)
    def stretch_all_table_widgets(self):
        #NOTE -> FindChildren returns many objects
        #NOTE -> FindChild return just one objects
        table_widgets = self.stackedWidget.findChildren(QTableWidget)
        for table_widget in table_widgets:

            table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def disable_all_push_buttons(self):
        for member in dir(self):
            if isinstance(getattr(self,member),QPushButton):
                pass
    def enable_all_push_buttons(self):
        for member in dir(self):
            if isinstance(member,QPushButton):
                print(member)
    def append_tables_to_scrollbar_area(self):
        base_frame_widget = QFrame()
        grid_layout_of_base_frame_widget = QGridLayout(base_frame_widget)

        scrollbar = self.stackedWidget.findChild(QStackedWidget)
        scrollbar = scrollbar.findChild(QScrollArea)
        print(scrollbar)
        count = 8
        example_customers = [
            "Ahmet yeşil",
            "Ahmet yeşil",
            "Ahmet yeşil","Ahmet yeşil",
            "Ahmet yeşil","Ahmet yeşil",
            "Ahmet yeşil","Ahmet yeşil",
            "Ahmet Yeşil"


        ]
        for i,customers in enumerate(example_customers):
            row = i // 3
            col = i % 3
            card_widget = QCardWidget(title=customers,text="Masa: %s" % (str(i)))
            fx = random.randint(1000,20_000)
            card_widget.timer.end_value = fx
            if count > 10:
                card_widget.setFixedHeight(150)
            card_widget.signal.mouse_long_press.connect(self.launch_card_table_info_window)
            grid_layout_of_base_frame_widget.addWidget(card_widget,row,col)
        scrollbar.setWidget(base_frame_widget)
    def launch_card_table_info_window(self):

        self.create_blur_window_effect()
        self.disable_all_push_buttons()
        winpos = find_window_cordinates("ASENA")
        self.animated_window = AnimatedWindow(geometry = calculate_animated_order_window_position(winpos))
        vly = QVBoxLayout(self.animated_window)
        pbp = QPushButton("Click me")
        pbp.clicked.connect(self.animated_window.close)
        vly.addWidget(pbp)
        self.animated_window.signal.closed.connect(self.create_blur_window_effect)
        self.animated_window.show()
    def create_blur_window_effect(self):
        if self.blur_effect_toggle:
            self.blur_effect.setBlurRadius(3)
            self.setGraphicsEffect(self.blur_effect)
        else:
            self.blur_effect.setBlurRadius(0)
            self.setGraphicsEffect(self.blur_effect)
        self.blur_effect_toggle = not self.blur_effect_toggle

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if "ASENA" in enum_windows():
        logger.info("App already running !")
        msgbox = QMessageBox()
        msgbox.setWindowIcon(QIcon(u":/resources/asena_main.ico"))
        msgbox.setWindowTitle("-*- HATA -*-")
        msgbox.setText("Çalışan bir asena uygulaması var !!! ")
        msgbox.exec()
        sys.exit(1)
    window = AsenaMainWindow()
    window.show()
    app.exec()