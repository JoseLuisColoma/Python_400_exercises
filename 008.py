# Exercise 008
# Create a program that counts from 1 to 100 inclusive and prints the numbers that are divisible by 2 and by 5

for i in range(0, 101):
    if i % 2 == 0 and i % 5 == 0:
        print(i, end=' ')