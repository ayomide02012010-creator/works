import random
print('Welcome to the Number Guessing Game!')
def get_guess():
  while True:
    try:
      user_guess = int(input('Guess a Number: '))    
      return user_guess 
    except ValueError:
      print('Please enter a valid number.')
def choose_difficulty():
  difficulty_level = int(input('Select Difficulty: [1]Easy, [2]Medium, [3]Hard: '))
  if difficulty_level == 1:
    return 50, 10
  elif difficulty_level == 2:
    return 100, 7
  elif difficulty_level == 3:
    return 200, 5
def generate_secret_number(maximum_number): 
    return random.choice(range(1, maximum_number+1))
def play_game():
    maximum_num, attempts = choose_difficulty()
    secret_num = generate_secret_number(maximum_num)
    while True:
        player_guess = get_guess()
        attempts -= 1
        if player_guess == secret_num:
            print('Correct! 🎉')
            break
        elif player_guess < secret_num :
            print('Too low!')
        elif player_guess > secret_num :
            print('Too high!')
            
        if attempts == 0:
            break
play_game()