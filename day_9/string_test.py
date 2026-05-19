'''
s = "hello"
s[0] = "H"   # ❌ Error: strings are immutable

s = "hello"
s = "H" + s[1:]
print(s)    # "Hello"


# Reverse a string
s = "Python"
print(s[::-1])    # nohtyP
'''
# Count vowels in a string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Vowel count:", count)
