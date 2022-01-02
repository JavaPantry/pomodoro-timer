import tkinter as tk
from typing import Any
import PyPDF2
import time
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from utils.functions import resize_image, convertSec, calcPercentage

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
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=6)

logo = Image.open('./assets/logoTransp.png')
logo = resize_image(logo, 400, 400)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0)

actualWorkPercentageDisplay = tk.Label(root, text="Actual work 0.0%", font="Raleway")
actualWorkPercentageDisplay.grid(columnspan=3, column=0, row=1)

timeDisplay = tk.Label(root, text=convertSec(0), font=("Arial Black", 50))
timeDisplay.grid(columnspan=3, column=0, row=3)

start_btn = tk.Button(root, text="Start", command=lambda:start_timer(), font="Raleway", bg="green", fg="white", height=2, width=15)
start_btn.grid(column=0, row=4)

timerDisplay = tk.Label(root, text=convertSec(0), font=("Arial Black", 40))
timerDisplay.grid(columnspan=2, column=1, row=4)

total_work_timer_label = tk.Label(root, text="total work time", font="Raleway")
total_work_timer_label.grid(column=0, row=5)

total_work_timerDisplay = tk.Label(root, text=convertSec(0), font=("Arial Black", 40))
total_work_timerDisplay.grid(columnspan=2, column=1, row=5)

total_app_work_timer_label = tk.Label(root, text="total app worktime", font="Raleway")
total_app_work_timer_label.grid(column=0, row=6)

total_app_work_timerDisplay = tk.Label(root, text=convertSec(0), font=("Arial Black", 40))
total_app_work_timerDisplay.grid(columnspan=2, column=1, row=6)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

updateTimeDisplay()
root.mainloop()