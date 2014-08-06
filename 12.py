from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 12

#print the problem
print_problem(questionno)


#
# Solution
#

def getFactors(n):
    factors_start = []
    factors_end = []

    i = 1
    factor = 1

    while True:

        factor = n / i

        if( n % i != 0 ):
            i += 1
            continue

        if(i >= factor + 1):
            break

        factors_start.append(i)
        factors_end.append(factor)

        i += 1

    # reverse the end array to get the correct order

    # merge arrays and convert to set to remove duplicates
    factors = sorted(list(set(factors_start + factors_end)))

    return factors 


c = 1
i = 2
answer = 0

while True:
    c = c + i

    factors = getFactors(c)
    num_factors = len(factors)

    if ( num_factors > 500 ):
        print c
        break

    i += 1


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % c
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'