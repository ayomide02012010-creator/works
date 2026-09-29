from lip import choose_difficulty, generate_secret_number, get_guess

def play_game(): 
  print('Welcome to the Number Guessing Game!') 
  
  maximum_num, attempts = choose_difficulty() 
  total_attempts = attempts 
  secret_num = generate_secret_number(maximum_num) 
  Attempt = 1
   
  while True:

    player_guess = get_guess(Attempt, total_attempts) 
    Attempt += 1 
    attempts -= 1 
    score = attempts
    if player_guess > maximum_num or player_guess <= 0:
      print(f'Please enter a number between 1 and {maximum_num}')
      continue 

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
def main():
    while True:
        play_game()
        play_again = input('Play again? (y/n):').lower().strip() 
        if play_again in ['y', 'yes']:
          continue
        else: 
          print('Thanks for playing!')
          return
main()
