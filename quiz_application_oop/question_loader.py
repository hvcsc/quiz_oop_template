#import package
import os
from tkinter import messagebox

#add class
class QuestionLoader:
    def __init__(self):
        #assign file
        self.questions = []

#load questions from the text file
    def load_question(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "../quiz_creator_oop/quiz_key.txt")

        try:
            with open(file_path, "r") as file:
                content = file.read().strip().split("\n\n")
                for block in content:
                    lines = block.strip().split("\n")
                    question = lines[0]
                    choices = {
                        'a': lines[1][3:].strip(),
                        'b': lines[2][3:].strip(),
                        'c': lines[3][3:].strip(),
                        'd': lines[4][3:].strip()
                    }
                    answer = lines[5].split(":")[1].strip()
                    self.questions.append({
                        "question": question,
                        "choices": choices,
                        "answer": answer
                    })
        except FileNotFoundError:
            messagebox.showerror("Error", f"{self.filename} not found!")
        return self.questions