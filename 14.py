from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 14

#print the problem
print_problem(questionno)


#
# Solution
#


max_chain = 0
starting_number = 1

#keep a dictionary of previous chain lengths
chain_history = {}

#loop though starting numbers
for i in range(1, 1000000, 1):

    n = i
    chain_len = 1

    while ( n > 1 ):

        # if we have previously calculated the chain length of the current 
        # number, grab it from the dictionary 
        if n in chain_history: 
            chain_len += chain_history[n]
            break

        # if even
        if( n % 2 == 0 ):
            n = n / 2

        #if odd
        else:
            n = (3 * n) + 1

        chain_len += 1

    # add chain length to dictionary
    chain_history[i] = chain_len

    # update the max value
    if(chain_len > max_chain):
        max_chain = chain_len
        starting_number = i



print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % starting_number
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'