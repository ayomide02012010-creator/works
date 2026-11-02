import csv

transactions = []
budget = {}
def set_budget_limit(budget):
    while True:
        category = input("Enter category: ").capitalize().strip()
        if category == "":
            print("❌ Your Category Can't Be Empty. Please Enter A Category")
            continue
        else:
            break
    while True:
        try:
            amount_of_budget = float(input("Enter The Limit Amount Of Your Budget: "))
            if amount_of_budget <= 0:
                print("❌ Enter An Amount Greater Than Zero")
                continue
            else:
                break
        except ValueError:
            print("❌ Invalid Amount")
    
    budget[category] = amount_of_budget
    print("\n Budget Limit Successfully Added")
def check_budget(transactions, budget):
    category_spending = view_by_category(transactions)
    for category, budget_amount in budget.items():
        spent = category_spending.get(category, 0)
        spending_ratio = spent/budget_amount * 100
        if spending_ratio >= 100:
            print(f"Budget for {category} has been exceeded")
        elif spending_ratio >= 80:
            print(f'⚠️ Warning! You have used {spending_ratio:.1f}% of your {category} budget.')  
        else:
            print(f"{category} budget still in limits")
def add_transaction(transactions, type_of_transactions):
    while True:
        category = input("\nEnter Category: ").capitalize().strip()
        if category == "":
            print("❌ Your Category Can't Be Empty. Please Enter A Category")
            continue
        else:
            break
    
    while True:
        description = input("Enter Description: ").capitalize().strip()
        if description == "":
            print("❌ Your Description Can't Be Empty. Please Enter A Description")
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
            print("❌ Enter A Valid Amount")
    
    while True:
        date = input("Enter The Date Of Your Transaction: ").capitalize().strip()
        if date == "":
            print("❌ Your Date Can't Be Empty. Please Enter A  Date")
            continue
        elif len(date) != 10:
            print("❌ Invalid format. Correct format (YYYY-MM-DD)")
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
        print(f"{idx}. {transaction['description']:<20} ₦{transaction['amount']:>14,.2f}")
def get_summary(transactions):
    total_income = 0
    total_expenses = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            total_income += transaction["amount"]
        elif transaction["type"] == "expense":
            total_expenses += transaction["amount"]
    return total_income, total_expenses
def view_by_category(transactions):
    category_total  = {}
    for category in transactions:
        if category["category"] in category_total and category["type"] == "expense":
            category_total[category["category"]] += category["amount"]
        elif category["category"] not in category_total and category["type"] == "expense":
            category_total[category["category"]] = category["amount"]
    return category_total
def save_transactions(transactions):
    with open("transactions.csv", "w", newline='') as transactionfile:
        writer = csv.writer(transactionfile)
        writer.writerow(["type", "category", "description", "amount", "date"])
        for transaction in transactions:
            writer.writerow([
                transaction["type"], 
                transaction["category"], 
                transaction["description"], 
                transaction["amount"],
                transaction["date"]
            ])           
def load_transactions():
    loaded_transactions = []
    try:
        with open("transactions.csv", "r", newline='') as transactionfile:
            for transaction in csv.DictReader(transactionfile):
                transaction["amount"] = float(transaction["amount"])
                loaded_transactions.append(transaction)
            return loaded_transactions
    except FileNotFoundError:
        return loaded_transactions
    
def save_budget(budget):
    with open("budget.csv", "w", newline='') as budgetfile:
        writer = csv.writer(budgetfile)
        writer.writerow(["category", "amount"])
        for category, limit in budget.items():
            writer.writerow([
               category,
               limit
            ])
def load_budget():
    budget = {}
    try:
        with open("budget.csv", "r", newline='') as budgetfile:
            for limit in csv.DictReader(budgetfile):
                amount  = float(limit["amount"])
                category = limit["category"]
                budget[category] = amount
            return budget
    except FileNotFoundError:
        return budget
def filter_by_month(transactions, month):
    filtered_transaction  = []
    for transaction in transactions:
        if transaction["date"].startswith(month):
            filtered_transaction.append(transaction)
    
    return filtered_transaction
    
def main():
    global transactions
    transactions = load_transactions()
    global budget
    budget = load_budget()
    while True:
        print(" BUDGET TRACKER ".center(26, "="))
        print("[1] Add Income  [2] Add Expense  [3] View All  [4] Summary  [5] By Category [6] Set Category Budget [7] Filter Transactions By Month [8] Exit")
        user_input = input("\n> ").lower().strip()
        if user_input == "1":
            type_of_transactions = "income"
            add_transaction(transactions, type_of_transactions)
            save_transactions(transactions)
        elif user_input == "2":
            type_of_transactions = "expense"
            add_transaction(transactions, type_of_transactions)
            save_transactions(transactions)
            check_budget(transactions,budget)
        elif user_input == "3":
            view_all(transactions)
        elif user_input == "4":
            total_income, total_expenses = get_summary(transactions)
            net_balance = total_income - total_expenses
            print("\n📊 FINANCIAL SUMMARY\n--------------------------")
            print(f"Total Income:    ₦ {total_income:>14,.2f}")
            print(f"Total Expenses:  ₦ {total_expenses:>14,.2f}")
            print(f"Net Balance:     ₦ {net_balance:>14,.2f}")
        elif user_input == "5":
            print("\n📁 SPENDING BY CATEGORY\n--------------------------")
            
            total_expense = 0
            for transaction in transactions:
                if transaction["type"] == "expense":
                    total_expense += transaction["amount"]
                    
            if total_expense == 0:  
                print("No expense yet")
            else:  
                each_category = view_by_category(transactions)
                for category, amount in each_category.items():
                    print(f"{category:<20} ₦{amount:>10,.2f} ({amount/total_expense*100:.1f}%)")
        elif user_input == "6":
            set_budget_limit(budget) 
            save_budget(budget)       
        elif user_input == "7":
            months = {
                "01" : "January",
                "02" : "February",
                "03" : "March",
                "04" : "April",
                "05" : "May",
                "06" : "June",
                "07" : "July",
                "08" : "August",
                "09" : "September",
                "10" : "October",
                "11" : "November",
                "12" : "December"
            }
            month = input("\nEnter Year & Month (YYYY-MM): ").strip()
            if len(month) != 7 or not month[:4].isdigit() or month[4] != "-":
                print("❌ Invalid Format. Correct Format(YYYY-MM).\n")
                continue
            if month[5:] not in months:
                print("Invalid month. Please enter a month between 01 and 12.\n")
                continue
            filtered_transactions = filter_by_month(transactions, month)
            if not filtered_transactions:
                print("No Transaction This Month.\n")
                continue  
            print(f"TRANSACTIONS FOR {months[month[5:]]} {month[:4]}\n--------------------------------")
            print(f"{'Description':<20} {'Amount':>6} {'Date':>23}\n")
            for monthly_transaction in filtered_transactions:
                print(f"{monthly_transaction['description']:<20} ₦{monthly_transaction['amount']:>14,.2f} {monthly_transaction['date']:>20}")
            print()
        elif user_input == "8":
            print("👋Goodbye! Your transactions has been saved")
            break
        else:
            print("Invalid Input")
            continue
main()