for i in range(1, 10):
    if i%2 == 0 :
        print("Even:", i)

# Same program in one line
[print("Even:", i) for i in range(1, 10) if i%2 == 0]

# One liner program to print every prime number between 1-10
print([num for num in range(2, 11) if all(num%i != 0 for i in range(2, int(num**0.5)+1))])

# One liner to check given number is armsdtrong or not
num = 153; print(f"{num} is Armstrong" if num == sum(int(digit)**3 for digit in str(num)) else f"{num} is not Armstrong")

# One liner loop tocheck input is prime or composite
n=int(input("Enter a number: ")); print(f"{n} is Prime" if n > 1 and all(n%i != 0 for i in range(2, int(n**0.5)+1)) else f"{n} is Composite")