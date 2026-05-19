# Check list elements frequency and print which element is there how many times. store values which are single in list and save at uniqe, add values which have duplicate values at duplicate. do not store duplicate values at duplicate.

my_list=input("Enter the list elements: ")
uniq=[]
duplicate=[]
count=0
for i in my_list:
    if my_list.count(i)==1:
        uniq.append(i)
    elif my_list.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
# print(f"{i} is present {my_list.count(i)} times")
print("Unique elements are:",uniq)
print("Duplicate elements are:",duplicate)
'''

# Check frequency froma string of each word
my_string = input("Enter a string: ")
words = my_string.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
for word, count in frequency.items():
    print(f"'{word}' is present {count} times")
'''