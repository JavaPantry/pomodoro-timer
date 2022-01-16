import tkinter as tk
import datetime
import time
import winsound
import os
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
        self.alarmHour = tk.Entry(root, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
        self.alarmHour.grid(column=2, row=0)

        self.dummyConfigLabel2 = tk.Label(root, text="Alarm minutes", font=LABEL_FONT)
        self.dummyConfigLabel2.grid(columnspan=2, column=0, row=1)
        self.alarmMinute = tk.Entry(root, width=10) # , font=DISPLAY_FONT , font=ENTRY_FONT
        self.alarmMinute.grid(column=2, row=1)

        self.setAlarmBtn = tk.Button(root, text="Set Alarm", command=lambda:self.setAlarm(), font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)
        self.setAlarmBtn.grid(column=0, row=4)


    def setAlarm(self):
        hour = int(self.alarmHour.get())
        minute = int(self.alarmMinute.get())
        # set alarm for hour:minute
        # set_alarm_timer = f"{hour}:{minute}:{0}"
        # self.alarm(set_alarm_timer)
        self.alarm(hour, minute)


    def alarm(self, hour, minute):
        now = datetime.datetime.now()
        # Choose 6PM today as the time the alarm fires.
        # This won't work well if it's after 6PM, though.
        alarm_time = datetime.datetime.combine(now.date(), datetime.time(hour, minute, 0))

        # Think of time.sleep() as having the operating system set an alarm for you,
        # and waking you up when the alarm fires.
        time.sleep((alarm_time - now).total_seconds())
        # os.system("start BTS_House_Of_Cards.mp3")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

    def alarmStupid(self, set_alarm_timer):
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()
            now = current_time.strftime("%H:%M:%S")
            # date = current_time.strftime("%d/%m/%Y")
            # print("The Set Date is:",date)
            print(now)
            
            delta = set_alarm_timer - now
            print(delta)
            # if now == set_alarm_timer:
            if delta < 0 :
                print("Time to Wake up")
                winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                break

    # def actual_time():
    #     set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    #     alarm(set_alarm_timer)