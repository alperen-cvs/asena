# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1132, 529)
        MainWindow.setStyleSheet(u"QFrame {\n"
"	background-color: \"#1c1c30\";\n"
"}\n"
"QFrame#main_container {\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel {\n"
"	font: 700 18pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton {	\n"
"	background-color: #625fb8;\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	font: 700 11pt \"Arial\";\n"
"	height: 38px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #8784e0;\n"
"}\n"
"QTableWidget {\n"
"	background-color: none;\n"
"	border-radius: 3px;\n"
"}	\n"
"\n"
"QTableCornerButton::section {\n"
"	background-color: 'transparent';\n"
"},\n"
"\n"
"QStackedWidget {\n"
"	border: 1px solid gray;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	background-color: \"yellow\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(859, 529))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_container.sizePolicy().hasHeightForWidth())
        self.main_container.setSizePolicy(sizePolicy)
        self.main_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.minisidebar = QFrame(self.main_container)
        self.minisidebar.setObjectName(u"minisidebar")
        self.minisidebar.setMaximumSize(QSize(60, 16777215))
        self.minisidebar.setStyleSheet(u"")
        self.minisidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.minisidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.minisidebar)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 0)
        self.minisidebar_active_orders_btn = QPushButton(self.minisidebar)
        self.minisidebar_active_orders_btn.setObjectName(u"minisidebar_active_orders_btn")
        icon = QIcon()
        icon.addFile(u":/resources/already_waiting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_active_orders_btn.setIcon(icon)
        self.minisidebar_active_orders_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_active_orders_btn)

        self.minisidebar_orders_history_btn = QPushButton(self.minisidebar)
        self.minisidebar_orders_history_btn.setObjectName(u"minisidebar_orders_history_btn")
        icon1 = QIcon()
        icon1.addFile(u":/resources/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_orders_history_btn.setIcon(icon1)
        self.minisidebar_orders_history_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_orders_history_btn)

        self.minisidebar_orders_screen_btn = QPushButton(self.minisidebar)
        self.minisidebar_orders_screen_btn.setObjectName(u"minisidebar_orders_screen_btn")
        icon2 = QIcon()
        icon2.addFile(u":/resources/orders.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_orders_screen_btn.setIcon(icon2)
        self.minisidebar_orders_screen_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_orders_screen_btn)

        self.minisidebar_table_management_btn = QPushButton(self.minisidebar)
        self.minisidebar_table_management_btn.setObjectName(u"minisidebar_table_management_btn")
        icon3 = QIcon()
        icon3.addFile(u":/resources/table32px.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_table_management_btn.setIcon(icon3)
        self.minisidebar_table_management_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_table_management_btn)

        self.minisidenar_endorsement_btn = QPushButton(self.minisidebar)
        self.minisidenar_endorsement_btn.setObjectName(u"minisidenar_endorsement_btn")
        icon4 = QIcon()
        icon4.addFile(u":/resources/endorsement_btn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidenar_endorsement_btn.setIcon(icon4)
        self.minisidenar_endorsement_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidenar_endorsement_btn)

        self.minisidebar_stock_management_btn = QPushButton(self.minisidebar)
        self.minisidebar_stock_management_btn.setObjectName(u"minisidebar_stock_management_btn")
        icon5 = QIcon()
        icon5.addFile(u":/resources/database_btn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_stock_management_btn.setIcon(icon5)
        self.minisidebar_stock_management_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_stock_management_btn)

        self.minisidebar_settings_btn = QPushButton(self.minisidebar)
        self.minisidebar_settings_btn.setObjectName(u"minisidebar_settings_btn")
        icon6 = QIcon()
        icon6.addFile(u":/resources/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_settings_btn.setIcon(icon6)
        self.minisidebar_settings_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_settings_btn)

        self.minisidebar_exit_btn = QPushButton(self.minisidebar)
        self.minisidebar_exit_btn.setObjectName(u"minisidebar_exit_btn")
        icon7 = QIcon()
        icon7.addFile(u":/resources/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minisidebar_exit_btn.setIcon(icon7)
        self.minisidebar_exit_btn.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.minisidebar_exit_btn)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.minisidebar)

        self.slide_sidebar = QFrame(self.main_container)
        self.slide_sidebar.setObjectName(u"slide_sidebar")
        self.slide_sidebar.setMaximumSize(QSize(153, 16777215))
        self.slide_sidebar.setStyleSheet(u"")
        self.slide_sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.slide_sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slide_sidebar)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, -1, 0)
        self.active_orders_btn = QPushButton(self.slide_sidebar)
        self.active_orders_btn.setObjectName(u"active_orders_btn")

        self.verticalLayout_2.addWidget(self.active_orders_btn)

        self.orders_history_btn = QPushButton(self.slide_sidebar)
        self.orders_history_btn.setObjectName(u"orders_history_btn")

        self.verticalLayout_2.addWidget(self.orders_history_btn)

        self.orders_screen_btn = QPushButton(self.slide_sidebar)
        self.orders_screen_btn.setObjectName(u"orders_screen_btn")

        self.verticalLayout_2.addWidget(self.orders_screen_btn)

        self.table_management_btn = QPushButton(self.slide_sidebar)
        self.table_management_btn.setObjectName(u"table_management_btn")

        self.verticalLayout_2.addWidget(self.table_management_btn)

        self.endorsement_btn = QPushButton(self.slide_sidebar)
        self.endorsement_btn.setObjectName(u"endorsement_btn")
        self.endorsement_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.endorsement_btn)

        self.stock_management_btn = QPushButton(self.slide_sidebar)
        self.stock_management_btn.setObjectName(u"stock_management_btn")

        self.verticalLayout_2.addWidget(self.stock_management_btn)

        self.settings_btn = QPushButton(self.slide_sidebar)
        self.settings_btn.setObjectName(u"settings_btn")

        self.verticalLayout_2.addWidget(self.settings_btn)

        self.exit_btn = QPushButton(self.slide_sidebar)
        self.exit_btn.setObjectName(u"exit_btn")

        self.verticalLayout_2.addWidget(self.exit_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 193, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.slide_sidebar)

        self.inside_container = QFrame(self.main_container)
        self.inside_container.setObjectName(u"inside_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inside_container.sizePolicy().hasHeightForWidth())
        self.inside_container.setSizePolicy(sizePolicy1)
        self.inside_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.inside_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.inside_container)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.inside_container)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 50))
        self.header_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, 0, 0)
        self.sidebar_toggle_btn_frame = QFrame(self.header_frame)
        self.sidebar_toggle_btn_frame.setObjectName(u"sidebar_toggle_btn_frame")
        self.sidebar_toggle_btn_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebar_toggle_btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.sidebar_toggle_btn_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 3, 0, 0)
        self.sidebar_toggle_btn = QPushButton(self.sidebar_toggle_btn_frame)
        self.sidebar_toggle_btn.setObjectName(u"sidebar_toggle_btn")
        icon8 = QIcon()
        icon8.addFile(u":/resources/sidebar_toggle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sidebar_toggle_btn.setIcon(icon8)
        self.sidebar_toggle_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.sidebar_toggle_btn, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_3.addWidget(self.sidebar_toggle_btn_frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.main_label_frame = QFrame(self.header_frame)
        self.main_label_frame.setObjectName(u"main_label_frame")
        self.main_label_frame.setMaximumSize(QSize(196, 44))
        self.main_label_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_label_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_label_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 3, -1, -1)
        self.app_name_label = QLabel(self.main_label_frame)
        self.app_name_label.setObjectName(u"app_name_label")

        self.horizontalLayout_5.addWidget(self.app_name_label)

        self.app_icon_label = QLabel(self.main_label_frame)
        self.app_icon_label.setObjectName(u"app_icon_label")
        self.app_icon_label.setPixmap(QPixmap(u":/resources/asena_main.ico"))

        self.horizontalLayout_5.addWidget(self.app_icon_label)


        self.horizontalLayout_3.addWidget(self.main_label_frame, 0, Qt.AlignmentFlag.AlignTop)

        self.corner_button_frame = QFrame(self.header_frame)
        self.corner_button_frame.setObjectName(u"corner_button_frame")
        self.corner_button_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.corner_button_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.corner_button_frame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 3, 6, 0)

        self.horizontalLayout_3.addWidget(self.corner_button_frame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.stacked_pages = QStackedWidget(self.inside_container)
        self.stacked_pages.setObjectName(u"stacked_pages")
        self.active_orders = QWidget()
        self.active_orders.setObjectName(u"active_orders")
        self.horizontalLayout_7 = QHBoxLayout(self.active_orders)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.scrollbar_of_active_order_page_area = QScrollArea(self.active_orders)
        self.scrollbar_of_active_order_page_area.setObjectName(u"scrollbar_of_active_order_page_area")
        self.scrollbar_of_active_order_page_area.setWidgetResizable(True)
        self.active_order_page_area = QWidget()
        self.active_order_page_area.setObjectName(u"active_order_page_area")
        self.active_order_page_area.setGeometry(QRect(0, 0, 905, 442))
        self.scrollbar_of_active_order_page_area.setWidget(self.active_order_page_area)

        self.horizontalLayout_7.addWidget(self.scrollbar_of_active_order_page_area)

        self.stacked_pages.addWidget(self.active_orders)
        self.orders_history_page = QWidget()
        self.orders_history_page.setObjectName(u"orders_history_page")
        self.hboxLayout = QHBoxLayout(self.orders_history_page)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.orders_history_table = QTableWidget(self.orders_history_page)
        self.orders_history_table.setObjectName(u"orders_history_table")

        self.hboxLayout.addWidget(self.orders_history_table)

        self.stacked_pages.addWidget(self.orders_history_page)
        self.order_page = QWidget()
        self.order_page.setObjectName(u"order_page")
        self.scrollbar_of_order_page_area = QScrollArea(self.order_page)
        self.scrollbar_of_order_page_area.setObjectName(u"scrollbar_of_order_page_area")
        self.scrollbar_of_order_page_area.setGeometry(QRect(380, 170, 120, 80))
        self.scrollbar_of_order_page_area.setWidgetResizable(True)
        self.order_page_area = QWidget()
        self.order_page_area.setObjectName(u"order_page_area")
        self.order_page_area.setGeometry(QRect(0, 0, 118, 78))
        self.scrollbar_of_order_page_area.setWidget(self.order_page_area)
        self.stacked_pages.addWidget(self.order_page)
        self.table_management_page = QWidget()
        self.table_management_page.setObjectName(u"table_management_page")
        self.verticalLayout_6 = QVBoxLayout(self.table_management_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.table_management_table = QTableWidget(self.table_management_page)
        self.table_management_table.setObjectName(u"table_management_table")

        self.verticalLayout_6.addWidget(self.table_management_table)

        self.stacked_pages.addWidget(self.table_management_page)
        self.turnover_page = QWidget()
        self.turnover_page.setObjectName(u"turnover_page")
        self.stacked_pages.addWidget(self.turnover_page)
        self.stock_management_page = QWidget()
        self.stock_management_page.setObjectName(u"stock_management_page")
        self.verticalLayout_5 = QVBoxLayout(self.stock_management_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stock_managament_table = QTableWidget(self.stock_management_page)
        self.stock_managament_table.setObjectName(u"stock_managament_table")

        self.verticalLayout_5.addWidget(self.stock_managament_table)

        self.stacked_pages.addWidget(self.stock_management_page)
        self.options_page = QWidget()
        self.options_page.setObjectName(u"options_page")
        self.verticalLayout_4 = QVBoxLayout(self.options_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stacked_widget_tab_btn = QFrame(self.options_page)
        self.stacked_widget_tab_btn.setObjectName(u"stacked_widget_tab_btn")
        self.stacked_widget_tab_btn.setMinimumSize(QSize(0, 50))
        self.stacked_widget_tab_btn.setStyleSheet(u"")
        self.stacked_widget_tab_btn.setFrameShape(QFrame.Shape.StyledPanel)
        self.stacked_widget_tab_btn.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.stacked_widget_tab_btn)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.settings_db_management_btn = QPushButton(self.stacked_widget_tab_btn)
        self.settings_db_management_btn.setObjectName(u"settings_db_management_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.settings_db_management_btn.sizePolicy().hasHeightForWidth())
        self.settings_db_management_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.settings_db_management_btn)

        self.reset_btn = QPushButton(self.stacked_widget_tab_btn)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout_9.addWidget(self.reset_btn)

        self.common_btn = QPushButton(self.stacked_widget_tab_btn)
        self.common_btn.setObjectName(u"common_btn")

        self.horizontalLayout_9.addWidget(self.common_btn)

        self.not_implented = QPushButton(self.stacked_widget_tab_btn)
        self.not_implented.setObjectName(u"not_implented")

        self.horizontalLayout_9.addWidget(self.not_implented)


        self.verticalLayout_4.addWidget(self.stacked_widget_tab_btn)

        self.options_tab = QStackedWidget(self.options_page)
        self.options_tab.setObjectName(u"options_tab")
        self.db_management_tab = QWidget()
        self.db_management_tab.setObjectName(u"db_management_tab")
        self.horizontalLayout_10 = QHBoxLayout(self.db_management_tab)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.options_tab.addWidget(self.db_management_tab)
        self.reset_tab = QWidget()
        self.reset_tab.setObjectName(u"reset_tab")
        self.options_tab.addWidget(self.reset_tab)

        self.verticalLayout_4.addWidget(self.options_tab)

        self.stacked_pages.addWidget(self.options_page)

        self.verticalLayout.addWidget(self.stacked_pages)


        self.horizontalLayout_2.addWidget(self.inside_container)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked_pages.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minisidebar_active_orders_btn.setText("")
        self.minisidebar_orders_history_btn.setText("")
        self.minisidebar_orders_screen_btn.setText("")
        self.minisidebar_table_management_btn.setText("")
        self.minisidenar_endorsement_btn.setText("")
        self.minisidebar_stock_management_btn.setText("")
        self.minisidebar_settings_btn.setText("")
        self.minisidebar_exit_btn.setText("")
        self.active_orders_btn.setText(QCoreApplication.translate("MainWindow", u"AKTIF SIPARI\u015eLER", None))
        self.orders_history_btn.setText(QCoreApplication.translate("MainWindow", u"SIPARI\u015e GE\u00c7MI\u015eI", None))
        self.orders_screen_btn.setText(QCoreApplication.translate("MainWindow", u"SIPARI\u015e EKRANI", None))
        self.table_management_btn.setText(QCoreApplication.translate("MainWindow", u"MASA TAKIBI", None))
        self.endorsement_btn.setText(QCoreApplication.translate("MainWindow", u"CIRO TAK\u0130B\u0130", None))
        self.stock_management_btn.setText(QCoreApplication.translate("MainWindow", u"STOK YONETIMI", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"AYARLAR", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"\u00c7IKI\u015e", None))
        self.sidebar_toggle_btn.setText("")
        self.app_name_label.setText(QCoreApplication.translate("MainWindow", u"ASENA", None))
        self.app_icon_label.setText("")
        self.settings_db_management_btn.setText(QCoreApplication.translate("MainWindow", u"Veritaban\u0131", None))
        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u"S\u0131f\u0131rlama", None))
        self.common_btn.setText(QCoreApplication.translate("MainWindow", u"Genel", None))
        self.not_implented.setText(QCoreApplication.translate("MainWindow", u"not_implented", None))
    # retranslateUi

