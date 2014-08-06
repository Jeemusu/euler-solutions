from euler import *
import time
import math


#start timer
start = time.time()

#question number
questionno = 22

#print the problem
print_problem(questionno)


#
# Solution
#

def getAlphaValue(n):
	value = 0
	for i in n:
		value += alphabet[i]
	return value

def getScore(n,p):
	return n * p
	
	
alphabet = {'A':1,'B':2, 'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
total = 0
names = sorted([n.rstrip().replace('"','') for n in open("resources/names.txt").read().split(',')])
	
for pos,name in enumerate(names):
	score = getScore(getAlphaValue(name), pos+1)
	total+=score

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s " % total
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'