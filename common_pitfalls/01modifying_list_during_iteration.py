# Modifying list while iterating can cause unexpected behavior

numbers = [1, 2, 3, 4, 5]

# Problematic way: removing items while iterating
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)

print("After removal:", numbers)
# Output: [1, 3, 5] (some even numbers skipped)

# Safe way: iterate over a copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)

print("Safely removed evens:", numbers)
# Output: [1, 3, 5]
