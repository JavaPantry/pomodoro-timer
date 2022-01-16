import tkinter as tk
import datetime
import time
import winsound
import os
from .constants import *

# ***********************************************************************
# ********                Alarm Clock                                  **
# **        Create an Alarm Clock using Tkinter - Using threads        **
# ** https://www.geeksforgeeks.org/creat-an-alarm-clock-using-tkinter/ **
# ***********************************************************************

class AlarmView:

    configData = {'workPeriod': 25,'breakPeriod': 5}
    # workPeriodEntry:tk.Entry = None
    # breakPeriodEntry:tk.Entry = None
    # saveBtn = None # tk.Button(None, text="Save", font=BUTTON_FONT, bg="green", fg="white", height=1, width=15)


    def __init__(self, root) -> None:
        self.root = root

        hoursLabel = tk.Label(root, text="Hours", font=LABEL_FONT)
        hoursLabel.grid(column=0, row=0)
        minutesLabel = tk.Label(root, text="Minutes", font=LABEL_FONT)
        minutesLabel.grid(column=1, row=0)

        self.alarmHour = tk.Entry(root)#, width=10
        self.alarmHour.grid(column=0, row=1)
        self.alarmMinute = tk.Entry(root)#, width=10
        self.alarmMinute.grid(column=1, row=1)
        self.setAlarmBtn = tk.Button(root, text="Add Alarm", command=lambda:self.addScheduledAlarm(), font=BUTTON_FONT, bg="green", fg="white")#, height=1, width=15
        self.setAlarmBtn.grid(column=2, row=1)

        ## add scrollable listbox for alarm history
        self.alarmSchedule = tk.Listbox(root, width=15, height=5)
        self.alarmSchedule.grid(column=0, row=2, columnspan=3)

    def addScheduledAlarm(self):
        if self.alarmHour.get() == '' or self.alarmMinute.get() == '':
            # get last item from listbox
            last_item = self.alarmSchedule.get(self.alarmSchedule.size()-1)

            if last_item == '':
                now = datetime.datetime.now()
                hour = now.hour
                minute = now.minute+1
                alarm_time = str(hour) + ":" + str(minute)
            else:
                # get minute from last item
                last_item_split = last_item.split(":")
                hour = int(last_item_split[0])
                minute = int(last_item_split[1])
                minute += 1
                alarm_time = str(hour) + ":" + str(minute)
        else:
            alarm_time = self.alarmHour.get() + ":" + self.alarmMinute.get()

        self.alarmSchedule.insert(tk.END, alarm_time)

        # hour = int(self.alarmHour.get())
        # minute = int(self.alarmMinute.get())
        # self.alarmSchedule.insert(tk.END, f"{hour}:{minute}")


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