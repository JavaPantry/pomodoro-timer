import tkinter as tk
from tkinter import ttk
from views.alarmView import AlarmView
from views.digitalClock import DigitalClock
from views.calcFunctions import *
from views.constants import *
from views.configTab import *
from views.PomodoroView import *
from views.logo import *
from views.gameScreen import *

def configUpdated(evt):
    print("in main.py: config updated event received configData = ",configPane.configData["workPeriod"], configPane.configData["breakPeriod"])

# *************************************************************
# ********         START UI          **************************
# *************************************************************

root = tk.Tk()
root.title("Time Tracker")
root.iconbitmap('./assets/logoTransp4icon24.ico')
rootFrame = tk.Frame(root)
rootFrame.grid(columnspan=1, rowspan=2)
rootFrame.pack(expand=1, fill="both")

digitalClockDisplay = DigitalClock(rootFrame)

notebook = ttk.Notebook(rootFrame)
notebook.grid(column=0, row=1) # , columnspan=1, rowspan=1

alarmTab = ttk.Frame(notebook)
pomodoroTab     = ttk.Frame(notebook)
configTab   = ttk.Frame(notebook)

notebook.add(alarmTab, text="Alarm Clock")
notebook.add(pomodoroTab, text="Pomodoro")
notebook.add(configTab, text="Pomodoro Config")

rootFrame.pack(expand=1, fill="both")

# alarmTab
alarmView = AlarmView(alarmTab)
pomodoroView = PomodoroView(pomodoroTab)
configPane = ConfigTab(configTab)

root.bind("<<ConfigUpdated>>", configUpdated)
root.mainloop()