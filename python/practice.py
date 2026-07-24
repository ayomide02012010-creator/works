# square = lambda x : x**2

# file = open("demofile.txt", "wt")
# number = (int(input("Enter A Number:\n")))
# result = square(number)

# file.write(str(result))


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
print(gen_password(5)) 
print(gen_password(12)) 