from cars.car import Car


red = Car('red', '4')
blue = Car('blue', 2)
red.honk()
blue.honk()

print(red.number_of_wheels)
print(red.number_of_doors)