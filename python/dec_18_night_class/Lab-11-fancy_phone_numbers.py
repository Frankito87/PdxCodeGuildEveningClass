# Program Fancy Phone Numbers. Here you going to make a program to give the
# answer to the user like this 503-55-1234 or (503)- 555- 1234


def fancy_phone_number():
    phone_number = input("Enter a phone number: ")
    # lst = list(phone_number)
    first_number = phone_number[0:3]
    second_number = phone_number[3:6]
    third_number = phone_number[6:]
    print("The number you write was: ({}) {} -{}".format(first_number, second_number, third_number))
    # print(third_number)
    # print(lst)

    play_again()


def play_again():
    a = input("Do you like to play again: ").lower()

    if a in 'yes':
        fancy_phone_number()
    elif a in 'no':
        quit()
    else:
        print(" I did not understand that! ")


fancy_phone_number()
