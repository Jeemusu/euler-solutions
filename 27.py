from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 27

#print the problem
print_problem(questionno)


#
# Solution
#

nmax = 0
a_co = 0
b_co = 0

for a in xrange(-1000, 1000):
    for b in xrange(-1000, 1000):

        n = 0

        while is_prime( abs( (n * n) + (a * n) + b ) ):
            n += 1

        if(n > nmax):
            nmax = n
            a_co = a
            b_co = b

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % (a_co * b_co)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'