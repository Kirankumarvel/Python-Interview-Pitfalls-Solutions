# Using 'is' for value comparison instead of '=='
a = 1000
b = 1000
print(a == b)  # True
print(a is b)  # False (usually) — Do not use 'is' for value equality

# Pitfall: late binding in closures
funcs = []
for i in range(3):
    funcs.append(lambda: i)  # All functions capture the same i

print([f() for f in funcs])  # Output: [2, 2, 2], not [0, 1, 2]

# Fix with default argument binding
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)

print([f() for f in funcs])  # Output: [0, 1, 2]
