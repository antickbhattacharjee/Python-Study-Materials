''' q3
Question:
Write a Python function fibonacci(n) that prints the first n terms of the Fibonacci series.
'''
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()  # for newline after printing the series
# Example usage:
fibonacci(10)