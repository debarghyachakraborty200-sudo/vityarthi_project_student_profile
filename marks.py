# marks.py
# everything related to marks, percentage, grade and result

import validation
import student

SUBJECTS = ["English", "Physics", "Chemistry", "Mathematics", "Computer Science"]


def enter_marks():
    roll_no = student.find_student()
    if roll_no is None:
        return
    data = student.students[roll_no]
    print("Enter marks for", data["name"], "(0 to 100)")
    for subject in SUBJECTS:
        data["marks"][subject] = validation.get_number(subject + ": ", 0, 100)
    print("Marks saved.")


def calculate_percentage(marks):
    """Returns total and percentage for a marks dictionary."""
    total = 0
    for subject in marks:
        total = total + marks[subject]
    percentage = total / len(SUBJECTS)
    return total, percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def get_result(percentage):
    if percentage >= 40:
        return "PASS"
    return "FAIL"


def update_result():
    """Menu option 3 - calculates everything for one student."""
    roll_no = student.find_student()
    if roll_no is None:
        return
    data = student.students[roll_no]
    if len(data["marks"]) < len(SUBJECTS):
        print("Marks are not entered yet. Use option 2 first.")
        return
    total, percentage = calculate_percentage(data["marks"])
    data["total"] = total
    data["percentage"] = percentage
    data["grade"] = calculate_grade(percentage)
    data["result"] = get_result(percentage)
    print("Total      :", total, "/ 500")
    print("Percentage : {:.1f}%".format(percentage))
    print("Grade      :", data["grade"])
    print("Result     :", data["result"])
