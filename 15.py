from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 15

#print the problem
print_problem(questionno)


#
# Solution
#

def genGridList(n, m):
    return [[0 for k in xrange(n)] for j in xrange(m)]


gridsize = 21

# generate multi-dimentional list structure of grid
grid = genGridList(gridsize,gridsize)

# fill first row with 1's
for i in range(0, gridsize):
    grid[0][i] = 1


for i in range(1, gridsize):

    # fill first col with 1's
    grid[i][0] = 1
    
    # second col increments by one each row
    grid[i][1] = i + 1;
    
    for j in range(2, gridsize):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % grid[-1][-1]
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'