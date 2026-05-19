try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Enter a valid number.")
else:
    print("Division successful. Result:", result)
finally:
    print("End of program.")