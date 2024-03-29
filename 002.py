# Exercise 002 (using functions and exceptions)
# Create a program that asks for two numbers via keyboard and displays their
# sum, difference, multiplication, and division.

# Ask for input
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

# Performs operations
sum_result = num1 + num2
dif_result = num1 - num2
mult_result = num1 * num2

# Check if the second number is not zero to avoig division by zero
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = 'Cannot divide by zero'

# Display results
print(sum_result)
print(dif_result)
print(mult_result)
print(div_result)
