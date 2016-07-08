#animal is an object
class Animal(object):
	pass

#Dog is an Animal
class Dog(Animal):
	def __init__(self,name):
		#Dog has a name
		self.name = name

#Cat is an animal
class Cat(Animal):
	def __init__(self, name):
		#Cat has a name
		self.name = name

#Person is an object
class Person(object):
	def __init__(self, name):
		#Person has a name
		self.name = name

		#Person has a pet
		self.pet = None

#Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
		##
		super(Employee, self).__init__(name)
		
		##Person has a salary
		self.salary = salary

#Fish is an object
class Fish(object):
	pass

#Salmon is a Fish
class Salmon(Fish):
	pass

#Halibut is a Fish
class Halibut(Fish):
	pass

#rover is a Dog
rover = Dog("Rover")

#satan is a cat
satan = Cat("Satan")

#Mary is a person
mary = Person("Mary")

mary.pet = satan

#Frank is an Employee
frank = Employee("Frank", 12000000)

frank.pet = rover

#Flipper is a fish
flipper = Fish()

#crouse is a Salmon
crouse = Salmon()

#harry is a Halibut
harry = Halibut()