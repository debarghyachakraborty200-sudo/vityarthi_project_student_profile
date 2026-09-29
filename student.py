# student.py
# stores all the students in a dictionary
# key = roll number, value = another dictionary with the details

import validation

students = {}


def add_student():
    roll_no = validation.get_roll_no()
    if roll_no in students:
        print("A student with this roll number already exists.")
        return
    name = validation.get_name()
    students[roll_no] = {
        "name": name,
        "marks": {},
        "total": 0,
        "percentage": 0.0,
        "grade": "-",
        "result": "-",
        "total_classes": 0,
        "attended": 0,
        "absent": 0,
        "attendance": 0.0,
        "status": "-",
    }
    print("Student added successfully.")


def find_student():
    """Asks for a roll number and returns the roll number if the student exists."""
    if len(students) == 0:
        print("No students added yet. Please add a student first.")
        return None
    roll_no = validation.get_roll_no()
    if roll_no not in students:
        print("Student not found.")
        return None
    return roll_no
