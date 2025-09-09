"""
Student Grade System
Covers: input, variables, data types, if-else, loops, functions, dicts,
lists, nesting, random (optional ID), scope, global vars/constants, docstrings
"""

import random  # to assign random student IDs

# ---- Global Constant ----
PASS_MARKS = 40

# ---- Global Variable ----
students = []  # list of dictionaries to store student data


# ---- Functions ----

def add_student():
    """Add a new student with name and marks"""
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))

    # Calculate grade
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= PASS_MARKS:
        grade = "D"
    else:
        grade = "Fail"

    student_id = random.randint(1000, 9999)  # unique ID
    student = {"id": student_id, "name": name, "marks": marks, "grade": grade}
    students.append(student)

    print(f"✅ Student {name} added with ID {student_id}")


def display_students():
    """Display all students with details"""
    if not students:
        print("⚠️ No students found.")
        return

    print("\n--- Student List ---")
    for stu in students:
        print(f"ID: {stu['id']} | Name: {stu['name']} | Marks: {stu['marks']} | Grade: {stu['grade']}")


def search_student():
    """Search for a student by ID"""
    sid = int(input("Enter student ID to search: "))
    for stu in students:
        if stu["id"] == sid:
            print(f"🔎 Found: {stu['name']} - Marks: {stu['marks']} - Grade: {stu['grade']}")
            return
    print("❌ Student not found.")


def class_average():
    """Calculate and display class average marks"""
    if not students:
        print("⚠️ No students available.")
        return

    total = sum(stu["marks"] for stu in students)
    avg = total / len(students)
    print(f"📊 Class Average Marks: {round(avg, 2)}")


def student_menu():
    """Main menu"""
    while True:
        print("\n--- Student Grade System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student by ID")
        print("4. Show Class Average")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_average()
        elif choice == "5":
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


# ---- Run Program ----
student_menu()
