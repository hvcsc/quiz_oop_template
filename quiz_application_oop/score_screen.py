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
#clear screen