print("""
      1. Python
      2. Java
      3. Php
      """)
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("You have selected Python")  
    case 2:
        print("You have selected Java")
    case 3:
        print("You have selected Php")
    case _:
        print("Invalid choice")