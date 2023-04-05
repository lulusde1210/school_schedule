import pytest
from school_schedule.high_school_student import HighSchoolStudent

def test_new_valid_high_school_student_with_default():
    name = "Ellis"
    grade = "jonior"
    classes = ["Painting"]

    ellis = HighSchoolStudent(name,grade,classes)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.has_parking_privileges 
    assert not ellis.clubs