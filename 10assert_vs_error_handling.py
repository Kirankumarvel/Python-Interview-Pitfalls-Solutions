# 10. Assert Statements
# assert_vs_error_handling.py

def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

try:
    print(divide(10, 0))
except AssertionError as e:
    print(f"AssertionError: {e}")
