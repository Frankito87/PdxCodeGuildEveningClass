"""
quarter = 25
dime = 10
nickle = 5
pennie = 1

"""

string = "Welcome to the return change program. This program will change your amount in coins, pennies or dimes."

print(string.center(50, " "))

quarters = 25
dime = 10
nickle = 5
pennie = 1


def return_change():

    amount = input("Enter the amount you want to change: ")

    quarter = int(amount) // int(quarters)

    print("You have: " + str(quarter) + " quarters")

    amount_dime = int(amount) - int(quarter) * quarters

    dimes = amount_dime // dime

    print("You have: " + str(dimes) + " dimes")

    amount_nickle = int(amount) - int(quarter) * quarters

    nickles = amount_nickle // nickle

    print("You have: " + str(nickles) + " nickles")

    amount_pennie = int(amount) - (dimes * dime) - (quarters * quarter) - (int(nickles) * nickle)

    pennies = amount_pennie // 1

    print("You have: " + str(pennies) + " pennie")

    play_again()


def play_again():

    ask = input("Do you want to play again (y/n): ")

    if ask in 'yes':
        return_change()

    elif ask in 'no':
        print("GoodBye.!!")
        quit()

    else:
        print("I do not understand that.!!")


return_change()
