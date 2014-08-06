from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 15

#print the problem
print_problem(questionno)


#
# Solution
#

total = 0

for i in str(2**1000):
    total = total + int(i)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % total
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'