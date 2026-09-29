# EXPENSE TRACKER

## What The Expense Tracker Does:

This project is designed to keep track of all expenses, including their 'Amount', 'Description' and 'Category'.

## Features

1. Add
2. View
3. Total spending
4. Spending by category
5. Delete
6. save / load

## How To Run

Make sure the Python 3 is installed Make sure u are at the current working directory

```bash
python3 expense_tracker.py
svg
```

## Example Usage

```
>>> (myenv) l2e@l2e-ThinkPad-L14-Gen-6:~/Desktop/works/PYTHON/ASSESSMENT/Expense_Tracker$ python3 expense_tracker.py 
=======EXPENSE TRACKER=======
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Delete expense
6. Exit
>>> Choose an option(1-6): 1
Enter an Amount: 3000
Enter a Category: Food
Enter a Description: Lunch
Successfully added!
=======EXPENSE TRACKER=======
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Delete expense
6. Exit
>>> Choose an option(1-6): 2
=======Your Expenses=======
0. Amount: $3900.00 | Category: Transport | Description: Car
1. Amount: $3000.00 | Category: Food | Description: Lunch
=======EXPENSE TRACKER=======
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Delete expense
6. Exit
>>> Choose an option(1-6): 3
Total Spending: $6900.00
=======EXPENSE TRACKER=======
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Delete expense
6. Exit
>>> Choose an option(1-6): 4
Transport --> $3900.00
Food --> $3000.00
=======EXPENSE TRACKER=======
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Delete expense
6. Exit
>>> Choose an option(1-6): 5
=======Your Expenses=======
0. Amount: $3900.00 | Category: Transport | Description: Car
1. Amount: $3000.00 | Category: Food | Description: Lunch
>>> Enter the number(index) of any expense to delete: 0
Successfully Deleted
=======EXPENSE TRACKER=======
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Delete expense
6. Exit
>>> Choose an option(1-6): 2
=======Your Expenses=======
0. Amount: $3000.00 | Category: Food | Description: Lunch
=======EXPENSE TRACKER=======
1. Add expense
2. View expenses
3. View total spending
4. View spending by category
5. Delete expense
6. Exit
>>> Choose an option(1-6): 6
👋Goodbye! Your expenses has been saved
>>> (myenv) l2e@l2e-ThinkPad-L14-Gen-6:~/Desktop/works/PYTHON/ASSESSMENT/Expense_Tracker$ 
svg
```

## Data Storage

This program as a special work that store expenses. Expenses are saved in store_expense.json. When the program starts, it loads the saved expenses from this file.

For more details: Visit [https://realpython.com/python-json/](https://realpython.com/python-json/)

## What I Learned

1. Lists
2. Dictionaries
3. Functions
4. Loops
5. Exceptions
6. File handling
7. JSON