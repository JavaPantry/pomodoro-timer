import tkinter as tk
from .constants import *

configData = {'workPeriod': 25,'breakPeriod': 5}

workPeriodEntry:tk.Entry = None
breakPeriodEntry:tk.Entry = None
saveBtn = None # tk.Button(None, text="Save", font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)


def saveConfig():
    global workPeriodEntry, breakPeriodEntry,configData
    print("Save config")
    print("Save config: workPeriodEntry = "     + workPeriodEntry.get())
    print("Save config: breakPeriodEntry = "    + breakPeriodEntry.get())

    configData['workPeriod'] = int(workPeriodEntry.get())
    configData['breakPeriod'] = int(breakPeriodEntry.get())

    # fire custom tk.Event() to update config in Main.py
    # by binding root to this custom Event root.bind("<<ConfigUpdated>>", configUpdated)
    # https://stackoverflow.com/questions/36237551/custom-events-in-tkinter
    # https://python.hotexamples.com/examples/Tkinter/Tk/event_generate/python-tk-event_generate-method-examples.html
    saveBtn.event_generate("<<ConfigUpdated>>", when="tail")
        

# ConfigTab
# configTab = tk.Frame(root, bg=BG_COLOR)
# configTab.grid(columnspan=3, column=0, row=0)

def createConfigView(configTab): # = tk.Frame(root, bg=BG_COLOR)
    global workPeriodEntry, breakPeriodEntry, saveBtn
    dummyConfigLabel1 = tk.Label(configTab, text="Work Period (in minutes)", font=LABEL_FONT)
    dummyConfigLabel1.grid(columnspan=2, column=0, row=0)
    workPeriodEntry = tk.Entry(configTab, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
    workPeriodEntry.grid(column=2, row=0)

    dummyConfigLabel2 = tk.Label(configTab, text="Break Period (in minutes)", font=LABEL_FONT)
    dummyConfigLabel2.grid(columnspan=2, column=0, row=1)
    breakPeriodEntry = tk.Entry(configTab, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
    breakPeriodEntry.grid(column=2, row=1)

    dummyConfigLabel3 = tk.Label(configTab, text="Dummy Config 3", font=LABEL_FONT)
    dummyConfigLabel3.grid(columnspan=2, column=0, row=2)

    dummyConfigLabel4 = tk.Label(configTab, text="Dummy Config 4", font=LABEL_FONT)
    dummyConfigLabel4.grid(columnspan=2, column=0, row=3)

    saveBtn = tk.Button(configTab, text="Save", command=lambda:saveConfig(), font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)
    saveBtn.grid(column=0, row=4)
