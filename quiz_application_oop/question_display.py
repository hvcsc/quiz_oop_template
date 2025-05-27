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
#control buttons on the bottom
#check answer
#permission to proceed to the next question
#clear screen