__author__ = 'jarvis'

def calc_sol(sol, wts, param):
    for k in wts:
        for i in range(1, param[1]+1):
            if i >= k:
                sol[i] = max(sol[i], k+sol[i - k])

    print sol[param[1]]

N = int(raw_input('Enter the total test cases: '))
for i in range(N):
    lis = []
    wts = []
    s = raw_input('Enter the count and the result weights: ')
    lis = map(int, s.split(' '))
    wts = map(int, raw_input('Enter the weights: ').split(' '))
    sol = []
    for i in range(lis[1]+1):
        sol.append(0)
    calc_sol(sol, wts, lis)
