from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 34

#print the problem
print_problem(questionno)

#
# Solution
#

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# create a dictionary of factorials
factorials = [factorial(x) for x in range(0, 10)]
factorials_sum = 0

# no good reason for upper bound, brute forced
for i in range(10,50000):
    num_list = map(int, str(i))
    i_sum = 0
    for digit in num_list:
        i_sum += factorials[digit]
        if(i_sum == i):
            factorials_sum += i


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s" % factorials_sum
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'