phonebook = {
    "poe": {'f_name': 'Sally', 'l_name': 'Poe', 'phone': '3602139814'},
    "grogans": {'f_name': 'Jacqueline', 'l_name': 'Grogans', 'phone': '5037862353'}
}

def gather_info():
    f_name = input('Enter the first name:\n')
    l_name = input('Enter the last name:\n')\
    phone = int(input('Enter phone number:\n'))
    entering = True
    while entering:
        try:
            phone = int(input('Enter the phone number:\n'))
            entering = False
        except ValueError:
            print("Please enter a 10 digit phone number with no formatting.")
    return f_name, l_name, phone

# Create New Contact
def create_contact(*args):
    phonebook[args[1].lower()] = {'f_name': args[0], 'l_name': args[1], 'phone': args[2]}

# Retrieve Contact Info
def search(name):
    name = name.lower()
    try:
        print('{} {}'.format(phonebook[name]['f_name'], phonebook[name]['l_name']))
        print('({}) {}-{}'.format(str(phonebook[name]['phone'])[:3],
                                str(phonebook[name]['phone'])[3:6]
                                str(phonebook[name]['phone'])[6:]
        ))
    except KeyError:
        print("I'm sorry. I cannot find anyone with the name {}.".format(name))

# Delete Contact
def delete(name):
    try:
        del phonebook[name.lower()]
    except KeyError:
        print("I can't find anyone with that name.")

# Update Existing Contact
def update(f_name, l_name, phone, old_name):
    delete(old_name)
    create_contact(f_name, l_name, phone)


while True:
    query = input('Would you like to (s)earch, (a)dd, (e)dit, or (d)elete?. Enter exit to quit program:\n').lower()

    if query == 's':
        l_name = input('What is the last name of the person you are looking for?:\n')
        search(l_name)

    elif query == 'a':
        f_name, l_name, phone = gather_info()
        create_contact(f_name, l_name, phone)
        print(f"{f_name} {l_name} has been entered in the phonebook.")

    elif query == 'e':
        old_name = input("What is the last name of the person you would like to change?:\n")
        f_name, l_name, phone = gather_info()
        update(f_name, l_name, phone)
        print("{} has been updated to:".format(old_name))
        search(l_name)

    elif query == 'd':
        name = input("What is the last name of the person you want to delete?:\n")
        q = input("Are you sure you would like to delete {}?\n".format(name))
        if q.lower in ['y', 'yes']:
        delete(name)
        print("{} has been deleted.".format(name))

    elif query == 'exit'
        exit()

    else:
        print("I didn't understand that. Please try again")
