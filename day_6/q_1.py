
my_list = []
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
    
my_list = list(set(my_list))
my_list.sort(reverse=True)
print("Final list after removing duplicates and sorting in descending order:")
print(my_list)