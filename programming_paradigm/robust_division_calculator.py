import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()


def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        result = num/denom 

        return f"Result: {result}"
    
    except ZeroDivisionError:
        return "Error! Division by zero is not allowed"

    except ValueError:
        return "Error! Non numeric input.Please enter valid numbers"
    
