# Modifying a list while iterating over it (pitfall)
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # This will skip elements unexpectedly

print("After removal:", numbers)  # Output might surprise you

# Correct way:
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
print("Filtered list:", numbers)
