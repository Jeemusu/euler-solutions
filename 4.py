from euler import *
import time
import math

#start timer
start = time.time()

#question number
questionno = 4

#print the problem
print_problem(questionno)


#
# Solution
#

def is_palindrome(n):
    n = str(n)
    if(n == n[::-1]):
        return True

palindromes = []
max_palindrome = 0

for i in range (100, 999):
    for j in range (100, 999):
        
        k = i*j

        if(is_palindrome(k) and k > max_palindrome):
                palindromes.append(k)
                max_palindrome = k
  
print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Largest palindrome: %s " % max_palindrome
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'