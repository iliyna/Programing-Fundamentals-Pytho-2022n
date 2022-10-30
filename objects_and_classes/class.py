class Class:

    def __init__(self, class_name, students_count=22):
        self.class_name = class_name
        self.students_count = students_count
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if self.students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            self.students_count -= 1

    def get_average_grade(self):
        return sum(self.grades) / len(self.students)

    def __repr__(self):
        return f"The students in {self.class_name}: {', '.join(self.students)}" \
               f".\nAverage grade: {Class.get_average_grade(self):.2f}" \



a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
