square = lambda x : x**2

file = open("demofile.txt", "wt")
number = (int(input("Enter A Number: ")))
result = square(number)

file.write(str(result))


import random, string

def gen_password(lent=8):
    if lent < 8:
        return "Password not Allowed"
    
    # uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" lowercase_letter = "abcdefghijklmnopqrstuvwxyz" digit_num = "0123456789" special_char = "!@#$"
    
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special_character = random.choice(string.punctuation)
    
    password = uppercase + lowercase + digit + special_character 
    
    all = string.ascii_lowercase + string.ascii_lowercase + string.digits + string.punctuation
    other = len(all) - len(password)
    
    convert_other = str(other)
    random.choice(str(convert_other))
    password += convert_other
    
    result = ""
    result += password
    # final_result = random.shuffle(result)
    return result
    
print(gen_password()) 
print(gen_password(12))              
first = float(input("First: "))
second = float(input("Second: "))                                         # numbers = [7, 2, 15, 4, 10]
summ = str(first + second)#                                               # largest = numbers[0]
print('Sum: ' + summ) #                                                   # for number in numbers[1:]: 
                                                                          #     if number > largest:
course = 'Python For Begginers'                                           #          largest = number
course = course.upper()                                                   #          print(largest)
print(course) #
print(course.find("R")) #
course = course.lower()
print(course) #
print(course.find("y")) #                                                         # in python we have three logical operators
print(course.replace("for", '4'))  #                                              # and (both meet the condition e.g (false false) (true true))                                                                                      #                                                                                      #
print("python" in course) #                                                       # or (at least one meet the requirement)
print(10 + 5,10 - 5,10 * 5,10 / 5,10 // 5,10 % 3,10 ** 3) #                       # not (it inverses any value we give it)
x = (10+3)*2
print(x) #
price = 70
print(price > 60 and price < 80) #True
price = 55
print(price > 60 and price < 80) #False
price = 70
print(price > 60 or price < 80) # True
price = 55
print(price > 60 or price < 80)  # True
price = 70
print(not price > 90)

# IF STATEMENT IN PHYTON

temprature = 45

if temprature > 50:
    print("It's a hot day")
    print('Drink plenty of H2O')
elif temprature > 20:
    print("It A Nice Day")
elif temprature > 10:
    print("It a bit cold")
else:
    print("It's cold ")        
print('Done')
# WHILE LOOPS                                                               # EXERSICE
number = 1                                                                  # weight_in_numbers = float(input("Weight: "))
while number <= 20:                                                          # weight_in_kilogram_or_pounds = input("Kg or lb: ")
    print(number * '*')                                                      
    number = number + 1                                                     # if weight_in_kilogram_or_pounds == "Kg":
                                                                            # conversion = weight_in_numbers * 2.2
                                                                            # conversion1 = str(conversion)
                                                                            # print("weight in pound: " + conversion1 +'lb')
                                                                            # elif weight_in_kilogram_or_pounds == "lb":
                                                                            # conversion = weight_in_numbers * 0.45
                                                                            # conversion1 = str(conversion)
                                                                            # print("weight in kilogram: " + conversion1 + 'kg')
    

def my_sum(*args):
    result = 0
    for param in args:
        result += param
    return result

print(my_sum( 10, 20, 30, 40, 50, 60, 70, 80))

list1 =[1, 2, 3]
list2 =[4, 5, 6]

result = [*list1, 'Go', *list2]
# result = [*[1, 2, 3], 'Go', *[4, 5, 6]] the work of the '*' is to unpack the list. so it becomes -> [1, 2, 3, 'Go', 4, 5, 6]
print(result)
name = input('Enter your name:')
year_born = input('Year you born:')
age = 2026 - int(year_born)
print(f'You are {name}. And your age is {age}.')
print(abs(complex(2+3j)))
print(abs(complex(-2+3j)))
from fractions import Fraction
print(abs(Fraction("1/2")))
print(abs(Fraction("-1/2")))

print(abs(Fraction("1/2")))
