# take a string input and separate every word in a list without splitting
input_string = "we are doing python"
separated_words = []
word= ""
for char in input_string:
    if char==" " or word==input_string[-1]:
        separated_words.append(word)
        word= ""
    else:
        word+=char
        

print(separated_words)