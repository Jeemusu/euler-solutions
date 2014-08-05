from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 7

#print the problem
print_problem(questionno)


#
# Solution
#

def get_nth_prime(n):


    primes = [2]
    counter = 1
    p = 3

    while counter < n:

        # making use of previous is_prime function to check primality
        if is_prime(p):
            primes.append(p)
            counter += 1
        
        p+=2

    return primes[n-1]

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % get_nth_prime(10001)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'