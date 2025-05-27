#import tkinter
import tkinter as tk

#add class
class PauseScreen:
    #define and assign
    def __init__(self, root, resume_callback):
        self.root = root
        self.resume_callback = resume_callback

    #pause and resume button
    def show(self):
        self.clear_screen()
        pause_label = tk.Label(
            self.root,
            text = "Quiz Paused",
            font = ("Times New Roman", 20),
            bg = "#EAE0D5",
            fg = "#22333B"
        )
        pause_label.place(relx = 0.5, rely = 0.4, anchor = "center")

        resume_button = tk.Button(
            self.root,
            text = "Resume",
            font = ("Times New Roman", 14),
            bg = "#C6AC8E",
            fg = "#0A0908",
            command = self.resume_callback
        )
        resume_button.place(relx = 0.5, rely = 0.6, anchor = "center")

#clear screen