from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 19

#print the problem
print_problem(questionno)


#
# Solution
#

dow = ['m','t','w','th','f','s','su']
i = 0
sundays = 0

#loop years
for year in range(1901, 2001):

	#loop months
	for month in range(1,13):
		if month == 2:
			if not year%4:
				max_days = 29
			else:
				max_days = 28		
		elif month in (4,6,9,11):
			max_days = 30
		else:
			max_days = 31
		
		#loop through days
		for day in range(1,max_days+1):
			
			i+=1 
			if i>6:
				i = 0
			
			if day == 1 and dow[i] == 'su':
				sundays += 1
				print "%s / %s / %s" % (year, month, day)
			print "%s / %s / %s (%s)" % (year, month, day, dow[i])


print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Total: %s " % (sundays)
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'