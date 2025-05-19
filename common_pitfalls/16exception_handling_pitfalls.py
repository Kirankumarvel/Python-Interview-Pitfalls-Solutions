# Catching broad exceptions, which is a bad practice
try:
    x = int("abc")
except:
    print("Something went wrong")  # This hides real bugs

# Better practice: catch specific exceptions
try:
    x = int("abc")
except ValueError:
    print("ValueError caught: Invalid literal for int()")

# Avoid bare except and always handle/log appropriately
