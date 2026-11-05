# =================1=====================
tasks = [
    {"title": "Learn Python", "completed": True},
    {"title": "Learn HTML", "completed": False},
    {"title": "Practise Go", "completed": False},
    {"title": "Study Mathematics", "completed": True},
    {"title": "Build a project", "completed": False}
]

def get_incomplete_tasks(tasks):
    incomplete_tasks = []
    for each_task in tasks:
        if each_task["completed"] == False:
            incomplete_tasks.append(each_task["title"])
    return incomplete_tasks

print(get_incomplete_tasks(tasks))

# ==============2================
expenses = [
    {"category": "Food", "amount": 5000},
    {"category": "Transport", "amount": 3000},
    {"category": "Books", "amount": 2000},
    {"category": "Food", "amount": 4000}
]

def calculate_average(expenses):
    total_spending = 0
    for amount in expenses:
        total_spending += amount["amount"]
    return total_spending/len(expenses)

print(calculate_average(expenses))

# ================3===============

scores = [
    {"player": "Ali", "score": 15},
    {"player": "Musa", "score": 20},
    {"player": "John", "score": 12},
    {"player": "David", "score": 25}
]

# def highest_scorer(scores):
#     high = []
#     for scorer in scores:
#         for player, score in scorer.items():
#             if score in high:
                
#             print(score)
            
# highest_scorer(scores)

# ======================4=====================
expenses = [
    {"category": "Food", "amount": 5000},
    {"category": "Transport", "amount": 3000},
    {"category": "Books", "amount": 2000},
    {"category": "Food", "amount": 4000}
]

def filter_expenses(expenses, minimum):
    my_list = []
    for expense in expenses:
        if expense["amount"] >= minimum:
            my_list.append(expense["amount"])
        else:
            pass
    return my_list
print(filter_expenses(expenses, 3000))
        
# ==================5================
tasks = [
    {"title": "Learn Python", "completed": True},
    {"title": "Learn HTML", "completed": False},
    {"title": "Practise Go", "completed": False},
    {"title": "Study Mathematics", "completed": True},
    {"title": "Build a project", "completed": False}
]

def count_tasks(tasks):
    for task in tasks:
        completed = 0
        incomplete = 0
        if task["completed"]  == True:
            completed += 1
        else:
            incomplete += 1
        
    filterd = {
        "completed": completed,
        "incomplete": incomplete
    }
    return filterd
print(count_tasks(tasks))