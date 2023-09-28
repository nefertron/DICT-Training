
# MATH OPERATIONS

def calculate(num1, num2, operation):
    if operation == '+':
        return f'The sum of {num1} and {num2} is {num1 + num2}'                                                                        
    elif operation == '-':
        return f'The difference of {num1} and {num2} is {num1 - num2}'
    elif operation == '*':
        return f'The product of {num1} and {num2} is {num1 * num2}'
    elif operation == '/':
        return f'The quotient of {num1} and {num2} is {num1 / num2}'
    else:
        return 'The operation is invalid. Please try again!'

stopper = True
while stopper:
    print("""\n\n
        [ OPERATIONS ]
      
        [+] - ADDITION
        [-] - SUBTRACTION
        [*] - MULTIPLICATION
        [/] - DIVISION
        [x] - EXIT
    """)

    num1 = input('Enter num 1 \t\t : ')
    if num1.isnumeric():
        num2 = input('Enter num 2 \t\t : ')
        if num2.isnumeric():
            operation = input('Enter operations \t : ')
            if operation != 'x':
                print(calculate(int(num1), int(num2), operation))
            else:
                if operation == 'x':
                    stopper = False
                    print('The program has been terminated')
                    break
                print('You entered an invalid input. Please try again!')
        else:
            if num2 == 'x':
                stopper = False
                print('The program has been terminated')
                break
            print('Num 2 must be a number!')
    else:
        if num1 == 'x':
            stopper = False
            print('The program has been terminated')
            break
        print('Num 2 must be a number!')

        