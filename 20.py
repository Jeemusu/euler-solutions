from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 20

#print the problem
print_problem(questionno)


#
# Solution
#

def factorial(n):
	res = 1
	for i in range(n, 1, -1):
		res*=i
	return res

def digitSum(n):
	res = 0
	for i in str(n):
		res += int(i)
	return res


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % digitSum(factorial(100))
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'