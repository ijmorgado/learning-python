print 'Hello Man!!!!'

class Person:
	"""This is the person class"""
	id = 5

	def __init__(self):
		self.name = "Ivan"
	def sayHello(self):
		print "Hello World from the Person object!!!"


p = Person()
p.sayHello()
print p.name
print p.id

class Driver:
	"""This is the driver class"""
	id = 6

	def __init__(self):
		self.car = "Mercedez Benz"

	def sayHello(self,name):
		return "Hello " + name + ", i know you drive a "+ self.car

	def sayBye(self,name):
		print "Bye " + name


d = Driver()
print d.sayHello("Ivan")

d.counter = 1
while d.counter < 10:
    d.counter = d.counter * 2
print d.counter
del d.counter
print d.__doc__
print p.__doc__


bye = d.sayBye
bye("Juan")

def sayCrazy():
	print "You're crazy"

d.sayBye = sayCrazy
d.sayBye()
d.sayBye()
del d.sayBye
d.sayBye("dd")

print d.__class__