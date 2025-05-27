#import files
import tkinter as tk
import random

from question_loader import QuestionLoader
from start_screen import StartScreen
from question_display import QuestionsDisplay
from pause_screen import PauseScreen
from score_screen import ScoreScreen

#add class
class QuizGame:
    #assign variables
    def __init__(self, root):
        self.root = root
        self.root.title("Object-Oriented Programming Quiz")
        self.root.geometry("700x500")
        self.root.config(bg="#EAE0D5")

        self.score = 0
        self.question_index = 0
        self.is_paused = False

        self.question_loader = QuestionLoader()
        self.questions = self.question_loader.load_questions()
        random.shuffle(self.questions)

        self.start_screen = StartScreen(self.root, self.start_quiz)
        self.question_display = None
        self.pause_screen = PauseScreen(self.root, self.resume_quiz)
        self.score_screen = None

        self.start_screen.show()
        
#start quiz function
#check answer
#next question
#pause and resume function
#show score on the screen
#main loop