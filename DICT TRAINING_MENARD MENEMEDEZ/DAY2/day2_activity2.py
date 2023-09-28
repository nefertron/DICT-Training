# PASSED OR FAILED ?

name = input('\n\nEnter your Name : ')
math = int(input('Enter your Math Grade : '))
science = int(input('Enter your Science Grade : '))
english = int(input('Enter your English Grade : '))

average = (math + science + english) / 3
print(f"""\n\n
        Name : {name.capitalize()}
        Math : {math}
        Science : {science}
        English : {english}
        Average : {average}
""")

if average >= 75:
    msg = None  # will remail None if the students didn't fail any subject
    if math < 75:
        msg = 'Math'

    if science < 75:
        if msg:
            msg = msg + ', Science'
        else:
            msg = 'Science'

    if english < 75:
        if msg:
            msg = msg + ', and English'
        else:
            msg = 'English'
    
    if msg:     # if the msg contained string, re-enroll message will be printed
        print(f'\nCongratulations! You passed the semester. But you need to re-enroll {msg} subject.\n\n')
    else:       # if msg stays None, re-enroll message will not be included
        print('\nCongratulations! You passed the semester.\n\n')
    
else:
    print('\nSorry you Failed the semester.\n\n')