students = 3
subjects = 5
highest_mark = 0
for i in range(students):
    marks = list(map(int, input(f"Enter marks for student {i+1} in {subjects} subjects: ").split()))
    total_marks = sum(marks)
    if total_marks > highest_mark:
        highest_mark = total_marks
    average_mark = sum(marks) / subjects
    if average_mark >= 90:
        grade = 'A'
    elif average_mark >= 80:
        grade = 'B'
    elif average_mark >= 70:
        grade = 'C'
    elif average_mark >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Student {i+1}: Grade = {grade}")
print(f"Highest Total Marks: {highest_mark}")
'''
students = 3
subjects = 5
highest_mark = 0
for i in range(students):
    total_marks = 0
    for j in range(subjects):
        mark = int(input(f"Enter mark for student {i+1} in subject {j+1}: "))
        total_marks += mark
    if total_marks > highest_mark:
        highest_mark = total_marks
    average_mark = total_marks / subjects
    if average_mark >= 90:
        grade = 'A'
    elif average_mark >= 80:
        grade = 'B'
    elif average_mark >= 70:
        grade = 'C'
    elif average_mark >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Student {i+1}: Total = {total_marks} Grade = {grade}")
print(f"Highest Total Marks: {highest_mark}")
'''