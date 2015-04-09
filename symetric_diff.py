__author__ = 'jarvis'
m = int(raw_input())
nums = raw_input()
M = nums.split()
m_set = set(list(map(int, M)))


n = int(raw_input())
nums = raw_input()
N = nums.split()
n_set = set(list(map(int, N)))


sol = list(m_set.difference(n_set))
sol2 = list(n_set.difference(m_set))
sol.extend(sol2)
sol.sort()
for elem in sol:
    print elem



