# swapusing bubble sort
n=[5,9,3,21,1]
for i in range(len(n)):
    for j in range(0,len(n)-i-1):
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
print(n)