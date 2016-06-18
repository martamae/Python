def whileFunction(var):
	i = 0
	numbers = []

	while i < var:
		numbers.append(i)

		i = i + 1

	return numbers


def printNum(numbers):
	print "The numbers: "
	
	for num in numbers:
		print num

print "Enter number:"
var = int(raw_input())

numbers = whileFunction(var)


printNum(numbers)