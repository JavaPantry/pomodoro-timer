import tkinter as tk
import time
import math
from .constants import *
from views.functions import resize_image
from .calcFunctions import *
from PIL import Image, ImageTk

class AnalogClock:

    def __init__(self, rootCanvas):
        self.canvas = tk.Canvas(rootCanvas, width=300, height=300)
        self.canvas.grid(column=0, row=0)
        self.canvas.create_oval(10, 10, 190, 190, fill="white")
        
        self.logo = Image.open('./assets/logoTransp.png')
        self.logo = resize_image(self.logo, 150, 150)
        self.logo = ImageTk.PhotoImage(self.logo)
        # logo_label = tk.Label(rootCanvas, image=logo)
        # logo_label.image = logo
        # logo_label.grid(column=0, row=0)

        self.update()

    def update(self):
        # draw the clock face
        self.canvas.create_oval(10, 10, 190, 190, fill="white")
        # draw the clock hands
        hours = getHours(time.strftime("%H:%M:%S"))
        hoursAngle = hours * 30
        # draw the hour hand
        self.canvas.create_line(100, 100, 100 + (math.sin(math.radians(hoursAngle)) * 60), 100 - (math.cos(math.radians(hoursAngle)) * 60), width=3, fill="black", arrow=tk.LAST)
        # draw the minute hand
        minutes = getMinutes(time.strftime("%H:%M:%S"))
        minutesAngle = minutes * 6
        self.canvas.create_line(100, 100, 100 + (math.sin(math.radians(minutesAngle)) * 80), 100 - (math.cos(math.radians(minutesAngle)) * 80), width=3, fill="black", arrow=tk.LAST)
        # draw the second hand
        seconds = getSeconds(time.strftime("%H:%M:%S"))
        secondsAngle = seconds * 6
        self.canvas.create_line(100, 100, 100 + (math.sin(math.radians(secondsAngle)) * 90), 100 - (math.cos(math.radians(secondsAngle)) * 90), width=3, fill="red", arrow=tk.LAST)


        self.canvas.create_image(200, 50, image=self.logo)
        drawClock(time.strftime("%H:%M:%S"), self.canvas, 200, 50,  40, "lightblue", False)
        drawClock(time.strftime("%H:%M:%S"), self.canvas, 180, 180, 30, "lightgreen")

        # call the update method again after 1 second
        self.canvas.after(1000, self.update)


        # mins = getMinutes(time.strftime("%H:%M:%S"))
        # minsAngle = mins * 6
        # secs = getSeconds(time.strftime("%H:%M:%S"))
        # secsAngle = secs * 6

        # self.canvas.create_line(100, 100, 100, (100 - (secs * 0.1)), fill="black")
        # self.canvas.create_line(100, 100, (100 - (mins * 0.1)), 100, fill="black")
        # self.canvas.create_line(100, 100, (100 - (hours * 0.1)), 100, fill="black")

        # self.canvas.create_line(100, 10, 100, 90, width=5, fill="black")
        # self.canvas.create_line(100, 10, 100, 50, width=5, fill="black")

        # draw the clock center
        # self.canvas.create_line(100, 100, 100, 100, width=5, fill="black")

        # draw the clock numbers
        # for i in range(1, 13):
        #     self.canvas.create_line(100, 10, 100 + (i * 8), 100, width=1, fill="black")
        #     self.canvas.create_text(100 + (i * 8), 100, text=str(i), font=("Helvetica", 8))
