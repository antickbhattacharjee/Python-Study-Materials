def counting_sort(arr):
    if not arr:
        return arr

    # 1. Find the range (max value)
    max_val = max(arr)
    
    # 2. Initialize count array with zeros
    # size is max_val + 1 to include the index for the max value itself
    count = [0] * (max_val + 1)
    
    # 3. Store the count of each element
    for num in arr:
        count[num] += 1
        
    # 4. Update count[i] to store the actual position of this element in output
    # Each index now contains the number of elements less than or equal to i
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # 5. Build the output array
    output = [0] * len(arr)
    
    # Iterate in REVERSE to maintain stability
    for num in reversed(arr):
        # Position is count[num] - 1 because Python uses 0-based indexing
        output[count[num] - 1] = num
        count[num] -= 1  # Decrement count for potential duplicate values
        
    return output

# Example Usage
data = [4, 2, 2, 8, 3, 3, 1]
sorted_data = counting_sort(data)
print(f"Sorted Array: {sorted_data}")
    
'''
arr=[4, 2, 2, 8, 3, 3, 1] -> max=8
count=[0,1,2,2,1,0,0,0,1]
count=[0,1,3,5,6,6,6,6,7]
arr=[1, 2, 2, 3, 3, 4, 8]
count=[0,0,1,3,6,6,6,6,6]
'''
