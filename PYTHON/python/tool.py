import random, csv,time 

def flip_coin():
  user_input = input("Choose a side of the coin: Heads or Tails: ").lower().strip()
  
  while user_input != "heads" and user_input != "tails":
    print("Invalid choice. Please choose Heads or Tails.")
    user_input = input("Choose a side of the coin: Heads or Tails: ").lower().strip()  
  
  print("\nTossing the coin".ljust(20, "."))
  time.sleep(2)
  
  machine_output = random.choice(["Heads","Tails"]).lower()
  
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
    print("\nStatistics are correct!\n")
  else:
    print("Something is wrong with the statistics!")

  wrate = calculate_win_rate(wins, rounds)
  lrate = calculate_loss_rate(losses, rounds)
  print('SUMMARY'.center(20, "="))
  print(f'Round Played:{rounds}')
  print(f"wins: {wins}")
  print(f"losses: {losses}")
  print(f"Win Rate: {wrate:.2f}%")
  print(f"Loss Rate: {lrate:.2f}%")
  print('-'.ljust(20, "-"))
  print()
  
def update_high_scores(high_score, name, mode, score, rounds=None):
  if mode == "classic":
    key = (name, mode, rounds)
  else:
    key = (name, mode)
    
  previous_score = high_score.get(key,0)
  if score > previous_score:
    high_score[key] = score
    save_high_scores(high_score)
    return True
  else:
    return False

def load_high_scores():
  high_scores = {}
  try:
    with open("high_scores.csv", mode="r", newline='') as scores_file:
      for high_score in csv.DictReader(scores_file):
        name = high_score["name"]
        mode = high_score["mode"]
        score = int(high_score["score"])
        if high_score["mode"] == "classic":
          rounds = int(high_score["rounds"])
          high_scores[(name, mode, rounds)] = score
        else:
          high_scores[(name, mode)] = score
      return high_scores
  except FileNotFoundError:
    return high_scores
  
def save_high_scores(high_scores):
  with open("high_scores.csv", mode="w", newline='') as scores_file:
    writer = csv.writer(scores_file)
    writer.writerow(["name","mode","rounds","score"])
    for high_score, value in high_scores.items():
      name = high_score[0]
      mode = high_score[1]
      if high_score[1] == "classic":
        rounds = high_score[2]
        score = value
      else:
        rounds = ''
        score = value
      writer.writerow([name,mode,rounds,score])