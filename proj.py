import sys
import math
__author__ = 'jarvis'
lim = int(sys.float_info.max)
i = sys.maxint
#print "Maxint: " + str(sys.maxint)

while i < lim:

    N = str(i)
    #M = N[len(N)-1] + N[0:len(N)-1]

    if int(N)%2 != 0:
       #print 'In the condition: ' + N
        continue
    if int(N[0]) > int(N[-3]):
        #print 'In condition: ' + N
        continue

    M = N[-3] + N[:-3]
    n = float(N)
    m = float(M)

    if (n*2) == m:
        print N + " : " + " : " + M
    i += 1

