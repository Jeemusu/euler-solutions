from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 13

#print the problem
print_problem(questionno)


#
# Solution
#

with open ("resources/13.txt", "r") as myfile:
    data=myfile.read()

split_list = map(long, data.split('\n'))

answer = str(sum(split_list))[0:10] 

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % answer
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'