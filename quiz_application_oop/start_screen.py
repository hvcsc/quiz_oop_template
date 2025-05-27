#import tkinter
import tkinter as tk

#add class
class StartScreen:
    def __init__(self, root, start_callback):
        #assign
        self.root = root
        self.start_callback = start_callback

#define screen, title label, start button
#clear screen