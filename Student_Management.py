print("Student Management System is starting...")

class StudentManagementSystem:
    def __init__(self):
        self.students = []  # List to store student records

    def add_student(self):
        student_id = input("Enter student ID: ")
        if any(student['student_id'] == student_id for student in self.students):
            print("Student ID already exists. Try again.")
            return

        name = input("Enter student name: ")
        surname = input("Enter student surname: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")

        student = {
            'name': name,
            'surname': surname,
            'student_id': student_id,
            'age': age,
            'grade': grade,
            'attendance': 0  
        }
        
        self.students.append(student)
        print(f"Student {name} {surname} added successfully!")

    def update_student(self):
        student_id = input("Enter the student ID to update: ")
        student = next((s for s in self.students if s['student_id'] == student_id), None)

        if student:
            print(f"Updating record for {student['name']} {student['surname']}")
            student['name'] = input(f"Enter new name (current: {student['name']}): ") or student['name']
            student['surname'] = input(f"Enter new surname (current: {student['surname']}): ") or student['surname']
            student['age'] = input(f"Enter new age (current: {student['age']}): ") or student['age']
            student['grade'] = input(f"Enter new grade (current: {student['grade']}): ") or student['grade']
            print("Student record updated successfully.")
        else:
            print("Student ID not found.")

    def delete_student(self):
        student_id = input("Enter the student ID to delete: ")
        student = next((s for s in self.students if s['student_id'] == student_id), None)

        if student:
            self.students.remove(student)
            print(f"Student {student['name']} {student['surname']} deleted successfully.")
        else:
            print("Student ID not found.")

    def search_student(self):
        student_id = input("Enter student ID to search: ")
        student = next((s for s in self.students if s['student_id'] == student_id), None)

        if student:
            print(f"Student found: {student}")
        else:
            print("Student ID not found.")

    def track_attendance(self):
        student_id = input("Enter student ID to track attendance: ")
        student = next((s for s in self.students if s['student_id'] == student_id), None)

        if student:
            attendance_status = input("Enter attendance status (Present/Absent): ").lower()
            if attendance_status == "present":
                student['attendance'] += 1
                print("Attendance marked as present.")
            elif attendance_status == "absent":
                print("Attendance marked as absent.")
            else:
                print("Invalid input. Attendance not updated.")
        else:
            print("Student ID not found.")

    def generate_report(self):
        for student in self.students:
            print(f"\nStudent Report for {student['name']} {student['surname']}")
            print(f"Student ID: {student['student_id']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            print(f"Attendance: {student['attendance']} days")

    def show_menu(self):
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. Search Student")
            print("5. Track Attendance")
            print("6. Generate Student Report")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.search_student()  # Fixed the function call
            elif choice == '5':
                self.track_attendance()
            elif choice == '6':
                self.generate_report()
            elif choice == '7':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance and call the method correctly
if __name__ == "__main__":
    system = StudentManagementSystem()  # Create the system instance
    system.show_menu()  # Call the menu function

input("Press Enter to exit...")
