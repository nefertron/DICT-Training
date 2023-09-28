# FACTORIAL OF A NUMBER

num = input('\n\nPlease enter a number : ')

if num.isnumeric():
    num = int(num)
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    
    print(f'\n\n\t\tThe factorial of {num} is equal to {factorial}\n\n')
else:
    print('\n\n\t\tThe number you entered is not an integer. Please try again!\n\n')

