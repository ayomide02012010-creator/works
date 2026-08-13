# Here are 10 exercises covering exception handling, packing/unpacking, spreading, enumerate, and zip — in the same spirit as the Day 17 material:

# **1. Basic try/except**
# Write a function `divide(a, b)` that divides two numbers. Use `try`/`except` to catch `ZeroDivisionError` and return `'Cannot divide by zero'` instead of crashing.

# **2. Multiple except blocks**
# Write a program that asks the user for two numbers and divides them. Handle `ValueError` (non-numeric input) and `ZeroDivisionError` separately, printing a specific message for each.

# **3. else and finally**
# Write a function that tries to convert a string to an integer. If it succeeds, print the doubled value in an `else` block. Regardless of success or failure, print `'Done attempting conversion'` in a `finally` block.

# **4. Catching with `as e`**
# Write a function `safe_list_access(lst, index)` that returns `lst[index]`, but catches `IndexError` using `except IndexError as e` and prints the actual error message `e`.

# **5. Unpacking a list into function arguments**
# Given `scores = [88, 92, 79, 95]`, write a function `average_of_four(a, b, c, d)` that returns their average. Call it using unpacking (`*scores`).

# **6. Unpacking with rest**
# Given `numbers = [3, 6, 9, 12, 15, 18, 21]`, unpack it so that `first` holds `3`, `last` holds `21`, and `middle` holds everything in between as a list.

# **7. Unpacking a dictionary into function arguments**
# Write a function `describe_book(title, author, year, pages)` that returns a formatted sentence. Given `book = {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965, 'pages': 412}`, call the function using `**book`.

# **8. Packing arguments**
# Write a function `find_max(*args)` that returns the largest number passed to it, without using the built-in `max()`. Test it with `find_max(4, 19, 7, 2, 33, 15)`.

# **9. Spreading two lists**
# Given `weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']` and `weekend = ['Sat', 'Sun']`, use spreading to combine them into one list called `full_week`, in correct order.

# **10. Enumerate and zip together**
# Given `students = ['Ana', 'Ben', 'Cleo']` and `grades = [85, 91, 76]`, use `zip` to pair each student with their grade, and `enumerate` to print each pair with a position number, like:
# ```
# 1. Ana scored 85
# 2. Ben scored 91
# 3. Cleo scored 76
# ```

print('=============1============')
def divide(x, y):
    return x/y

try:
    print(divide(20,5))
except ZeroDivisionError:
    print('Cannot divide by zero')
  
print('=============2============')
num1 = int(input("Enter two numbers:" ))
num2 = int(input("Enter two numbers:" ))

try:
    output = divide(num1,num2)
    print(output)
except ValueError:
    print("not an int")
except ZeroDivisionError:
    print("number can't be divided by zero")
    
print('=============3============')
def string_converter(string):
    return int(string)
try:
    result = string_converter('246')
except ValueError:
    print("Unable to convert: Possible non-numeric in the string")
else:
    print(result*2)
finally:
    print('Done attempting conversion')
    
print('=============4============')
def safe_list_access(lst, index):
    lst = [3,4,5,6,7]
    return lst[index]

print('=============5============')
scores = [88, 92, 79, 95]
def average_of_four(a,b,c,d):
    return (a/2, b/2, c/2, d/2)

print(average_of_four(*scores))

print('=============6============')
numbers = [3, 6, 9, 12, 15, 18, 21]
first, *middle, last = numbers
print(first, middle, last)

print('=============7============')
# def discribe_book(title, author, year, pages):
#     book = {'title': 'Dune', 'author': 'Frank Herbert', 'year': 1965, 'pages': 412}
#     return book#({f'title: {title}, author: {author}, year: {year}, pages: {pages}'})

# print(discribe_book(**book))
#===========8==============
#===========9==============
weekdays = ['Mon','Tue','Wed','Thu','Fri']
weekend = ['Sat','Sun']
full_week = [*weekdays, *weekend]
print(full_week) 
#===========10==============
students = ['Ana', 'Ben', 'Cleo']
grades = [85, 91, 76]

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

