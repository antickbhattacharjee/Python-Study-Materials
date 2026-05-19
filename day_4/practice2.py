# Find max and min
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

'''
if a<b<c:
    print(f"{c} is the largest number\n{a} is the smallest number")
elif a<c<b:
    print(f"{b} is the largest number\n{a} is the smallest number")
elif b<a<c:
    print(f"{c} is the largest number\n{b} is the smallest number")
elif b<c<a:
    print(f"{a} is the largest number\n{b} is the smallest number")
elif c<a<b:
    print(f"{b} is the largest number\n{c} is the smallest number")
else:
    print(f"{a} is the largest number\n{c} is the smallest number")



if (a >= b and a >= c):
    print("Largest is", a)
elif b >= a and b >= c:
    print("Largest is", b)
else:
    print("Largest is", c)
if (a <= b and a <= c):
    print("Smallest is", a)
elif b <= a and b <= c:
    print("Smallest is", b)
else:
    print("Smallest is", c)
'''

'''
If a,b,c are equal or any 2 are equal then print like "max - a b or min - a b"
'''

if a == b == c:
    print(f"All numbers are equal: {a}")
elif a >= b and a >= c:
    if b == c:
        print(f"Max is {a}\nMin is {b} and {c}")
    else:
        if b < c:
            print(f"Max is {a}\nMin is {b}")
        else:
            print(f"Max is {a}\nMin is {c}")
elif b >= a and b >= c:
    if a == c:
        print(f"Max is {b}\nMin is {a} and {c}")
    else:
        if a < c:
            print(f"Max is {b}\nMin is {a}")
        else:
            print(f"Max is {b}\nMin is {c}")
else:
    if a == b:
        print(f"Max is {c}\nMin is {a} and {b}")
    else:
        if a < b:
            print(f"Max is {c}\nMin is {a}")
        else:
            print(f"Max is {c}\nMin is {b}")
