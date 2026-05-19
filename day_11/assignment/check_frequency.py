# check frequency of elements in a input.txt

with open("input.txt", "r") as file:
    content = file.read().split()
    frequency = {}

    for word in content:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    print(frequency)