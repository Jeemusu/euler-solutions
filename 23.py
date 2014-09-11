from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 23

#print the problem
print_problem(questionno)


#
# Solution
#

# Returns the factors of a number
def factors(n):
    result = []
    for i in xrange(1, int(n**0.5 + 1)):
        if n % i is 0:
            result.append(i)
            if i is not n / i:
                result.insert(0, n / i)
    if n in result: result.remove(n)
    return result

# Tests if a number is abundant
def is_abundant(n):
	return n < sum(factors(n))

# Generate a list of abundant numbers upto limit
def gen_abundant(limit):
	result = []
	for i in xrange(1,limit):
		if is_abundant(i):
			result.append(i)
	return result

limit = 28123
abundants = gen_abundant(limit)	
results = range(limit)

for i in abundants:
	for j in abundants:
		if i+j >= limit:
			break
		results[i+j] = 0

total = sum(results)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % total
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'