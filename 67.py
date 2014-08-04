from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 18

#print the problem
print_problem(questionno)


#
# Solution
#
with open ("resources/triangle.txt", "r") as myfile:
    data = "\n" + myfile.read()

data = data.split('\n')
dataDic = [map(int, x.split()) for x in data]

#triangles height
height = len(dataDic)

#start at the bottom
for row in range(height, 0, -1):
	
	for key,i in enumerate(dataDic[row-1]):
		
		if key == len(dataDic[row-1])-1:
			break
			
		if i > dataDic[row-1][key+1]:
			dataDic[row-2][key] += i
		else:
			dataDic[row-2][key] += int(dataDic[row-1][key+1])

	
print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print 'Maximum Total: %s' % dataDic[1][0]
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'