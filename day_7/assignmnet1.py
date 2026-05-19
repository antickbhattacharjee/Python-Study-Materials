'''
🧠 Problem Statement: Student Marks Storage and Analysis
You are given a list of students and their marks in 3 subjects: Math, Science, and English.

🎯 Tasks:
Store the data in a dictionary.

Calculate and display the total marks for each student.

Find the student who scored the highest total marks.

Find the average marks per subject.

📝 Sample Data:
students = {
    "Alice": {"Math": 85, "Science": 78, "English": 92},
    "Bob": {"Math": 70, "Science": 82, "English": 88},
    "Charlie": {"Math": 90, "Science": 85, "English": 87}
}

✅ Expected Output:
Total marks:
Alice: 255
Bob: 240
Charlie: 262

Topper: Charlie with 262 marks

Average Marks:
Math: 81.66
Science: 81.66
English: 89.0
'''
# Step 1: Create the dictionary of student marks
students = {
    "Alice": {"Math": 85, "Science": 78, "English": 92},
    "Bob": {"Math": 70, "Science": 82, "English": 88},
    "Charlie": {"Math": 90, "Science": 85, "English": 87}
}

# Step 2: Calculate total marks for each student
totals = {}
for name in students:
    total = 0
    for subject in students[name]:
        total += students[name][subject]
    totals[name] = total

# Step 3: Print total marks
print("Total marks:")
for name in totals:
    print(name + ":", totals[name])

# Step 4: Find the student with highest total
highest_name = ""
highest_score = 0
for name in totals:
    if totals[name] > highest_score:
        highest_score = totals[name]
        highest_name = name

print("\nTopper:", highest_name, "with", highest_score, "marks")

# Step 5: Calculate average marks per subject
subject_totals = {"Math": 0, "Science": 0, "English": 0}
num_students = 0

for name in students:
    num_students += 1
    for subject in students[name]:
        subject_totals[subject] += students[name][subject]

print("\nAverage Marks:")
for subject in subject_totals:
    avg = subject_totals[subject] / num_students
    print(subject + ":", round(avg, 2))