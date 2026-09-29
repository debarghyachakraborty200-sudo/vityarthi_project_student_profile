# report.py
# shows the report of one student and the list of all students

import student
import marks


def display_report():
    roll_no = student.find_student()
    if roll_no is None:
        return
    data = student.students[roll_no]

    if len(data["marks"]) < len(marks.SUBJECTS) or data["total_classes"] == 0:
        print("Marks and attendance both must be entered before viewing the report.")
        print("Use options 2, 3 and 4 first.")
        return

    print()
    print("-" * 40)
    print("        STUDENT REPORT")
    print("-" * 40)
    print()
    print("Roll No:", roll_no)
    print("Name:", data["name"])
    print()
    print("Marks:")
    for subject in marks.SUBJECTS:
        print("{:<17}: {}".format(subject, data["marks"][subject]))
    print()
    print("Total Marks      : {}/500".format(data["total"]))
    print("Percentage       : {:.1f}%".format(data["percentage"]))
    print("Grade            :", data["grade"])
    print("Result           :", data["result"])
    print()
    print("Attendance:")
    print("Total Classes    :", data["total_classes"])
    print("Attended         :", data["attended"])
    print("Absent           :", data["absent"])
    print("Attendance       : {:.1f}%".format(data["attendance"]))
    print("Status           :", data["status"])
    print()
    print("-" * 40)


def view_all_students():
    if len(student.students) == 0:
        print("No students added yet.")
        return
    print()
    print("{:<8}{:<15}{:<8}{:<7}{:<8}{:<14}".format(
        "Roll", "Name", "Perc.", "Grade", "Att.", "Status"))
    print("-" * 60)
    for roll_no in student.students:
        data = student.students[roll_no]
        print("{:<8}{:<15}{:<8}{:<7}{:<8}{:<14}".format(
            roll_no, data["name"],
            "{:.1f}".format(data["percentage"]), data["grade"],
            "{:.1f}".format(data["attendance"]), data["status"]))
