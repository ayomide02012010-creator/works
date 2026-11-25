import json, datetime
tasks = [
    {
        "id" : "a1b2c3d4",
        "title" : "Submit assingment",
        "category" : "Study",
        "priority" : "High",
        "due-date" : "2026-12-01",
        "completed" : False,
        "created_at" : "2026-11-25"
    }
]
# ================= Helper Function ====================
def is_empty(parameter):
    return not parameter
    
# ==================== Display Menu ======================
def display_menu():
    print("="*50 + "\n")
    print("WELCOME TO Text-Based To-Do List Application")
    print("="*50 + "\n")
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
        i_d = input("Enter task id: ").strip()
        if is_empty(i_d):
            print("id can't be Empty.\n")
            continue
        break
    while True:
        title = input("Enter task Title: ").strip().capitalize()
        if is_empty(title):
            print("Task Title can't be Empty.\n")
            continue
        break
    while True:
        category = input("Enter task Category: ").strip().capitalize()
        if is_empty(category):
            print("Task Title can't be Empty.\n")
            continue
        break
    while True:
        priority = input("Enter task Priority: ").strip().capitalize()
        if is_empty(priority):
            print("Task Title can't be Empty.\n")
            continue
        break
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        if is_empty(due_date):
            print("due date can't be empty.\n")
            continue
        break
    
    each_task = {
        "id" : i_d,
        "title": title,
        "category" : category,
        "priority" : priority,
        "due-date" : due_date,
        "completed" : False,
        "created_at" : datetime.date.today().isoformat()
    }
    
    tasks.append(each_task)
    
# ================== PROGRAM ENTRY ========================
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        user_input = input("> ")
        if user_input == "1":
            add_tasks(tasks)
            save_tasks(tasks)
            print("Task successfully saved\n")
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        elif user_input == "0":
            break
        else:
            print("Invalid input.")
            continue
    
if __name__ == "__main__":
    main()