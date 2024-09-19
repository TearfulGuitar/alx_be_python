# pattern_drawing.py

# Prompt the user for a positive integer to determine the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row
row = 0
while row < size:
    # Use a for loop to print asterisks side by side in each row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after completing a row
    print()
    
    # Increment the row counter
    row += 1
