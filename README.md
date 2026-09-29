# Student Academic Performance and Attendance Management System

**Name:** Debarghya Chakraborty
**Registration No:** 26BCE11053
**Faculty:** Devaraju S
**Course project:** VITyarthi - Build Your Own Project (Python)

## Overview

This is a small menu-driven Python program. It stores the marks and attendance of many students and calculates the total, percentage, grade, pass/fail result, attendance percentage and attendance eligibility. It can also show a report for one student and a small summary of the whole class.

## Features

- Add students (roll number and name)
- Enter marks in 5 subjects (English, Physics, Chemistry, Mathematics, Computer Science)
- Calculate total, percentage, grade and PASS/FAIL result
- Enter attendance and calculate absent classes, attendance percentage and ELIGIBLE / NOT ELIGIBLE
- Full student report with marks and attendance
- List of all students
- Class summary (average, topper, pass/fail count, rank list, low attendance list)
- Input checking for every value the user types

## Technologies used

- Python 3 (no external libraries, nothing to install)
- Concepts: variables, input/output, lists, dictionaries, if-elif-else, for and while loops, functions, modules
- Git and GitHub for version control

## Project structure

```
student_project/
├── main.py            # menu and main loop
├── student.py         # add student, students dictionary
├── marks.py           # marks, total, percentage, grade, result
├── attendance.py      # attendance calculation
├── report.py          # student report and all students list
├── analysis.py        # class summary and rank list
├── validation.py      # input checking
├── tests/
│   └── test_project.py
├── docs/              # diagrams
├── README.md
└── statement.md
```

## How to install and run

1. Install Python 3 from python.org (Python 3.8 or newer is fine).
2. Download or clone this repository:
   ```
   git clone <your-repository-link>
   cd student_project
   ```
3. Run the program:
   ```
   python main.py
   ```
   (On some systems use `python3 main.py`.)
4. Choose options from the menu. A normal order is 1 -> 2 -> 3 -> 4 -> 5.

## How to test

Run the test file from the project folder:

```
python tests/test_project.py
```

It checks the percentage, grade, result and attendance calculations and the rank sorting. All 5 tests should print PASS.

Manual testing: try wrong inputs such as marks 150, marks -5, letters instead of numbers, attended classes more than total classes, or a roll number with letters. The program should show a message and ask again.

## Sample

Input: Roll 101, Rahul, marks 82, 76, 71, 88, 91, total classes 100, attended 86.

```
Total Marks      : 408/500
Percentage       : 81.6%
Grade            : A
Result           : PASS
Attendance       : 86.0%
Status           : ELIGIBLE
```

## Screenshots

Add your own screenshots in a `screenshots` folder and link them here, for example:

```
![Menu](screenshots/menu.png)
![Report](screenshots/report.png)
```

## Limitations

Data is stored only while the program is running. When the program is closed, all data is lost.
