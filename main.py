import tkinter as tk
from tkinter import ttk
from views.calcFunctions import *
from views.constants import *
from views.configTab import *
from views.mainTab import *
from views.logo import *


def configUpdated(evt):
    print("in main.py: config updated event received configData = ",configPane.configData["workPeriod"], configPane.configData["breakPeriod"])

# *************************************************************
# ********         START UI          **************************
# *************************************************************

root = tk.Tk()
root.title("Time Tracker")
root.iconbitmap('./assets/logoTransp4icon24.ico')
rootCanvas = tk.Canvas(root, width=600, height=300)
rootCanvas.grid(columnspan=1, rowspan=2)

logo = Logo( rootCanvas)

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

rootCanvas.pack(expand=1, fill="both")

mainPane = MainTab(root,mainTab)
configPane = ConfigTab(configTab)

mainPane.updateTimeDisplay()

root.bind("<<ConfigUpdated>>", configUpdated)
root.mainloop()