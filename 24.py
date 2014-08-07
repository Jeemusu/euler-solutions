from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 24

#print the problem
print_problem(questionno)


#
# Solution
#

# get all lexicographic permutations of a string of numbers
def permutations(string):
    results = []
    
    if len(string) <=1:
        return string
    else:
        for i in permutations(string[1:]):
            for j in range(len(string)):
                results.append(i[:j] + string[0:1] + i[j:]) 

	return sorted(results)
	
lexicographic_perms = permutations('0123456789')


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % lexicographic_perms[999999]
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'