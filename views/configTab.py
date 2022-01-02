import tkinter as tk
from .constants import *


# ConfigTab
# configTab = tk.Frame(root, bg=BG_COLOR)
# configTab.grid(columnspan=3, column=0, row=0)

def createView(configTab): # = tk.Frame(root, bg=BG_COLOR)
    dummyConfigLabel1 = tk.Label(configTab, text="Dummy Config 1", font=LABEL_FONT)
    dummyConfigLabel1.grid(columnspan=3, column=0, row=3)
    dummyConfigLabel2 = tk.Label(configTab, text="Dummy Config 2", font=LABEL_FONT)
    dummyConfigLabel2.grid(columnspan=3, column=0, row=4)
    dummyConfigLabel3 = tk.Label(configTab, text="Dummy Config 3", font=LABEL_FONT)
    dummyConfigLabel3.grid(columnspan=3, column=0, row=5)
    dummyConfigLabel4 = tk.Label(configTab, text="Dummy Config 4", font=LABEL_FONT)
    dummyConfigLabel4.grid(columnspan=3, column=0, row=6)
