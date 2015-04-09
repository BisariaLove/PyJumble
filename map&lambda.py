__author__ = 'jarvis'

def fib_gen(num):
    lis = []
    if num > 0:
        lis.append(0)
    if num > 1:
        lis.append(1)
    for i in range(2, num):
        ele = lis[i-1] + lis[i-2]
        lis.append(ele)
    return lis


triple_root = lambda n: n*n*n

N = int(raw_input())
lis = fib_gen(N)
print map(triple_root, lis)