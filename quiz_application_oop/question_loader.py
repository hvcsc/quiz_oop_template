#import package
from tkinter import messagebox

#add class
class QuestionLoader:
    def __init__(self, filename = "quiz_key.txt"):
        #assign file
        self.filename = filename

#load questions from the text file
    def load_question(self):
        questions = []
        try:
            with open(self.filename, "r") as file:
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
                    questions.append({
                        "question": question,
                        "choices": choices,
                        "answer": answer
                    })
        except FileNotFoundError:
            messagebox.showerror("Error", f"{self.filename} not found!")
        return questions