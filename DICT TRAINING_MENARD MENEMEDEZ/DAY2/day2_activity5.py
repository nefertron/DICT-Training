# CHILD, TEEN, ADULT, or SENIOR ?

age = input('\n\nEnter your age : ')

if age.isnumeric():
    age = int(age)
    if age <= 12:
        print('You are a Child\n\n')

    elif age <= 19:
        print('You are a Teen\n\n')

    elif age <= 64:
        print('You are an Adult\n\n')

    else:
        print('You are a Senior\n\n')

else:
    print('The input you entered is not an integer\n\n')

