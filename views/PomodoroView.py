import tkinter as tk
import time
from .constants import *
from .calcFunctions import *

class PomodoroView:

    configData = {'workPeriod': 25,'breakPeriod': 5}

    timerOn = False

    appWorkingTimeTotal = 0
    appWorkingTimeStart = time.time()

    workingTimerStart           = time.time()
    workingTimerTicks           = 0
    workingTimerTotal           = 0
    workingTimerTotalRuntime    = 0

    def __init__(self, root, mainTab) -> None:
        self.root = root
        self.actualWorkPercentageDisplay = tk.Label(mainTab, text="Actual work 0.0%", font=LABEL_FONT_BOLD)
        self.actualWorkPercentageDisplay.grid(columnspan=3, column=0, row=1)

        buttonFrame = tk.Frame(mainTab, bg="white")
        buttonFrame.grid(column=0, row=4) # , columnspan=3, rowspan=1
        self.start_btn = tk.Button(buttonFrame, text="Start", command=lambda:self.start_timer(), font=BUTTON_FONT, bg="green", fg="white") # , height=1, width=14
        self.start_btn.grid(column=0, row=0, columnspan=2)
        self.reset_btn = tk.Button(buttonFrame, text="X", command=lambda:self.reset_timer(), font=BUTTON_FONT, bg="green", fg="white") # , height=1, width=1
        self.reset_btn.grid(column=2, row=0)

        self.timerDisplay = tk.Label(mainTab, text=convertSec(0), font=DISPLAY_FONT)
        self.timerDisplay.grid(columnspan=2, column=1, row=4)

        self.total_work_timer_label = tk.Label(mainTab, text="Total work time", font=LABEL_FONT)
        self.total_work_timer_label.grid(column=0, row=5)

        self.total_work_timerDisplay = tk.Label(mainTab, text=convertSec(0), font=DISPLAY_FONT)
        self.total_work_timerDisplay.grid(columnspan=2, column=1, row=5)

        self.total_app_work_timer_label = tk.Label(mainTab, text="Total app worktime", font=LABEL_FONT)
        self.total_app_work_timer_label.grid(column=0, row=6)

        self.total_app_work_timerDisplay = tk.Label(mainTab, text=convertSec(0), font=DISPLAY_FONT)
        self.total_app_work_timerDisplay.grid(columnspan=2, column=1, row=6)
        self.update()

    def update(self):
        currentTimeTicks    = time.time()
        self.appWorkingTimeTotal = currentTimeTicks - self.appWorkingTimeStart
        workingTimerTicks   = currentTimeTicks - self.workingTimerStart
        if(self.timerOn == True):
            self.workingTimerTotalRuntime   = self.workingTimerTotal +  workingTimerTicks
        else:
            # don't add ticks otherwise Actual time working will think that you are working
            self.workingTimerTotalRuntime   = self.workingTimerTotal 

        self.total_app_work_timerDisplay.config(text=convertSec(self.appWorkingTimeTotal))
        self.actualWorkPercentageDisplay.config(text="Actual work time: " + calcPercentage(self.appWorkingTimeTotal/1000., self.workingTimerTotalRuntime/1000.) + "%")

        if(self.timerOn == True):
            self.timerDisplay.config(text=convertSec(workingTimerTicks))
            self.total_work_timerDisplay.config(text=convertSec(self.workingTimerTotalRuntime))

        self.root.after(1000, self.update)

    def start_timer(self):
        # On STOP, reset the timer
        if(self.timerOn == True):
            self.timerOn = False
            self.start_btn.config(text="Start")
            self.start_btn.config(bg="green")
            # don't stop # workingTimerStart = 0
            self.workingTimerTotal = self.workingTimerTotalRuntime

        # On START, start the timer
        else:
            self.timerOn = True
            self.start_btn.config(text="Stop")
            self.start_btn.config(bg="red")
            self.workingTimerStart = time.time();

    def reset_timer(self):
        self.timerOn = False
        self.start_btn.config(text="Start")
        self.start_btn.config(bg="green")

        self.workingTimerTotal      = 0
        self.workingTimerStart      = 0
        self.appWorkingTimeTotal    = 0
        self.appWorkingTimeStart    = time.time()
        self.timerDisplay.config(text=convertSec(0))
        self.total_work_timerDisplay.config(text=convertSec(0))
