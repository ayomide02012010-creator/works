
# # #=====================1========================
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# # ==================2========================
# import random
# import time
# score = 0
# wins = 0
# losses = 0
# rounds = 0

# def flip_coin():
#   user_input = input("Choose Heads or Tails: ").lower().strip()
#   while user_input != "heads" and user_input != "tails":
#     print("Invalid choice. Please choose Heads or Tails.")
#     user_input = input("Choose Heads or Tails: ").lower().strip()  
#   machine_output = random.choice(["Heads", "Tails"]).lower()
#   print("Tossing the coin...")
#   time.sleep(2)
#   if user_input == machine_output:
#     result ="won"
#   else:
#     result = "lost"
#   return {"user": user_input,"computer": machine_output,"result": result}
# def calculate_win_rate(wins, rounds):
#   if rounds > 0:
#     win_rate = wins/rounds * 100
#     return win_rate
#   else:
#     print('No rounds played, so win rate is 0%.')
#     return 0 
  
# while True:
#   game = flip_coin()
#   print("You Pick:", game['user'])
#   print("Computer Pick:", game["computer"])
#   if game["result"] == "won":
#     score += 1
#     wins += 1
#     rounds += 1
#     print('You won! 🎉')
#     print(f'Score:{score}')
#   else:
#     rounds += 1
#     losses += 1
#     print('You lost! 😢')
#     print(f'Score:{score}')
    
#   another_try = input("Play again? ")
#   convert_another_try = another_try.lower().strip()
  
#   while convert_another_try != 'yes' and convert_another_try != 'no':
#     print('Please enter yes or no.')
#     convert_another_try = input('Play again? ').lower().strip()
#   if  convert_another_try == 'yes':
#     continue
#   elif convert_another_try == 'no':
#     rate = calculate_win_rate(wins, rounds)
#     print("Thanks for playing!")
#     print('========SUMMARY========')
#     print(f'Round Played:{rounds}')
#     print(f"wins: {wins}")
#     print(f"losses: {losses}")
#     print(f"Final score:{score}")
#     print(f"Win Rate: {rate:.2f}%")
#     print('------------------------')
#     break
# ======================3========================
import random
names = input('Enter two or more names: ').split(',')
ls = names.split(',')
while len(ls) < 2:
    print('Enter at least two names.')
    names = input('Enter two or more names: ') 
    ls = names.split(',')
while True:
  if len(ls) > 1: 
    person_to_pay = random.choice(ls)
    print(f'{person_to_pay}, Sorry the bill is on You')
    break
  
  
  