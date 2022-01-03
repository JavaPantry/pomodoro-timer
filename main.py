import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from utils.functions import resize_image
from views.calcFunctions import *
from views.constants import *
from views.configTab import *
from views.mainTab import *


def configUpdated(evt):
    print("in main.py: config updated event received configData = ",configPane.configData["workPeriod"], configPane.configData["breakPeriod"])

# *************************************************************
# ********         START UI          **************************
# *************************************************************

root = tk.Tk()
root.title("Time Tracker")
root.iconbitmap('./assets/logoTransp4icon24.ico')
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='asset/logoTransp.png'))
rootCanvas = tk.Canvas(root, width=600, height=300)
rootCanvas.grid(columnspan=1, rowspan=2)
logo = Image.open('./assets/logoTransp.png')
logo = resize_image(logo, 400, 400)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(rootCanvas, image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)


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