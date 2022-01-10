import tkinter as tk
from PIL import Image, ImageTk

from .constants import *
from views.functions import resize_image


class Logo:

    def __init__(self, rootCanvas):
        logo = Image.open('./assets/logoTransp.png')
        logo = resize_image(logo, 200, 200)
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(rootCanvas, image=logo)
        logo_label.image = logo
        logo_label.grid(column=0, row=0)
