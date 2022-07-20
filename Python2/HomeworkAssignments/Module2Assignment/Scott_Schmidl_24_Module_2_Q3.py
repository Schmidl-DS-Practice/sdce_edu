# Scott Schmidl - COMP 661 - Programming with Python II - 04/12/2021 to 06/10/2021 - Section 2.4 Module 2 Assignment

def display_view():

    '''
    DISPLAYS THE COMMAND MENU
    ARGUMENT: NONE
    '''

    print('\nCOMMAND MENU')
    print('list - Display all contacts')
    print('view - View a contact')
    print('add - Add a contact')
    print('del - Delete a contact')
    print('exit - Exit program')

def list_con(contacts):

    '''
    DISPLAYS NAME OF EACH CONTACT
    ARUGMENTS: CONTACTS - LIST
    '''

    for num, contact in enumerate(contacts):
        print(f'{num + 1}. {contact[0]}')

def view_con(contacts):

    '''
    DISPLAYS INFORMATION FOR SELECTED CONTACT
    ARGUMENTS: CONTACTS - LIST
    '''
    con_num = int(input('Number: '))

    print(f'Name: {contacts[con_num-1][0]}')
    print(f'Email: {contacts[con_num-1][1]}')
    print(f'Phone: {contacts[con_num-1][2]}')

def add_con(contacts):

    '''
    RETURN: NEW CONTACT LIST WITH SELECTED CONTACT
    ARGUMENTS: CONTACTS - LIST
    '''

    name = input('Name: ')
    email = input('Email: ')
    phone = input('Phone: ')

    new_contact = [name, email, phone]
    contacts.append(new_contact)

    print(f'{name} was added.')

    return contacts


def delete_con(contacts):

    '''
    RETURN: NEW CONTACT LIST WITHOUT SELECTED CONTACT
    ARGUMENTS: CONTACTS - LIST
    '''

    con_num = int(input('Number: '))
    print(f'{contacts[con_num-1][0]} was deleted.')
    del contacts[con_num-1]

    return contacts

def main():

    # DEFINE LIST AND DISPLAY MENU
    contacts = [['Marilyn Monroe', 'MarilynMonroe@whatever.org', '+11 22 3456 3576'],
                ['Abraham Lincoln', 'AbrahamLincoln@whitehouse.org', '+22 33 4567 4687']]
    print('Contact Manager')
    display_view()

    # CONTINUE TO PROMPT USER FOR AN INPUT UNTIL THEY DECIDE TO EXIT PROGRAM
    while True:
        command = input('\nCommand: ').lower()

        if command == 'list':
            list_con(contacts)
        elif command == 'view':
            view_con(contacts)
        elif command == 'add':
            contacts = add_con(contacts)
        elif command == 'del':
            contacts = delete_con(contacts)
        elif command == 'exit':
            break
        else:
            print('That was not a valid command. Try again!')
    print('Bye!')

if __name__ == '__main__':
    main()