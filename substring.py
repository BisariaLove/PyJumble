__author__ = 'jarvis'

sup = raw_input()
sub = raw_input()
count = 0
for i in range(len(sup) - len(sub)+1):
    if sup[i:].startswith(sub):
        count += 1
print count