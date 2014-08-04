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
# Alternate solution finds the largest prime factor as a product of 
# prime numbers
#

number = 600851475143
prime_factors = []

i = 2 # start with the smallest prime number

while (number > 1):
    
    # could skip this and just find all factors
    if(!is_prime(i)):
        break

    if is_factor(number,i):
        number = number / i
        prime_factors.append(i)
    else :
        i += 1 

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Largest prime factor: %s " % prime_factors[-1]
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'