import csv
with open('numbers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    numbers = []
    for i in range(10):
        num = int(input(f'Enter number {i+1}: '))
        numbers.append(num)
    writer.writerow(numbers)
with open('numbers.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        numbers = list(map(int, row))
        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]
print(f'Even numbers: {len(even_numbers)}')
print(f'Odd numbers: {len(odd_numbers)}')
        