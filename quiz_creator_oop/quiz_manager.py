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