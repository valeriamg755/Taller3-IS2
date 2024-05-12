from MultiLayer.database import Database

class StudentManager:
    def __init__(self):
        self.db = Database()

    def add_student(self, name, roll_number):
        self.db.add_student(name, roll_number)

    def remove_student(self, roll_number):
        return self.db.remove_student(roll_number)

    def update_student(self, roll_number, new_name):
        return self.db.update_student(roll_number, new_name)

    def get_all_students(self):
        return self.db.get_all_students()