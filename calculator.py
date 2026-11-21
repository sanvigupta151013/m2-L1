
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

operations = print("chose the operation you want to perform: 1. addition 2.subtracion 3.multiplication 4.divide")
choice = int(input("enter your choice: "))

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

if choice == 1:
    
    result = add(a, b)
    print(result)

elif choice == 2:
    result = subtract(a, b)
    print(result)

elif choice == 4:
    result = divide(a, b)
    print(result)

else:
    result = multiply(a, b)
    print(result)