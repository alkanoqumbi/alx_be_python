# Requirement 1: Define Global Conversion Factors
# Factors are defined as: F to C is 5/9, C to F is 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 # This MUST be 9/5, not (9/5) or '1.8'

def convert_to_celsius(fahrenheit: float):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Formula: C = (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float):
    """
    Converts a temperature from Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Handles user interaction, input validation, and displays the conversion result.
    """
    try:
        temp_input = input("Enter the temperature to convert: ")
        # Requirement: Input validation - convert to float
        temperature = float(temp_input) 
        
    except ValueError:
        # Requirement: Raise a custom error message for non-numeric input
        print("Invalid temperature. Please enter a numeric value.")
        return 

    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
        
    else:
        # Input validation for the unit
        print("Invalid unit specified. Please enter 'C' or 'F'.")

if __name__ == "_main_":
    main()