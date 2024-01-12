import random

def display_intro():
    print("Welcome to the Quiz Game!")
    print("Answer each question by entering the number of your choice.")
    print("-----------------------------------------------")

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    user_answer = get_user_input(len(options))
    
    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}: {options[correct_answer - 1]}\n")
        return 0

def get_user_input(max_value):
    while True:
        try:
            user_input = int(input(f"Enter your answer (1-{max_value}): "))
            if 1 <= user_input <= max_value:
                return user_input
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz():
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Paris', 'Berlin', 'Rome', 'Madrid'],
            'correct_answer': 1
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
            'correct_answer': 1
        },
        {
            'question': 'What is the largest mammal?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 2
        }
    ]

    total_score = 0

    display_intro()

    for i, question_data in enumerate(questions, 1):
        question = question_data['question']
        options = question_data['options']
        correct_answer = question_data['correct_answer']

        print(f"Question {i}:")
        total_score += ask_question(question, options, correct_answer)

    print(f"Quiz completed! Your final score is {total_score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
