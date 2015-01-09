class Increment:
	def __init__(self):
		print "Hello!!"

	def printWord(self):
		name = raw_input("Enter your name:")
		print "Hello " + name + "!"
		

num1 = Increment();
num1.printWord();