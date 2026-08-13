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
  convert_another_try = another_try.lower()
  if convert_another_try == "no":
    print('Thanks for playing!')
    break


names = ['Ali', "Ridwan", "Muhyideen", 'Taj', "Abdullah"]
names[0] = "ALI"
print(names[0:2])
print(names)

numbers = [1,2,3,4,5,6]
for num in numbers:
    print(num)
    
i = 0
while i < len(numbers):
    print(numbers)
    i = i + 1

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))
num4 = int(input('Enter number 4: '))
num5 = int(input('Enter number 5: '))

all_nums = [num1, num2, num3, num4, num5]
largest_num = all_nums[0]
for number in all_nums[1:]:
    if number > largest_num:
        largest_num = number
        
smallest_num = all_nums[0]
for number in all_nums[1:]:
    if number < smallest_num:
        smallest_num = number

sum_total = sum(all_nums)

print("Largest: ", largest_num)
print("Smallest: ", smallest_num)
print("Total: ", sum_total)
print(1/0)

