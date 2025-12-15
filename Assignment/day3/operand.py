
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)

if __name__ == "__main__":
    result1 = calculate(10, 5, add)
    print(f"10 + 5 = {result1}")  

    result2 = calculate(10, 5, subtract)
    print(f"10 - 5 = {result2}")  

    result3 = calculate(10, 5, multiply)
    print(f"10 * 5 = {result3}") 

    result4 = calculate(10, 5, divide)
    print(f"10 / 5 = {result4}")  
   
    result5 = calculate(7.5, 2.5, add)
    print(f"7.5 + 2.5 = {result5}")  

    try:
        result6 = calculate(10, 0, divide)
        print(f"10 / 0 = {result6}")
    except ValueError as e:
        print(f"Error: {e}")  
   
    result7 = calculate(-10, 5, subtract)
    print(f"-10 - 5 = {result7}")  
