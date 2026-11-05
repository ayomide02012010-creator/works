from tool import flip_coin, show_summary, update_high_scores, load_high_scores
import csv
wins, losses, rounds, score = 0,0,0,0
history = []
high_scores = {}
high_scores = load_high_scores()
print("Welcome to coin flip game\n")
def greetings(name):
  return f"Welcome {name}\n"
name = input("Enter your name: ").capitalize().strip()
while name == "":
  print("\nName can't be Empty\n")
  name = input("Enter your name: ").capitalize().strip()
greeting = greetings(name)
print(greeting)
print("Select A Mode:   [A] Classic Mode     [B] Survival Mode")
chosen_mode = input("> ").strip().capitalize()
while chosen_mode not in ["A","B"]:
  print("Select the correct mode\n")
  print("Select A Mode:   [A] Classic Mode     [B] Survival Mode")
  chosen_mode = input("> ").strip().capitalize()
print()
if chosen_mode == 'A':
  round_to_be_played = input("Enter The Number Of You Round Want Play: ").strip()
  while not round_to_be_played.isdigit() or round_to_be_played == '0':
    print("❌ Invalid Number Of Rounds")
    round_to_be_played = input("Enter The Number Of You Want play: ").strip()
  for num_of_round in range(int(round_to_be_played)):
    game = flip_coin()
    history.append(f'Round {rounds + 1}: You Picked {game["user"]} | Computer picked {game["computer"]} | Result: {game["result"]}')
    print("You Pick:", game['user'])
    print("Computer Pick:", game["computer"])
    if game["result"] == "won":
      score += 1
      wins += 1
      rounds += 1
      print('You won! 🎉\n')
    else:
      losses += 1
      rounds += 1
      print('You lost! 😢\n')
  show_summary(wins, losses, rounds)
  print('HISTORY'.center(23, "="))
  for record in history:
    print(record)
  is_new_record = update_high_scores(high_scores, name, "classic", score, int(round_to_be_played))
  if is_new_record:
    print("🏆 New High Score!")
  else:
    print('High score not beaten')
elif chosen_mode == 'B':
  while True:
    game = flip_coin()
    history.append(f'Round {rounds + 1}: You Picked {game["user"]} | Computer picked {game["computer"]} | Result: {game["result"]}')
    print("You Pick:", game['user'])
    print("Computer Pick:", game["computer"])
    if game["result"] == "won":
      score += 1
      wins += 1
      rounds += 1
      print('You won! 🎉\n')
    else:
      losses += 1
      rounds += 1
      print('You lost! 😢')
      show_summary(wins, losses, rounds)
      print('HISTORY'.center(23, "="))
      for record in history:
        print(record)
      break
  is_new_record = update_high_scores(high_scores, name, "survival", score)
  if is_new_record:
    print("🏆 New High Score!")
  else:
    print('High score not beaten')