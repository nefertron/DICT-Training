# GET THE SUMMATION

num = input('\n\nPlease enter a number : ')

if num.isnumeric():
    num = int(num)
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i
    
    print(f'\n\n\t\tThe sum of numbers from 1 to {num} is equal to {sum}\n\n')
else:
    print('\n\n\t\tThe number you entered is not an integer. Please try again!\n\n')