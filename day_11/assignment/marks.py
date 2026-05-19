# take user input 3 students marks in file and check highest marks
with open("assignment/marks.txt", "w") as f:
    for _ in range(3):
        name = input("Enter student name: ")
        score = input("Enter student marks: ")
        f.write(f"{name} {score}\n")

with open("assignment/marks.txt", "r") as file:
    content = file.read().split()
    marks = {}
    for i in range(0, len(content), 2):
        name = content[i]
        score = int(content[i + 1])
        marks[name] = score

    highest_scorer = max(marks, key=marks.get)
    print(f"Highest scorer: {highest_scorer} with marks {marks[highest_scorer]}")