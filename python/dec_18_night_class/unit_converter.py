print("Welcome to the unit converter program!\n")
print("This program convert miles to feet, meter, inch, km and yard.!\n")

option_1 = input("Select 1 to converter to feet, 2 to converter to meter, 3 to converter to inch, 4 to converter to km,"
                 "5 to converter to yard: ")
# option_2 = input("Select 2 if you want to converter to meter: ")
# option_3 = input("Select 3 if you want to converter to inch: ")
# option_4 = input("Select 4 if you want to converter to km: ")
# option_5 = input("Select 5 if you want to converter to yard: ")

number = input("Give me a number you want to converter: ")

# unit = input("Give me a unit to converter! Remember you can converter miles to feet, meter, inch, km and yard: ")


if option_1 == '1':
    print(int(number) * 5280)

elif option_1 == '2':
    print(int(number) * 1609.34)

elif option_1 == '3':
    print(int(number) * 63360)

elif option_1 == '4':
    print(int(number) * 1.60934)

elif option_1 == '5':
    print(int(number) * 1760)

else:
    print("You enter a different number. Sorry!")
