# count how many times i is in the string Antidisestablishmentterianism.
def string_methods():
    number = 'Antidisestablishmentterianism.'
    sub = "i"
    print(number.count(sub))


# show me the letters in that position [-6:-1]

    word = 'Pneumonoultramicroscopicsilicovolcanoconiosis'
    letters = word[-6:-1]
    print(letters)

    letters = word[-15]
    print(letters)



# convert the string the user give me in lower string

    convert_string = input("Give me a name of your favorite sport! Please write this in Capital letters: ")

    print(convert_string.lower())


    play_again()






def play_again():
    a = input("Do you like to play again: ").lower()

    if a in 'yes':
        string_methods()
    elif a in 'no':
        quit()
    else:
        print(" I did not understand that! ")

string_methods()
