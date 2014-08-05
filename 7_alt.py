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

    # next number to check should be 3
    p = 3
    
    while counter < n:

        is_prime = True

        for i in primes:

            # only need to check for factors less than the squareroot of the
            # number
            if(i > int(math.sqrt(p))):
                break

            # if p has previous prime factors then it is not prime
            if (p % i == 0):
                is_prime = False
                break

        if is_prime == True:
            primes.append(p)
            counter += 1

        # reduce scope to odd numbers
        p += 2

    return primes[n-1]

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % get_nth_prime(10001)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'