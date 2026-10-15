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
def select_question():
    while True:
        try:
            user_choice = int(input("Enter the number of questions You want to answer:\n> "))
            if user_choice <= 0 or user_choice > len(questions):
                print("❌ Invalid Choice: Enter correct Number")
                continue
            else:
                break
        except ValueError:
            print("❌ Invalid Input")
    random.shuffle(questions)
    questions_to_be_answered = questions[:user_choice]
    return questions_to_be_answered
def display_questions(each_question):
    idx=0
    for each_options in each_question["options"]:
        idx+=1
        print(f"{idx}. {each_options}")
    print()
    
def get_answer(each_question):
    while True:
        try:
            chosen_option = int(input("Your answer: "))
            if chosen_option > len(each_question["options"]) or chosen_option < 1: 
                print("❌ Invalid Input")
                continue
            else:
                return chosen_option
            
        except ValueError:
            print("❌ Enter a valid number")
            
def validate_answer(each_question, user_answer):
    answer = each_question["options"].index(each_question["answer"]) + 1
    if user_answer == answer:
        print("Correct! 🎉\n")
        return True
    else:
        print("Wrong! ❌")
        print(f'The answer was "{each_question["answer"]}"\n')
        return False
def load_high_score():
    try:
        with open("highscore.txt", 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
def save_high_score(highest_score):
    with open("highscore.txt","w") as f:
        f.write(str(highest_score))
def main():
    highest_score = load_high_score()
    while True:
        score = 0
        no_of_question = 0
        print("Welcome to Trivia Quiz Game\n")
        user_quest = select_question()
        for each_question in user_quest:
            print(f'Question {no_of_question+1}/{len(user_quest)}')
            print(each_question["question"],"\n")
            random.shuffle(each_question["options"])
            display_questions(each_question)
            user_answer = get_answer(each_question)
            user = validate_answer(each_question, user_answer)
            no_of_question += 1
            if user:
                score +=1
        if score > highest_score:
            highest_score = score
        save_high_score(highest_score)
        print(f'Quiz finished!\nYour score: {score}/{no_of_question} ({score/no_of_question*100:.0f}%)\nHighest Score: {highest_score}\n')
        
        replay_or_not = input("Would you like to play again? (yes,y or no/n): ").lower().strip()
        
        while replay_or_not not in ["yes","y"] and replay_or_not not in ["no","n"]:
            print("❌ Invalid Input")
            replay_or_not = input("Would you like to play again? (yes,y or no/n): ").lower().strip()
        
        if replay_or_not in ["yes","y"]:
            print()
            continue
        elif replay_or_not in ["no","n"]:
            print(f'\nThanks for playing.\nYour highest score was: {highest_score}')
            break
main()


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