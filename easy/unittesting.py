def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return "Division by zero is not allowed."
    return a/b


print("Unit Testing Results")
print("-"*25)

tests = [
    ("Addition", add(10,5), 15),
    ("Subtraction", sub(10,5), 5),
    ("Multiplication", mul(10,5), 50),
    ("Division", div(10,5), 2),
    ("Division by Zero", div(10,0), "Division by zero is not allowed.")
]

for name, actual, expected in tests:
    if actual == expected:
        print(name, ": PASS")
    else:
        print(name, ": FAIL")