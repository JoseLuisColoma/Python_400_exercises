# Exercise 009
# Create a program that prints a multiplication table from 2 to 9. Each table should display its multiplication
# values from 1 to 9 inclusive

for i in range(1, 10):
    print('-----------------------------')
    print(f'Tabla de multiplicar del {i}')
    print('-----------------------------')
    for j in range(2, 11):
        print(f'{i} x {j} = {i*j}')

