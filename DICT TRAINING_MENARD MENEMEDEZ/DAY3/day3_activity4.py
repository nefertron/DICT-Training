# GROCERY LIST

my_array = []
from termcolor import colored

def add_item():
    print(colored(f'\n\t{"=" * 60}', 'green'))
    print(colored("""
        [ Add Item ]
    """, 'blue'))

    item_name = str(input('\tPlease enter an item name : ')).lower()
    my_array.append(item_name)
    print('\n\tAn Item has been added!')
    print((colored(f'\n\t{"=" * 60}', 'green')))



def remove_item():
    print((colored(f'\n\t{"=" * 60}', 'green')))
    print(colored("""
        [ Remove Item ]
    """, 'blue'))
    for i in range(0, len(my_array) - 1):
        print(f'\tItem [{i+1}] - ', my_array[i])
    print(f'\tItem [x] - exit\n')

    item_number = input('\tPlease enter an item to Remove : ')

    if item_number.isnumeric:
        item_number = int(item_number)
        if item_number != 'x' and len(my_array) > 0 and item_number < len(my_array):
            print(f'\t{my_array[item_number - 1]} has been removed!')
            del my_array[item_number - 1]
        elif item_number == 'x':
            print((colored(f'\n\t{"=" * 60}', 'green')))
            return True
        else:
            print(colored('\n\tYour input is invalid. Please try again!', 'red'))
    else:
        print(colored('\n\tYour input is invalid. Please try again!', 'red'))

    print((colored(f'\n\t{"=" * 60}', 'green')))



stopper = True
while stopper:
    print(colored("""\n\n
        [ MENU ]
      
        [1] - Print Grocery List
        [2] - Add Item in Grocery List
        [3] - Remove an Item in Grocery List
        [4] - Exit
    """, 'blue'))

    menu_number = input('\tEnter a number : ')

    if menu_number.isnumeric():
        menu_number = int(menu_number)

        if menu_number == 1:
            print(f'\n\n\t{"=" * 60}')
            print(colored("\n\t[ All Groceries ]\n", 'blue'))
            if len(my_array) > 0:
                for i in range(0, len(my_array) - 1):
                    print(f'\tItem #{i+1} - ', my_array[i])
            else:
                print(colored('\tSorry we couldn`t find any items on your list\n', 'red'))
            print(f'\t{"=" * 60}')

        elif menu_number == 2:
            add_item()
        elif menu_number == 3:
            remove_item()
        elif menu_number == 4:
            stopper = False
            print((colored(f'\n\t{"=" * 60}', 'green')))
            print(colored('\n\tThe program has been terminated!', 'red'))
            print((colored(f'\n\t{"=" * 60}', 'green')))
            break
        else:
            print((colored(f'\n\t{"=" * 60}', 'green')))
            print(colored('\n\tThe number you entered is not on the list. Please try again!', 'red'))
            print((colored(f'\n\t{"=" * 60}', 'green')))
    
    else:
        print(f'\n\n\t{"=" * 60}')
        print(colored('\n\tThe number you entered is Invalid. Please try again!', 'red'))
        print((colored(f'\n\t{"=" * 60}', 'green')))
