#add class
class QuizManager:
    #define the text file
    def __init__(self, filename = "quiz_key.txt"):
        self.filename = filename
        self.questions = []

        #append questions
        def add_question(self, question):
            self.questions.append(question)

        #save inputs to file
        def save_to_file(self):
            with open(self.filename, "a") as file:
                for q in self.questions:
                    file.write(f"{q.text}\n")
                    file.write(f"a. {q.choices['a']}\n")
                    file.write(f"b. {q.choices['b']}\n")
                    file.write(f"c. {q.choices['c']}\n")
                    file.write(f"d. {q.choices['d']}\n")
                    file.write(f"answer: {q.answer}\n")
                    file.write("\n")
            print(f"\n{len(self.questions)} question/s saved to '{self.filename}'.")
