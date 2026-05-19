# check number is armstrong number or not
number= int(input("Enter number: "))
n = len(str(number))
number_copy = number
sum = 0
while number > 0:
    
    for i in range(n):
        digit = number % 10
        sum += digit ** n
        number //= 10
    if sum == number_copy:
        print("Armstrong number")
        break
    else:
        print("Not an Armstrong number")
        break  