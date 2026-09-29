# def file_handling():
#     with open('sentence.txt', 'r') as f:
#         return f.read()

# file_context = file_handling()
# print(file_context)
# # for each_line in file_handling():
# #     print(each_line)
import json

expenses = [
    {
    "amount": 5000,
    "category": "Food",
    "description": "Lunch"
}
]

with open("store_expense.json", 'w') as f:
    json.dump(expenses, f)
def reading_from_file():
    with open("store_expense.json", 'r') as f:
        return json.load(f)
file_context = reading_from_file()
print(file_context)