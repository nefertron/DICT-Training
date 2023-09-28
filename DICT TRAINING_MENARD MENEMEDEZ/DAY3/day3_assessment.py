contacts = []
############### ADD CONTACT
def add_contact(name, phone_number, email):
    temp_dict = {
        'Name' : name,
        'Phone' : phone_number,
        'Email' : email
    }
    contacts.append(temp_dict)
    print('\n\n\tNew contact has been added! Press enter to continue')
    raw = input()
############### SEARCH CONTACT
def search_contact():
    print(f'\n\n\n\t{"=" * 70}')
    print('\n\t[ SEARCH CONTACT ]\n')
    name = input('\tEnter a name to search : ').lower()
    found = False
    for contact in contacts:
        if name in contact['Name']:
            print(f'\n\n\n\t{"+" * 50}')
            print(f"""
                CONTACT INFORMATION
                    [NAME]          - {contact['Name'].capitalize()}
                    [PHONE NUMBER]  - {contact['Phone']}
                    [EMAIL ADDRESS] - {contact['Email']}
            """)
            found = True
            print(f'\n\t{"+" * 50}')

    if found == False:
        print(f'\n\tSorry, the name [{name.capitalize()}] was not found. Please try again!')
    print(f'\n\n\n\t{"=" * 70}')

############### EDIT CONTACT
def edit_contact(name_to_edit):
    for contact in contacts:
        if name_to_edit in contact['Name']:
            print(f"""

                PLEASE ENTER A NUMBER BASED ON THE OPTIONS BELOW
                  
                CURRENT CONTACT INFORMATION
                    [1] -   [NAME]          - {contact['Name'].capitalize()}
                    [2] -   [PHONE NUMBER]  - {contact['Phone']}
                    [3] -   [EMAIL ADDRESS] - {contact['Email']}
                    [4] -   [CLOSE THIS]    - EXIT PROGRAM
            """)

            option = input('\n\tEnter menu number : ')

            if option.isnumeric():
                option = int(option) 
                if option == 1:
                    new_name = input('\n\tEnter New Name : ').lower()
                    contact['Name'] = new_name
                    print('\n\tA contact information has been modified! Press enter to go back.')
                    raw = input()
                    main_menu()
                
                elif option == 2:
                    new_phone = input('\n\tEnter New Phone Number : ')
                    contact['Phone'] = new_phone
                    print('\n\tA contact information has been modified! Press enter to go back.')
                    raw = input()
                    main_menu()
                
                elif option == 3:
                    new_email = input('\n\tEnter New Email Address : ')
                    contact['Email'] = new_email
                    print('\n\tA contact information has been modified! Press enter to go back.')
                    raw = input()
                    main_menu()

                elif option == 4:
                    print('\n\tYou are about to leave the edit information panel. Press enter to continue.')
                    raw = input()
                    main_menu()
                
                else:
                    print('\n\tThe option you entered is invalid. Press enter to continue.')
                    raw = input()
                    edit_contact(name_to_edit)

            else:
                print('\n\tThe number you entered is invalid. Please enter to try again!')
                raw = input()
                edit_contact(name_to_edit)

############### DISPLAY CONTACT
def display_contacts():
    if len(contacts) > 0:
        print(f'\n\n\n\t{"=" * 70}')
        print('\n\t[ LIST OF CONTACTS ]')
        i = 1
        for contact in contacts:
            print(f"""
                CONTACT NO [{i}]
                    [NAME]          - {contact['Name'].capitalize()}
                    [PHONE NUMBER]  - {contact['Phone']}
                    [EMAIL ADDRESS] - {contact['Email']}
            """)
            i += 1
            print('\n')
        print(f'\n\n\n\t{"=" * 70}')
        
    else:
        print('\n\n\tSorry, we couldn`t find any contacts. Press enter to go back.\n')
        raw = input()
        main_menu()

############### REMOVE CONTACT
def remove_contact(name):
    found = False

    index = 0
    for contact in contacts:
        if name == contact['Name']:
            print(f'\n\n\n\t{"+" * 50}')
            print(f"""
                CONTACT INFORMATION
                    [NAME]          - {contact['Name'].capitalize()}
                    [PHONE NUMBER]  - {contact['Phone']}
                    [EMAIL ADDRESS] - {contact['Email']}
            """)
            found = True
            print(f'\n\t{"+" * 50}')

            decision = input('Are you sure you want to remove this contact [y] / [n] ? ').lower()

            if decision == 'y':
                print(f'The contact information of {name.capitalize()} has been removed!')
                contact.pop(index)
                main_menu()
            else:
                print(f'It seems like you don`t want to removed this contact information. Press enter to continue')
                raw = input()
                main_menu()
        index = index + 1

    if found == False:
        print(f'\n\tSorry, the name [{name.capitalize()}] was not found. Please try again!')

############### MAIN MENU
def main_menu():
    print("""\n\n
        [ MENU ]
      
        [1] - ADD NEW CONTACT
        [2] - DISPLAY CONTACTS
        [3] - SEARCH  CONTACT
        [4] - EDIT    CONTACT
        [5] - REMOVE  CONTACT
        [6] - EXIT THE PROGRAM
    """)
    
    selected = input('\n\tEnter menu number : ')
    if selected.isnumeric():
        selected = int(selected)

        if selected == 1:
            print(f'\n\n\n\t{"=" * 70}')
            print('\n\t[ ADD NEW CONTACT ]\n')
            name = input('\n\tName            : ').lower()
            phone_number = input('\n\tPhone Number    : ')
            email_address = input('\n\tEmail Address   : ')
            add_contact(name, phone_number, email_address)
            print(f'\n\n\t{"=" * 70}')
        
        elif selected == 2:
            display_contacts()
        
        elif selected == 3:
            search_contact()
        
        elif selected == 4:
            print(f'\n\n\t{"=" * 70}')
            print('\n\t[ EDIT CONTACT INFORMATION ]')
            name_to_edit = input('\n\tEnter Name : ').lower()
            edit_contact(name_to_edit)
            print(f'\n\n\t{"=" * 70}')

        elif selected == 5:
            print(f'\n\n\t{"=" * 70}')
            print('\n\t[ REMOVE CONTACT ]')
            name_to_remove = input('\n\tEnter Name : ').lower()
            remove_contact(name_to_remove)
            print(f'\n\n\t{"=" * 70}')

        elif selected == 6:
            import sys
            print('\n\tYou terminated the program. Press enter to continue.\n')
            raw = input()
            sys.exit(0)
        else:
            print('\n\tThe number you entered is invalid. Please try again!')

    else:
        print('\n\tThe number you entered is invalid. Please try again!')
    main_menu()

main_menu()