from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 36

#print the problem
print_problem(questionno)

#
# Solution
#

base_two_palindromes = []

for n in range(1,1000001):
    base_ten_n = intToBinary(n)
    
    if(base_ten_n[0] == "0"):
        continue
    
    if(is_palindrome(n) and is_palindrome(base_ten_n)):
        base_two_palindromes.append(n)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s" % sum(base_two_palindromes)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'