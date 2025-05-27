#import files
from question_builder import QuestionBuilder
from quiz_manager import QuizManager

#define imported files
def main():
    builder = QuestionBuilder()
    quiz = QuizManager()

    #ask if the user wants to add more question
    while True:
        question = builder.create_question()
        quiz.add_question(question)

        cont = input("Do you want to enter another question? (y/n): ").strip().lower()
        if cont != "y":
            print("Bye.")
            break

    #save and exit
    quiz.save_to_file()

if __name__ == "__main__":
    main()

