# PyJumble
Python Repo

##Things to remember about Python:
###1- range vs xrange
The range function creates a list containing numbers defined by the input. The xrange function creates a number generator. You will often see that xrange is used much more frequently than range. This is for one reason only - resource usage. The range     function generates a list of numbers all at once, where as xrange generates them as needed. This means that less memory is      used, and should the for loop exit early, there's no need to waste time creating the unused numbers. This effect is tiny in     smaller lists, but increases rapidly in larger lists as you can see in the examples below.
