# 7. Nested Functions
# nested_functions_scope.py

def outer():
    x = "outer variable"

    def inner():
        nonlocal x
        x = "inner variable"
        print("Inner x:", x)

    inner()
    print("Outer x:", x)

outer()
