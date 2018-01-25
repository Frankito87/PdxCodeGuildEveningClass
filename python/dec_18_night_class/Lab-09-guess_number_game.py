import random

print("Welcome to the guess number game!")

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37',
           '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73',
           '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
           '92', '93', '94', '95', '96', '97', '98', '99', '100']


def guess_number():

    computer_guess = random.choice(numbers)

    print(computer_guess)
    #print(random.choice(numbers))

    guess_number = True

    while guess_number == True:
        user_guess = input("Guess the number between 1 to 100: ")
        # if 101 > int(user_guess) > 0:
        if int(user_guess) > 0 and int(user_guess) <= 100:

            if int(user_guess) == int(computer_guess):
                print("You WIN !! You acert the number. Congratulations.")
                guess_number = False

            elif int(user_guess) < int(computer_guess):
                print("Your number is too low to the guess number so keep trying.")

            elif int(user_guess) > int(computer_guess):
                print("Your number is too high to the guess number so keep trying.")

        else:
            print("That number is out of range.")

    else:
        print("The game is over!!")
        #  print("Do you want to play again? Please select the option: ")
        # print("1 to continuos. or 2 to stop!")
        # option_1 = input("Let's try again.")
        # option_2 = input("See you next time.")

    play_again()


def play_again():

    ask = input("Do you want to play again. yes or no: ").lower()

    if ask == 'yes':
        guess_number()
    else:
        quit()

guess_number()