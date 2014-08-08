from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 31

#print the problem
print_problem(questionno)

#
# Solution
#

goal = 200

# coins value in pence
coins = [1, 2, 5, 10, 20, 50, 100, 200]

# dictionary with 200 indexes predefined
solutions = dict.fromkeys( xrange( 0, goal + 1 ), 0 )

# set the first index
solutions[0] = 1

# loop though each coin type
for coin in coins:
    for i in xrange( coin, goal + 1 ):

        # we can calculate the # of combination by subtracting each coins value
        # from the current goal range(1-200) and adding the value for the 
        # # of combinations previously stored at that index to the current val
        # I.E When attempting to for combinations for a target of 5p
        
        # goal - coin = index
        # 5 - 1 = 4
        # 5 - 2 = 3
        # 5 - 5 = 0

        # in this case the values at those indexes are 1 2 and 1 respectively, 
        # this tells us there are 4 combinations

        solutions[i] = solutions[i] + solutions[i - coin]


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "No of distinct terms: %s" % solutions[goal]
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'