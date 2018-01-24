
print("Welcome to a greeting program. We will ask you some questions!")


def greeting_game():

    name = input("Enter your name: ")

    age = input("How old are you: ")

    year_old = int(age) + 1

    print("********************** Your name is: {}, Your age is: {}, and you going to be in a year: {}*****************"
          .format(name, age, year_old))

    play_again()


def play_again():

    ask = input("Do you want to play again. yes or no: ").lower()

    if ask == 'yes':
        greeting_game()
    else:
        quit()


greeting_game()
