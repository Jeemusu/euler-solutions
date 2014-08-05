from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 10

#print the problem
print_problem(questionno)


#
# Solution
#

primes = prime_sieve(10)


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % sum(primes)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'