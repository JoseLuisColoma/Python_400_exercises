# Exercise 003
# Create a program that asks for an age and determines if the person is of legal age.

FULL_AGE = 18
MIN_AGE = 0
MAX_AGE = 125

while True:
    age = int(input("Enter your age: "))
    if MIN_AGE <= age < MAX_AGE:
        # Check if the age is greater than or equal to 18
        if age >= FULL_AGE:
            print("You are of legal age.")
        else:
            print("You are not of legal age.")
        # Exit the loop once a valid age is entered
        break
    else:
        print("Invalid age entered. Please enter a new one.")
