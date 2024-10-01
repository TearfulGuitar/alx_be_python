def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    match operation:
        case "add":
            result = num1 + num2
        case "subtract":
            result = num1 - num2
        case "multiply":
            result = num1 * num2
        case "divide":
            if num1 == 0 or num2 == 0:
                return("cannot divide by zero")
            elif num1 !=0 or num2 != 0:
                result = num1 / num2
    return(result)

num1 = 5
num2 = 6

result = num1/num2
print(f"Result:{result}")