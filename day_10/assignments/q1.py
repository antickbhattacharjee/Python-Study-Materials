''' q1 
Question:
Write a Python function shopping_cart(customer_name, *items, discount=0) that:

Takes customer name (string).

Accepts any number of items as ("item_name", price) tuples.

Applies discount (if given).

Returns the final bill amount.
'''
def shopping_cart(customer_name, *items, discount=0):
    total = sum(price for item, price in items)
    if discount:
        total -= total * (discount / 100)
    return f"Customer: {customer_name}, Final Bill Amount: ${total:.2f}"
# Example usage:
print(shopping_cart("Alice", ("apple", 100), ("banana", 50), discount=10))
# Example usage:
print(shopping_cart("Bob", ("milk", 200), ("bread", 150)))