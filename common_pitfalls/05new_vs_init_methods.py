class MyClass:
    def __new__(cls):
        print("Creating instance (new)")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("Initializing instance (init)")

obj = MyClass()

# Output:
# Creating instance (new)
# Initializing instance (init)
