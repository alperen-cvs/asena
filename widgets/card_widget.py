from .clickable_frame import QClickAbleFrame
from .counter_widget import QCounterLabel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap

class QCardWidget(QClickAbleFrame):

    def __init__(self,title = "This is a title",text = "This is a text",image = None,parent = None):
        """
        :param title: for title
        :param text: for text(message)
        :param image: You can add the image if you want, but remember that the image must be 400x400 maximum, otherwise a ValueError exception will be thrown.
        :param parent:
        """

        super(QCardWidget,self).__init__(parent=parent)

        self.count = 0
        self.vertical_layout = QVBoxLayout(self)


        self.counter_widget = QCounterLabel()
        self.counter_timer = self.counter_widget.counter_timer

        self.text_label = QLabel(title)

        self.customer_label = QLabel(text,alignment=Qt.AlignmentFlag.AlignCenter)
        self.customer_label.setStyleSheet("border: none;\ncolor: #625fb8;\nfont: 700 18pt \"Arial\";\nborder: none;")
        self.customer_label.setWordWrap(True)


        self.text_label.setWordWrap(True)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setStyleSheet("border: none;")

        self.vertical_layout.addWidget(self.customer_label)
        self.vertical_layout.addWidget(self.text_label)

        if not image is None and isinstance(image,str):
            self.image_label = QLabel()
            self.image_label.setFixedSize(QSize(16,16))
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.pixmap = QPixmap(image)
            if self.pixmap.width() > 400 and self.pixmap.height() > 400:
                raise ValueError("Image size overflow pictures must be maximum 400x400")
            self.image_label.setPixmap(self.pixmap.scaled(QSize(self.image_label.width(),self.image_label.height()),Qt.AspectRatioMode.KeepAspectRatio))
            self.vertical_layout.addWidget(self.image_label,alignment=Qt.AlignmentFlag.AlignCenter)
        self.vertical_layout.addWidget(self.counter_widget)
        self.counter_timer.start(1000)
