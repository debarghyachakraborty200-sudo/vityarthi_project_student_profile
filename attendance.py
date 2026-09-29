# attendance.py
# attendance percentage and eligibility

import validation
import student


def calculate_attendance(total_classes, attended):
    """Returns absent classes, attendance percentage and status."""
    absent = total_classes - attended
    if total_classes == 0:
        percentage = 0.0
    else:
        percentage = attended / total_classes * 100
    if percentage >= 75:
        status = "ELIGIBLE"
    else:
        status = "NOT ELIGIBLE"
    return absent, percentage, status


def enter_attendance():
    roll_no = student.find_student()
    if roll_no is None:
        return
    data = student.students[roll_no]
    total_classes = validation.get_number("Total classes: ", 1, 500)
    attended = validation.get_number("Classes attended: ", 0, total_classes)

    absent, percentage, status = calculate_attendance(total_classes, attended)
    data["total_classes"] = total_classes
    data["attended"] = attended
    data["absent"] = absent
    data["attendance"] = percentage
    data["status"] = status
    print("Absent     :", absent)
    print("Attendance : {:.1f}%".format(percentage))
    print("Status     :", status)
