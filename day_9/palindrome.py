
# With Slicing
word = input("Enter a word: ")
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# Without Slicing
word = input("Enter a word: ") # Get user input
reversed_word = "" # Initialize an empty string to hold the reversed word
for char in word:
    reversed_word = char + reversed_word # Prepend each character to build the reversed word
if word == reversed_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
