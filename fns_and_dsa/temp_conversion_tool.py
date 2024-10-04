FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


# If the user entered a wrong input,raise an error “Invalid temperature. Please enter a numeric value.”
while True:
    try:
        temperature = float(input("Enter the temperature to convert: "))
        break
    except (ValueError):
        print("Invalid temperature. Please enter a numeric value.")

temp_type = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

''' 
Step2: Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius
and returns the temperature converted to Fahrenheit.
'''


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


'''
Step 3 : Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit 
and returns the temperature converted to Celsius.
'''


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit


if temp_type == 'c':
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
elif temp_type == 'f':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
else:
    print("Please choose either C for Celsius or F for Fahrenheit.")