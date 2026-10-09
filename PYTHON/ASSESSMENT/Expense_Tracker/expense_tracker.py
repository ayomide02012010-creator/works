import json
expenses = []

def add_expense():
    while True:
        try:
            amount = float(input('Enter an Amount: '))
            if amount < 1:
                print("❌ Invalid Amount. Please enter a Valid number")
                continue
            else:
                break
        except ValueError:
            print('❌ Invalid Amount. Please enter a number')  
    while True:
        category = input('Enter a Category: ').strip()
        if category == "":
            print("❌ Invalid Category")
            continue
        else:
            break
    while True:
        description = input('Enter a Description: ').strip()
        if description == "":
            print("❌ Invalid description")
            continue
        else:
            break
    expense_dict = {
        "Amount" : amount,
        "Category" : category,
        "Description" : description
    }    
    expenses.append(expense_dict)

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
        idx += 1
        print(f"{idx}. Amount: ${expense['Amount']:.2f} | Category: {expense['Category']} | Description: {expense['Description']}")
    print()

def delete_expense():
    view_expenses()
    while True:
        try:
            del_exp = int(input('Enter the number(index) of any expense to delete: '))
            
            if del_exp <= 0 or del_exp > len(expenses):
                print('Choose a correct number(index)')
                continue
            else:
                confirm_del_exp = input("Are you sure you want to delete the expense (y/n)? ").lower().strip()
                if confirm_del_exp not in ["y","yes"] and confirm_del_exp not in ["n","no"]:
                    print("❌ Invalid choice")
                    continue
                elif confirm_del_exp in ["y","yes"]:
                    del_exp -= 1
                    del expenses[del_exp]
                    save_expenses()
                    print('Successfully Deleted')
                    break
                else:
                    break
        except ValueError:
            print('❌ Invalid input. Try again')
def save_expenses():
    with open("store_expense.json", 'w') as f:
        json.dump(expenses, f, indent=4)
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
    print('6. Exit\n')
    choice = input('Choose an option(1-6): ').strip()
    print()
    return choice
    
    
def main():
    global expenses
    expenses = load_expenses()
    while True:
        user_choice = show_menu()
        
        if user_choice == '1':
            add_expense()
            save_expenses()
            print('Successfully added!')
        elif user_choice == '2':
            if not expenses:
                print('No Expense added yet')
                continue
            view_expenses()
        elif user_choice == '3':
            print('=' * 7 + 'Total spending' + '=' * 7)
            total = calculate_total()
            print(f'Total Spending: ${total:.2f}\n')
        elif user_choice == '4':
            print('=' * 7 + 'Spending by category' + '=' * 7)
            spending_by_category = calculate_by_category()
            for key, value in spending_by_category.items():
                print(f"{key} --> ${value:.2f}")
            print()
        elif user_choice == '5':
            if not expenses:
                print('No expense added yet')
                continue
            delete_expense()
        elif user_choice == '6':
            print('👋Goodbye! Your expenses has been saved')
            break
        else:
            print('❌ Invalid choice. Please choose a number from 1 to 6')
      
main()