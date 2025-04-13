# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from assets import assets

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(504, 616)
        Form.setMinimumSize(QSize(504, 616))
        Form.setMaximumSize(QSize(504, 616))
        Form.setStyleSheet(u"QFrame#main_frame  {\n"
"		border-radius: 10px;\n"
"		background-color: \"#1c1c30\";\n"
"}\n"
"\n"
"QLineEdit { \n"
"    background-color: \"white\";\n"
"	font: 700 11pt \"Arial\";\n"
"    color: \"black\";\n"
"    border-radius: 10px;\n"
"    padding: 10;\n"
"    background-repeat: no-repeat;\n"
"    background-position: right;\n"
"    border: 3px solid  #625fb8;\n"
"\n"
"}\n"
"\n"
"QLineEdit#passwd {\n"
" 	background-image: url(:/resources/key32px.png);\n"
" }\n"
"\n"
"\n"
"QLineEdit#username {\n"
"	background-image: url(:/resources/user32px.png);\n"
"}\n"
"\n"
"QLabel#login_panel_main_text {\n"
"	font: 700 22pt \"Arial\";\n"
"}\n"
"\n"
"QLabel#status_label {\n"
"	font: 700 11pt \"Arial\";\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QLabel#main_label {\n"
"	font: 700 28pt \"Arial\";\n"
"}\n"
"QPushButton {\n"
"	background-color: #625fb8;\n"
"    border-radius: 10px;\n"
"	font: 700 11pt \"Arial\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #8784e0;\n"
"}\n"
"QLabel#footer_text {\n"
"		font: 700 "
                        "11pt \"Arial\";\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(Form)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, -1)
        self.footer = QFrame(self.main_frame)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.Shape.NoFrame)
        self.footer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.footer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 3, 3, -1)
        self.btn_frame = QFrame(self.footer)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setMinimumSize(QSize(30, 30))
        self.btn_frame.setMaximumSize(QSize(70, 40))
        self.btn_frame.setStyleSheet(u"\n"
"padding: 3px;")
        self.btn_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.btn_frame)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 7)
        self.minimize_btn = QPushButton(self.btn_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        icon = QIcon()
        icon.addFile(u":/resources/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.btn_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/resources/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.verticalLayout_6.addWidget(self.btn_frame, 0, Qt.AlignmentFlag.AlignRight)

        self.icon_frame = QFrame(self.footer)
        self.icon_frame.setObjectName(u"icon_frame")
        self.icon_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.icon_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.icon_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.icon_label = QLabel(self.icon_frame)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setPixmap(QPixmap(u":/resources/rose32px.png"))
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_8.addWidget(self.icon_label)


        self.verticalLayout_6.addWidget(self.icon_frame)

        self.main_label = QLabel(self.footer)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.main_label.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.main_label)


        self.verticalLayout.addWidget(self.footer)

        self.frame_3 = QFrame(self.main_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(300, 82))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, -1, -1)
        self.username = QLineEdit(self.frame)
        self.username.setObjectName(u"username")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy1)
        self.username.setMinimumSize(QSize(200, 50))
        self.username.setMaximumSize(QSize(300, 22))
        self.username.setMaxLength(34)

        self.verticalLayout_4.addWidget(self.username)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 10)
        self.passwd = QLineEdit(self.frame_4)
        self.passwd.setObjectName(u"passwd")
        sizePolicy1.setHeightForWidth(self.passwd.sizePolicy().hasHeightForWidth())
        self.passwd.setSizePolicy(sizePolicy1)
        self.passwd.setMinimumSize(QSize(200, 50))
        self.passwd.setMaximumSize(QSize(300, 22))
        self.passwd.setMaxLength(34)

        self.verticalLayout_3.addWidget(self.passwd, 0, Qt.AlignmentFlag.AlignTop)

        self.status_label_container = QFrame(self.frame_4)
        self.status_label_container.setObjectName(u"status_label_container")
        self.status_label_container.setMinimumSize(QSize(282, 36))
        self.status_label_container.setMaximumSize(QSize(282, 96))
        self.status_label_container.setFrameShape(QFrame.Shape.NoFrame)
        self.status_label_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.status_label_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 3, 0, 4)
        self.status_label = QLabel(self.status_label_container)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setMinimumSize(QSize(280, 36))
        self.status_label.setMaximumSize(QSize(280, 96))
        self.status_label.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.status_label)


        self.verticalLayout_3.addWidget(self.status_label_container)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_2 = QFrame(self.main_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(160, 45))
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_btn = QPushButton(self.frame_5)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(160, 45))
        self.exit_btn.setMaximumSize(QSize(160, 45))

        self.horizontalLayout_2.addWidget(self.exit_btn)

        self.login_btn = QPushButton(self.frame_5)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(160, 45))
        self.login_btn.setMaximumSize(QSize(160, 45))

        self.horizontalLayout_2.addWidget(self.login_btn)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.frame_8)

        self.footer_text = QLabel(self.frame_6)
        self.footer_text.setObjectName(u"footer_text")
        self.footer_text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_7.addWidget(self.footer_text)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.main_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.icon_label.setText("")
        self.main_label.setText(QCoreApplication.translate("Form", u"ASENA", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"L\u00fctfen Kullan\u0131c\u0131 ad\u0131 giriniz.", None))
        self.passwd.setPlaceholderText(QCoreApplication.translate("Form", u"L\u00fctfen \u015eifre Giriniz.", None))
        self.status_label.setText("")
        self.exit_btn.setText(QCoreApplication.translate("Form", u"\u00c7\u0131k\u0131\u015f", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"Giri\u015f", None))
        self.footer_text.setText(QCoreApplication.translate("Form", u"Coded By DotPEEK", None))
    # retranslateUi

