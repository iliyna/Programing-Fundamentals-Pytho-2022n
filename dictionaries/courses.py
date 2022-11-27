course_student = {}
course_students = input()
while course_students != 'end':
    if course_students == 'end':
        break
    course, students = course_students.split(' :')
    if course not in course_student:
        course_student[course] = []
    course_student[course].append(students)
    course_students = input()
for course in course_student.keys():
    print(f'{course}: {len(course_student[course])}')
    for student in course_student[course]:
        print(f'--{"".join(student)}')
