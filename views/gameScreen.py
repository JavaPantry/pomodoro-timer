import pygame
import os
import platform
import tkinter as tk
from PIL import Image, ImageTk

from .constants import *
from views.functions import resize_image

#*****************************
#** https://stackoverflow.com/questions/23319059/embedding-a-pygame-window-into-a-tkinter-or-wxpython-frame
#** https://stackoverflow.com/questions/55755305/im-embedding-a-pygame-window-into-tkinter-how-do-i-manipulate-the-pygame-windo
#      - see demo for this post in scrapbook\pygameTk.py
#*****************************

class GameScreen:

    def __init__(self, rootCanvas):
        # pygame
        # self.pygame_frame = tk.Frame(rootCanvas, width=514, height=514, highlightbackground='#595959', highlightthickness=2)
        self.embed = tk.Frame(rootCanvas, width = 500, height = 500) #creates embed frame for pygame window
        # self.embed.grid(columnspan = (600), rowspan = 500) # Adds grid
        # self.embed.pack(side = "left") #packs window to the left

        os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())
        if platform.system == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'

        #Start pygame
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        self.screen.fill(pygame.Color(255,0,0))
        pygame.display.init()
        pygame.display.update()
        pygame.draw.circle(self.screen, (0,0,0), (250,250), 125)
        pygame.display.update()
        # while True:
        #     pygame.display.update()
        #     rootCanvas.update()
