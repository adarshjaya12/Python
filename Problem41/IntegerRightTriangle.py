

def isPrime(x):
	if x <1:
		return False
	if x == 1 or x ==2  or x == 3:
		return True
	if x%2 == 0 or x%3 == 0:
		return False
	i = 5
	
	while i*i <= x:
		if( x % i == 0 or x % (i+2) == 0):
			return False
		i+=6
	return True

def isUnique(val):
	print("Unique {0}".format(val))
	for ind in range(0,len(val)):
		if val[ind+1::].find(val[ind]) == -1:
			continue
		else:
			return False
	return True
	
def pandigitalPrime(val):
	if isPrime(val):
		digL= list(str(val))
		digitList = map(lambda x: int(x),digL)
		for dig in digitList:
			if(not isPrime(dig)):
				return False
		return isUnique(str(val))


numberList = range(900000000,1000000000)
numberList.reverse()
for val in numberList:
	if pandigitalPrime(val):
		print("The largest pandigital prime is {0}".format(val))

	
	
	
	