from report import calculate_grade, student_summary
import pytest

def test_calculate_grade_raises_ValueError_above_100():
    with pytest.raises(ValueError):
        calculate_grade(200)
def test_calculate_grade_raises_ValueError_below_0():
    with pytest.raises(ValueError):
        calculate_grade(-5)
def test_calculate_grade_returns_A():
    assert(calculate_grade(96)) == ("A", 4.0)
    
def test_calculate_grade_returns_C():
    assert(calculate_grade(75)) == ("C", 2.0)

def test_calculate_grade_returns_F():
    assert(calculate_grade(6)) == ("F", 0.0)
    
def test_calculate_grade_returns_maximum():
    assert(calculate_grade(100)) == ("A", 4.0)
    
def test_calculate_grade_returns_minimum():
    assert(calculate_grade(0)) == ("F", 0.0)

def test_student_summary_returns_correct_summary():
    assert(student_summary("Amara Okafor", {
        "Mathematics": [56,67,87],
        "English": [72, 88, 91],
        "Physics": [65, 70, 80]
        }))== {
        'name': 'Amara Okafor', 
        'subjects': {
            'Mathematics': 70.0, 
            'English': 83.66666666666667, 
            'Physics': 71.66666666666667
            }, 
        'overall_average': 75.1,
        'grade': 'C', 
        "gpa": 2.0}
    
def test_student_summary_raises_valueerror():
    with pytest.raises(ValueError):
        student_summary("Amara Okafor", {
            "Mathematics": [],
            "English": [],
            "Physics": []
            }
                        )
        
def test_student_summary_check_empty_subject():
    assert(student_summary("Amara Okafor", {
        "Mathematics": [56,67,87],    
        "English": [72, 88, 91],
        "Physics": []
        })) == {
        'name': 'Amara Okafor', 
        'subjects': {
            'Mathematics': 70.0, 
            'English': 83.66666666666667, 
            }, 
        'overall_average': 76.8,
        'grade': 'C', 
        "gpa": 2.0}
