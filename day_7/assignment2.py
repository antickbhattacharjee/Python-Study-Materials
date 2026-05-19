# create employee salary dictionary, employee_id and salary. Increment salary by 10% for each employee who are earing less than 30000. Display updated dictionary
employee_salary = {
    'E001': 25000,
    'E002': 32000,
    'E003': 28000,
    'E004': 40000,
    'E005': 15000
}
for emp_id in employee_salary:
    if employee_salary[emp_id] < 30000:
        employee_salary[emp_id] = int(employee_salary[emp_id] * 1.1)
print("Updated Employee Salary Dictionary:")
print(employee_salary)
