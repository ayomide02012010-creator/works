from report import calculate_grade
import pytest

def test_calculate_grade_returns_A():
    assert(calculate_grade(120)) == ("A", 4.0)
    
def test_calculate_grade_returns_C():
    assert(calculate_grade(75)) == ("C", 2.0)
    
def test_calculate_grade_returns_F():
    assert(calculate_grade(55)) == ("F", 0.0)
