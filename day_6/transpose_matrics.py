# Transpose a matrix
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
b=[]
for i in range(len(a[0])):
    row=[]
    for j in range(len(a)):
        row.append(a[j][i])
    b.append(row)
print(b)