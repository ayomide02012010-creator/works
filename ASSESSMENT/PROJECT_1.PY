import json
import os

FILENAME = "expenses.json"

# ----------------- Data Functions -----------------
def load_expenses():
    """Load expenses from JSON file, or return empty list if file doesn't exist."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    """Save the current expense list to a JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=2)


# ----------------- Core Features -----------------
def add_expense(expenses):
    """Prompt user and add a new expense dict to the list."""
    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    print("✅ Expense added!")


def view_expenses(expenses):
    """Display all stored expenses."""
    if not expenses:
        print("📭 No expenses recorded.")
        return

    print("\n--- Your Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. Amount: ${exp['amount']:.2f} | Category: {exp['category']} | Description: {exp['description']}")


def total_spending(expenses):
    """Calculate and return the sum of all expense amounts."""
    return sum(exp["amount"] for exp in expenses)


def spending_by_category(expenses, category):
    """Calculate total spending for a specific category (case-insensitive)."""
    return sum(
        exp["amount"] for exp in expenses if exp["category"].lower() == category.lower()
    )


def delete_expense(expenses):
    """Delete an expense by its numbered listing."""
    view_expenses(expenses)
    if not expenses:
        return

    try:
        idx = int(input("Enter the number of the expense to delete: ").strip()) - 1
        if 0 <= idx < len(expenses):
            removed = expenses.pop(idx)
            print(f"🗑️ Deleted: Amount: ${removed['amount']:.2f} | {removed['category']} - {removed['description']}")
        else:
            print("❌ Invalid number. Try again.")
    except ValueError:
        print("❌ Please enter a valid number.")


# ----------------- Main Menu -----------------
def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Spending")
        print("4. Calculate Spending by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total = total_spending(expenses)
            print(f"💰 Total spending: ${total:.2f}")

        elif choice == "4":
            cat = input("Enter category to analyze: ").strip()
            category_total = spending_by_category(expenses, cat)
            print(f"📂 Spending in '{cat}': ${category_total:.2f}")

        elif choice == "5":
            delete_expense(expenses)
            save_expenses(expenses)

        elif choice == "6":
            save_expenses(expenses)
            print("👋 Goodbye! Your expenses have been saved.")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()