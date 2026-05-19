list1 = [1, 2, 3]
list2 = [1, 4, 3]
list3 = [1, 6, 2]

comparison = [a == b == c for a, b, c in zip(list1, list2, list3)]
print(comparison)