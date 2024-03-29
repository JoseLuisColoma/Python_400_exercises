# Exercise 002 (using functions and exceptions)
# Create a program that asks for two numbers via keyboard and displays their
# sum, difference, multiplication, and division.

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))


def summ(n1, n2):
    return n1 + n2


def diff(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return 'It is not possible a division by Zero'


print(summ(num1, num2))
print(diff(num1, num2))
print(mult(num1, num2))
print(div(num1, num2))
