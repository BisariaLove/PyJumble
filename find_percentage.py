__author__ = 'jarvis'
def get_avg(lis):
    def print_avg():
        avg = float()
        for ele in lis:
            avg += float(ele)
        print '%.2f' % (avg/len(lis))
    return print_avg


N = int(raw_input())
record = dict()
for i in range(N):
    entry = raw_input()
    temp = entry.split()
    record[temp[0]] = temp[1:]
name = raw_input()
lis = []
lis = record.get(name)
foo = get_avg(lis)
foo()
