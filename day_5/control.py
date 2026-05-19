
# break
for i in range(1, 10):
    if i == 5:
        break
    print("Count:", i)  # Output: 1 2 3 4

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print("Printing:", i)  # Output: 1 2 4 5

# used to skip writing body temporarily
for i in range(5):
    if i == 3:
        pass  # Will add handling for 3 later
    else:
        print("Processing:", i)
    #print("Processing:", i)
