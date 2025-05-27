#add class
class QuizManager:
    #define the text file
    def __init__(self, filename = "quiz_key.txt"):
        self.filename = filename
        self.questions = []

#append questions
#save inputs to file