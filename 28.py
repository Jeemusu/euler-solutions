from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 28

#print the problem
print_problem(questionno)


#
# Solution
#


size = 1001
diagonal = 1;
diagonals = [1]

for i in range(2, size, 2):
    for j in range(4):
        diagonal = diagonal + i
        diagonals.append(diagonal);

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Sum: %s" % sum(diagonals)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'