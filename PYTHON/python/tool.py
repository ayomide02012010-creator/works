import random
import time

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
  
  return {"user": user_input,"computer": machine_output,"result": result }

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

def show_summary(wins, losses, rounds):
  check_stat = check_statistics(wins, losses, rounds)
  if check_stat:
    print("Statistics are correct!\n")
  else:
    print("Something is wrong with the statistics!")

  wrate = calculate_win_rate(wins, rounds)
  lrate = calculate_loss_rate(losses, rounds)
  print('=' * 8 + 'SUMMARY' + '=' * 8)
  print(f'Round Played:{rounds}')
  print(f"wins: {wins}")
  print(f"losses: {losses}")
  print(f"Win Rate: {wrate:.2f}%")
  print(f"Loss Rate: {lrate:.2f}%")
  print('------------------------')