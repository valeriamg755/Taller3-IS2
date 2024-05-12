class Database:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number):
        self.students.append({'name': name, 'roll_number': roll_number})

    def remove_student(self, roll_number):
        for student in self.students:
            if student['roll_number'] == roll_number:
                self.students.remove(student)
                return True
        return False

    def update_student(self, roll_number, new_name):
        for student in self.students:
            if student['roll_number'] == roll_number:
                student['name'] = new_name
                return True
        return False

    def get_all_students(self):
        return self.students
