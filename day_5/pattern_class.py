# Hollow diamond pattern, 9 rows

for i in range(1, 10):
    if i <= 5:
        print(" " * (5 - i) + "* " * i)
    else:
        print(" " * (i - 5) + "* " * (10 - i))