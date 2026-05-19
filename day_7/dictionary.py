student = {
    "name": "Alice",
    "age": 22,
    "course": "Python"
}

print(student["name"])       # Alice
print(student.get("age"))    # 22

student["age"] = 23             # Update value
student["email"] = "a@x.com"    # Add new key-value

print(student)

print(student.keys())      # dict_keys(['name', 'age'])

for key, value in student.items():
    print(key, "->", value)

del student["course"]           # Remove a key
print(student)
student.pop("email")            # Also removes a key
print(student)
student.clear()                 # Clears entire dictionary
print(student)

