# 9. Generators
# generator_example.py

def countdown(num):
    while num > 0:
        yield num
        num -= 1

for n in countdown(5):
    print(n)
