
import random 
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
      else: print("Please choose 1, 2, or 3") 
    except ValueError: 
      print("Please choose 1, 2, or 3") 

def generate_secret_number(maximum_number): 
  return random.choice(range(1, maximum_number+1))
