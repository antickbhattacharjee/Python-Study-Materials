
n=5
# for hollow diamond
for i in range(1, n+1):
    for k in range((n+1)-i):
        print(" ", end="")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print("\n")
for i in range(n-1, 0, -1):
    for k in range((n+1)-i):
        print(" ", end="")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print("\n")


# for solid diamond
for i in range(1, n+1):
    for k in range((n+1)-i):
        print(" ", end="")
    for j in range(1, i):
        print("* ", end="")
    print("\n")
for i in range(n, 0, -1):
    for k in range(n-i):
        print(" ", end="")
    for j in range(1, i+1):
        print("* ", end="")
    print("\n")