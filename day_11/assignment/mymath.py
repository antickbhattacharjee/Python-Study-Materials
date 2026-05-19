# creating module for mathematical operations +,_,*,/,//,** for n numbers

def add(*args):
    return sum(args)

def subtract(*args):
    if len(args) == 0:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

def power(a, b):
    return a ** b