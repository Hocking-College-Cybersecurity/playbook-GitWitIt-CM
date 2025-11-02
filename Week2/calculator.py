
# Ask user for input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operator = input("Enter an operator (+, -, *, /): ")

# Convert inputs to floats (to allow decimals)
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result is: {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result is: {result}")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
