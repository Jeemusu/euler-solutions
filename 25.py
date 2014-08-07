from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 25

#print the problem
print_problem(questionno)


#
# Solution
#

f = [1,1]

while len(str(f[-1])) < 1000:
	f.append(f[-1] + f[-2])

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % len(f)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'