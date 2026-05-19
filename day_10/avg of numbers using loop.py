# avg of numbers using loop and function

def calculate_average(nums):
    total = 0
    count = len(nums)
    for num in nums:
        total += num
    return total / count if count > 0 else 0

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("The average is:", calculate_average(numbers))