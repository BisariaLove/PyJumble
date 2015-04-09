def outer():

    def inner():
       print 'Inside Inner'

    return inner

foo = outer()
print foo
foo()




