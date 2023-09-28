# AREA OF RECTANGLE

from termcolor import colored

def calculate_area(length, width):
    return length * width

stopper = True
while stopper:
    print((colored(f'\n\t{"=" * 70}', 'green')))
    length = input('\n\tEnter the Length (in cm) \t: ')
    width = input('\tEnter the Width (in cm) \t: ')
    print((colored(f'\n\t{"=" * 70}', 'green')))

    if length.isnumeric() and width.isnumeric():
        area = calculate_area(int(length), int(width))
        print((colored(f'\n\t{"=" * 70}', 'green')))
        print(f'\n\tThe area of the rectable with W = {width} and H = {length} is {area} cm²')
        print((colored(f'\n\t{"=" * 70}', 'green')))
    
    else:
        if length.isnumeric() and not width.isnumeric():
            print((colored(f'\n\t{"=" * 70}', 'green')))
            print(colored('\n\tInvalid input. Width must be a number', 'red'))
            print((colored(f'\n\t{"=" * 70}', 'green')))
        
        elif width.isnumeric() and not length.isnumeric():
            print((colored(f'\n\t{"=" * 70}', 'green')))
            print(colored('\n\tInvalid input. Length must be a number', 'red'))
            print((colored(f'\n\t{"=" * 70}', 'green')))
        
        else:
            print((colored(f'\n\t{"=" * 70}', 'green')))
            print(colored('\n\tInvalid input. Length and Width must be numbers', 'red'))
            print((colored(f'\n\t{"=" * 70}', 'green')))


