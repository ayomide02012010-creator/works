import json
expenses = []

def add_expense():
    try:
        amount = float(input('Enter an Amount: '))
    except ValueError:
        print('❌ Invalid Amount. Please enter a number')
        return
    
    category = input('Enter a Category: ').strip()
    description = input('Enter a Description: ').strip()
    
    expense_dict = {
        "Amount" : amount,
        "Category" : category,
        "Description" : description
    }    
    expenses.append(expense_dict)
    print('Successfully added!')

def calculate_total():   
    running_total = 0
    for expense in expenses:
        running_total += expense["Amount"]
    return running_total

def calculate_by_category():
    category_total = {}
    for expense in expenses:
        if expense['Category'] in category_total:
            category_total[expense["Category"]] += expense['Amount'] 
        else:
            category_total[expense['Category']] = expense["Amount"]
    return category_total

def view_expenses():
    print("=" * 7 + 'Your Expenses' + "=" * 7)
    idx = 0
    for expense in expenses:
        print(f"{idx}. Amount: ${expense['Amount']:.2f} | Category: {expense['Category']} | Description: {expense['Description']}")
        idx += 1

def delete_expense():
    view_expenses()
    try:
        del_exp = int(input('Enter the number(index) of any expense to delete: '))
        if del_exp < 0:
            print('Invalid number')
            return
        del expenses[del_exp] 
    except IndexError:
        print('Look again and choose a correct number(index)')
        return
    except ValueError:
        print('Invalid input. Try again')
        return
    print('Successfully Deleted')
def save_expenses():
    with open("store_expense.json", 'w') as f:
        json.dump(expenses, f)
def load_expenses():
    try:
        with open("store_expense.json", 'r') as f:
            load_expense = json.load(f)
            if isinstance(load_expense, list):
                return load_expense
            else:
                return []
    except FileNotFoundError:
        print("File Doesn't exist yet")
        return expenses
    except json.JSONDecodeError:
        print('File exists, but the JSON is invalid.')
        return expenses
        
    
def show_menu():
    print("=" * 7 + 'EXPENSE TRACKER' + "=" * 7)
    print('1. Add expense')
    print('2. View expenses')
    print('3. View total spending')
    print('4. View spending by category')
    print('5. Delete expense')
    print('6. Exit')
    choice = input('Choose an option(1-6): ')
    return choice
    
    
def main():
    global expenses
    expenses = load_expenses()
    while True:

        user_choice = show_menu()
        
        if user_choice == '1':
            add_expense()
        elif user_choice == '2':
            if not expenses:
                print('No Expense added yet')
                continue
            view_expenses()
        elif user_choice == '3':
            total = calculate_total()
            print(f'Total Spending: ${total:.2f}')
        elif user_choice == '4':
            spending_by_category = calculate_by_category()
            for key, value in spending_by_category.items():
                print(f"{key} --> ${value:.2f}")
        elif user_choice == '5':
            if not expenses:
                print('No expense added yet')
                continue
            delete_expense()
        elif user_choice == '6':
            save_expenses()
            print('👋Goodbye! Your expenses has been saved')
            break
        else:
            print('❌ Invalid choice. Please choose 1 to 6')
      
main()