transactions = []
def add_transaction(transactions, type_of_transactions):
    while True:
        category = input("Enter Category: ").capitalize().strip()
        if category == "":
            print("Your Category Can't Be Empty. Please Enter A Category")
            continue
        else:
            break
    
    while True:
        description = input("Enter Description: ").capitalize().strip()
        if description == "":
            print("Your Description Can't Be Empty. Please Enter A Description")
            continue
        else:
            break
        
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount <= 0:
                print("Amount Must Be Greater Than Zero")
                continue
            else:
                break
        except ValueError:
            print("Enter A Valid Amount")
    
    while True:
        date = input("Enter The Date Of Your Transaction: ").capitalize().strip()
        if date == "":
            print("Your Date Can't Be Empty. Please Enter A  Date")
            continue
        else:
            break
        
    current_transactions = {
        "type": type_of_transactions,
        "category": category,
        "description": description,
        "amount": amount,
        "date": date
    }
    
    transactions.append(current_transactions)
    print("Transaction added successfully!")
def view_all(transactions):
    idx = 0
    print(f"\n{'Description':<20} {'Amount':>10}")
    for transaction in transactions:
        idx += 1
        print(f"{idx}. {transaction['description']:<20} ₦{transaction['amount']:>10,.2f}")

def get_summary(transactions):
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
    return total_income
    for transaction in transactions:
        if transaction["type"] == "expense":
            total_expenses += transaction["amount"]
    return total_expenses
        
def main():
    while True:
        print("===== BUDGET TRACKER =====")
        print("[1] Add Income  [2] Add Expense  [3] View All  [4] Summary  [5] By Category  [6] Exit")
        user_input = input("\n> ").lower().strip()
        if user_input == "1":
            type_of_transactions = "income"
            add_transaction(transactions, type_of_transactions)
        elif user_input == "2":
            type_of_transactions = "expense"
            add_transaction(transactions, type_of_transactions)
        elif user_input == "3":
            view_all(transactions)
        elif user_input == "4":
            total_income, total_expenses = get_summary(transactions)
            net_balance = total_income - total_expenses
            print("\n📊 FINANCIAL SUMMARY\n--------------------------")
            print(f"Total Income:    ₦{total_income:,.2}")
            print(f"Total Expenses:  ₦{total_expenses:,.2}")
            print(f"Net Balance:     ₦{net_balance:,.2}")
        elif user_input == "6":
            break
        else:
            print("Invalid Input")
            continue
main()