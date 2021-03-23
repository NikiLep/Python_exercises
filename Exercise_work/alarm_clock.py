# File: Ex2_10
# Author: Niki Leppänen
# Description: Code the alarm clock, use objects.

import datetime
import time
from tkinter import *
from tkinter.ttk import *


class AlarmClock:

    def __init__(self):
        self.wake_up_time = ""
        self.current = ""

    # This method allows user to set alarm
    def set_alarm(self, wakeup):
        self.wake_up_time = wakeup

    # This method returns value of user input in set_alarm function
    def get_alarm_time(self):
        return self.wake_up_time

    def get_time(self):
        current_time = datetime.datetime.now()
        self.current = current_time.strftime("%H:%M:%S")
        return self.current







