# pattern_drawing.py
# Objective: Draw a square pattern using while loop and nested for loop

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for each row
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after a row is printed
    row += 1
