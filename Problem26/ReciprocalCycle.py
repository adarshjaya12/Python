def findPattern(s):
	filterCopy =s.split('.')[1]
	Incrementer = 0;
	i = (filterCopy+filterCopy).find(filterCopy,1,-1)
	if i == -1:
		return Incrementer;
	else:
		Incrementer = len(filterCopy[:i])
		return Incrementer
	

def fractionOfVal(x):
	fraction = (1/float(x))
	decimalValue = fraction - int(fraction)
	#print("The fraction is {0} and the decimalValue is {1}".format(fraction,decimalValue))
	return str(decimalValue)

denominator= 0;
fractionCount = 0;
for val in range(2,1001):
	result = findPattern(fractionOfVal(val))
	if(result > fractionCount):
		denominator = val
		fractionCount = result

print("The value is {0} and the count is {1}".format(denominator,fractionCount))
		