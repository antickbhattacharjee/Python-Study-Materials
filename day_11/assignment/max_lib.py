# create library to find maximum between 3 numbers without using max() function and list

def find_maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 20
    num3 = 15
    maximum = find_maximum(num1, num2, num3)
    print(f"The maximum between {num1}, {num2}, and {num3} is {maximum}")

''' 
Why if __name__ == "__main__": is used in Python scripts?
The if __name__ == "__main__": construct in Python is used to determine whether 
a script is being run as the main program or if it is being imported as a module in another script.
When a Python script is run, the special built-in variable __name__ is set to "__main__". 
However, if the script is imported as a module in another script, __name__ is set to the name of the script/module.
This allows you to include code that should only execute when the script is run directly, and not when it is imported. 
This is useful for testing or demonstrating functionality without executing that code during an import.
'''