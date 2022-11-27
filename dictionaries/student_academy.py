students_grades = {}
n = int(input())
for i in range(n):
    students = input()
    grade = float(input())
    if students not in students_grades.keys():
        students_grades[students] = []
        students_grades[students].append(grade)
    else:
        students_grades[students].append(grade)
for name, grades in students_grades.items():
    averageGrade = sum(students_grades[name]) / len(students_grades[name])
    if averageGrade >= 4.50:
        print(f'{name} -> {averageGrade:.2f}')
