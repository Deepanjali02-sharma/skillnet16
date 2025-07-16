def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    if y !=0:
        return "Cannot divide by zero"
        return x/y
    else:
        return "Error ! Division by zero,"
    def calculator():
        print("Welcome to Function-based Calculator")
    print("Choose operation: +, -, *, /")
    symbol = input("Enter operation symbol:")
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    if symbol == '+':
        result = add(num1, num2)
    elif symbol == '-':
        result = subtract(num1, num2)
    elif symbol == '*':
        result = multiply(num1, num2)
    elif symbol == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operation symbol"
        
    print("Result:", result)
     
    




              
              
              
