from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 6

#print the problem
print_problem(questionno)


#
# Solution
#

numbers = range(1,101)
squares = []

for i in numbers:
    squares.append(i*i)

sum_of_squares = sum(squares)
square_of_sum = sum(numbers) * sum(numbers)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % (square_of_sum - sum_of_squares)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'