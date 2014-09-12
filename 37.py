from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 37

#print the problem
print_problem(questionno)

#
# Solution
#

truncated_primes = []
primes = prime_sieve(1000000)
invalid_primes = [2, 3, 5, 7]

for p in primes:
    prime = True
    p_str = str(p)

    for i in range(0, len(p_str)-1):

        if "1" in p_str[0] or "1" in p_str[-1]:
            prime = False
            break

        # left -> right
        if not is_prime(int(p_str[i+1:len(p_str)])):
            prime = False
            break
            
        # right -> left
        if not is_prime(int(p_str[0:len(p_str)-1-i])):
            prime = False
            break

    if prime:
        truncated_primes.append(p)

# remove invalid primes from list
truncated_primes = [x for x in truncated_primes if x not in invalid_primes]

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s" % sum(truncated_primes)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'