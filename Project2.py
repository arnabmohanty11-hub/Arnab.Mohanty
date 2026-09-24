def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Add , Subtract , Multiply , Divide")
operator = input("Choose (Add/Subtract/Multiply/Divide): ")

try:  
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == 'Add':
        print("Result:", add(num1, num2))
    elif operator == 'Subtract':
        print("Result:", subtract(num1, num2))
    elif operator == 'Multiply':
        print("Result:", multiply(num1, num2))
    elif operator == 'Divide':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice selected.")

except ValueError:
    print("Error: Please enter numbers only.")

except ZeroDivisionError:
    print("Error: Can't divide by zero.")
    
