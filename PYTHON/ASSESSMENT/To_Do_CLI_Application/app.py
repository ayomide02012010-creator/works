tasks = [
    {
        "title": "Learn python",
        "completed": True,
        "priority": "High",
        "due_date": "2026-10-07"
        },
    {
        "title": "Learn H.T.M.L",
        "completed": False,
        "priority": "medium",
        "due_date": "2026-10-09"
        },
    
    {
        "title": "python fundamentals",
        "completed": True,
        "priority": "High",
        "due_date": "2026-07-07"
        },
    {
        "title": "python built-in-functions",
        "completed": False,
        "priority": "High",
        "due_date": "2026-10-10"        
        }
]
def display_task():
    for i, task in enumerate(tasks, 1):
        print(f'{i}. {task["title"]}\n   Completed: {task["completed"]}\n   Priority: {task["priority"]}\n   Due date: {task["due_date"]}\n')
def add_task():
    while True:
        title = input("Enter your task Title: ").strip()
        if title == "":
            print("❌ Invalid Input")
            continue
        else:
            break
    while True:
        priority = input("Enter your Priority to the task(High, Medium, or Low): ").lower().strip()
        if priority == "" or priority not in ["high","medium","low"]:
            print("❌ Invalid Input: Please enter High, Medium, or Low")
            continue
        else:
            break
    while True:
        due_date = input("Enter the due date of your task: ").strip()
        if due_date == "":
            print("❌ Invalid Input")
            continue
        else:
            break
    task = {
        "title": title,
        "completed": False,
        "priority": priority,
        "due_date": due_date
        }
    tasks.append(task)
def complete_task():
    print("=" * 7 + "List Of Task" + "=" * 7)
    idx = 0
    for current_task in tasks:
        if current_task['completed'] == False:
            idx+=1
            print(f"{idx}. {current_task['title']} ❌")
        else:
            idx +=1
            print(f"{idx}. {current_task['title']}  ✅")      
    while True: 
        try:
            idx_task = int(input('Enter the number of task to complete: '))
            while idx_task <= 0 or idx_task > len(tasks):
                print("❌ Invalid Input: Enter a Valid Number")
                idx_task = int(input('Enter the number of task to complete: '))
        
            if tasks[idx_task-1]["completed"] == True:
                print(f"Task {idx_task} is already completed")
                return
            else:
                tasks[idx_task-1]['completed'] = True
                print(f"{idx_task}. {tasks[idx_task-1]['title']}  ✅")  
                return
        except ValueError:
            print("❌ Invalid Input")
    

def main():
    add_task()
    display_task()
    complete_task()

main()