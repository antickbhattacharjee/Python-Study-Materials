word = list(input("Enter a word: ").split())
if len(word) != 1:
    print("Please enter a single word.")
    exit()
palindrome = False
for i in range(len(word[0]) // 2):
    if word[0][i] == word[0][-i - 1]:
        palindrome = True
    else:
        palindrome = False
        break
if palindrome:
    print(f"{word[0]} is a palindrome")
else:
    print(f"{word[0]} is not a palindrome")