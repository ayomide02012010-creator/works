import random, json
def select_question(questions):
    while True:
        
        user_choice = input("Select the number of questions You want to answer:\n> (a) 5 (b) 10 (c) 15 (d) 20 (e) 25 (f) 30 (g) Any\n>  ").lower().strip()
        if user_choice not in ["a","b","c","d","e","f","g"]:
            print("❌ Invalid Choice: Enter correct option\n")
            continue
        else:
            if user_choice == "a":
                return 5  
            elif user_choice == "b":
                return 10
            elif user_choice == "c":
                return 15
            elif user_choice == "d":
                return 20
            elif user_choice == "e":
                return 25
            elif user_choice == "f":
                return 30
            else:
                while True:
                    try:
                        any_choice = int(input("Enter the number of question you want to answer: "))
                        if any_choice < 1 or any_choice > len(questions):
                            print("❌ Invalid number of question")
                            continue
                        else:
                            break
                    except ValueError:
                        print("❌ Invalid Input: you Enterd Letters instead of Numbers")
                return any_choice
        
def display_option(each_question):
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
        print(f'The answer was: {each_question["answer"]}\n')
        return False
def load_high_score():
    try:
        with open("highscore.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except ValueError:
        return {}
def save_high_score(high_scores):
    with open("highscore.json","w") as f:
        json.dump(high_scores, f, indent=4)
        
def load_quest():
    with open("questions/python.json", encoding="utf-8") as file:
        return json.load(file)
def main():
    questions = load_quest()
    highest_score = load_high_score()
    while True:
        score = 0
        no_of_question = 0
        print("Welcome to Trivia Quiz Game\n")
        user_quest = select_question(questions)
        questions_to_be_answered = random.sample(questions, user_quest)
        for each_question in questions_to_be_answered:
            print(f'Question {no_of_question+1}/{user_quest}')
            print(each_question["question"],"\n")
            random.shuffle(each_question["options"])
            display_option(each_question)
            user_answer = get_answer(each_question)
            user = validate_answer(each_question, user_answer)
            no_of_question += 1
            if user:
                score += 1
        if str(user_quest) in highest_score:
            if score > highest_score[str(user_quest)]:
                highest_score[str(user_quest)] = score
        else:
            highest_score[str(user_quest)] = score
        
        save_high_score(highest_score)
        print(f'Quiz finished!\nYour score: {score}/{no_of_question} ({score/no_of_question*100:.0f}%)\nHighest Score: {highest_score[str(user_quest)]}\n')
        
        replay_or_not = input("Would you like to play again? (yes,y or no/n): ").lower().strip()
        
        while replay_or_not not in ["yes","y"] and replay_or_not not in ["no","n"]:
            print("❌ Invalid Input")
            replay_or_not = input("Would you like to play again? (yes,y or no/n): ").lower().strip()
        
        if replay_or_not in ["yes","y"]:
            print()
            continue
        elif replay_or_not in ["no","n"]:
            print(f'\nThanks for playing.\nThe highest score for {user_quest} Question is: {highest_score[str(user_quest)]}')
            break
main()
