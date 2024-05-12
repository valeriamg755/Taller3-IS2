from MultiLayer.StudentManager import StudentManager

class CLI:
    def __init__(self):
        self.student_manager = StudentManager()

    def display_menu(self):
        print("Student Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student")
        print("4. View All Students")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.view_all_students()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        self.student_manager.add_student(name, roll_number)
        print("Student added successfully")

    def remove_student(self):
        roll_number = input("Enter student roll number to remove: ")
        if self.student_manager.remove_student(roll_number):
            print("Student removed successfully")
        else:
            print("Student not found")

    def update_student(self):
        roll_number = input("Enter student roll number to update: ")
        new_name = input("Enter updated name: ")
        if self.student_manager.update_student(roll_number, new_name):
            print("Student updated successfully")
        else:
            print("Student not found")

    def view_all_students(self):
        students = self.student_manager.get_all_students()
        if students:
            print("All Students:")
            for student in students:
                print(f"Name: {student['name']}, Roll Number: {student['roll_number']}")
        else:
            print("No students found")


if __name__ == "__main__":
    cli = CLI()
    cli.run()