student_records = []

def add_student(name, age, grade):
    student = (name, age, grade)
    student_records.append(student)
    print('\n\tA student has been added on the list!\n')
    
    print(f'\n\t{"=" * 70}')

    start()

def diplay_students():
    print(f'\n\n\n\t{"=" * 70}')
    print('\n\t[STUDENT RECORDS]')
    print(f'\n\t{"=" * 70}')
    j = 1
    for i in student_records:     
        
        print(f'\n\tStudent [{j}]')
        print(f'\t\tName\t: {i[0]}')
        print(f'\t\tAge\t: {i[1]}')
        print(f'\t\tGrade\t: {i[2]}')

        j = j + 1
    print(f'\n\t{"=" * 70}')
    
    print('\n\tThese are the student records\n')
    start()

def start():
    print("""\n\n
        [ OPTIONS ]
      
        [1] - ADD STUDENT
        [2] - DISPLAY STUDENTS
          
    """)

    enter = input('\n\tEnter a number : ')

    if enter.isnumeric():
        enter = int(enter)

        if enter == 1:
            print(f'\n\n\n\t{"=" * 70}')
            name = input('\n\tNAME : ')
            age = input('\n\tAGE : ')
            if age.isnumeric():
                age = int(age)
                grade = input('\n\tGRADE : ')
                if grade.isnumeric():
                    grade = int(grade)
                    add_student(name, age, grade)
                else:
                    print(f'\n\t{"=" * 70}')
                    print('\n\tThe grade is invalid. Please try again!')
                    print(f'\n\t{"=" * 70}')
            else:
                print(f'\n\t{"=" * 70}')
                print('\n\tThe age is invalid. Please try again!')
                print(f'\n\t{"=" * 70}')
        elif enter == 2:
            diplay_students()
        else:
            print(f'\n\t{"=" * 70}')
            print('\n\tThe num you entered is invalid. Please try again!')
            print(f'\n\t{"=" * 70}')
            start()
    return 0


start()
