# Functions to be tested

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


# Test Cases

print("Unit Testing Results")
print("-" * 30)

# Test 1
expected = 15
actual = add(10, 5)
if expected == actual:
    print("Test 1 (Addition): PASS")
else:
    print("Test 1 (Addition): FAIL")

# Test 2
expected = 5
actual = subtract(10, 5)
if expected == actual:
    print("Test 2 (Subtraction): PASS")
else:
    print("Test 2 (Subtraction): FAIL")

# Test 3
expected = 50
actual = multiply(10, 5)
if expected == actual:
    print("Test 3 (Multiplication): PASS")
else:
    print("Test 3 (Multiplication): FAIL")

# Test 4
expected = 2
actual = divide(10, 5)
if expected == actual:
    print("Test 4 (Division): PASS")
else:
    print("Test 4 (Division): FAIL")

# Test 5
expected = "Division by zero is not allowed."
actual = divide(10, 0)
if expected == actual:
    print("Test 5 (Division by Zero): PASS")
else:
    print("Test 5 (Division by Zero): FAIL")