from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 29

#print the problem
print_problem(questionno)

#
# Solution
#

size = 101
sequence = []

for a in xrange(2, size):
    for b in xrange(2, size):
        sequence.append(a**b);

sequence = list(set(sequence));


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "No of distinct terms: %s" % len(sorted(sequence))
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'