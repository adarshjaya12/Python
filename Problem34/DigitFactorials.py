def factorial(x):
	if x <= 1:
		return 1
	return  x *  factorial( x-1)

def findFactorialEqual(x):
	checkValue = x;
	indNumber = map(lambda x: int(x) , list(str(x)))
	factorialSum = 0
	for val in indNumber:
		factorialSum += factorial(val)
	if checkValue == factorialSum:
		return checkValue
	return 0
result = 0		
for val in range(2,200000):
	result += findFactorialEqual(val)
	
print("The Total sum is {0}".format(result))