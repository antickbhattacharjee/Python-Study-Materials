# Check words by alphabet and count frequencies like dog=good=2, pot=top=2, eat=1, eaten=1.
words = ["dog", "good", "pot", "top", "eat", "eaten"]
word_frequencies = {}

for word in words:
    word = word.lower()
    word = ''.join(sorted(set(word)))   
    if word not in word_frequencies:
        word_frequencies[word] = 1
    else:
        word_frequencies[word] += 1

print(f"{word_frequencies}\n")
