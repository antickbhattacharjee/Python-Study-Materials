# Perfect Circle pattern using nested for loop
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if (i==0 and j>0 and j<n-1) or (i==n-1 and j>0 and j<n-1) or (j==0 and i>0 and i<n-1) or (j==n-1 and i>0 and i<n-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
