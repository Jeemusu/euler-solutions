from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 30

#print the problem
print_problem(questionno)

#
# Solution
#

def sumOfPowerOfDigits(n,p):
    n = str(n)
    total = 0

    for i in n:
        total += int(i)**p

    return total

valid_numbers = []

for i in range (10,999999):
    if(sumOfPowerOfDigits(i,5) == i):
        valid_numbers.append(i)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "No of distinct terms: %s" % sum(valid_numbers)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'