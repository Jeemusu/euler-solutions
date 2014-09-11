from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 35

#print the problem
print_problem(questionno)

#
# Solution
#

# a list of circular primes
circular_primes = []

# get all prime numbers below 1 million
primes = prime_sieve(1000000)

# check each prime
for prime in primes:

    # skip primes with a zero
    if "0" in str(prime):
        continue

    # get all rotations of a prime number
    prime_rots = getRotationsOfNum(prime)

    is_circular = True

    # check if each rotation variant is prime
    for n in prime_rots:
        if not is_prime(int(n)):
            is_circular = False
            break
    
    if(is_circular):
        circular_primes.append(prime)


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s" % len(circular_primes)

print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'