import json

#=====================   HANDLE INPUT  ======================
def is_empty(parameter):
    return not parameter

def validate_student_name(student_name):
    if is_empty(student_name):
        print("Student Name Can't Be Empty")
        return False
    if len(student_name.split()) < 2:
        print("Both First Name And Surname Is Required")
        return False
    all_name = student_name.split()
    for name in all_name:
        if any(char.isdigit() for char in name):
            print("Student Name Must Be A Valid String e.g Amara Okafor")
            return False
    return True

def validating_name():
    while True:
        student_name = input("\nEnter A Student Name: ").strip().title()
        validation = validate_student_name(student_name)  
        if not validation:
            continue
        else:
            break
    return student_name

def add_student(students):
    student_name = validating_name()
    if student_name in students:
        print(f"{student_name} already exist")
        return
    students[student_name] = {}
    print("✅ Student Successfully Added") 

def add_subject():
    while True:
        subject_name = input("\nEnter Subject Name: ").strip().title()

        if is_empty(subject_name):
            print("Subject Name Can't Be Empty")
            continue

        if subject_name.isdigit():
            print("Subject Name Must Be A Valid String e.g Mathematics")
            continue
    
        break
    return subject_name

def add_score():
    while True:
        subject_score = input("\nEnter Subject Score: ").strip()
        if subject_score == "":
            print("Subject Score Can't Be Empty")
            continue

        if not subject_score.isdigit():
            print("Subject Score Must Be A Valid Integer e.g 67")
            continue
        
        # if len(subject_score) > 3 or (len(subject_score) == 3 and (int(subject_score[0]) > 1 or int(subject_score[1]) > 0 or int(subject_score[2]) > 0)):
        if not 0 <= int(subject_score) <= 100:
            print("Score Must Be Between 0 and 100")
            continue
        break
    return int(subject_score)

def confirm_student(students):
    while True:
        student_name = validating_name()
        if student_name not in students:
            print("The Name You Entered Is Not In The Student List. Kindly Add The Student First.\n")
            print(f"This Are The Name Of Available Student\n{list(students)}")
            continue
        break
    return student_name

def add_student_info(students):
    if is_empty(students):
        print("No Available student")
        return
    
    student_name = confirm_student(students)
    subject_name = add_subject()
    subject_score = add_score()
    
    if subject_name not in students[student_name]:
        students[student_name][subject_name] = [] 
    students[student_name][subject_name].append(subject_score)
    print("✅ Score Is Added Successfully!")
#=======================  HANDLE REPORT  ========================
def calculate_grade(average):
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100")
    
    if 0 <= average < 60:
        grade = "F"
        point = 0.0
    elif 60 <= average < 70:
        grade = "D"
        point = 1.0
    elif 70 <= average < 80:
        grade = "C"
        point = 2.0
    elif 80 <= average < 90:
        grade = "B"
        point = 3.0
    elif 90 <= average <= 100:
        grade = "A"
        point = 4.0
    return (grade, point)

def student_summary(student_name, scores):
    subject_scores = {}
    list_of_scores = []
    for subject_name, subject_score in scores.items():
        if is_empty(subject_score):
            continue
        
        average = sum(subject_score)/len(subject_score)
        grade, gpa = calculate_grade(average)
        
        subject_scores[subject_name] = average, grade ,gpa
        
        list_of_scores.extend(subject_score)
    if is_empty(list_of_scores):
        raise ValueError("Student has no record on scores")
    overall_average = sum(list_of_scores) / len(list_of_scores)
    grade, gpa = calculate_grade(overall_average)
    
    subject_averages =  {
        "name": student_name,
        "subjects": subject_scores,
        "overall_average": round(overall_average, 1),
        "grade": grade,
        "gpa": gpa
    }
    return subject_averages

def format_student_report(summary):
    student_report = ""
    student_report += f"\nSTUDENT: {summary['name']}\n{"-"*50}\n"
    for subject, subject_score in summary["subjects"].items():
        student_report += f"{subject:<20}  {subject_score[0]:>15.1f}  {subject_score[1]:>10}  {subject_score[2]:>10}\n"
    student_report += f"{"-"*50 + "\n"}Overall Average: {summary['overall_average']:>20} {summary['grade']:>10} {summary['gpa']:>10}\n"
    return student_report

def write_report(reports):
    if is_empty(reports):
        print("No Record To Export")
        return reports
    with open("report.txt", "w") as file:
        file.write("="*50+"\n")
        file.write("CLASS REPORT — YEAR 10A".center(50, " ") +"\n")
        file.write("="*50+"\n")
        
        for report in reports:
            result = format_student_report(report)
            file.write(result)
            
        file.write("\nCLASS RANKING\n")
        file.write("-"*50 + "\n")
        for num, rep in enumerate(reports, 1):
            file.write(f"{num}. {rep['name']:<15}   {rep['overall_average']}\n")
        
        print("✅ Report successfully exported to report.txt")

def display_student_report(students, name):
    if name not in students:
        print(f"❌ Student '{name}' not found.")
        return  
    try:
        summary = student_summary(name, students[name])  
    except ValueError:
        print(f"{name} has no record on score")    
        return
    result = format_student_report(summary)
    print(result)
    print("=" * 50 + "\n")
#=======================    RANKING      ========================

def class_ranking(ranks):
    if is_empty(ranks):
        print("No Record Of Student")
        return
    print("\nCLASS RANKING\n")
    print("-"*50 + "\n")
    for num, rep in enumerate(ranks, 1):
        print(f"{num}. {rep['name']:<15}   {rep['overall_average']}\n")
         
def rank_students(students):
    students_report = []
    
    if is_empty(students):
        return students_report
    for student in students:
        if is_empty(students[student]):
            continue
        try:
            student_report = student_summary(student, students[student])
        except ValueError:
            continue
        students_report.append(student_report)
    sort_student_report = sorted(students_report, key=lambda report: report["overall_average"], reverse=True)
    return sort_student_report

# ===================== SAVE AND LOAD DATA   =====================

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
        
        
def load_students():
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
            if isinstance(students, dict):
                return students
            else:
                return {}
    except FileNotFoundError:
        return {}  
    except json.JSONDecodeError:
        return {}
# ======================= PROGRAM ENTRY ===========================
    
def main():
    print("🎓 Welcome to the Student Grade Management System!\n")
    students = load_students()
    
    while True:
        print("="*32)
        print("STUDENT GRADE MANAGEMENT".center(32))
        print("="*32)
        print(
"""
    1. Add Student
    2. Add Scores
    3. View Student Report
    4. View Class Ranking
    5. Export Class Report
    6. Exit
"""
)
        user_input = input("> ").strip()
        if user_input == "1":
            add_student(students)
            save_students(students)
        elif user_input == "2":
            add_student_info(students)
            save_students(students)
        elif user_input == "3":
            student_name = validating_name()
            display_student_report(students, student_name)
        elif user_input == "4":
            ranks = rank_students(students)
            class_ranking(ranks)
        elif user_input == "5":
            result = rank_students(students)
            write_report(result)
        elif user_input == "6":
            break
        else:
            print("❌ Invalid choice.")
            
if __name__ == "__main__":
    main()



































































































































































# """
# Project 1.3 — Student Grade Calculator & Report Generator
# A comprehensive grade management system for teachers
# """

# # Step 1 — Data Model
# students = {}

# # Step 2 — Grade Calculator Function
# def calculate_grade(average):
#     """
#     Convert numeric average to letter grade and GPA
    
#     Args:
#         average (float): Numeric average score
    
#     Returns:
#         tuple: (letter_grade, gpa)
#     """
#     if average >= 90:
#         return ('A', 4.0)
#     elif average >= 80:
#         return ('B', 3.0)
#     elif average >= 70:
#         return ('C', 2.0)
#     elif average >= 60:
#         return ('D', 1.0)
#     else:
#         return ('F', 0.0)


# # Step 3 — Student Summary Function
# def get_student_summary(name, scores_dict):
#     """
#     Calculate comprehensive statistics for a single student
    
#     Args:
#         name (str): Student's name
#         scores_dict (dict): Dictionary of subjects and their score lists
    
#     Returns:
#         dict: Summary containing subject averages, overall average, grade, and GPA
#     """
#     summary = {
#         'name': name,
#         'subjects': {},
#         'overall_average': 0.0,
#         'letter_grade': '',
#         'gpa': 0.0
#     }
    
#     # Calculate average for each subject
#     subject_averages = []
#     for subject, scores in scores_dict.items():
#         if scores:  # Check if there are scores
#             avg = sum(scores) / len(scores)
#             letter, gpa = calculate_grade(avg)
#             summary['subjects'][subject] = {
#                 'average': avg,
#                 'letter': letter,
#                 'gpa': gpa,
#                 'scores': scores
#             }
#             subject_averages.append(avg)
    
#     # Calculate overall average
#     if subject_averages:
#         summary['overall_average'] = sum(subject_averages) / len(subject_averages)
#         summary['letter_grade'], summary['gpa'] = calculate_grade(summary['overall_average'])
    
#     return summary


# # Step 4 — Ranking Function
# def get_class_ranking():
#     """
#     Rank all students by overall average (highest to lowest)
    
#     Returns:
#         list: Sorted list of student summaries
#     """
#     rankings = []
    
#     for name, scores in students.items():
#         summary = get_student_summary(name, scores)
#         rankings.append(summary)
    
#     # Sort by overall average in descending order
#     rankings.sort(key=lambda student: student['overall_average'], reverse=True)
    
#     return rankings


# # Step 5 — Report Writer Function
# def generate_report(filename='class_report.txt'):
#     """
#     Generate and save a formatted class report to a file
    
#     Args:
#         filename (str): Output filename
#     """
#     rankings = get_class_ranking()
    
#     with open(filename, 'w') as f:
#         # Header
#         f.write("=" * 50 + "\n")
#         f.write("   CLASS REPORT — YEAR 10A\n")
#         f.write("=" * 50 + "\n\n")
        
#         # Individual student reports
#         for summary in rankings:
#             f.write(f"STUDENT: {summary['name']}\n")
#             f.write("-" * 50 + "\n")
            
#             # Subject breakdown
#             for subject, data in summary['subjects'].items():
#                 f.write(f"{subject:<20} {data['average']:>5.1f}    "
#                        f"{data['letter']:>1}    {data['gpa']:.1f}\n")
            
#             f.write("-" * 50 + "\n")
#             f.write(f"Overall Average: {summary['overall_average']:>5.1f}   "
#                    f"{summary['letter_grade']:>1}    {summary['gpa']:.1f}\n\n")
        
#         # Class Rankings
#         f.write("\n" + "=" * 50 + "\n")
#         f.write("CLASS RANKING\n")
#         f.write("-" * 50 + "\n")
        
#         for rank, summary in enumerate(rankings, 1):
#             f.write(f"{rank}. {summary['name']:<25} {summary['overall_average']:>5.1f}\n")
        
#         f.write("=" * 50 + "\n")
    
#     print(f"✅ Report successfully generated: {filename}")


# # Display Functions
# def display_student_report(name):
#     """Display a formatted report for a single student"""
#     if name not in students:
#         print(f"❌ Student '{name}' not found.")
#         return
    
#     summary = get_student_summary(name, students[name])
    
#     print("\n" + "=" * 50)
#     print(f"STUDENT REPORT: {name}")
#     print("=" * 50)
    
#     for subject, data in summary['subjects'].items():
#         print(f"{subject:<20} {data['average']:>5.1f}    "
#               f"{data['letter']:>1}    {data['gpa']:.1f}")
#         print(f"  Test Scores: {data['scores']}")
    
#     print("-" * 50)
#     print(f"Overall Average: {summary['overall_average']:>5.1f}   "
#           f"{summary['letter_grade']:>1}    {summary['gpa']:.1f}")
#     print("=" * 50 + "\n")


# def display_class_ranking():
#     """Display class rankings to console"""
#     rankings = get_class_ranking()
    
#     print("\n" + "=" * 50)
#     print("CLASS RANKING")
#     print("=" * 50)
    
#     for rank, summary in enumerate(rankings, 1):
#         print(f"{rank}. {summary['name']:<25} "
#               f"{summary['overall_average']:>5.1f}  ({summary['letter_grade']})")
    
#     print("=" * 50 + "\n")


# # Data Management Functions
# def add_student(name):
#     """Add a new student to the system"""
#     if name in students:
#         print(f"⚠️  Student '{name}' already exists.")
#         return
    
#     students[name] = {}
#     print(f"✅ Student '{name}' added successfully.")


# def add_subject_scores(name, subject, scores):
#     """
#     Add or update scores for a subject
    
#     Args:
#         name (str): Student name
#         subject (str): Subject name
#         scores (list): List of test scores
#     """
#     if name not in students:
#         print(f"❌ Student '{name}' not found.")
#         return
    
#     students[name][subject] = scores
#     print(f"✅ Added {len(scores)} score(s) for {subject} to {name}'s record.")


# def list_all_students():
#     """Display all students in the system"""
#     if not students:
#         print("📋 No students in the system.")
#         return
    
#     print("\n" + "=" * 50)
#     print("ALL STUDENTS")
#     print("=" * 50)
    
#     for i, name in enumerate(sorted(students.keys()), 1):
#         subject_count = len(students[name])
#         print(f"{i}. {name} ({subject_count} subject(s))")
    
#     print("=" * 50 + "\n")


# # Step 6 — Interactive Menu
# def display_menu():
#     """Display the main menu"""
#     print("\n" + "=" * 50)
#     print("📚 STUDENT GRADE MANAGEMENT SYSTEM")
#     print("=" * 50)
#     print("1. Add New Student")
#     print("2. Add Subject Scores")
#     print("3. View Student Report")
#     print("4. View Class Ranking")
#     print("5. List All Students")
#     print("6. Generate Full Report (to file)")
#     print("7. Load Sample Data")
#     print("8. Exit")
#     print("=" * 50)


# def load_sample_data():
#     """Load sample data for testing"""
#     global students
    
#     students = {
#         "Amara Okafor": {
#             "Mathematics": [85, 90, 78],
#             "English": [72, 88, 91],
#             "Physics": [65, 70, 80]
#         },
#         "Chidi Nwachukwu": {
#             "Mathematics": [78, 82, 75],
#             "English": [85, 80, 88],
#             "Physics": [70, 72, 68]
#         },
#         "Fatima Bello": {
#             "Mathematics": [70, 75, 72],
#             "English": [78, 76, 80],
#             "Physics": [72, 68, 74]
#         },
#         "Kwame Mensah": {
#             "Mathematics": [92, 95, 88],
#             "English": [90, 88, 93],
#             "Physics": [85, 89, 91]
#         }
#     }
    
#     print("✅ Sample data loaded successfully!")


# def main():
#     """Main program loop"""
#     print("🎓 Welcome to the Student Grade Management System!")
    
#     while True:
#         display_menu()
#         choice = input("Enter your choice (1-8): ").strip()
        
#         if choice == '1':
#             name = input("Enter student name: ").strip()
#             if name:
#                 add_student(name)
#             else:
#                 print("❌ Name cannot be empty.")
        
#         elif choice == '2':
#             name = input("Enter student name: ").strip()
#             subject = input("Enter subject name: ").strip()
#             scores_input = input("Enter scores (comma-separated): ").strip()
            
#             try:
#                 scores = [float(s.strip()) for s in scores_input.split(',')]
#                 add_subject_scores(name, subject, scores)
#             except ValueError:
#                 print("❌ Invalid score format. Please enter numbers separated by commas.")
        
#         elif choice == '3':
#             name = input("Enter student name: ").strip()
#             display_student_report(name)
        
#         elif choice == '4':
#             if students:
#                 display_class_ranking()
#             else:
#                 print("📋 No students in the system.")
        
#         elif choice == '5':
#             list_all_students()
        
#         elif choice == '6':
#             if students:
#                 filename = input("Enter filename (default: class_report.txt): ").strip()
#                 if not filename:
#                     filename = 'class_report.txt'
#                 generate_report(filename)
#             else:
#                 print("📋 No students to generate report for.")
        
#         elif choice == '7':
#             load_sample_data()
        
#         elif choice == '8':
#             print("👋 Thank you for using the Grade Management System!")
#             break
        
#         else:
#             print("❌ Invalid choice. Please enter a number between 1 and 8.")


# # Run the program
# if __name__ == "__main__":
#     main()
    