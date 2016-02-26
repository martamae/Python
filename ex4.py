cars = 100
spaceInCar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCap = carsDriven * spaceInCar
avgPassengersPerCar = passengers / carsDriven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers availalbe"
print "There will be", carsNotDriven, "empty cars"
print "We can transport", carpoolCap, "people"
print "We have", passengers, "to carpool today"
print "We need to put about", avgPassengersPerCar, "in each car"