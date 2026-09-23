import random

def generate_secret_number(maximum_number): 
    return random.randint(1, maximum_number)

def calculate_score(max_attempts, attempts_used, difficulty_multiplier):
    return (max_attempts - attempts_used + 1) * difficulty_multiplier
