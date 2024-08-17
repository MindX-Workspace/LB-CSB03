class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

if __name__ == "__main__":
    manager = GradeManager()

    student1 = Student("Alice")
    student2 = Student("Bob")
    manager.add_student(student1)
    manager.add_student(student2)

    student1.add_grade(85)
    student1.add_grade(90)
    student2.add_grade(75)

    print(student1.calculate_average())