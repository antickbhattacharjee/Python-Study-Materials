# Using list and tuple to find unique and duplicate values

my_tuple = (5,7,3,8,6,3,9,8)
unique_values = []
duplicated_values = []

for x in my_tuple:
    count = 0
    for y in my_tuple:
        if x == y:
            count += 1
    if count == 1:
        # appears only once -> unique
        if x not in unique_values:
            unique_values.append(x)
    else:
        # appears more than once -> duplicated (store once)
        if x not in duplicated_values:
            duplicated_values.append(x)

print("Unique values:", unique_values)
print("Duplicated values:", duplicated_values)