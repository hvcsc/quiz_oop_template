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
    def start_quiz(self):
        self.score = 0
        self.question_index = 0
        self.is_paused = False

        self.question_display = QuestionsDisplay(
            self.root,
            self.questions,
            self.on_answer_checked,
            self.next_question,
            self.toggle_pause,
            self.root.quit
        )
        self.question_display.show_question()

    #check answer
    def on_answer_checked(self, correct):
        if correct:
            self.score += 1

    #next question
    def next_question(self):
        has_next = self.question_display.next_question()
        if not has_next:
            self.show_score()

    #pause and resume function
    def toggle_pause(self):
        if self.is_paused:
            self.is_paused = False
            self.question_display.is_paused = False
            self.question_display.show_question()
        else:
            self.is_paused = True
            self.question_display.is_paused = True
            self.pause_screen.show()

    def resume_quiz(self):
        self.is_paused = False
        self.question_display.is_paused = False
        self.question_display.show_question()

    #show score on the screen
    def show_score(self):
        self.score_screen = ScoreScreen(
            self.root,
            self.score,
            len(self.questions),
            self.start_quiz,
            self.root.quit
        )
        self.score_screen.show()

#main loop