# Exercise 004
# Create a program that requests an age and prints 'It's older' if it's of legal age, otherwise print 'It's younger'"

FULL_AGE = 18
MIN_AGE = 0
MAX_AGE = 125

while True:
    try:
        age = int(input("Enter your age: "))
        if MIN_AGE <= age < MAX_AGE:
            # Check if the age is greater than or equal to 18
            if age >= FULL_AGE:
                print("It's older")
            else:
                print("It's younger")
            break
        else:
            print("Invalid age entered. Please enter a new one.")
    except ValueError:
        print('Invalid age entered. Please enter a new one.')