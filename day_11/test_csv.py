import csv
'''
# Insert Data in single column
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    numbers = [10, 20, 30, 40, 50]
    for number in numbers:
        writer.writerow([number])

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    numbers = [10, 20, 30, 40, 50]
    writer.writerow(numbers)

with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        numbers = list(map(int, row))
        average = sum(numbers) / len(numbers)
        print(f'Average: {average}')
'''
with open('data.csv', mode='r+', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        numbers = list(map(int, row))
        average = sum(numbers) / len(numbers)
        # Save the Average in that file
        file.seek(0, 2)  # Move to the end of the file
        writer = csv.writer(file)
        writer.writerow([average])

        print(f'Average: {average}')

    
    