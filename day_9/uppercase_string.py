# Convert every word's first letter to uppercase in a given string without title function.
my_str = input("Enter a string: ")
result = my_str.title()
print("String with every word's first letter capitalized:", result)
###########################################################################
my_str = input("Enter a string: ") # "my name is arnab"
words = my_str.split() # ['my', 'name', 'is', 'arnab']
capitalized_words = ""
for word in words:
    capitalized_word = word[0].upper() + word[1:] # 'Arnab'
    capitalized_words += capitalized_word + " " # "My Name Is Arnab "
print("String with every word's first letter capitalized:", capitalized_words)

