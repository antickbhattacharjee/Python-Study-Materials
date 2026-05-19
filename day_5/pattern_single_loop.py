n=5
for i in range(1,n*2):
    if i<=n:
        print(" "*(n-i),"* "*i,end="")
        print("\n")
    elif i>n:
        print(" "*(i-n),"* "*(2*n-i),end="")
        print("\n")