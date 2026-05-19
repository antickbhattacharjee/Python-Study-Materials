try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
