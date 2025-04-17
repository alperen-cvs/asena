
from PySide6.QtCore import QRect, QAbstractAnimation
from PySide6.QtWidgets import QWidget

from PySide6.QtCore import QPropertyAnimation

from source.signal import AnimatedWindowSignal
from containers import WinPosition
from utils.win32 import find_window_cordinates
from utils.win32 import get_current_window_text

class AnimatedWindow(QWidget):
    """
    The Animated Window class is a window that can be opened in an animated way, no different than a normal window, inherits the QWidget class

    triggers the close signal when the window is closed

    The Animated Window class is a window that can be opened in an animated way, it is no different from a normal window, it inherits the QWidget class

    triggers the close signal when the window is closed

    if you want to open the window in the foreground
    you can use the find_window_cordinates function
    e.g: utils.win32.find_window_cordinates
    """

    def __init__(self,parent = None,geometry = WinPosition(15,130,500,500)):
        super(AnimatedWindow,self).__init__(parent = parent)
        self._geometry = geometry
        self.start_anim = QPropertyAnimation(self,b"geometry")
        self.start_anim.setDuration(300)
        self.start_anim.setStartValue(QRect(self._geometry.x,self._geometry.y,self._geometry.width,0))
        self.start_anim.setEndValue(QRect(self._geometry.x,self._geometry.y,self._geometry.width,self._geometry.height))
        self.signal = AnimatedWindowSignal()
        self.setWindowTitle("Animated Window Title")
        self.toggle = True
        self.static_close = True
    def closeEvent(self,event,/):

        """
        The close signal will be triggered when the window is closed.
        :param event:
        :return:
        """
        if self.toggle:
            event.ignore() # We ignored the incident so that it would not be closed directly.
            self.setMinimumSize(0,0) #set fixed size if set make it default
            self.close_anim = QPropertyAnimation(self, b"geometry")
            if not self.static_close: #
               self._geometry = find_window_cordinates(self.windowTitle())
            self.close_anim.setDuration(300)
            self.close_anim.setStartValue(QRect(self._geometry.x,self._geometry.y, self._geometry.width, self._geometry.height))
            self.close_anim.setEndValue(QRect(self._geometry.x, self._geometry.y, self._geometry.width, 0))
            self.close_anim.start(QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)
            self.signal.closed.emit(True)
            self.close_anim.finished.connect(self.close)
        else:
            self.close()
        self.toggle = not self.toggle
    def showEvent(self, event, /):

        if self.minimumHeight() == self.maximumHeight():
            self.setMaximumHeight(self._geometry.height)
        self.start_anim.start(QAbstractAnimation.DeletionPolicy.DeleteWhenStopped) # This allows the window to open in an animated manner when it opens, and it closes in the same way.
        self.setFixedSize()
