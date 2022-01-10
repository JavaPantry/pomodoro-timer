import math
import tkinter as tk

def calcPercentage(total, part):
    percent = 0.0
    if(total != 0 ):
        percent = (part * 100.0) / total
    # percent = 100 - percent
    return "{:10.2f}".format(percent)

def convertSec(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    # return str(hours) + ":" + str(mins) + ":" + str(sec)
    return "{0:02}:{1:02}:{2:02}".format(int(hours),int(mins),int(sec))


# time = time.split(":")
# hours = int(time[0])
# mins = int(time[1])
# sec = int(time[2])
# return hours * 3600 + mins * 60 + sec


def getSeconds(time):
    time = time.split(":")
    return int(time[2])

def getMinutes(time):
    time = time.split(":")
    return int(time[1])

def getHours(time):
    time = time.split(":")
    return int(time[0])

def drawClock(timeStr, canvas, x, y, r, color):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)
    # draw the clock hands
    hours = getHours(timeStr)
    hoursAngle = hours * 30
    # draw the hour hand
    canvas.create_line(x, y, x + (math.sin(math.radians(hoursAngle)) * r*0.60), y - (math.cos(math.radians(hoursAngle)) * r*0.60), width=3, fill="black", arrow=tk.LAST)
    # draw the minute hand
    minutes = getMinutes(timeStr)
    minutesAngle = minutes * 6
    canvas.create_line(x, y, x + (math.sin(math.radians(minutesAngle)) * r*0.80), y - (math.cos(math.radians(minutesAngle)) * r*0.80), width=3, fill="black", arrow=tk.LAST)
    # draw the second hand
    seconds = getSeconds(timeStr)
    secondsAngle = seconds * 6
    canvas.create_line(x, y, x + (math.sin(math.radians(secondsAngle)) * r*0.90), y - (math.cos(math.radians(secondsAngle)) * r*0.90), width=3, fill="red", arrow=tk.LAST)
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")