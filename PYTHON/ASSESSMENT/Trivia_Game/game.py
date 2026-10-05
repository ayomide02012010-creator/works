# questions = [
#     {
#         "question": "What is 2 + 2?",
#         "options": ["3", "4", "5", "6","7","8"],
#         "answer": "4" 
#     },
#     {
#         "question": "____ is the perfect first programming language",
#         "options": ["JavaScript","Java",".net","python"],
#         "answer": "python"
#     },
#     {
#         "question": "What is the primary function of the CPU in a computer?",
#         "options": ["To connect to the internet","To display images on the screen","To perform arithmetic and logical operations on data","To store data permanently"],
#         "answer": "To perform arithmetic and logical operations on data"
#     },
#     {
#         "question": "What is one common challenge beginners face when learning Python?",
#         "options": ["Understanding indentation and its role in Python syntax","Writing code without using any variables","Configuring Python to run on a quantum computer","Memorizing all Python libraries"],
#         "answer": "Understanding indentation and its role in Python syntax" 
#     },
#     {
#         "question": "2+10=?", 
#         "options": ["12","13","34","3"],
#         "answer": "12"
#     }
# ]
# score = 0
# no_of_question = 0

# for each_question in questions:
#     idx=0 
#     print(each_question["question"],"\n")
#     for each_options in each_question["options"]:
#         idx+=1
#         print(f"{idx}. {each_options}")
#     chosen_option = input("Your answer: ") 
#     while chosen_option > str(len(each_question["options"])) or chosen_option < '1' :
#         print("❌ Invalid Input")
#         chosen_option = input("Your answer: ")
#     no_of_question+=1   
#     answer = list(each_question["options"]).index(each_question["answer"]) + 1
#     if chosen_option == str(answer):
#         score += 1
#         print("Correct! 🎉")
#     elif chosen_option != str(answer):
#         print("Wrong! ❌")
#     if len(questions) == no_of_question:
#         print(f'Quiz finished!\nYour score: {score}/{no_of_question}')
#         break
#     print()
import random
questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4" 
    },
    {
        "question": "____ is the perfect first programming language",
        "options": ["JavaScript","Java",".net","python"],
        "answer": "python"
    },
    {
        "question": "What is the primary function of the CPU in a computer?",
        "options": ["To connect to the internet","To display images on the screen","To perform arithmetic and logical operations on data","To store data permanently"],
        "answer": "To perform arithmetic and logical operations on data"
    },
    {
        "question": "What is one common challenge beginners face when learning Python?",
        "options": ["Understanding indentation and its role in Python syntax","Writing code without using any variables","Configuring Python to run on a quantum computer","Memorizing all Python libraries"],
        "answer": "Understanding indentation and its role in Python syntax" 
    },
    {
        "question": "2+10=?", 
        "options": ["12","13","34","3"],
        "answer": "12"
    }

]
score = 0
no_of_question = 0
random.shuffle(questions)
def display_questions(questions):
    for each_question in questions:
        idx=0 
        print(each_question["question"],"\n")
        for each_options in each_question["options"]:
            idx+=1
            print(f"{idx}. {each_options}")
    for each_question in questions:
        return each_question
def get_answer(each_question):
    each_question = display_questions()
    while True:
        try:
            chosen_option = int(input("Your answer: "))
            if chosen_option > len(each_question["options"]) or chosen_option < 1: 
                print("❌ Invalid Input")
                continue
            else:
                return chosen_option
            
        except ValueError:
            print("❌ Write a valid number")
def validate_answer(each_question, user_answer):
    global score, no_of_question
    user_answer = get_answer()
    each_question = display_questions()
    no_of_question += 1   
    answer = each_question["options"].index(each_question["answer"]) + 1
    if user_answer == answer:
        score += 1
        print("Correct! 🎉")
    else:
        print("Wrong! ❌")
    if len(questions) == no_of_question:
        print()
        print(f'Quiz finished!\nYour score: {score}/{no_of_question}')
        
def main():
    each_question = display_questions(questions)
    user_answer = get_answer(each_question)
    validate_answer(each_question, user_answer)
    
main()