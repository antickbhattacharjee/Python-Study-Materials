n = int(input("Enter a number: "))  #1224

# Ensure at least double-digit number
if n < 10:
    n = int(input("Enter at least a double-digit number: "))

seen = set()  # to track numbers we've already seen

while n != 1 and n not in seen:
    seen.add(n) #seen = {1224,85,}
    current_sum_of_squares = 0
    temp_n = n
    while temp_n > 0:
        digit = temp_n % 10 #digit=2
        current_sum_of_squares += digit ** 2 #85
        temp_n //= 10   #0
    n = current_sum_of_squares #85

if n == 1:
    print("The number is a Happy Number.")
else:
    print("The number is NOT a Happy Number (it entered a cycle).")

print("The final value is:", n)
