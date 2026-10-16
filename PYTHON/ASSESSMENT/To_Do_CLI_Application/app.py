tasks = [
    {
        "title": "Learn python",
        "completed": True,
        "priority": "High",
        "due_date": "2026-10-07"
        },
    {
        "title": "Learn H.T.M.L",
        "completed": False,
        "priority": "medium",
        "due_date": "2026-10-09"
        },
    
    {
        "title": "python fundamentals",
        "completed": True,
        "priority": "High",
        "due_date": "2026-07-07"
        },
    {
        "title": "python built-in-functions",
        "completed": False,
        "priority": "High",
        "due_date": "2026-10-10"        
        }
]
def display_task():
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task["title"]}\n   Completed: {task["completed"]}\n   Priority: {task["priority"]}\n   Due date: {task["due_date"]}\n')
def add_task():
    while True:
        title = input("Enter your task Title: ").strip()
        if title == "":
            print("❌ Invalid Input")
            continue
        else:
            break
    while True:
        priority = input("Enter your Priority to the task(High, Medium, or Low): ").lower().strip()
        if priority == "" or priority not in ["high","medium","low"]:
            print("❌ Invalid Input: Please enter High, Medium, or Low")
            continue
        else:
            break
    while True:
        due_date = input("Enter the due date of your task: ").strip()
        if due_date == "":
            print("❌ Invalid Input")
            continue
        else:
            break
    task = {
        "title": title,
        "completed": False,
        "priority": priority,
        "due_date": due_date
        }
    tasks.append(task)
def complete_task():
    print("=" * 7 + "List Of Task" + "=" * 7)
    idx = 0
    for current_task in tasks:
        if current_task['completed'] == False:
            idx+=1
            print(f"{idx}. {current_task['title']} ❌")
        else:
            idx +=1
            print(f"{idx}. {current_task['title']}  ✅")      
    while True: 
        try:
            idx_task = int(input('Enter the number of task to complete: '))
            while idx_task <= 0 or idx_task > len(tasks):
                print("❌ Invalid Input: Enter a Valid Number")
                idx_task = int(input('Enter the number of task to complete: '))
        
            if tasks[idx_task-1]["completed"] == True:
                print(f"Task {idx_task} is already completed")
                return
            else:
                tasks[idx_task-1]['completed'] = True
                print(f"{idx_task}. {tasks[idx_task-1]['title']}  ✅")  
                return
        except ValueError:
            print("❌ Invalid Input")
    

def main():
    add_task()
    display_task()
    complete_task()

main()


#  import random, json
# questions = [
#     {
#         "question": "What is 2 + 2?",
#         "options": ["3", "4", "5", "6"],
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
# def select_question():
#     while True:
#         try:
#             user_choice = input("Select the number of questions You want to answer:\n> (a) 5 (b) 10 (c) 15 (d) 20 (e) 25 (f) 30\n>  ").lower().strip()
#             if user_choice not in ["a","b","c","d","e","f",]:
#                 print("❌ Invalid Choice: Enter correct option\n")
#                 continue
#             else:
#                 if user_choice == "a":
#                     return 5  
#                 elif user_choice == "b":
#                     return 10
#                 elif user_choice == "c":
#                     return 15
#                 elif user_choice == "d":
#                     return 20
#                 elif user_choice == "e":
#                     return 25
#                 else:
#                     return 30
#         except ValueError:
#             print("❌ Invalid Input")
            
# def display_option(each_question):
#     idx=0
#     for each_options in each_question["options"]:
#         idx+=1
#         print(f"{idx}. {each_options}")
#     print()
    
# def get_answer(each_question):
#     while True:
#         try:
#             chosen_option = int(input("Your answer: "))
#             if chosen_option > len(each_question["options"]) or chosen_option < 1: 
#                 print("❌ Invalid Input")
#                 continue
#             else:
#                 return chosen_option
            
#         except ValueError:
#             print("❌ Enter a valid number")
            
# def validate_answer(each_question, user_answer):
#     answer = each_question["options"].index(each_question["answer"]) + 1
#     if user_answer == answer:
#         print("Correct! 🎉\n")
#         return True
#     else:
#         print("Wrong! ❌")
#         print(f'The answer was "{each_question["answer"]}"\n')
#         return False
# def load_high_score():
#     try:
#         with open("highscore.json", 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}
#     except ValueError:
#         return {}
# def save_high_score(high_scores):
#     with open("highscore.json","w") as f:
#         json.dump(high_scores, f, indent=4)
# def main():
#     highest_score = load_high_score()
#     while True:
#         score = 0
#         no_of_question = 0
#         print("Welcome to Trivia Quiz Game\n")
#         user_quest = select_question()
#         random.shuffle(questions)
#         questions_to_be_answered = questions[:user_quest]
#         for each_question in questions_to_be_answered:
#             print(f'Question {no_of_question+1}/{user_quest}')
#             print(each_question["question"],"\n")
#             random.shuffle(each_question["options"])
#             display_option(each_question)
#             user_answer = get_answer(each_question)
#             user = validate_answer(each_question, user_answer)
#             no_of_question += 1
#             if user:
#                 score +=1
#         # if str(user_quest) in highest_score:
#         if score > highest_score[str(user_quest)]:
#             highest_score[str(user_quest)] = score
#         else:
#             highest_score[str(user_quest)] = highest_score[str(user_quest)]
#         # else:
#         #     highest_score[str(user_quest)] = score
#         high_scores = {"5": score,"10": score ,"15": score, "20": score, "25": score, "30": score}
#         save_high_score(high_scores)
#         print(f'Quiz finished!\nYour score: {score}/{no_of_question} ({score/no_of_question*100:.0f}%)\nHighest Score: {highest_score[str(user_quest)]}\n')
        
#         replay_or_not = input("Would you like to play again? (yes,y or no/n): ").lower().strip()
        
#         while replay_or_not not in ["yes","y"] and replay_or_not not in ["no","n"]:
#             print("❌ Invalid Input")
#             replay_or_not = input("Would you like to play again? (yes,y or no/n): ").lower().strip()
        
#         if replay_or_not in ["yes","y"]:
#             print()
#             continue
#         elif replay_or_not in ["no","n"]:
#             print(f'\nThanks for playing.\nYour highest score was: {highest_score[str(user_quest)]}')
#             break
# main()