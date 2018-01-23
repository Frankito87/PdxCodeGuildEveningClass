phonebook = {'Kieran': {'name': 'Kieran',
                        'number': 8456331959},
            'Lambda': {'name': 'Lambda',
                        'number': 8454185633,
}}

from phonebook_mapper import load_phonebook, save_phonebook
def create_contact():

    name = input("Enter a name: ")

    phone_number = input("Enter the phone number of that person: ")

    phonebook.update({name: {'name': name, 'number': phone_number}})
    print(phonebook)

    save_phonebook(phonebook)

    select_option()

def delete_contact():

    delete = input("Enter the name or phone number of the person you want to delete.\n")

    if delete in phonebook:
        del phonebook[delete]
        print(phonebook)

    else:
        print('This person or phone number is not in the list.')


    select_option()

def search_contact():

    search = input("Enter the name of the person you would like to search: ")

    if search in phonebook:
        print(phonebook[search])

    else:
        print("I can not find that person in the phonebook.! Do you can create that contact on the principal menu: ")

    select_option()

def update_contact():

    update_contact = input("Enter the name or phone number of the person you want to update.\n")

    if update_contact in phonebook:

        print("This perosn is already in the list!")
    else:

        name = input("Enter a name: ")

        phone_number = input("Enter the phone number of that person: ")

        phonebook.update({name: {'name': name, 'number': phone_number}})
        print(phonebook)



    select_option()

def select_option():
    a = input("Select the option you want to do:\n 1. Create Contact\n 2. Retrieve Contact\n 3. Update Contact\n 4. Delete Contact\n").lower()

    if a in '1':
        create_contact()

    elif a in '2':
        search_contact()

    elif a in '3':
        update_contact()

    elif a in '4':
        delete_contact()

    else:
        quit()

select_option()

#def retrieve_contact():

#    phonebook.items
