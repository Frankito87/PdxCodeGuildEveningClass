print("Welcome to a program wall painting!\n")
print("Here you will know the cost of the paint you want to use!\n")

width = input("Enter the width of the wall you want to paint: ")

height = input("Enter the height of the wall you want to paint: ")

price_gallons_paints = input("Enter the amount of one gallons of paint: ")

how_many_coats = input("How many times do you want to paint the wall: ")

cost = int(width) * int(height)

gallons_paint = cost * int(price_gallons_paints) * int(how_many_coats)

print("The cost to paint your wall: {} coat is: {} ".format(how_many_coats, gallons_paint))
