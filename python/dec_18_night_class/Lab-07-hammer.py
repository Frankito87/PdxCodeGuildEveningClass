
print("Welcome to a hammer program!")
# variable time to take the value the user pass


def hammer_time():

    time = input("What time is it ?:(HH am/pm): ")

    # to check the space

    meridian = time[-2:]
    time = time[:-2].strip() + " " + meridian

    # Breakfast = 7 - 9
    # Lunch = 12 - 2
    # Dinner = 7 - 9
    # Hammer = 10 - 4

    if time == '7 am' or time == '8 am' or time == '9 am':
        print("It is Breakfast time!")

    elif time == '12 pm' or time == '1 pm' or time == '2 pm':
        print("It is Lunch time!")

    elif time == '7 pm' or time == '8 pm' or time == '9 pm':
        print("It is Dinner time!")

    elif time == '10 pm' or time == '11 pm' or time == '12 pm' or time == '1 am' or time == '2 am' or time == '3 am' \
            or time == '4 am':
        print("It is Hammer time!")

    else:
        print("We are closed!")

    play_again()


def play_again():

    ask = input("Do you want to check again. yes or no: ")

    if ask == 'yes':
        hammer_time()
    else:
        quit()


hammer_time()