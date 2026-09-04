"""
Project 1.3 — Student Grade Calculator & Report Generator
A comprehensive grade management system for teachers
"""

# Step 1 — Data Model
students = {}

# Step 2 — Grade Calculator Function
def calculate_grade(average):
    """
    Convert numeric average to letter grade and GPA
    
    Args:
        average (float): Numeric average score
    
    Returns:
        tuple: (letter_grade, gpa)
    """
    if average >= 90:
        return ('A', 4.0)
    elif average >= 80:
        return ('B', 3.0)
    elif average >= 70:
        return ('C', 2.0)
    elif average >= 60:
        return ('D', 1.0)
    else:
        return ('F', 0.0)


# Step 3 — Student Summary Function
def get_student_summary(name, scores_dict):
    """
    Calculate comprehensive statistics for a single student
    
    Args:
        name (str): Student's name
        scores_dict (dict): Dictionary of subjects and their score lists
    
    Returns:
        dict: Summary containing subject averages, overall average, grade, and GPA
    """
    summary = {
        'name': name,
        'subjects': {},
        'overall_average': 0.0,
        'letter_grade': '',
        'gpa': 0.0
    }
    
    # Calculate average for each subject
    subject_averages = []
    for subject, scores in scores_dict.items():
        if scores:  # Check if there are scores
            avg = sum(scores) / len(scores)
            letter, gpa = calculate_grade(avg)
            summary['subjects'][subject] = {
                'average': avg,
                'letter': letter,
                'gpa': gpa,
                'scores': scores
            }
            subject_averages.append(avg)
    
    # Calculate overall average
    if subject_averages:
        summary['overall_average'] = sum(subject_averages) / len(subject_averages)
        summary['letter_grade'], summary['gpa'] = calculate_grade(summary['overall_average'])
    
    return summary


# Step 4 — Ranking Function
def get_class_ranking():
    """
    Rank all students by overall average (highest to lowest)
    
    Returns:
        list: Sorted list of student summaries
    """
    rankings = []
    
    for name, scores in students.items():
        summary = get_student_summary(name, scores)
        rankings.append(summary)
    
    # Sort by overall average in descending order
    rankings.sort(key=lambda student: student['overall_average'], reverse=True)
    
    return rankings


# Step 5 — Report Writer Function
def generate_report(filename='class_report.txt'):
    """
    Generate and save a formatted class report to a file
    
    Args:
        filename (str): Output filename
    """
    rankings = get_class_ranking()
    
    with open(filename, 'w') as f:
        # Header
        f.write("=" * 50 + "\n")
        f.write("   CLASS REPORT — YEAR 10A\n")
        f.write("=" * 50 + "\n\n")
        
        # Individual student reports
        for summary in rankings:
            f.write(f"STUDENT: {summary['name']}\n")
            f.write("-" * 50 + "\n")
            
            # Subject breakdown
            for subject, data in summary['subjects'].items():
                f.write(f"{subject:<20} {data['average']:>5.1f}    "
                       f"{data['letter']:>1}    {data['gpa']:.1f}\n")
            
            f.write("-" * 50 + "\n")
            f.write(f"Overall Average: {summary['overall_average']:>5.1f}   "
                   f"{summary['letter_grade']:>1}    {summary['gpa']:.1f}\n\n")
        
        # Class Rankings
        f.write("\n" + "=" * 50 + "\n")
        f.write("CLASS RANKING\n")
        f.write("-" * 50 + "\n")
        
        for rank, summary in enumerate(rankings, 1):
            f.write(f"{rank}. {summary['name']:<25} {summary['overall_average']:>5.1f}\n")
        
        f.write("=" * 50 + "\n")
    
    print(f"✅ Report successfully generated: {filename}")


# Display Functions
def display_student_report(name):
    """Display a formatted report for a single student"""
    if name not in students:
        print(f"❌ Student '{name}' not found.")
        return
    
    summary = get_student_summary(name, students[name])
    
    print("\n" + "=" * 50)
    print(f"STUDENT REPORT: {name}")
    print("=" * 50)
    
    for subject, data in summary['subjects'].items():
        print(f"{subject:<20} {data['average']:>5.1f}    "
              f"{data['letter']:>1}    {data['gpa']:.1f}")
        print(f"  Test Scores: {data['scores']}")
    
    print("-" * 50)
    print(f"Overall Average: {summary['overall_average']:>5.1f}   "
          f"{summary['letter_grade']:>1}    {summary['gpa']:.1f}")
    print("=" * 50 + "\n")


def display_class_ranking():
    """Display class rankings to console"""
    rankings = get_class_ranking()
    
    print("\n" + "=" * 50)
    print("CLASS RANKING")
    print("=" * 50)
    
    for rank, summary in enumerate(rankings, 1):
        print(f"{rank}. {summary['name']:<25} "
              f"{summary['overall_average']:>5.1f}  ({summary['letter_grade']})")
    
    print("=" * 50 + "\n")


# Data Management Functions
def add_student(name):
    """Add a new student to the system"""
    if name in students:
        print(f"⚠️  Student '{name}' already exists.")
        return
    
    students[name] = {}
    print(f"✅ Student '{name}' added successfully.")


def add_subject_scores(name, subject, scores):
    """
    Add or update scores for a subject
    
    Args:
        name (str): Student name
        subject (str): Subject name
        scores (list): List of test scores
    """
    if name not in students:
        print(f"❌ Student '{name}' not found.")
        return
    
    students[name][subject] = scores
    print(f"✅ Added {len(scores)} score(s) for {subject} to {name}'s record.")


def list_all_students():
    """Display all students in the system"""
    if not students:
        print("📋 No students in the system.")
        return
    
    print("\n" + "=" * 50)
    print("ALL STUDENTS")
    print("=" * 50)
    
    for i, name in enumerate(sorted(students.keys()), 1):
        subject_count = len(students[name])
        print(f"{i}. {name} ({subject_count} subject(s))")
    
    print("=" * 50 + "\n")


# Step 6 — Interactive Menu
def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("📚 STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add New Student")
    print("2. Add Subject Scores")
    print("3. View Student Report")
    print("4. View Class Ranking")
    print("5. List All Students")
    print("6. Generate Full Report (to file)")
    print("7. Load Sample Data")
    print("8. Exit")
    print("=" * 50)


def load_sample_data():
    """Load sample data for testing"""
    global students
    
    students = {
        "Amara Okafor": {
            "Mathematics": [85, 90, 78],
            "English": [72, 88, 91],
            "Physics": [65, 70, 80]
        },
        "Chidi Nwachukwu": {
            "Mathematics": [78, 82, 75],
            "English": [85, 80, 88],
            "Physics": [70, 72, 68]
        },
        "Fatima Bello": {
            "Mathematics": [70, 75, 72],
            "English": [78, 76, 80],
            "Physics": [72, 68, 74]
        },
        "Kwame Mensah": {
            "Mathematics": [92, 95, 88],
            "English": [90, 88, 93],
            "Physics": [85, 89, 91]
        }
    }
    
    print("✅ Sample data loaded successfully!")


def main():
    """Main program loop"""
    print("🎓 Welcome to the Student Grade Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '1':
            name = input("Enter student name: ").strip()
            if name:
                add_student(name)
            else:
                print("❌ Name cannot be empty.")
        
        elif choice == '2':
            name = input("Enter student name: ").strip()
            subject = input("Enter subject name: ").strip()
            scores_input = input("Enter scores (comma-separated): ").strip()
            
            try:
                scores = [float(s.strip()) for s in scores_input.split(',')]
                add_subject_scores(name, subject, scores)
            except ValueError:
                print("❌ Invalid score format. Please enter numbers separated by commas.")
        
        elif choice == '3':
            name = input("Enter student name: ").strip()
            display_student_report(name)
        
        elif choice == '4':
            if students:
                display_class_ranking()
            else:
                print("📋 No students in the system.")
        
        elif choice == '5':
            list_all_students()
        
        elif choice == '6':
            if students:
                filename = input("Enter filename (default: class_report.txt): ").strip()
                if not filename:
                    filename = 'class_report.txt'
                generate_report(filename)
            else:
                print("📋 No students to generate report for.")
        
        elif choice == '7':
            load_sample_data()
        
        elif choice == '8':
            print("👋 Thank you for using the Grade Management System!")
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 8.")


# Run the program
if __name__ == "__main__":
    main()