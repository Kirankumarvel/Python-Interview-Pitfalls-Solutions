# 4. List Modification
# list_modification.py

numbers = [1, 2, 3, 4]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)
