import random


def magicball():
    string = "Welcome to the Magic 8 Ball game!! "
    print(string.center(50, " "))

    prediction = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
                  'As I see it', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
                  'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
                  'Do not count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

    answer = random.choice(prediction)

    question = input("Enter the question: ")
    print(answer)

    play_again()


def play_again():
    a = input("Do you like to play again: ").lower()

    if a in 'yes':
        magicball()
    elif a in 'no':
        print("Good Bye!!")
        exit()
    else:
        print(" I did not understand that! ")


magicball()





