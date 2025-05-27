#import quiz question  file
from quiz_question import Question

#add class
class QuestionBuilder:
    #create questions
    def create_question(self):
        print("\nEnter a question.")
        question = input("Question: ")

        #add the choices
        choices = {}
        choices["a"] = input("Option a: ")
        choices["b"] = input("Option b: ")
        choices["c"] = input("Option c: ")
        choices["d"] = input("Option d: ")

        #check if all choices are filled
        while not all(choices[key] for key in ['a', 'b', 'c', 'd']):
            print("Please make sure all options are filled in.")
            choices['a'] = input("Option a: ")
            choices['b'] = input("Option b: ")
            choices['c'] = input("Option c: ")
            choices['d'] = input("Option d: ")

            #input the correct answer
        while True:
            answer = input("Correct answer (a/b/c/d): ").lower()
            if answer in choices:
                break
            else:
                print("Please choose a, b, c, or d.")

        return Question(question, choices, answer)

