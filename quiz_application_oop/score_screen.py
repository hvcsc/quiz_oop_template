#import tkinter
import tkinter as tk

#add class
class ScoreScreen:
    #define and assign
    def __init__(self, root, score, total_questions, restart_callback, exit_callback):
        self.root = root
        self.score = score
        self.total_questions = total_questions
        self.restart_callback = restart_callback
        self.exit_callback = exit_callback

    #congratulatory message, score, restart, and exit button display
    def show(self):
        self.clear_screen()
        frame = tk.Frame(self.root, bg = "#EAE0D5")
        frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        congrats_label = tk.Label(
            frame,
            text = "Congratulations!",
            font = ("Times New Roman", 22, "bold"),
            bg = "#EAE0D5",
            fg = "#22333B"
        )
        congrats_label.pack(pady = 10)

        score_label = tk.Label(
            frame,
            text = f"Score: {self.score}/{self.total_questions}",
            font = ("Times New Roman", 18),
            bg = "#EAE0D5",
            fg = "#22333B"
        )
        score_label.pack(pady = 5)

        restart_button = tk.Button(
            frame,
            text = "Restart",
            font = ("Times New Roman", 14),
            bg = "#C6AC8E",
            fg = "#0A0908",
            command = self.restart_callback
        )
        restart_button.pack(pady = 10)

        exit_button = tk.Button(
            frame,
            text = "Exit",
            font = ("Times New Roman", 14),
            bg = "#5E503F",
            fg = "white",
            command = self.exit_callback
        )
        exit_button.pack()

    #clear screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()