from phonebook_mapper import load_phone_book, save_phone_book

phone_book_dict = {'Kieran': {'name': 'Kieran',
                              'number': 8456331959},
                   'Lambda': {'name': 'Lambda',
                              'number': 8454185633}}


def create_contact():

    name = input("Enter a name: ")

    phone_number = input("Enter the phone number of that person: ")

    phone_book_dict.update({name: {'name': name, 'number': phone_number}})
    print(phone_book_dict)

    save_phone_book(phone_book_dict)

    select_option()


def delete_contact():

    delete = input("Enter the name or phone number of the person you want to delete.\n")

    if delete in phone_book_dict.keys():
        del phone_book_dict[delete]
        print(phone_book_dict)
    else:
        print('This person or phone number is not in the list.')

    select_option()


def search_contact():

    search = input("Enter the name of the person you would like to search: ")

    if search in phone_book_dict.keys():
        print(phone_book_dict[search])

    else:
        print("I can not find that person in the phone_book.! Do you can create that contact on the principal menu: ")

    select_option()


def update_contact():

    update = input("Enter the name or phone number of the person you want to update.\n")

    if update in phone_book_dict:
        print("This person is already in the list!")
    else:

        name = input("This person is not in the list please Enter a name to add: ")

        phone_number = input("Enter the phone number of that person: ")

        phone_book_dict.update({name: {'name': name, 'number': phone_number}})
        print(phone_book_dict)

    select_option()


def select_option():
    a = input("Select the option do you want to do:\n"
              " 1. Create Contact\n "
              "2. Retrieve Contact\n "
              "3. Update Contact\n "
              "4. Delete Contact\n").lower()

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
