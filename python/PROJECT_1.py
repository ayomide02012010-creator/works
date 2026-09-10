import random
print('Welcome to the Number Guessing Game!')
def get_guess():
  while True:
    try:
      user_guess = int(input(f'Enter your guess: '))    
      return user_guess 
    except ValueError:
      print('Please enter a valid number.')
def choose_difficulty():
  difficulty_level = int(input('Select Difficulty: [1]Easy, [2]Medium, [3]Hard: '))
  if difficulty_level == 1:
    print("I'm thinking of a number between 1 and 50\nYou have 10 attempts.")
    return 50, 10
  elif difficulty_level == 2:
    print("I'm thinking of a number between 1 and 100\nYou have 7 attempts.")
    return 100, 7
  elif difficulty_level == 3:
    print("I'm thinking of a number between 1 and 200\nYou have 5 attempts.")
    return 200, 5
def generate_secret_number(maximum_number): 
    return random.choice(range(1, maximum_number+1))
def play_game():
    maximum_num, attempts = choose_difficulty()
    secret_num = generate_secret_number(maximum_num)
    while True:
        player_guess = get_guess()
        attempts -= 1
        score = attempts+1
        if player_guess == secret_num:
            print('Correct! 🎉')
            print(f'Score = {score}')
            break
        elif player_guess < secret_num :
            print('Too low! Try higher.')
            print(f'Attempts remaining: {attempts}')
        elif player_guess > secret_num :
            print('Too high! Try lower.')
            print(f'Attempts remaining: {attempts}')
        if attempts == 0:
            print(f'Game Over!\nThe number was {secret_num}.\nScore = {score - 1}')
            break
        
play_game()