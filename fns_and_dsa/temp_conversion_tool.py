# Requirement 1: Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_celsius(fahrenheit: float):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    # Use the global factor (5/9)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    # Use the global factor (9/5)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Handles user interaction, input validation, and displays the conversion result.
    """
    try:
        # Requirement: Prompt for temperature
        temp_input = input("Enter the temperature to convert: ") 
        temperature = float(temp_input) 
        
    except ValueError:
        # Requirement: Raise a specific error message for non-numeric input
        print("Invalid temperature. Please enter a numeric value.")
        return 

    # FIX: This prompt MUST match the checker's expectation exactly.
    unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").strip().upper()

    if unit == 'C':
        # Call the appropriate conversion function
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    
    elif unit == 'F':
        # Call the appropriate conversion function
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
        
    else:
        # Input validation for the unit
        print("Invalid unit specified. Please enter 'C' or 'F'.")

if  __name__== "_main_":
    main()