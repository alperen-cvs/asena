import sys

from PySide6.QtCore import QTimer

from source.signal import TimerSignal
class Timer(QTimer):
    """
    end value is the threshold value of the timer if the threshold value is exceeded the stopped signal will be triggered

    Signals:
    started: triggered when the timer is started
    stopped: triggered when the timer stops or when the threshold value is exceeded

    NOTE: DO NOT USE THE SAME TIMERS NAMES ANYWAY!! THERE IS A POSSIBILITY OF THEM OVERLAPPING

    E.G:

    class FirstSimpleClass:
        self.timer = Timer()
    class SecondSimpleClass:
        self.timer = Timer()
    DO NOT USE LIKE THIS !!!

    """
    def __init__(self,*args,**kwargs):

        super(Timer,self).__init__(*args,**kwargs)
        self.end_value = 5000
        self.signal = TimerSignal()
        self.elapsed = 0
        self.set_elapsed_timer_if_needed()
    def start(self, value = 100):
        self.signal.started.emit(True)
        self.set_elapsed_timer_if_needed()
        super().start(value)

    def stop(self):
        self.signal.stopped.emit(True)
        super(Timer,self).stop()

    def set_elapsed_timer_if_needed(self):
        if self.end_value > 0:
            self.timerEvent = self._timer_event # If the threshold value is greater than 0, the timerEvent function will be overridden accordingly.

    def _timer_event(self,arg_1):
        if self.elapsed > self.end_value:
            self.stop()
        if self.isActive(): # The timeout signal will be triggered as long as the timer is active to prevent the timeout from exceeding
            self.timeout.emit()
        self.elapsed += self.interval()



