# Exercise 005
# Create a program that prompts for a color via keyboard input and prints 'You can go' if the entered color is green,
# 'Caution' if it's yellow, 'Do not go' if it's red, or 'Invalid color' if it's any other

while True:
    try:
        input_color = input('Introduce a color: ')
        color = input_color.lower()
        if color == 'green':
            print('You can go')
            break
        elif color == 'yellow':
            print('Caution')
            break
        elif color == 'red':
            print('Do not go')
            break
        else:
            print('Invalid color')
    except ValueError:
        print('Invalid color')