from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from source.qtimer import Timer

class QCounterLabel(QLabel):
    def __init__(self,parent = None,msecs = 5000,end_value = 0):
        super().__init__(parent)

        self.hour = 0
        self.minute = 0
        self.second = 0

        self.counter_timer = Timer()
        self.counter_timer.setInterval(msecs)
        self.counter_timer.timeout.connect(self.set_text_of_label)
        self.counter_timer.signal.stopped.connect(self.finish_text)

        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("color: #625fb8;\nfont: 700 18pt \"Arial\";\nborder: none;")

    def set_text_of_label(self):
        self.fmt = self.create_string_format()
        if self.second == 60:
            self.second = 0
            self.minute += 1
        elif self.minute == 60:
            self.minute = 0
            self.hour+=1
        self.second+=1
        self.setText(self.fmt)

    def create_string_format(self):
        fmt = " %s Saniye" % (self.second)
        if self.minute > 0 and self.hour < 1:
            fmt = f"{self.minute} Dakika {self.second} Saniye"
        if self.hour > 0:
            if self.minute == 0:
                fmt = f"{self.hour} Saat {self.second} Saniye"
            else:
                fmt = f"{self.hour} Saat {self.minute} Dakika {self.second} Saniye"
        if self.minute >= 5:
            self.setStyleSheet(self.styleSheet().replace("#625fb8","red"))
        out_text = "Geçen Süre: " + fmt if self.minute < 5 and self.hour < 1 else "Zaman Aşımı Geçen sipariş !!! " + fmt
        return out_text
    def finish_text(self):
        self.setText("Zaman Süresi doldu !!!")
    def start_timer_label(self):
        self.counter_timer.start(self.msecs_interval)
