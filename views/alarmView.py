import tkinter as tk
from .constants import *


class AlarmView:

    configData = {'workPeriod': 25,'breakPeriod': 5}
    # workPeriodEntry:tk.Entry = None
    # breakPeriodEntry:tk.Entry = None
    # saveBtn = None # tk.Button(None, text="Save", font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)


    def __init__(self, root) -> None:
        self.root = root
        self.dummyConfigLabel1 = tk.Label(root, text="Alarm Hours", font=LABEL_FONT)
        self.dummyConfigLabel1.grid(columnspan=2, column=0, row=0)
        self.workPeriodEntry = tk.Entry(root, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
        self.workPeriodEntry.grid(column=2, row=0)

        self.dummyConfigLabel2 = tk.Label(root, text="Alarm minutes", font=LABEL_FONT)
        self.dummyConfigLabel2.grid(columnspan=2, column=0, row=1)
        self.breakPeriodEntry = tk.Entry(root, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
        self.breakPeriodEntry.grid(column=2, row=1)

        self.setAlarmBtn = tk.Button(root, text="Set Alarm", command=lambda:self.setAlarm(), font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)
        self.setAlarmBtn.grid(column=0, row=4)


    def setAlarm(self):
        pass
        # self.configData['workPeriod'] = int(self.workPeriodEntry.get())
        # self.configData['breakPeriod'] = int(self.breakPeriodEntry.get())
        # self.saveBtn.event_generate("<<ConfigUpdated>>", when="tail")
