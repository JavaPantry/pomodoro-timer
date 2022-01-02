import tkinter as tk
from tkinter import ttk
from typing import Any
import PyPDF2
import time
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from utils.functions import resize_image, convertSec, calcPercentage

MAIN_DISPLAY_FONT = ("Arial Black", 60)
DISPLAY_FONT = ("Arial Black", 30)
LABEL_FONT = ("Helvetica", 16)
LABEL_FONT_BOLD = ("Helvetica", 16, "bold")
BUTTON_FONT = ("Areal Black", 16)

timerOn = False

appWorkingTimeTotal = 0
appWorkingTimeStart = time.time()

workingTimerStart           = time.time()
workingTimerTicks           = 0
workingTimerTotal           = 0
workingTimerTotalRuntime    = 0

def updateTimeDisplay():
    global timerOn, appWorkingTimeTotal, appWorkingTimeStart, workingTimerTicks, workingTimerStart, workingTimerTotal, workingTimerTotalRuntime

    currentTimeTicks    = time.time()
    appWorkingTimeTotal = currentTimeTicks - appWorkingTimeStart
    workingTimerTicks   = currentTimeTicks - workingTimerStart
    if(timerOn == True):
        workingTimerTotalRuntime   = workingTimerTotal +  workingTimerTicks
    else:
        # don't add ticks otherwise Actual time working will think that you are working
        workingTimerTotalRuntime   = workingTimerTotal 

    timeDisplay.config(text=time.strftime("%H:%M:%S"))
    total_app_work_timerDisplay.config(text=convertSec(appWorkingTimeTotal))
    actualWorkPercentageDisplay.config(text="Actual work time: " + calcPercentage(appWorkingTimeTotal/1000., (workingTimerTotalRuntime)/1000.) + "%")

    if(timerOn == True):
        timerDisplay.config(text=convertSec(workingTimerTicks))
        total_work_timerDisplay.config(text=convertSec(workingTimerTotalRuntime))

    root.after(1000, updateTimeDisplay)


def start_timer():
    global timerOn, workingTimerStart, workingTimerTotal, workingTimerTotalRuntime
    
    # On STOP, reset the timer
    if(timerOn == True):
        timerOn = False
        start_btn.config(text="Start")
        start_btn.config(bg="green")
        # don't stop # workingTimerStart = 0
        workingTimerTotal = workingTimerTotalRuntime

    # On START, start the timer
    else:
        timerOn = True
        start_btn.config(text="Stop")
        start_btn.config(bg="red")
        workingTimerStart = time.time();

# *************************************************************
# ********         START UI          **************************
# *************************************************************

root = tk.Tk()
root.title("Time Tracker")
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='asset/logoTransp.png'))
rootCanvas = tk.Canvas(root, width=600, height=300)
rootCanvas.grid(columnspan=1, rowspan=2)
logo = Image.open('./assets/logoTransp.png')
logo = resize_image(logo, 400, 400)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(rootCanvas, image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)


tabs = ttk.Notebook(rootCanvas)
tabs.grid(column=0, row=1, columnspan=1, rowspan=1)
mainTab     = ttk.Frame(tabs)
configTab   = ttk.Frame(tabs)

tabs.add(mainTab, text="Main")
mainCanvas = tk.Canvas(mainTab) # , width=600, height=300
mainCanvas.grid(columnspan=3, rowspan=6)

tabs.add(configTab, text="Config")
configCanvas = tk.Canvas(configTab) # , width=600, height=300
configCanvas.grid(columnspan=3, rowspan=6)


# tabs.pack(expand=1, fill="both")
rootCanvas.pack(expand=1, fill="both")


# *************************************************************
# ********         mainTab          **************************
# *************************************************************

actualWorkPercentageDisplay = tk.Label(mainTab, text="Actual work 0.0%", font=LABEL_FONT_BOLD)
actualWorkPercentageDisplay.grid(columnspan=3, column=0, row=1)

timeDisplay = tk.Label(mainTab, text=convertSec(0), font=MAIN_DISPLAY_FONT)
timeDisplay.grid(columnspan=3, column=0, row=3)

start_btn = tk.Button(mainTab, text="Start", command=lambda:start_timer(), font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)
start_btn.grid(column=0, row=4)

timerDisplay = tk.Label(mainTab, text=convertSec(0), font=DISPLAY_FONT)
timerDisplay.grid(columnspan=2, column=1, row=4)

total_work_timer_label = tk.Label(mainTab, text="Total work time", font=LABEL_FONT)
total_work_timer_label.grid(column=0, row=5)

total_work_timerDisplay = tk.Label(mainTab, text=convertSec(0), font=DISPLAY_FONT)
total_work_timerDisplay.grid(columnspan=2, column=1, row=5)

total_app_work_timer_label = tk.Label(mainTab, text="Total app worktime", font=LABEL_FONT)
total_app_work_timer_label.grid(column=0, row=6)

total_app_work_timerDisplay = tk.Label(mainTab, text=convertSec(0), font=DISPLAY_FONT)
total_app_work_timerDisplay.grid(columnspan=2, column=1, row=6)

# *************************************************************
# ********         ConfigTab          **************************
# *************************************************************

dummyConfigLabel1 = tk.Label(configTab, text="Dummy Config", font=("Arial Black", 50))
dummyConfigLabel1.grid(columnspan=3, column=0, row=3)
dummyConfigLabel2 = tk.Label(configTab, text="Dummy Config", font=("Arial Black", 50))
dummyConfigLabel2.grid(columnspan=3, column=0, row=4)
dummyConfigLabel3 = tk.Label(configTab, text="Dummy Config", font=("Arial Black", 50))
dummyConfigLabel3.grid(columnspan=3, column=0, row=5)
dummyConfigLabel4 = tk.Label(configTab, text="Dummy Config", font=("Arial Black", 50))
dummyConfigLabel4.grid(columnspan=3, column=0, row=6)

updateTimeDisplay()
root.mainloop()