class StudentRecordManager:
    def __init__(self):
        self.student_records = {}

    def check_id(self, student_id):
      if student_id in self.student_records:
        return True
    
    def add_student(
        self, student_id, name, dob, address, email, phone_number, department, cgpa
    ):
        if student_id not in self.student_records:
            self.student_records[student_id] = {
                "Name": name,
                "Email": email,
                "Department": department,
                "CGPA": cgpa,
                "DOB": dob,
                "Address": address,
                "Phone Number": phone_number,
                "Marked": False,
            }
            print(f"Student {name} added successfully.")
        else:
            print("Student ID already exists.")

    def delete_student(self, student_id):
        if student_id in self.student_records:
            del self.student_records[student_id]
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")

    def update_student(self, student_id, values):
        if student_id in self.student_records:
            for key, value in values.items():
                if key in self.student_records[student_id]:
                    if key == "Marked":
                        if value.lower() == "true":
                            self.student_records[student_id]["Marked"] = True
                            break
                        if value.lower() == "false":
                            self.student_records[student_id]["Marked"] = False
                            break
                    self.student_records[student_id][key] = value
                    print(f"Updated {key} for student ID-9{student_id}.")
                else:
                    print(f"Invalid attribute '{key}' for student record.")
        else:
            print("Student ID not found.")

    def see_all_students(self):
        if not self.student_records:
            print("\nNo records found.")
            return
        print("\nStudent Details:")
        print("----------------")
        print(
            "\tID\t Name\t\t Email\t Department\t CGPA\t\t Date of Birth\t\t Address\t Phone Number"
        )
        print(
            "----------------------------------------------------------------------------------------------------------------------------"
        )
        for student_id, record in self.student_records.items():
            name = record.get("Name")
            email = record.get("Email")
            department = record.get("Department")
            cgpa = str(record.get("CGPA"))
            dob = record.get("DOB")
            address = record.get("Address")
            phone = record.get("Phone Number")
            marked = "**" if record.get("Marked", False) else ""
            print(
                f"{marked}\t{student_id}\t {name}\t {email}\t {department}\t {cgpa}\t\t {dob}\t {address}\t {phone}"
            )

    def display_student(self, student_id):
        if student_id in self.student_records:
            print("\nStudent Details:")
            print("----------------")
            print(
                "\tID\t Name\t\t Email\t Department\t CGPA\t\t Date of Birth\t\t Address\t Phone Number"
            )
            print(
                "----------------------------------------------------------------------------------------------------------------------------"
            )
            record = self.student_records[student_id]
            name = record.get("Name")
            email = record.get("Email")
            department = record.get("Department")
            cgpa = str(record.get("CGPA"))
            dob = record.get("DOB")
            address = record.get("Address")
            phone = record.get("Phone Number")
            marked = "**" if record["Marked"] else ""
            print(
                f"{marked}\t{student_id}\t {name}\t {email}\t {department}\t {cgpa}\t\t {dob}\t {address}\t {phone}"
            )
        else:
            print("Student ID not found.")

    def search_student(self, query):
        student_found = None
        for student_id, record in self.student_records.items():
            for value in record.values():
                if str(value).lower() == query.lower():
                    student_found = student_id
                    break
        if student_found:
            result = self.student_records.get(student_found)
            print(
                f"\n====Record Found!====\nName: {result['Name']}\n"
                f"DOB: {result['DOB']}\n"
                f"Address: {result['Address']}\n"
                f"Email: {result['Email']}\n"
                f"Phone Number: {result['Phone Number']}\n"
                f"Department: {result['Department']}\n"
                f"GPA: {result['CGPA']}"
            )
        else:
            print("No record found.")

    def sort_student(self):
        sorted_records = sorted(self.student_records.items())
        print("\n===== Sorted Student Records By ID =====")
        for student_id, record in sorted_records:
            print(
                f"Student ID: {student_id}, Name: {record['Name']}, CGPA: {record['CGPA']}"
            )

    def mark_student(self, student_id):
        if student_id in self.student_records:
            self.student_records[student_id]["Marked"] = True
            print("\nStudent marked successfully.")
        else:
            print("\nStudent ID not found.")

    def save_records_to_file(self, name):
        try:
            file_name = name + ".txt"
            file = open(file_name, "w")

            for student_id, record in self.student_records.items():
                file.write(f"Student ID: {student_id}\n")
                for key, value in record.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
            file.close()
            print("\nStudent records exported successfully.")
        except:
            print("\nError! Something went wrong.")
