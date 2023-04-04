import pytest
from school_schedule.student import Student


def test_new_valid_student():
    name = "Falipe"
    grade = "Junior"
    classes = ["Art", "Math", "Computer Science"]

    falipe = Student(name, grade, classes)

    assert falipe.name == name
    assert falipe.grade == grade
    assert falipe.get_num_classes() == 3


def test_add_class():
    student = Student("Ty", "Senior", ["Art", "Math", "Computer Science"])
    class_name = "PE"

    result = student.add_class(class_name)

    assert len(student.classes) == 4
    assert class_name in student.classes
    assert result == ["Art", "Math", "Computer Science", "PE"]


def test_get_num_classes_return_len():
    # Arrange
    student = Student("Ty", "junior", ["Math", "Spanish"])

    # Act
    result = student.get_num_classes()

    # Assert
    assert result == 2


def test_get_num_classes_no_classes():
    # Arrange
    student = Student("Ty", "junior", [])

    # Act
    result = student.get_num_classes()

    # Assert
    assert result == 0
