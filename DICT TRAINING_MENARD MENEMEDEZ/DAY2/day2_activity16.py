# ARRAY WITH APPEND FUNCTION

arr_names = []

print('\n\nTo stop the program, please enter the word "stop" \n\n')

while True:
    name = input('\nEnter the name of the fish : ')

    if name.lower() in arr_names:
        print(f'{name} is already entered. Please try another\n')
        continue
    elif name.lower() == 'stop':
        print('The program has been terminated.')
        break
    else:
        arr_names.append(name.lower())



print('\n\nThe names you collected are ', end=' ')
for i in range(0, len(arr_names) - 1):
    print(f'{arr_names[i]}', end=', ')
print('\n\n')
