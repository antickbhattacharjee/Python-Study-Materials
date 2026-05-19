# Quick Sort using Python List without user define function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
# Example usage
if __name__ == "__main__":
    sample_array = [3,6,8,10,1,2,1]
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)

'''
Explanation: For example
Given the array [3,6,8,10,1,2,1], the quick_sort function will sort it to [1,1,2,3,6,8,10].
Step 1: Choose a pivot (in this case, 10).
Step 2: Partition the array into three lists:
- Left: [3,6,8,1,2,1] (elements less than pivot)
- Middle: [10] (elements equal to pivot)
- Right: [] (elements greater than pivot)
Step 3: Recursively apply quick_sort to the left and right lists.
Step 4: Combine the sorted left list, middle list, and sorted right list to get the final sorted array.
'''