# Initial unsorted list
mylist = [5, 3, 7, 2, 6, 1, 4, 8]
my_list = sorted(mylist)
# Print sorted list
print("Sorted list:", my_list)

# Binary Search manually
target = 6  # You can change this value to test other targets

low = 0
high = len(my_list)
found = False

while low <= high:
    mid = (low + high) // 2
    print("Current low:", low, "high:", high, "mid:", mid)
    if my_list[mid] == target:
        print("Element", target, "found at index", mid)
        found = True
        break
    elif my_list[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element", target, "not found in the list.")
