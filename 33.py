from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 33

#print the problem
print_problem(questionno)

#
# Solution
#

def is_non_trivial(x,y):
    if(x[0] == y[0] or x[-1] == y[-1]):
        return False
    return True

def get_common(x,y):
    for i in x:
        if(i in y):
            return i

results = []
for numerator in range(10,100):
    for denominator in range(numerator + 1,100):

        # skip potential trivial fractions
        if(numerator % 10 == 0 or denominator % 10 == 0):
            continue

        # convert to lists
        numerator_l = map(int, str(numerator))
        denominator_l = map(int, str(denominator))

        common_digit = get_common(numerator_l, denominator_l)

        if( is_non_trivial(numerator_l, denominator_l) and common_digit ):

            val = numerator / float(denominator)

            numerator_l.remove(common_digit)
            denominator_l.remove(common_digit)
            
            simplified_val = numerator_l[0] / float(denominator_l[0])

            if(simplified_val == val):
                
                results.append( numerator/float(denominator) )

prod = 1
for i in results:
    prod *= i

answer = "%s / 100" % (prod * 100)



print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s" % answer
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'