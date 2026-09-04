
# # #=====================1========================
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# # ==================2========================
import random
import time
wins = 0
losses = 0
rounds = 0
score = 0
def flip_coin():
  user_input = input("Choose Heads or Tails: ").lower().strip()
  while user_input != "heads" and user_input != "tails":
    print("Invalid choice. Please choose Heads or Tails.")
    user_input = input("Choose Heads or Tails: ").lower().strip()  
  machine_output = random.choice(["Heads", "Tails"]).lower()
  print("Tossing the coin...")
  time.sleep(2)
  if user_input == machine_output:
    result = "won"
  else:
    result = "lost"
  return {"user": user_input,"computer": machine_output,"result": result}
def calculate_win_rate(wins, rounds):
  if rounds > 0:
    win_rate = wins/rounds * 100
    return win_rate
  else:
    print('No rounds played, so win rate is 0%.')
    return 0 
def calculate_loss_rate(losses, rounds):
  if rounds > 0:
    loss_rate = losses/rounds * 100
    return loss_rate
  else:
    print('No rounds played, so loss rate is 0%.')
    return 0 
def check_statistics(wins, losses, rounds):
  if wins + losses == rounds:
    return True
  else:
    return False  
def show_summary(wins, losses, rounds, score):
  check_stat = check_statistics(wins, losses, rounds)
  if check_stat:
    print("Statistics are correct!")
  else:
    print("Something is wrong with the statistics!")

  wrate = calculate_win_rate(wins, rounds)
  lrate = calculate_loss_rate(losses, rounds)
  print('========SUMMARY========')
  print(f'Round Played:{rounds}')
  print(f"wins: {wins}")
  print(f"losses: {losses}")
  print(f"Final score:{score}")
  print(f"Win Rate: {wrate:.2f}%")
  print(f"Loss Rate: {lrate:.2f}%")
  print('------------------------')
while True:
  game = flip_coin()
  print("You Pick:", game['user'])
  print("Computer Pick:", game["computer"])
  if game["result"] == "won":
    score += 1
    wins += 1
    rounds += 1
    print('You won! 🎉')
  else:
    losses += 1
    rounds += 1
    print('You lost! 😢')
  
  show_summary(wins, losses, rounds, score)
  
  another_try = input("Play again? ").lower().strip()
  while another_try != 'yes' and another_try != 'no':
    print('Please enter yes or no.')
    another_try = input('Play again? ').lower().strip()
  if  another_try == 'yes':
    continue
  elif another_try == 'no':
    print("Thanks for playing!")  
    break
# ======================3========================
import random
names = input("Enter two or more names(preceeding each name with ','): ").split(',')
while len(names) < 2:
    print('Enter at least two names.')
    names = input('Enter two or more names: ').split(',')
while True:
  if len(names) > 1: 
    person_to_pay = random.choice(names)
    print(f'{person_to_pay}, Sorry the bill is on You')
    break
  
  
  