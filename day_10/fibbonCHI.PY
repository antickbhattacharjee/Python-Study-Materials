# !st 10 fibbonachi series using function
def fibbonachi(a,b,n):
    if n==0:
        print("\nDone")
    else:
        print(f"{a},",end="")
        fibbonachi(b,a+b,n-1)
fibbonachi(0,1,10)