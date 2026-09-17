# Student Record Management System

students = []
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Branch": branch,
        "Marks": marks
    }

    students.append(student)

    print("Student record added successfully!")


def display_students():
    print("\n--- All Student Records ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("Name   :", student["Name"])
        print("Roll No:", student["Roll No"])
        print("Branch :", student["Branch"])
        print("Marks  :", student["Marks"])
        print("-------------------------")


def search_student():
    print("\n--- Search Student ---")

    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["Name"].lower() == name.lower():
            print("\nStudent Found!")
            print("Name   :", student["Name"])
            print("Roll No:", student["Roll No"])
            print("Branch :", student["Branch"])
            print("Marks  :", student["Marks"])
            found = True

    if not found:
        print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")

    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["Roll No"] == roll_no:
            students.remove(student)
            print("Student record deleted successfully!")
            return

    print("Student record not found.")


while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")