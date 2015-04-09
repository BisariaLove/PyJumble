__author__ = 'jarvis'

def outer(num=[]):
    def print_num():
        for elem in num:
            n = str(elem)
            disp = '+91 ' + n[:5]+' '+n[5:]
            print disp
    return print_num

N = int(raw_input())
lis = []
for i in range(N):
    n = raw_input()
    ele = n[-10:]
    lis.append(int(ele))
lis.sort()
foo = outer(lis)
foo()


