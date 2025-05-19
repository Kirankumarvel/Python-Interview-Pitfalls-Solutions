# 5. Loop Else Clause
# loop_else_example.py

def find_even(nums):
    for num in nums:
        if num % 2 == 0:
            print(f"Found even number: {num}")
            break
    else:
        print("No even numbers found")

find_even([1, 3, 5])
find_even([1, 4, 5])
