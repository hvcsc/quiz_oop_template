#import tkinter
import tkinter as tk

#add class
class PauseScreen:
    #defind and assign
    def __init__(self, root, resume_callback):
        self.root = root
        self.resume_callback = resume_callback

#pause and resume button
#clear screen