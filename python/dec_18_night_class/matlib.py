import random

name = input("What is your name: ")

#adj = input("Give me a adjective: ")
adj = input("Give me three adjective separeted by comma: ")

p = adj.split()

print(p)

animal = input("Give me a name of a animal: ")

vocal = input("Give me a vocal: ")

movie = input("Give me a name of a movie: ")

x = " Your name is {} you give a adjective {} you select this animal {} you give me this vocal {} and you type this movie {} ".format(name, random.choice(p), animal, vocal, movie)

print(x)

keep_going = input("Do you want to keep going ! Please select Yes or No !: ")

while keep_going == "Yes":

    name = input("What is your name: ")

#adj = input("Give me a adjective: ")
    adj = input("Give me three adjective separeted by comma: ")

    p = adj.split()

    print(p)

    animal = input("Give me a name of a animal: ")

    vocal = input("Give me a vocal: ")

    movie = input("Give me a name of a movie: ")

    x = " Your name is {} you give a adjective {} you select this animal {} you give me this vocal {} and you type this movie {} ".format(name, random.choice(p), animal, vocal, movie)

    print(x)

    # keep_going = keep_going + 1
    keep_going = input("Do you want to keep going ! Please select Yes or No !: ")


else:
    print("You finish the game!! Thanks!")
