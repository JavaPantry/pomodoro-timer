import tkinter as tk
from .constants import *


class ConfigTab:

    configData = {'workPeriod': 25,'breakPeriod': 5}
    # workPeriodEntry:tk.Entry = None
    # breakPeriodEntry:tk.Entry = None
    # saveBtn = None # tk.Button(None, text="Save", font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)


    def __init__(self, configTab) -> None:
        self.dummyConfigLabel1 = tk.Label(configTab, text="Work Period (in minutes)", font=LABEL_FONT)
        self.dummyConfigLabel1.grid(columnspan=2, column=0, row=0)
        self.workPeriodEntry = tk.Entry(configTab, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
        self.workPeriodEntry.grid(column=2, row=0)

        self.dummyConfigLabel2 = tk.Label(configTab, text="Break Period (in minutes)", font=LABEL_FONT)
        self.dummyConfigLabel2.grid(columnspan=2, column=0, row=1)
        self.breakPeriodEntry = tk.Entry(configTab, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
        self.breakPeriodEntry.grid(column=2, row=1)

        self.dummyConfigLabel3 = tk.Label(configTab, text="Dummy Config 3", font=LABEL_FONT)
        self.dummyConfigLabel3.grid(columnspan=2, column=0, row=2)

        self.dummyConfigLabel4 = tk.Label(configTab, text="Dummy Config 4", font=LABEL_FONT)
        self.dummyConfigLabel4.grid(columnspan=2, column=0, row=3)

        self.saveBtn = tk.Button(configTab, text="Save", command=lambda:self.saveConfig(), font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)
        self.saveBtn.grid(column=0, row=4)


    def saveConfig(self):
        self.configData['workPeriod'] = int(self.workPeriodEntry.get())
        self.configData['breakPeriod'] = int(self.breakPeriodEntry.get())
        self.saveBtn.event_generate("<<ConfigUpdated>>", when="tail")
