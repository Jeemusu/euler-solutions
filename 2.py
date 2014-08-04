from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 2

#print the problem
print_problem(questionno)


#
# Solution
#

sequence = get_fibonacci_lt_n(4000000)
even_list = []

for i in sequence:
    if(is_even(i)):
        even_list.append(i)


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Sum: %s " % sum(even_list)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'