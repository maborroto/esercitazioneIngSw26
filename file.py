def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise "Division by zero is not supported"
    return a / b
