from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 17

#print the problem
print_problem(questionno)


#
# Solution
#

# Unique values
numDict = {
    0:'',
    1:'one', 
    2:'two', 
    3:'three', 
    4:'four', 
    5:'five', 
    6:'six', 
    7:'seven', 
    8:'eight', 
    9:'nine', 
    10:'ten', 
    11:'eleven', 
    12:'twelve', 
    13:'thirteen', 
    14:'fourteen', 
    15:'fifteen', 
    16:'sixteen', 
    17:'seventeen', 
    18:'eighteen', 
    19:'nineteen', 
    20:'twenty', 
    30:'thirty', 
    40:'forty', 
    50:'fifty', 
    60:'sixty', 
    70:'seventy', 
    80:'eighty', 
    90:'ninety', 
    1000:'onethousand'
}

total_len = 0

# Build dictionary for unaccounted numbers
for i in range(1, 1001):

	if not i in numDict.keys():

		if i < 100:
			numDict[i] = numDict[(i/10)*10] + numDict[i%10]
		else:
			numDict[i] = numDict[i/100]+"hundred"
			if(i%100):
				numDict[i] += "and" + numDict[i%100]			

for i in numDict.values():
	total_len += len(i)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Total: %s" % total_len
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'