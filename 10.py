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

def prime_sieve(limit):

    not_prime = set()
    primes = []

    for i in xrange(2, limit):

        if i in not_prime:
            continue

        for f in xrange(i*i, limit, i):
            not_prime.add(f)

        primes.append(i)

    return primes

primes = prime_sieve(2000000)


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % sum(primes)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'