
# # #=====================1========================
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# # ==================2========================
from tool import flip_coin, show_summary
wins = 0
losses = 0
rounds = 0
score = 0
history = []

while True:
  game = flip_coin()
  history.append(f'Round {rounds + 1}: You Picked {game["user"]} | Computer picked {game["computer"]} | Result: {game["result"]}')
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
  
  show_summary(wins, losses, rounds)
  
  another_try = input("Play again? ").lower().strip()
  while another_try not in ['y', 'yes'] and another_try not in ['n','no']:
    print('Please enter yes or no.')
    another_try = input('Play again? ').lower().strip()
  if another_try in ['y', 'yes']:
    continue
  elif another_try in ['n', 'no']:
    print(f"\nThanks for playing!\nFinal score:{score}")
    print('=' * 8 + 'HISTORY' + '=' * 8)
    for record in history:
      print(record)
    break
  
# ======================3========================
# import random
# names = input("Enter two or more names(preceeding each name with ','): ").split(',')
# while len(names) < 2:
#     print('Enter at least two names.')
#     names = input('Enter two or more names: ').split(',')
# while True:
#   if len(names) > 1: 
#     person_to_pay = random.choice(names)
#     print(f'{person_to_pay}, Sorry the bill is on You')
#     break
  
  
  