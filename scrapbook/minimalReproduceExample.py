import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Time Tracker")
root.iconbitmap('./assets/logoTransp4icon24.ico')
rootFrame = tk.Frame(root, width=600, height=300)
rootFrame.grid(columnspan=1, rowspan=2)
rootFrame.pack(expand=1, fill="both")

tabs = ttk.Notebook(rootFrame)
tabs.grid(column=0, row=1, columnspan=1, rowspan=1)

mainTab     = ttk.Frame(tabs)
mainTab.grid(columnspan=3, rowspan=6)

buttonFrame = tk.Frame(mainTab, bg="white")
buttonFrame.grid(column=0, row=4, columnspan=3, rowspan=1)
start_btn = tk.Button(buttonFrame, text="Start", command=lambda:self.start_timer(), font="Arial", bg="green", fg="white") # , height=1, width=14
start_btn.grid(column=0, row=0, columnspan=2)
reset_btn = tk.Button(buttonFrame, text="X", command=lambda:self.reset_timer(), font="Arial", bg="green", fg="white") # , height=1, width=1
reset_btn.grid(column=2, row=0)

timerDisplay = tk.Label(mainTab, text="00:00:00", font="Arial")
timerDisplay.grid(columnspan=2, column=1, row=4)

tabs.add(mainTab, text="Main")

rootFrame.pack(expand=1, fill="both")

root.mainloop()