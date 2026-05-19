'''
age = int(input("Enter your age: "))
has_id = bool(input("Do you have an ID? (True/False): "))
print(strtobool(has_id))
'''
age = 16
had_id = False
if age >= 18:
    if has_id:
        print("You can vote")
    else:
        print("You cannot vote without an ID")      
else:
    print("You are not 18+")


'''
If Statement
if condition:
    execution

If Else
if condition:
    execution
else:
    execution

Elif
if condition:
    execution
elif condition:
    execution
else:
    execution

Nested If
if condition:
    if condition:
        execution
    else:
        execution
else:
    execution
'''
