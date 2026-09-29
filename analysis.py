# analysis.py
# small class summary using loops and lists
# (uses the ideas of counting, summation, maximum and sorting)

import student


def class_summary():
    if len(student.students) == 0:
        print("No students added yet.")
        return

    # only students whose marks are calculated
    done = []
    for roll_no in student.students:
        if student.students[roll_no]["grade"] != "-":
            done.append(roll_no)
    if len(done) == 0:
        print("No student has a calculated result yet (use option 3).")
        return

    total_percentage = 0
    passed = 0
    failed = 0
    topper = done[0]
    for roll_no in done:
        data = student.students[roll_no]
        total_percentage = total_percentage + data["percentage"]
        if data["result"] == "PASS":
            passed = passed + 1
        else:
            failed = failed + 1
        if data["percentage"] > student.students[topper]["percentage"]:
            topper = roll_no

    average = total_percentage / len(done)

    print()
    print("Students with result :", len(done))
    print("Class average        : {:.1f}%".format(average))
    print("Passed               :", passed)
    print("Failed               :", failed)
    print("Topper               : {} ({:.1f}%)".format(
        student.students[topper]["name"], student.students[topper]["percentage"]))

    print()
    print("Rank list:")
    ranked = sort_by_percentage(done)
    rank = 1
    for roll_no in ranked:
        data = student.students[roll_no]
        print("{}. {} - {:.1f}%".format(rank, data["name"], data["percentage"]))
        rank = rank + 1

    print()
    print("Students with low attendance (below 75%):")
    found = False
    for roll_no in student.students:
        data = student.students[roll_no]
        if data["total_classes"] > 0 and data["status"] == "NOT ELIGIBLE":
            print("-", data["name"], "({:.1f}%)".format(data["attendance"]))
            found = True
    if not found:
        print("None")


def sort_by_percentage(roll_list):
    """Selection sort - highest percentage first. Returns a new list."""
    items = roll_list[:]
    for i in range(len(items)):
        best = i
        for j in range(i + 1, len(items)):
            if student.students[items[j]]["percentage"] > student.students[items[best]]["percentage"]:
                best = j
        items[i], items[best] = items[best], items[i]
    return items
