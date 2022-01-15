import tkinter as tk
import time
from .constants import *
from .calcFunctions import *

class DigitalClock:

    def __init__(self, root):
        self.root = root
        self.mainDisplay = tk.Label(root, text=convertSec(0), font=MAIN_DISPLAY_FONT)
        self.mainDisplay.grid(columnspan=3, column=0, row=0)
        self.update()

    def update(self):
        # draw the clock face
        self.mainDisplay.config(text=time.strftime("%H:%M:%S"))
        # call the update method again after 1 second
        self.root.after(1000, self.update)

