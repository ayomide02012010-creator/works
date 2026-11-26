import json, datetime, uuid
tasks = [
    {
        "id" : "a1b2c3d4",
        "title" : "Submit assingment",
        "category" : "Study",
        "priority" : "High",
        "due_date" : "2026-12-01",
        "completed" : False,
        "created_at" : "2026-11-25"
    }
]
# ================= Helper Function ====================

def is_empty(parameter):
    return not parameter
    
# ==================== Display Menu ======================

def display_menu():
    print("[0] Exit")
    print("[1] Add Task")
    print("[2] Complete Task")
    print("[3] Edit Task")
    print("[4] Delete Task")
    print("[5] Display Task\n")

# =============== File Persistence Layer =================

def load_tasks():
    try:
        with open("tasks.json" ,"r") as file:
            tasks = json.load(file)
            if isinstance(tasks, list):
                return tasks
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError :
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

# =======================CRUD Functions=========================  

def add_tasks(tasks):
    while True:
        title = input("\nEnter task Title: ").strip().capitalize()
        if is_empty(title):
            print("Task Title can't be Empty.\n")
            continue
        break
    while True:
        category = input("\nEnter task Category: ").strip().capitalize()
        if is_empty(category):
            print("Task Title can't be Empty.\n")
            continue
        break
    while True:
        priority = input("\nEnter task Priority: ").strip().capitalize()
        if is_empty(priority):
            print("Task Title can't be Empty.\n")
            continue
        if priority not in ["High", "Medium", "Low"]:
            print("Prority can only be (High, Medium, Low)")
            continue
        break
    while True:
        due_date = input("\nEnter due date (YYYY-MM-DD): ").strip()
        if is_empty(due_date):
            print("due date can't be empty.\n")
            continue
        break
    
    each_task = {
        "id" : str(uuid.uuid4()),
        "title": title,
        "category" : category,
        "priority" : priority,
        "due-date" : due_date,
        "completed" : False,
        "created_at" : datetime.date.today().isoformat()
    }
    
    tasks.append(each_task)

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            break 
    else:
        print("The id did not match any of the available task")

def display_tasks(tasks):
    print("\n📋 YOUR TASKS (sorted by due date)""\n" + '=' * 50+"")
    is_complete = 0
    for task in tasks:
        if task["completed"] == True:
            complete = "✅"
            is_complete += 1
        else:
            complete = "⬜"  
            
        if task["priority"] == "High":
            prior = "!"
        else:
            prior = " "
        print(f"{complete} [{prior}] {task["title"]}   [{task["priority"]}]   [{task["category"]}]")
    print("=" * 50)
    print(f"Total: {len(tasks)}  |  {is_complete} completed  |  3 pending  |  1 overdue")
# ================== PROGRAM ENTRY ========================
def main():
    tasks = load_tasks()
    print("="*50)
    print("WELCOME TO Text-Based To-Do List Application".center(50))
    print("="*50 + "\n")
    while True:
        display_menu()
        user_input = input("> ")
        if user_input == "1":
            add_tasks(tasks)
            save_tasks(tasks)
            print("Task successfully saved\n")
        elif user_input == "2":
            task_id = input("Enter The Id Of The Task To Complete: ")
            print()
            complete_task(tasks, task_id)
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            display_tasks(tasks)
        elif user_input == "0":
            break
        else:
            print("Invalid input.")
            continue
    
if __name__ == "__main__":
    main()