# usinf nested for loop hollow parallelogram
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(n):
        if i == 0 or i == n - 1 or k == 0 or k == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()