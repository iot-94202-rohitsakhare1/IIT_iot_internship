def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


result1 = apply_operation(add, 5, 3) 
print(result1) 

result2 = apply_operation(multiply, 5, 3)  
print(result2)  
