
print('\n\n')
cont = True
sum = 0
loop_count = 1
while cont == True:
    number = input(f'[{loop_count}] Please enter a number : ')
    loop_count = loop_count + 1

    if number.isnumeric():
        sum = sum + int(number)
        continue
    else:
        print(f'\n\nThe sum of the numbers entered by the user is {sum}\n\n')
        break