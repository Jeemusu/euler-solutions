from euler import *
import time
import math
from operator import mul

#start timer
start = time.time()

#question number
questionno = 5

#print the problem
print_problem(questionno)


#
# Solution
#

def product(iterable):
    return reduce(mul, iterable, 1)

primes = prime_sieve(20);
values = []

for prime in primes:
    power = int(math.log(20)/math.log(prime))
    values.append(pow(prime,power))

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Largest palindrome: %s " % product(values) 
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'