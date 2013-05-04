

class Person(object):
	def __init__(self):
		self.name = 'Jose'
		self.age = 18
		self.listItems = ['one','two']

	def sayHello(self):
		print "Hello " + self.name

	def printItems(self):
		for item in self.listItems:
			print item


class Worker(Person):
	def __init__(self):
		self.position = 'Lawyer'
		super(Worker, self).__init__()

	def work(self):
		print "I'm already working as " + self.position

w = Worker()
w.work()
w.sayHello()
w.printItems()
w.listItems.append('tree')
print "After added...."
w.printItems()


class Hero:
	pass

ironman = Hero()

ironman.name = 'Tony'
ironman.last_name = 'Stark'

print ironman.name