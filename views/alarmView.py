import tkinter as tk
import datetime
import time
import winsound
import os
from threading import *
from .constants import *

# ***********************************************************************
# ********                Alarm Clock                                  **
# ***********************************************************************

class AlarmView:

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

        self.update()

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

    def update(self):
        if self.alarmSchedule.size() == 0:
            # print("Skip Empty Alarm schedule")
            self.root.after(1000, self.update)
            return

        current_time = datetime.datetime.now()

        # print("Alarm Thread self.alarmSchedule.get(0, tk.END)", self.alarmSchedule.get(0, tk.END))
        # Alarm Thread self.alarmSchedule.get(0, tk.END) ('20:37', '20:38', '20:39')

        # exception in: for idx, item in enumerate(self.alarmSchedule.get(0, tk.END)):
        for item in self.alarmSchedule.get(0, tk.END):
            # get hour and minute from item
            item_split = item.split(":")
            hour = int(item_split[0])
            minute = int(item_split[1])
            
            if current_time.hour == hour and current_time.minute == minute:
                # remove item from listbox
                idx = self.alarmSchedule.get(0, tk.END).index(item)
                self.alarmSchedule.delete(idx)
                winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        self.root.after(1000, self.update)
        


# ***********************************************************************
# ********                Alarm Clock                                  **
# **        Create an Alarm Clock using Tkinter - Using threads        **
# ** https://www.geeksforgeeks.org/creat-an-alarm-clock-using-tkinter/ **
# ***********************************************************************

# Python class instance starts method in new thread
# https://stackoverflow.com/questions/18416116/python-class-instance-starts-method-in-new-thread

# def Threading():
#     t1=Thread(target=alarmThread)
#     t1.start()

# def alarmThread():
#     while True:
#         time.sleep(5)
#         if _this.alarmSchedule.size() == 0:
#             print("Skip Empty Alarm schedule")
#             continue

#         current_time = datetime.datetime.now()
#         now = current_time.strftime("%H:%M:%S")
#         print("Alarm Thread", now)

#         # for each item form alarmSchedule
#         itemIndex = 0
#         for item in _this.alarmSchedule.get(itemIndex):
#             print("Alarm Thread looping:", item)
#             # get hour and minute from item
#             item_split = item.split(":")
#             hour = int(item_split[0])
#             minute = int(item_split[1])
            
#             # set_alarm_timer = f"{hour}:{minute}:{0}"
#             # print(set_alarm_timer)
#             # if now == set_alarm_timer:
#             if current_time.hour == hour and current_time.minute == minute:
#                 # remove item from listbox
#                 print("time to alarm", item)
#                 _this.alarmSchedule.delete(itemIndex)
#                 winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
#             if itemIndex < _this.alarmSchedule.size()-1:
#                 itemIndex += 1
#             else:  # if itemIndex == self.alarmSchedule.size()-1:
#                 break


# start threading
# Threading()

    # def actual_time():
    #     set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    #     alarm(set_alarm_timer)

    # def alarmStupid(self, set_alarm_timer):
    #     while True:
    #         time.sleep(1)
    #         current_time = datetime.datetime.now()
    #         now = current_time.strftime("%H:%M:%S")
    #         # date = current_time.strftime("%d/%m/%Y")
    #         # print("The Set Date is:",date)
    #         print(now)
            
    #         delta = set_alarm_timer - now
    #         print(delta)
    #         # if now == set_alarm_timer:
    #         if delta < 0 :
    #             print("Time to Wake up")
    #             winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
    #             break


    # def setAlarm(self):
    #     hour = int(self.alarmHour.get())
    #     minute = int(self.alarmMinute.get())
    #     # set alarm for hour:minute
    #     # set_alarm_timer = f"{hour}:{minute}:{0}"
    #     # self.alarm(set_alarm_timer)
    #     self.alarm(hour, minute)


    # def alarm(self, hour, minute):
    #     now = datetime.datetime.now()
    #     # Choose 6PM today as the time the alarm fires.
    #     # This won't work well if it's after 6PM, though.
    #     alarm_time = datetime.datetime.combine(now.date(), datetime.time(hour, minute, 0))

    #     # Think of time.sleep() as having the operating system set an alarm for you,
    #     # and waking you up when the alarm fires.
    #     time.sleep((alarm_time - now).total_seconds())
    #     # os.system("start BTS_House_Of_Cards.mp3")
    #     winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
