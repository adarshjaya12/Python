#For right angle triangle with perimeter
#Lesser than 1000, The longest side cannot be 
#less than 334

import math
#a square + b square = c square

def getPerimeter(a,b):
	cal = a + b + math.sqrt(a*a+b*b)
	if (cal).is_integer():
		return cal
	return 0

def rightAngled(p):
	maxSolution = 0
	possibleValue = (p/3)+1
	for a in range (1,possibleValue):
		for b in range(1,possibleValue):
			if p == getPerimeter(a,b):
				maxSolution+=1
	return maxSolution

resultPerimeter = 0
maxSolution = 0
for p in range(10,1001):
	result = rightAngled(p)
	if result > maxSolution:
		maxSolution = result
		resultPerimeter = p
		
		
		
print("The maximum solution is {0} and the count is {1}".format(resultPerimeter,maxSolution))