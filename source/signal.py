from PySide6.QtCore import Signal,QObject
from utils import create_rand_char
from random import  randint
"""
def create_new_timer_signal():
    class TimerSignal(QObject):
        started = Signal(bool)
        stopped = Signal(bool)
    return type(f"Timer_Signal_{randint(1,999)}_{create_rand_char(32)}",(TimerSignal,),{})()
    # Disabled
"""
class TimerSignal(QObject):
    started = Signal(bool)
    stopped = Signal(bool)

class AnimatedWindowSignal(QObject):
    closed = Signal(bool)

class ClickAbleFrameSignal(QObject):
    mouse_long_press = Signal(bool)