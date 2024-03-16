# main.py

from student_manager import StudentRecordManager
from menu import print_menu, update_menu

manager = StudentRecordManager()

def update_options(student_id, update_choice):
    if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        if update_choice == "1":
            attribute = "Name"
        elif update_choice == "2":
            attribute = "Email"
        elif update_choice == "3":
            attribute = "Department"
        elif update_choice == "4":
            attribute = "DOB"
        elif update_choice == "5":
            attribute = "CGPA"
        elif update_choice == "6":
            attribute = "Address"
        elif update_choice == "7":
            attribute = "Phone_number"
        elif update_choice == "8":
            attribute = "Marked"
        value = input(f"Enter new value: ")
        manager.update_student(student_id, {attribute: value})
    else:
        print("Invalid choice. Please choose a number from 1 to 9.")

while True:
    if choice == "1":
        student_id = input("Enter Student ID: ")
        while(manager.check_id(student_id)):
          print(f"\n\nID: {student_id} already exists, Try again.")
          student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        address = input("Enter Address: ")
        phone_number = input("Enter Phone Number: ")
        manager.add_student(
            student_id, name, dob, address, email, phone_number, department, cgpa
        )

    elif choice == "2":
        student_id = input("Enter Student ID to delete: ")
        manager.delete_student(student_id)

    elif choice == "3":
        student_id = input("Enter Student ID to update: ")
        while True:
            update_menu()
            update_choice = input("Enter your choice (1-9): ")
            if update_choice == "9":
                break
            else:
                update_options(student_id, update_choice)

    elif choice == "4":
        student_id = input("Enter Student ID to display details: ")
        manager.display_student(student_id)

    elif choice == "5":
        manager.sort_student()

    elif choice == "6":
        manager.see_all_students()

    elif choice == "7":
        student_id = input("Enter Student ID to mark: ")
        manager.mark_student(student_id)

    elif choice == "8":
        query = input("Enter search query: ")
        manager.search_student(query)

    elif choice == "9":
        name = input("Enter file name: ")
        manager.save_records_to_file(name)

    elif choice == "10":
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
