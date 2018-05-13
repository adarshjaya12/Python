#We can ignore the n 
import math

def isPrime(n):
	if n < 1:
		return False
	if n == 2 or n == 3 or n == 1:
		return True
	if n%2 == 0 or  n%3 == 0:
		return False
	i = 5
	while i * 5 <= val:
		if val % i ==0 or val % (i+2) == 0:
			return False
		i+=6
	return True

def closestPrime(val):
	maxValue = int(math.sqrt(val))
	possiblePrime = range(1,val)
	possiblePrime.reverse()
	possibePrimeList = []
	for val in possiblePrime:
		if isPrime(val):
			possibePrimeList.append(val)
		if len(possibePrimeList) == 4:
			return possibePrimeList
	return possibePrimeList
	
def isChristianGoldbach(val):
	print("The given value is {0}".format(val))
	primeList = closestPrime(val)
	print("Prime list is {0}".format(primeList))
	if len(primeList) == 0:
		return False
	for val in primeList:
		for int in range(1,3):
			result = val + 2*(int*int)
			print(result)
			if result == val:
				print("True")
				return True
			if result > val:
				break
	return False
	
for val in range(4,1000):
	compValue = (2*val +1)
	if isChristianGoldbach(compValue):
		continue
	else:
		print("The smallest number is {0}".format(compValue))
		break
		
