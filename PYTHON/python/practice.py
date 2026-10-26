# square = lambda x : x**2

# file = open("demofile.txt", "wt")
# number = (int(input("Enter A Number: ")))
# result = square(number)

# file.write(str(result))


# import random, string

# def gen_password(lent=8):
#     if lent < 8:
#         return "Password not Allowed"
    
#     # uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" lowercase_letter = "abcdefghijklmnopqrstuvwxyz" digit_num = "0123456789" special_char = "!@#$"
    
#     uppercase = random.choice(string.ascii_uppercase)
#     lowercase = random.choice(string.ascii_lowercase)
#     digit = random.choice(string.digits)
#     special_character = random.choice(string.punctuation)
    
#     password = uppercase + lowercase + digit + special_character 
    
#     all = string.ascii_lowercase + string.ascii_lowercase + string.digits + string.punctuation
#     other = len(all) - len(password)
    
#     convert_other = str(other)
#     random.choice(str(convert_other))
#     password += convert_other
    
#     result = ""
#     result += password
#     # final_result = random.shuffle(result)
#     return result
    
# print(gen_password()) 
# print(gen_password(12))              
# first = float(input("First: "))
# second = float(input("Second: "))                                         # numbers = [7, 2, 15, 4, 10]
# summ = str(first + second)#                                               # largest = numbers[0]
# print('Sum: ' + summ) #                                                   # for number in numbers[1:]: 
#                                                                           #     if number > largest:
# course = 'Python For Begginers'                                           #          largest = number
# course = course.upper()                                                   #          print(largest)
# print(course) #
# print(course.find("R")) #
# course = course.lower()
# print(course) #
# print(course.find("y")) #                                                         # in python we have three logical operators
# print(course.replace("for", '4'))  #                                              # and (both meet the condition e.g (false false) (true true))                                                                                      #                                                                                      #
# print("python" in course) #                                                       # or (at least one meet the requirement)
# print(10 + 5,10 - 5,10 * 5,10 / 5,10 // 5,10 % 3,10 ** 3) #                       # not (it inverses any value we give it)
# x = (10+3)*2
# print(x) #
# price = 70
# print(price > 60 and price < 80) #True
# price = 55
# print(price > 60 and price < 80) #False
# price = 70
# print(price > 60 or price < 80) # True
# price = 55
# print(price > 60 or price < 80)  # True
# price = 70
# print(not price > 90)

# # IF STATEMENT IN PHYTON

# temprature = 45

# if temprature > 50:
#     print("It's a hot day")
#     print('Drink plenty of H2O')
# elif temprature > 20:
#     print("It A Nice Day")
# elif temprature > 10:
#     print("It a bit cold")
# else:
#     print("It's cold ")        
# print('Done')
# # WHILE LOOPS                                                               # EXERSICE
# number = 1                                                                  # weight_in_numbers = float(input("Weight: "))
# while number <= 20:                                                          # weight_in_kilogram_or_pounds = input("Kg or lb: ")
#     print(number * '*')                                                      
#     number = number + 1                                                     # if weight_in_kilogram_or_pounds == "Kg":
# with open('workfile', encoding="utf-8") as f:
#     read_data = f.read()
# f.closed                                                                           # conversion = weight_in_numbers * 2.2
#                                                                             # conversion1 = str(conversion)
                                                                            # print("weight in pound: " + conversion1 +'lb')
                                                                            # elif weight_in_kilogram_or_pounds == "lb":
                                                                            # conversion = weight_in_numbers * 0.45
                                                                            # conversion1 = str(conversion)
                                                                            # print("weight in kilogram: " + conversion1 + 'kg')
    

# def my_sum(*args):
#     result = 0
#     for param in args:
#         result += param
#     return result

# print(my_sum( 10, 20, 30, 40, 50, 60, 70, 80))

# list1 =[1, 2, 3]
# list2 =[4, 5, 6]

# result = [*list1, 'Go', *list2]
# # result = [*[1, 2, 3], 'Go', *[4, 5, 6]] the work of the '*' is to unpack the list. so it becomes -> [1, 2, 3, 'Go', 4, 5, 6]
# print(result)
# name = input('Enter your name:')
# year_born = input('Year you born:')
# age = 2026 - int(year_born)
# print(f'You are {name}. And your age is {age}.')
# print(abs(complex(2+3j)))
# print(abs(complex(-2+3j)))
# from fractions import Fraction
# print(abs(Fraction("1/2")))
# print(abs(Fraction("-1/2")))
# print(abs(Fraction("1/2")))




# name = input('Enter file:')
# handle = open(name)
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#       counts[word] = counts.get(word, 0) + 1  
# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)
# # An asynchronous generator function acts as an async iterable/iterator
# async def news_feed():
#     for i in range(1, 4):
#         await asyncio.sleep(1)  # Simulates a non-blocking I/O delay
#         yield f"News item {i}"

# async def main():
#     # Consuming the async iterable using async for
#     async for news in news_feed():
#         print(news)

# asyncio.run(main())

# import asyncio
# from codetiming import Timer

# async def run_task(name, duration):
#     print(f'\tTask started: {name}')
#     timer = Timer(text=f"\tTask finished: '{name}' took {{:.1f}}")
#     timer.start()
    
#     await asyncio.sleep(duration)
#     timer.stop()
#     return name

# TASK_LIST = [('Start laptop', 10), ('Make coffee', 3), ("open percel", 3)]

# async def main():
#     main_timer = Timer(text=f'\nTotal time: {{:.1f}}')
#     main_timer.start()
    
#     await asyncio.gather(
#         run_task(*TASK_LIST[0]), run_task(*TASK_LIST[1]), run_task(*TASK_LIST[2])
#     )
#     main_timer.stop()
    
# if __name__ == "__main__":
#     asyncio.run(main())

# # import asyncio
# async def async_numbers():
#     for i in range(1, 11):
#         await asyncio.sleep(2) # Simulate an async taskif __name__ == "__main__":
#         yield i

# async def main():
#     async for number in aiter(async_numbers()):
#         print(number)

# asyncio.run(main())

# import asyncio

# # asynchronous generator function
# async def news_feed():
#     for i in range(1, 4):
#         await asyncio.sleep(1)  # Simulate API delay
#         yield f"News {i}"

# # main function
# async def main():
#     async for news in aiter(news_feed()):
#         print(news)

# asyncio.run(main()) # calling main function
# import asyncio

# # asynchronous generator function
# async def websocket_mock():
#     messages = ["Hi!", "How are you?", "Bye!"]
#     for msg in messages:
#         await asyncio.sleep(1)
#         yield msg

# # main function
# async def main():
#     async for message in aiter(websocket_mock()):
#         print(f"Message: {message}")

# asyncio.run(main()) # calling main function
# ============================================Basic Sting Method=======================================================
# Course = 'Asynchronous Programming'

# Course.upper()
# Course.lower()
# Course.title()
# Course.find()
# Course.replace()
# started, stopped = False,False
# while True:
#     user_input = input("> ").lower().strip()
    
#     if user_input == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to exit""")
#     elif user_input == "start":
#         if started:
#             print("Car already started")
#         elif stopped:
#             print("Car started.......Ready to go")
#         else:
#             started = True
#             print("Car started.......Ready to go")
#     elif user_input == "stop":
#         if not started:
#             print('Car has not been started yet')
#         elif stopped:
#             print("Car already stopped")
#         else:
#             stopped = True
#             print("Car stopped")
#     elif user_input == "quit":
#         break
#     else:
#         print("I don't understand that...........")

prices = [10,20,30]
total_price = 0
for item in prices:
    total_price += item
print(total_price)

for x in range(10):
    for y in range(5):
        print(f"({x}, {y})")
numbers = [6,2,6,2,6]
for num in numbers:
    print(num * 'x')

# lists  = [78,34,56,23,45,43,23,45,23]
# nums = lists[0]
# all = input()
# # for num in lists:
# #     if num not in all:
# #         all.append(num)
# print(all)

customer = {
    "name": "Yusuf",
    "age": 17,
    "is_verified": True
}
customer["birthdate"] = "jan 02 01" 
print(customer["birthdate"])
print(customer)

phone_number = input("Phone: ")
numbers = {
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

for num in phone_number:
    print(numbers.get(num, '!'),end=' ',)
print()


def emoji_converter(message):
    words = message.split()
    emoji = {
        ":)": "😀",
        ":(": "😔",
        "love": "❤️ ",
        "python": "🐍"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output
message = input("> ")
print(f"converted :{emoji_converter(message)}")

def greet_user(first_name, last_name):
    print(f'Hi {first_name}, {last_name}')
    print('Welcome Abroad')
    
print("Start")
greet_user("Abdulrasaq",last_name="Alli")
print("Finish")

age = int(input("Your Age: "))
print(age)

class Point:
    def move():
        print("move")
        
    def draw():
        print("draw")
    
Point.draw()


from codetiming import Timer

t = Timer(name="manual_timer")
t.start()

# Code you want to time
data = [x**2 for x in range(10000000)]

t.stop()  # Automatically prints elapsed time


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I'm {self.name} ")

john = Person("john smith")
print(john.name)
john.talk()
Person.talk()

