from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 21

#print the problem
print_problem(questionno)


#
# Solution
#

# get sum of proper divisors (factors without n)
def d(n):
    result = []
    for i in xrange(1, int(n**0.5 + 1)):
        if n % i is 0:
            result.append(i)
            if i is not n / i:
                result.insert(0, n / i)
    if n in result: result.remove(n)
    return sum(result)

# check if number is amicable
def is_amicable(n):
  sopd = d(n)
  return d(sopd) == n and not sopd == n


result = 0
for i in xrange(1,10001):
	if(is_amicable(i)):
		result+=i

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % result
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'
