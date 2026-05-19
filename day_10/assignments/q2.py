''' q2
Question:
Write a Python function is_prime(n) that returns True if the number n is prime, otherwise returns False.
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Example usage:
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False