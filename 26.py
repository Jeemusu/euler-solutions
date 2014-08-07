from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 26

#print the problem
print_problem(questionno)


#
# Solution
#

# Returns the length of the recurring cycle in a number n
def cycle_len(n):
	c = 1

	# pow(10, c, n) == 10^c % n
	while pow(10, c, n) - 1 > 0:
		c += 1
		
	return c


max_cyc_len = 0
answer = 0

# limit scope to primes as provide best repetitive sections
# loop through primes in reverse
for n in prime_sieve(1000):
    cyc_len = cycle_len(n)

    if(cyc_len > max_cyc_len):
        max_cyc_len = cyc_len
        answer = n


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % answer
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'