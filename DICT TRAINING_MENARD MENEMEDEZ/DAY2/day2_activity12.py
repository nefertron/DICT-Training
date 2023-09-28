import random

cont = True
print('\n\n')

while cont == True:
    name = input('Enter your name : ')

    if name.lower() == 'stop':
        print('The loop ended. \n\n')
        cont = False
        break
    else:
        continue

