def perform_operation(num1,num2,operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operation."
    
num1 = 5
num2 = 6

result = num1 + num2
print (f"Result:{result}") 
