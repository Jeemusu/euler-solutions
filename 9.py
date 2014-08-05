from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 9

#print the problem
print_problem(questionno)


#
# Solution
#

product = 0
abcsum = 1000

for b in range(1, abcsum):
    for a in range(1,abcsum):
        
        # a < b < c
        if(b <= a):
            break

        # a + b + c = 1000
        c = abcsum - a - b

        # use c to confirm which a & b make the triplet
        if (a**2 + b**2 == c**2):
            product = a*b*c 

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % product
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'