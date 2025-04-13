# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setup.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import assets_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(593, 500)
        Form.setMinimumSize(QSize(593, 500))
        Form.setMaximumSize(QSize(593, 500))
        Form.setStyleSheet(u"QWidget {\n"
"	background-color: \"#1c1c30\";\n"
"}\n"
"\n"
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
"\n"
"QLineEdit { \n"
"    background-color: #625fb8;\n"
"	font: 700 11pt \"Arial\";\n"
"    color: \"black\";\n"
"    border-radius: 10px;\n"
"    padding: 10;\n"
"\n"
"    border: 3px solid  #625fb8;\n"
"}\n"
"\n"
"\n"
"QTextEdit {\n"
"	font: 700 9pt \"Arial\";\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_widget = QWidget(Form)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout = QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.main_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.app_text = QLabel(self.frame_6)
        self.app_text.setObjectName(u"app_text")
        self.app_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.app_text)

        self.icon_label = QLabel(self.frame_6)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setPixmap(QPixmap(u":/resources/rose32px.png"))

        self.horizontalLayout_3.addWidget(self.icon_label)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.main_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.path_line_edit = QLineEdit(self.frame_4)
        self.path_line_edit.setObjectName(u"path_line_edit")
        self.path_line_edit.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.path_line_edit)

        self.file_dialog_btn = QPushButton(self.frame_4)
        self.file_dialog_btn.setObjectName(u"file_dialog_btn")
        self.file_dialog_btn.setMinimumSize(QSize(45, 45))
        icon = QIcon()
        icon.addFile(u":/resources/folder32px.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.file_dialog_btn.setIcon(icon)
        self.file_dialog_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.file_dialog_btn)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.persistance_btn = QCheckBox(self.frame_5)
        self.persistance_btn.setObjectName(u"persistance_btn")

        self.horizontalLayout_4.addWidget(self.persistance_btn)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.status_line = QTextEdit(self.main_widget)
        self.status_line.setObjectName(u"status_line")
        self.status_line.setMaximumSize(QSize(16777215, 0))
        self.status_line.setFrameShape(QFrame.Shape.NoFrame)
        self.status_line.setReadOnly(True)
        self.status_line.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout.addWidget(self.status_line)

        self.frame_3 = QFrame(self.main_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_btn = QPushButton(self.frame_3)
        self.exit_btn.setObjectName(u"exit_btn")

        self.horizontalLayout_2.addWidget(self.exit_btn)

        self.setup_btn = QPushButton(self.frame_3)
        self.setup_btn.setObjectName(u"setup_btn")

        self.horizontalLayout_2.addWidget(self.setup_btn)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.main_widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.app_text.setText(QCoreApplication.translate("Form", u"Asena", None))
        self.icon_label.setText("")
        self.path_line_edit.setPlaceholderText(QCoreApplication.translate("Form", u"L\u00fctfen Bir patika se\u00e7iniz", None))
        self.file_dialog_btn.setText("")
        self.persistance_btn.setText(QCoreApplication.translate("Form", u"Her sistem a\u00e7\u0131l\u0131\u015f\u0131nda otomatik ba\u015flatma", None))
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u00c7\u0131k", None))
        self.setup_btn.setText(QCoreApplication.translate("Form", u"Kur", None))
    # retranslateUi

