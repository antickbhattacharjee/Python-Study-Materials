# with single logic
age = 15
if age >= 18:
    print("You are eligible to vote.")

# with else statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")

# with else is
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# nested if ladder
x = -7
if x > 0:
    if x % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Zero or Negative")


