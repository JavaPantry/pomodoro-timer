import tkinter as tk
from tkinter import ttk
from views.analogClock import AnalogClock
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
root.title("Time Tracker (dead branch commit)")
root.iconbitmap('./assets/logoTransp4icon24.ico')
rootFrame = tk.Frame(root, width=600, height=300)
rootFrame.grid(columnspan=1, rowspan=2)
rootFrame.pack(expand=1, fill="both")

# don't use: logo = GameScreen(rootFrame)
# logo = Logo(rootFrame)
# logo = AnalogClock(rootFrame)
# will put DigitalClock in the logo area and then pull/remove mainDisplay from (mainTab)pomodoro tab (in separated-digitalClock-panel branch)

# ****************************************************************
# ********  This will be dead branch with logo area           ****
# ********  made after switch to digital clock in logo arrea  ****
# ****************************************************************

tabs = ttk.Notebook(rootFrame)
tabs.grid(column=0, row=1, columnspan=1, rowspan=1)

# rename mainTab into pomodoroTab (in separated-digitalClock-panel branch)
mainTab     = ttk.Frame(tabs)
mainTab.grid(columnspan=3, rowspan=6)
configTab   = ttk.Frame(tabs)
configTab.grid(columnspan=3, rowspan=6)

tabs.add(mainTab, text="Main")
tabs.add(configTab, text="Config")

rootFrame.pack(expand=1, fill="both")

mainPane = MainTab(root,mainTab)
configPane = ConfigTab(configTab)

mainPane.updateTimeDisplay()

root.bind("<<ConfigUpdated>>", configUpdated)
root.mainloop()