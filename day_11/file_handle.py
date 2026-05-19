#file = open("sample.txt", "r")  # "r" = read mode

# write
with open("output.txt", "w") as file:
    file.write("This is a test.")

# read
with open("output.txt", "r") as file:
    #content = file.read()
    #content = file.readline()    # Reads one line
    content = file.readlines()   # Reads all lines into a list
    print(content)

# read + write
with open("output.txt", "r+") as file:
    content = file.read()
    print("Before write:", content)

    file.seek(0)  # Move cursor to beginning
    file.write("Appended line.")

with open("output.txt", "r") as file:
    print("After write:", file.read())

# append
with open("output.txt", "a") as file:
    file.write("\nLet's learn together!")

with open("output.txt", "r") as file:
    print(file.read())


# copying content one to another file
with open("input.txt", "r") as inp, open("copy.txt", "w") as out:
    for line in inp:
        out.write(line)
        
