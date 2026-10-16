# names = ['Ali', "Ridwan", "Muhyideen", 'Taj', "Abdullah"]
# names[0] = "ALI"
# print(names[0:2])
# print(names)

# numbers = [1,2,3,4,5,6]
# for num in numbers:
#     print(num)
    
# i = 0
# while i < len(numbers):
#     print(numbers)
#     i = i + 1

# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# num3 = int(input('Enter number 3: '))
# num4 = int(input('Enter number 4: '))
# num5 = int(input('Enter number 5: '))

# all_nums = [num1, num2, num3, num4, num5]
# largest_num = all_nums[0]
# for number in all_nums[1:]:
#     if number > largest_num:
#         largest_num = number
        
# smallest_num = all_nums[0]
# for number in all_nums[1:]:
#     if number < smallest_num:
#         smallest_num = number

# sum_total = sum(all_nums)

# print("Largest: ", largest_num)
# print("Smallest: ", smallest_num)
# print("Total: ", sum_total)
# print(1/0)
# import random
# import time
# user_input = input("Choose a side of a coin: Heads or Tails: ")
# machine_output = random.choice(['Heads','Tails'])
# print('Tossing...')
# time.sleep(3)
# print("Computer Pick:", machine_output)

# if user_input != machine_output:
#     print("Oooops! U Guess wrongly")
# else:
#     print("CONGRATULATIONS!!! U WON")   



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