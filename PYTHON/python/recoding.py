# # =================1=====================
# tasks = [
#     {"title": "Learn Python", "completed": True},
#     {"title": "Learn HTML", "completed": False},
#     {"title": "Practise Go", "completed": False},
#     {"title": "Study Mathematics", "completed": True},
#     {"title": "Build a project", "completed": False}
# ]

# def get_incomplete_tasks(tasks):
#     incomplete_tasks = []
#     for each_task in tasks:
#         if each_task["completed"] == False:
#             incomplete_tasks.append(each_task["title"])
#     return incomplete_tasks

# print(get_incomplete_tasks(tasks))

# # # ==============2================
# expenses = [
#     {"category": "Food", "amount": 5000},
#     {"category": "Transport", "amount": 3000},
#     {"category": "Books", "amount": 2000},
#     {"category": "Food", "amount": 4000}
# ]

# def calculate_average(expenses):
#     total_spending = 0
#     for amount in expenses:
#         total_spending += amount["amount"]
#     return total_spending/len(expenses)

# print(calculate_average(expenses))

# # ================3===============

# scores = [
#     {"player": "Ali", "score": 15},
#     {"player": "Musa", "score": 20},
#     {"player": "John", "score": 12},
#     {"player": "David", "score": 25}
# ]

# def highest_scorer(scores):
#     highest = scores[0]["score"]
#     highest_player = scores[0]["player"]
#     for scorer in scores:
#         if highest < scorer["score"]:
#             highest = scorer["score"]
#             highest_player = scorer["player"]
#     return highest_player
           
            
# print(highest_scorer(scores))

# # ======================4=====================
# expenses = [
#     {"category": "Food", "amount": 5000},
#     {"category": "Transport", "amount": 3000},
#     {"category": "Books", "amount": 2000},
#     {"category": "Food", "amount": 4000}
# ]

# def filter_expenses(expenses, minimum):
#     my_list = []
#     for expense in expenses:
#         if expense["amount"] >= minimum:
#             my_list.append(expense["amount"])
#     return my_list
# print(filter_expenses(expenses, 3000))
        
# # ==================5================
# tasks = [
#     {"title": "Learn Python", "completed": True},
#     {"title": "Learn HTML", "completed": False},
#     {"title": "Practise Go", "completed": False},
#     {"title": "Study Mathematics", "completed": True},
#     {"title": "Build a project", "completed": False}
# ]

# def count_tasks(tasks):
#     completed = 0
#     incomplete = 0
#     for task in tasks:
#         if task["completed"]  == True:
#             completed += 1
#         else:
#             incomplete += 1
        
#     filterd = {
#         "completed": completed,
#         "incomplete": incomplete
#     }
#     return filterd
# print(count_tasks(tasks))
# # ================6====================
# expenses = [
#     {"category": "Food", "amount": 5000},
#     {"category": "Transport", "amount": 3000},
#     {"category": "Books", "amount": 2000},
#     {"category": "Food", "amount": 4000}
# ]

# def top_categories(expenses, n):
#     category_total ={}
#     for expense in expenses:
#         if expense["category"] in category_total:
#             category_total[expense["category"]] += expense["amount"]
#         else:
#             category_total[expense["category"]] = expense["amount"]
#     sorted_categories = sorted(category_total, key=lambda category: (-category_total[category], category))
#     return sorted_categories[n]
    

# print(top_categories(expenses, 0))
# # ======================7====================
# books = [
#     {"title": "Python Basics", "available": True},
#     {"title": "Learning Java", "available": False},
#     {"title": "Clean Code", "available": True}
# ]

# def find_book(books, title):
#     for book in books:
#         if title == book["title"]:
#             return book     
#     return None
        
# print(find_book(books, "Python Basics"))
# print(find_book(books, "JavaScript"))

# # =========================8=====================
# books = [
#     {"title": "Python Basics", "available": True},
#     {"title": "Learning Java", "available": False},
#     {"title": "Clean Code", "available": True},
#     {"title": "Fluent Python", "available": True}
# ]

# def available_titles(books):
#     available_title = []
#     for book in books:
#         if book["available"]:
#             available_title.append(book["title"])
        
#     sort = sorted(available_title)
#     return sort

# print(available_titles(books))
# # ==========================9=========================
# books = [
#     {"title": "Python Basics", "available": True},
#     {"title": "Learning Java", "available": False},
#     {"title": "Clean Code", "available": True},
#     {"title": "Fluent Python", "available": True},
#     {"title": "Data Structures", "available": False}
# ]

# def count_books(books):
        
#     available = 0
#     un_available = 0

#     for book in books:
#         if book["available"]:
#             available += 1
#         else:
#             un_available += 1
#     book_stat = {
#         "available": available,
#         "unavailable": un_available
#     }
#     return book_stat

# print(count_books(books))

# =======================10========================
# transactions = [5000, 2000, -1500, 3000, -500]

# def first_overdraft(transactions):
#     for transaction in transactions:
#         if transaction < 0:
#             return transaction
#     return None

# print(first_overdraft(transactions))

# ===========================11========================

# def apply_transaction(balance, amount):
#     if amount < 0 and balance >= -amount:
#         return balance - abs(amount)
#     elif amount > 0:
#         return balance + amount
#     elif amount < 0 and balance < -amount:
#         return "Insufficient funds"
#     return balance

# print(apply_transaction(5000, -2000))
# print(apply_transaction(5000, -7000))
# print(apply_transaction(5000, 2000))

# # =================12==============================
# def count_transactions(transactions):
#     deposit = 0
#     withdrawal = 0
#     for transaction in transactions:
#         if transaction < 0:
#             withdrawal += 1
#         elif transaction > 0:
#             deposit += 1
#     return {"deposits": deposit, "withdrawals": withdrawal}

# transactions = [5000, -2000, 3000, -1000, 0, 4000]
# print(count_transactions(transactions))

# # =====================13==========================
# def largest_transaction(transactions):
#     if not transactions:
#         return None
#     largest = transactions[0]
#     for transaction in transactions:
#         if transaction > largest:
#             largest = transaction
#     return largest

# transactions = [-500, 2000, 7500, -1000, 3000]
# print(largest_transaction(transactions))

# # ======================14========================
# def calculate_balance(transactions):
#     balance = 0
#     for transaction in transactions:
#         balance += transaction
#     return balance        

# transactions = [5000, -2000, 3000, -1000, 4000]
# print(calculate_balance(transactions))

# ==================15==========================
# def large_transactions(transactions, limit):
#     amount_greater_than_limits = []
#     for transaction in transactions:
#         if transaction > limit:
#             amount_greater_than_limits.append(transaction)
#     return amount_greater_than_limits

# transactions = [500, 2000, 7500, 1000, 9000, 300]
# limit = 1500

# print(large_transactions(transactions, limit))

# # ==========================16====================
def group_transactions(transactions):
    deposit = []
    withdrawal = []
    for transaction in transactions:
        if transaction < 0:
            withdrawal.append(transaction)
        elif transaction > 0:
            deposit .append(transaction)
    return {"deposits": deposit, "withdrawals": withdrawal}

transactions = [5000, -2000, 3000, -1000, 0, 4000]
print(group_transactions(transactions))
# # ====================17====================
def average_transaction(transactions):
    if not transactions:
        return 0
    
    average = sum(transactions)/len(transactions)
    return round(average, 1)

transactions = [1000, 2000, 3000, 4000]
print(average_transaction(transactions))

# =====================18==============
def transaction_frequency(transactions):
    frequency = {}
    counter = 0
    for transaction in transactions:
        if transaction in frequency:
            frequency[transaction] = frequency[transaction] + 1
        else: 
            frequency[transaction] = counter+1
    return frequency
transactions = [1000, 2000, 1000, 3000, 2000,3000, 1000]
print(transaction_frequency(transactions))

# ===================19==============
def most_frequent_transaction(transactions):
    if not transactions:
        return None
    
    frequency = {}
    counter = 0
    for transaction in transactions:
        if transaction in frequency:
            frequency[transaction] = frequency[transaction] + 1
        else: 
            frequency[transaction] = counter+1
    highest_frequency = 0
    high = 0
    for amount, value in frequency.items():
        if value > highest_frequency:
            highest_frequency = value
            high = amount
    return high
            
        
transactions = [1000, 1000, 2000, 1000, 2000, 3000, 3000, 3000, 3000]
print(most_frequent_transaction(transactions))
# ==========================20==================
products = [
    {"name": "Laptop", "price": 200000},
    {"name": "Phone", "price": 100000},
    {"name": "Mouse", "price": 10000}
]

discount = 10
def apply_discount(products, discount):
    for product in products:
        disc = product["price"] - (product["price"]*discount/100)
        product["price"] = round(disc)
    return products

print(apply_discount(products, discount))

# =====================21===================
products = [
    {"name": "Laptop", "quantity": 15},
    {"name": "Mouse", "quantity": 4},
    {"name": "Keyboard", "quantity": 8},
    {"name": "Monitor", "quantity": 2},
    {"name": "USB Cable", "quantity": 20}
]

threshold = 10

def low_stock(products, threshold):
    below_threshold = []
    for product in products:
        if product["quantity"] < threshold:
            below_threshold.append(product["name"])
    return below_threshold

print(low_stock(products, threshold))

# ======================22===================
def inventory_value(products):
    all_value = []
    for product in products:
        calc = product["price"]* product["quantity"]
        all_value.append(calc)
    return sum(all_value)    
    
products = [
    {"name": "Laptop", "price": 200000, "quantity": 3},
    {"name": "Mouse", "price": 5000, "quantity": 10},
    {"name": "Keyboard", "price": 10000, "quantity": 5}
]

print(inventory_value(products))
# ===================23=======================
def most_expensive(products):
    if not products:
        return None
    name = None
    highest = 0
    for product in products:
        if  product["price"] > highest:
            highest = product["price"]
            name = product["name"]
    return name
            
products = [
    {"name": "Laptop", "price": 200000, "quantity": 3},
    {"name": "Mouse", "price": 5000, "quantity": 10},
    {"name": "Keyboard", "price": 10000, "quantity": 5}
]

print(most_expensive(products))