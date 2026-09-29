# Student Academic Performance and Attendance Management System
# Name: Debarghya Chakraborty
# Reg No: 26BCE11053

import student
import marks
import attendance
import report
import analysis


def show_menu():
    print()
    print("=" * 40)
    print(" STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. Enter Marks")
    print("3. Calculate Percentage and Grade")
    print("4. Enter Attendance")
    print("5. View Student Report")
    print("6. View All Students")
    print("7. Class Summary")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            student.add_student()
        elif choice == "2":
            marks.enter_marks()
        elif choice == "3":
            marks.update_result()
        elif choice == "4":
            attendance.enter_attendance()
        elif choice == "5":
            report.display_report()
        elif choice == "6":
            report.view_all_students()
        elif choice == "7":
            analysis.class_summary()
        elif choice == "8":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


main()
