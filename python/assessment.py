import random
import time
user_input = input("Choose a side of a coin: Heads or Tails: ")
machine_output = random.choice(['Heads','Tails'])
print('Tossing...')
time.sleep(3)
print("Computer Pick:", machine_output)

if user_input != machine_output:
    print("Oooops! U Guess wrongly")
else:
    print("CONGRATULATIONS!!! U WON")    

#=====================1========================
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# ==================2========================
import random
import time        
def flip_coin():
  user_input = input("Choose Heads or Tails: ")
  print("Tossing the coin...")
  time.sleep(2)
  machine_output = random.choice(["Heads", "Tails"])
  user_input = user_input.lower()
  machine_output = machine_output.lower()
  print("Computer Pick:", machine_output)
  if user_input != "heads" and user_input != "tails":
    print("Invalid choice. Please choose Heads or Tails.")
  elif user_input == machine_output:
    print("You won!")
  else:
    print("You lost!")
while True:
  flip_coin()
  another_try = input("Play again? ")
  if another_try == "no":
    print('Thanks for playing!')
    break


    

    