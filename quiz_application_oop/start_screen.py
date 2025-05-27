#import tkinter
import tkinter as tk

#add class
class StartScreen:
    def __init__(self, root, start_callback):
        #assign
        self.root = root
        self.start_callback = start_callback

#define screen, title label, start button
    def show(self):
        self.clear_screen()
        frame = tk.Frame(self.root, bg = "#EAE0D5")
        frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        title_label = tk.Label(
            frame,
            text = "Object-Oriented Programming Quiz",
            font = ("Times New Roman", 24, "bold"),
            bg = "#EAE0D5",
            fg = "#22333B"
        )
        title_label.pack(pady = 20)

        start_button = tk.Button(
            frame,
            text = "Start",
            command = self.start_callback,
            font = ("Times New Roman", 16),
            bg = "#C6AC8E",
            fg = "#0A0908",
            width = 12
        )
        start_button.pack()

#clear screen