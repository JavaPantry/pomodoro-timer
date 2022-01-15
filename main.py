import tkinter as tk
from tkinter import ttk
from views.analogClock import AnalogClock
from views.digitalClock import DigitalClock
from views.calcFunctions import *
from views.constants import *
from views.configTab import *
from views.mainTab import *
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
rootFrame = tk.Frame(root, width=600, height=300)
rootFrame.grid(columnspan=1, rowspan=2)
rootFrame.pack(expand=1, fill="both")

mainDisplay = DigitalClock(rootFrame)

notebook = ttk.Notebook(rootFrame)
notebook.grid(column=0, row=1, columnspan=1, rowspan=1)

pomodoroTab     = ttk.Frame(notebook)
pomodoroTab.grid(columnspan=3, rowspan=6)
configTab   = ttk.Frame(notebook)
configTab.grid(columnspan=3, rowspan=6)

notebook.add(pomodoroTab, text="Pomodoro")
notebook.add(configTab, text="Pomodoro Config")

rootFrame.pack(expand=1, fill="both")

mainPane = PomodoroView(root,pomodoroTab)
configPane = ConfigTab(configTab)

mainPane.updateTimeDisplay()

root.bind("<<ConfigUpdated>>", configUpdated)
root.mainloop()