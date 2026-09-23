from utils import generate_secret_number
from utils import calculate_score

EASY_MAX = 50
EASY_ATTEMPTS = 10

MEDIUM_MAX = 100
MEDIUM_ATTEMPTS = 7

HARD_MAX = 200
HARD_ATTEMPTS = 5

EASY_MULTIPLIER = 1
MEDIUM_MULTIPLIER = 2
HARD_MULTIPLIER = 3


def get_guess(attempts_used, total_attempt):
  while True:
    try:
      user_guess = int(input(f'Attempt {attempts_used+1}/{total_attempt} - Enter your guess: '))    
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
        return EASY_MAX, EASY_ATTEMPTS, EASY_MULTIPLIER
      elif difficulty_level == 2:
        print("I'm thinking of a number between 1 and 100\nYou have 7 attempts.\n")
        return MEDIUM_MAX, MEDIUM_ATTEMPTS, MEDIUM_MULTIPLIER
      elif difficulty_level == 3:
        print("I'm thinking of a number between 1 and 200\nYou have 5 attempts.\n")
        return HARD_MAX, HARD_ATTEMPTS, HARD_MULTIPLIER
      else:
        print("Please choose 1, 2, or 3")
    except ValueError:
      print("Please choose 1, 2, or 3")
def show_summary(result, attempts_used, attempts_remaining, score):
  print("=" * 8 + 'GAME SUMMARY' + '=' * 8)
  print(f"Result: {result}")
  print(f"Attempts used: {attempts_used}")
  print(f"Attempts remaining: {attempts_remaining}")
  print(f"Score: {score}")
  print('=' * 14 + "=" * 14)
def play_game():
  print('Welcome to the Number Guessing Game!')
  maximum_num, max_attempts, difficulty_multiplier = choose_difficulty()
  total_attempts = max_attempts
  secret_num = generate_secret_number(maximum_num)
  attempts_used = 0
  while True:
    player_guess = get_guess(attempts_used, total_attempts)
    while player_guess > maximum_num or player_guess <= 0:
      print(f'Please enter a number between 1 and {maximum_num}')
      player_guess = get_guess(attempts_used, total_attempts)
    attempts_used += 1
    attempts_remaining = max_attempts - attempts_used
    score = calculate_score(max_attempts, attempts_used, difficulty_multiplier)
    if player_guess == secret_num:
      result = 'Won'
      print(f'🎉 Correct! You got it in {attempts_used} attempts!')
      print(f'Your score = {score}')
      break
    elif player_guess < secret_num :
      print('📉 Too low! Try higher.')
      print(f'Attempts remaining: {attempts_remaining}\n')  
    elif player_guess > secret_num :
      print('📈 Too high! Try lower.')
      print(f'Attempts remaining: {attempts_remaining}\n')
    if attempts_remaining == 0:
      result = 'Lost'
      print(f'Game Over!\nThe number was {secret_num}.\nYour Score = {score}\n')
      break
  show_summary(result, attempts_used, attempts_remaining, score)
  return result, attempts_used, attempts_remaining, score
while True:
  result, attempts_used, attempts_remaining, score = play_game()
  play_again = input('Play again? (y/n):').lower().strip()
  while play_again not in ['y','yes'] and play_again not in ['n','no']:
    print('Enter "y" or "n".')
    play_again = input('Play again? (y/n):').lower().strip()
  if play_again in ['y', 'yes']:
    continue
  elif play_again in ['n', 'no']:
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