import mymath

print(mymath.add(2, 3))  # Should print 5
print(mymath.add(1, 2, 3, 4))  # Should print 10

print(mymath.subtract(10, 5))  # Should print 5
print(mymath.subtract(20, 5, 3))  # Should print
print(mymath.subtract(2))

print(mymath.multiply(2, 3))  # Should print 6
print(mymath.multiply(2, 3, 4))  # Should print
print(mymath.multiply())

print(mymath.divide(10, 2))  # Should print 5.0
# print(mymath.divide(5, 0))  # Should raise ValueError

print(mymath.floor_divide(10, 3))  # Should print 3
# print(mymath.floor_divide(10, 0))  # Should raise ValueError

print(mymath.power(2, 3))  # Should print 8
print(mymath.power(5, 0))  # Should print 1 14
