from utils import generate_secret_number
from utils import calculate_score
def get_guess(Attempt, total_attempt):
  while True:
    try:
      user_guess = int(input(f'Attempt {Attempt}/{total_attempt} - Enter your guess: '))    
      return user_guess 
    except ValueError:
      print('Please enter a valid number.\n')
def choose_difficulty():
  while True:
    try:
      difficulty_level = int(input('Select Difficulty: [1]Easy, [2]Medium, [3]Hard:\n> '))
      print()
      if difficulty_level == 1:
        print("I'm thinking of a number between 1 and 50\nYou have 10 attempts.\n")
        return 50, 10
      elif difficulty_level == 2:
        print("I'm thinking of a number between 1 and 100\nYou have 7 attempts.\n")
        return 100, 7
      elif difficulty_level == 3:
        print("I'm thinking of a number between 1 and 200\nYou have 5 attempts.\n")
        return 200, 5
      else:
        print("Please choose 1, 2, or 3")
    except ValueError:
      print("Please choose 1, 2, or 3")
def play_game():
  print('Welcome to the Number Guessing Game!')
  maximum_num, attempts = choose_difficulty()
  total_attempts = attempts
  secret_num = generate_secret_number(maximum_num)
  Attempt = 1
  while True:
    player_guess = get_guess(Attempt, total_attempts)
    while player_guess > maximum_num or player_guess <= 0:
      print(f'Please enter a number between 1 and {maximum_num}')
      player_guess = get_guess(Attempt, total_attempts)
    Attempt += 1
    attempts -= 1
    score = calculate_score(attempts)
    if player_guess == secret_num:
        print(f'🎉 Correct! You got it in {Attempt-1} attempts!')
        print(f'Your score = {score}')
        break
    elif player_guess < secret_num :
      print('📉 Too low! Try higher.')
      print(f'Attempts remaining: {attempts}\n')  
    elif player_guess > secret_num :
      print('📈 Too high! Try lower.')
      print(f'Attempts remaining: {attempts}\n')
    if attempts == 0:
        print(f'Game Over!\nThe number was {secret_num}.\nYour Score = {score}\n')
        break
while True:
  play_game()
  play_again = input('Play again? (y/n):').lower().strip()
  while play_again != 'y' and play_again != 'n':
    print('Enter "y" or "n".')
    play_again = input('Play again? (y/n):').lower().strip()
  if play_again == 'y':
    continue
  elif play_again == 'n':
    print('Thanks for playing!')
    break

# import random 
# def get_guess(Attempt, total_attempt): 
#   while True:
#     try: 
#       user_guess = int(input(f'Attempt {Attempt}/{total_attempt} - Enter your guess: ')) 
#       return user_guess 
#     except ValueError: 
#       print('Please enter a valid number.\n')

# def choose_difficulty(): 
#   while True:
#     try: 
#       difficulty_level = int(input('Select Difficulty: [1]Easy, [2]Medium, [3]Hard:\n> ')) 
#       print() 
#       if difficulty_level == 1: 
#         print("I'm thinking of a number between 1 and 50\nYou have 10 attempts.\n") 
#         return 50, 10 
#       elif difficulty_level == 2: 
#         print("I'm thinking of a number between 1 and 100\nYou have 7 attempts.\n") 
#         return 100, 7 
#       elif difficulty_level == 3: 
#         print("I'm thinking of a number between 1 and 200\nYou have 5 attempts.\n") 
#         return 200, 5 
#       else: print("Please choose 1, 2, or 3") 
#     except ValueError: 
#       print("Please choose 1, 2, or 3") 

# def generate_secret_number(maximum_number): 
#   return random.choice(range(1, maximum_number+1))

# def play_game(): 
#   print('Welcome to the Number Guessing Game!') 
#   maximum_num, attempts = choose_difficulty() 
#   total_attempts = attempts 
#   secret_num = generate_secret_number(maximum_num) 
#   Attempt = 1 
#   while True: 
#     player_guess = get_guess(Attempt, total_attempts) 
#     if player_guess > maximum_num or player_guess <= 0:
#       print(f'Please enter a number between 1 and {maximum_num}')
#       continue
#       # player_guess = get_guess(Attempt, total_attempts) 
#     Attempt += 1 
#     attempts -= 1 
#     score = attempts 
#     if player_guess == secret_num: 
#       print(f'🎉 Correct! You got it in {Attempt-1} attempts!') 
#       print(f'Your score = {score}') 
#     elif player_guess < secret_num : 
#       print('📉 Too low! Try higher.') 
#       print(f'Attempts remaining: {attempts}\n') 
#       continue
#     elif player_guess > secret_num : 
#       print('📈 Too high! Try lower.') 
#       print(f'Attempts remaining: {attempts}\n')
#       continue
#     if attempts == 0: 
#       print(f'Game Over!\nThe number was {secret_num}.\nYour Score = {score}\n')  

#     play_again = input('Play again? (y/n):').lower().strip() 
#     if play_again in ['y', 'yes']:
#       play_game()
#     else: 
#       print('Thanks for playing!')
#       return


# play_game()