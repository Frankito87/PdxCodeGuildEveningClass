import random


def mat_lib_game():

    name = input("What is your name: ")
    # adj = input("Give me a adjective: ")
    adj = input("Give me three adjective separeted by comma: ")
    p = adj.split()
    print(p)
    animal = input("Give me a name of a animal: ")
    vocal = input("Give me a vocal: ")
    movie = input("Give me a name of a movie: ")
    print("Your name is {} you give a adjective {} you select this animal {} you give me this vocal {} and you type "
          "this movie {} ".format(name, random.choice(p), animal, vocal, movie))

    play_again()


def play_again():

    keep_going = input("Do you want to keep going ! Please select Yes or No !: ").lower()

    if keep_going == "yes":
        mat_lib_game()
    else:
        quit()


mat_lib_game()
