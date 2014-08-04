from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 1

#print the problem
print_problem(questionno)


#
# Solution
#

multiples = []

for i in range(1,1000):
    if(is_multiple_of(i, 3) or is_multiple_of(i, 5)):
        multiples.append(i)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Sum: %s " % sum(multiples)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'