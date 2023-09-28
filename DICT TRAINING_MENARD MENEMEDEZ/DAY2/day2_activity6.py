# GRADE

    # 90 - 100
    # 80 - 89

    # if grade >= 90 or grade <= 100:
    #     excellent
    
    # elif grade >= 80 or grade <= 89:
    #     good job

    # 89.5 will cause an error if and operator is used

grade = float(input('\n\nEnter your grade : '))

if grade < 0:
    print('\nInvalid input! It seems like you entered a negative number.\n\n')

elif grade < 60:
    print('\nSorry, you didnt`t pass the subject!\n\n')

elif grade <= 69:
    print('\nYou need to work harder.\n\n')

elif grade <= 79:
    print('\nYou are doing okay!\n\n')

elif grade <= 89:
    print('\nGood Job!\n\n')

elif grade <= 100:
    print('\nWhat an Excellent student you are!\n\n')

else:
    print('\nInvalid input! It seems like you entered number greater than 100.\n\n')

