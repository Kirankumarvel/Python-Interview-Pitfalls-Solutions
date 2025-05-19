class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 4))  # Output: 7

# Monkey patching: change add method at runtime
def new_add(self, a, b):
    print("Adding numbers with new method")
    return a + b + 1  # modified behavior

Calculator.add = new_add
print(calc.add(3, 4))  # Output: Adding numbers with new method \n 8
