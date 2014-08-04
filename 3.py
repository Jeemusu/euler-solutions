from euler import *
import time
import math

#start timer
start = time.time()

#question number
questionno = 3

#print the problem
print_problem(questionno)


#
# Solution
#

number = 600851475143

prime_factors = []

# reduce the scope by limiting our search for factors less than the square root 
# of the original number
scope = int(math.sqrt(number))

# get prime numbers within our scope
primes = prime_sieve(scope)

for prime in primes:
    if(is_factor(number, prime)):
       prime_factors.append(prime)


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Sum: %s " % prime_factors[-1]
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'