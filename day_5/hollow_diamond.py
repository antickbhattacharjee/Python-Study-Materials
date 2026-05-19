# hollow diamond pattern
n=5
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=2*i-1:
        if k==1 or k==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
        k=k+1
    print()
    i=i+1
i=n-1
while i>=1:
    j=1
    while j<=n-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=2*i-1:
        if k==1 or k==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
        k=k+1
    print()
    i=i-1   