# validation.py
# small helper functions to take correct input from the user


def get_number(message, low, high):
    """Keeps asking until the user enters a whole number between low and high."""
    while True:
        value = input(message)
        if not value.strip().lstrip("-").isdigit():
            print("Please enter a number only.")
            continue
        value = int(value)
        if value < low or value > high:
            print("Number must be between", low, "and", high)
            continue
        return value


def get_roll_no():
    """Roll number must be a positive number like 101."""
    while True:
        roll_no = input("Enter roll number: ").strip()
        if roll_no.isdigit() and int(roll_no) > 0:
            return roll_no
        print("Roll number should contain only digits, for example 101.")


def get_name():
    """Name should not be empty and should have letters only (spaces allowed)."""
    while True:
        name = input("Enter student name: ").strip()
        if name != "" and name.replace(" ", "").isalpha():
            return name.title()
        print("Name should have only letters.")
