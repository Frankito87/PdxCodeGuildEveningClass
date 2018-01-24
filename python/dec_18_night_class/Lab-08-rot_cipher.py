print("Welcome to the ROT program!")


def rot_cipher_program ():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    rot_13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l', 'm']

    user = input("Enter your code, you will receive the message in ROT-13: ")

    message = []

    for i in user:
        message += i

        print(message)

    new_string = ""

    for i in message:
        index = alphabet.index(i)
        new_string += rot_13[index]

        print(new_string)

rot_cipher_program()