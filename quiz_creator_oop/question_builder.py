#import quiz question  file
from quiz_question import Question

#add class
class QuestionBuilder:
    #create questions
    def create_question(self):
        print("\nEnter a question.")
        text = input("Question: ")

#add the choices
#check if all choices are filled
#input the correct answer
