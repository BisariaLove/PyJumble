__author__ = 'jarvis'

def print_name(lis):
    def print_dic():
        entry = str()
        for elem in lis:
            if elem[3] == 'M':
                entry = 'Mr. '
            else:
                entry = 'Ms. '
            entry += elem[0]+' '+elem[1]
            print entry
    return print_dic




def get_age(item):
    return item[2]

N = int(raw_input())
full_list = []
for i in range(N):
    entry = raw_input()
    lis = entry.split(' ')
    lis[2] = int(lis[2])
    full_list.append(lis)
full_list.sort(key = get_age)
foo = print_name(full_list)
foo()
