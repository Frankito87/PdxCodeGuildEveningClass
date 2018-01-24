
def extract_header():

    email = input("Give me an email address: ")

    at_index = email.index('@')

    # com_index = email.index('.com')

    com_index = email.rindex('.')

    print(email[at_index + 1:com_index])

    play_again()


def play_again():
    ask = input("Do you want to play again: yes or no").lower()

    if ask == 'yes':
        extract_header()
    else:
        quit()


extract_header()