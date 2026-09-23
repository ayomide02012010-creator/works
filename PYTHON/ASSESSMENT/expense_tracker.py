expenses = [
    {
        "amount": 15000,
        "category": "Football",
        "description": "Sport"
    },
    {
        "amount": 5000,
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": 5000,
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": 2000,
        "category": "Transport",
        "description": "Bus"
    }
]

for expense in expenses:
    print(expense)
    

running_total = 0
for expense in expenses:
    running_total += expense['amount']
print(f'Total Expense: {running_total}')


category_total = {}
for expense in expenses:
    if expense['category'] in category_total:
        category_total[expense["category"]] += expense['amount'] 
    else:
        category_total[expense['category']] = expense["amount"]
for key, value in category_total.items():
    print(key, value)

def add_expense():
    amount = float(input('Enter an Amount: '))
    category = (input('Enter a Category: '))
    description = (input('Enter a Discription: '))
    
    expense_dict = {
        "amount" : amount,
        "category" : category,
        "description" : description
    }
    expenses.append(expense_dict)
    
def view_expenses():
    for expense in expenses:
        print(expense)
add_expense()
view_expenses()