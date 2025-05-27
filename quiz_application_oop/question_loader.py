#import package
from tkinter import messagebox

#add class
class QuestionLoader:
    def __init__(self, filename = "quiz_key.txt"):
        #assign file
        self.filename = filename

#load questions from the text file