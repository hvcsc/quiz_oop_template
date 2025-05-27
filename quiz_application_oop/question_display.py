#import tkinter
import tkinter as tk

#add class
class QuestionsDisplay:
    #define and assign
    def __init__(self, root, questions, on_answer_checked, on_next, on_pause, on_exit):
        self.root = root
        self.questions = questions
        self.question_index = 0
        self.score = 0
        self.is_paused = False

        self.on_answer_checked = on_answer_checked
        self.on_next = on_next
        self.on_pause = on_pause
        self.on_exit = on_exit

        self.answer_buttons = []

    #display of questions and options
    def show_question(self):
        self.clear_screen()

        if self.question_index >= len(self.questions):
            return False

        current_question = self.questions[self.question_index]

        self.top_frame = tk.Frame(self.root, bg = "#EAE0D5")
        self.top_frame.pack(expand = True)

        self.question_label = tk.Label(
            self.top_frame,
            text = current_question["question"],
            font = ("Times New Roman", 18),
            wraplength = 600,
            justify = "center",
            bg = "#EAE0D5",
            fg = "#22333B"
        )
        self.question_label.pack(pady = 10)

        self.answer_buttons.clear()
        for key in ['a', 'b', 'c', 'd']:
            btn = tk.Button(
                self.top_frame,
                text = f"{key}.{current_question['choices'][key]}",
                font = ("Times New Roman", 14),
                bg = "#C6AC8E",
                width = 40,
                command = lambda selected_key = key: self.check_answer(selected_key)
            )
            btn.pack(pady = 5)
            self.answer_buttons.append((key, btn))

            #control buttons on the bottom
            self.bottom_frame = tk.Frame(self.root, bg = "#EAE0D5")
            self.bottom_frame.pack(side = "bottom", pady = 20)

            self.pause_button = tk.Button(
                self.bottom_frame,
                text = "Pause",
                font = ("Times New Roman", 12),
                bg = "#C6AC8E",
                fg = "#0A0908",
                command = self.on_pause
            )
            self.pause_button.pack(side = "left", padx=20)

            self.next_button = tk.Button(
                self.bottom_frame,
                text = "Next",
                font = ("Times New Roman", 12),
                bg = "#C6AC8E",
                fg = "#0A0908",
                command = self.on_next,
                state = "disabled"
            )
            self.next_button.pack(side = "left", padx = 20)

            self.exit_button = tk.Button(
                self.bottom_frame,
                text = "Exit",
                font = ("Times New Roman", 12),
                bg = "#5E503F",
                fg = "white",
                command = self.on_exit
            )
            self.exit_button.pack(side = "right", padx = 20)

            return True

#check answer
#permission to proceed to the next question
#clear screen