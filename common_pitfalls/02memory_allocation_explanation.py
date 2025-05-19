# Demonstrating Python memory allocation for immutable vs mutable objects

a = 1000
b = 1000
print(a is b)  # False for large ints because different objects

x = [1, 2, 3]
y = x
print(x is y)  # True: both refer to same list object

# Immutable objects like strings and ints create new objects for new values
# Mutable objects like lists share references unless explicitly copied
