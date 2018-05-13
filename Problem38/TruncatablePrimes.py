def isPrime(val):
	if val <= 1:
		return False
	elif val == 2:
		return True
	elif val == 3:
		return True
	elif val % 2 == 0 or val% 3 == 0:
		return False
	i = 5
	while i * i <=  val:
		if val % i ==0 or val % (i+2) == 0:
			return False
		i = i+6
	return True
	
def isTruncatablePrime(val):
	valAsString = str(val)
	reverseString = str(val)[::-1]
	
	length = len(valAsString)
	for index in (0,length):
		leftToRight = valAsString[index:length]
		
		if(not isPrime(int(leftToRight))):
			return False
		rightToLeft = reverseString[index:length]
		if(not isPrime(int(rightToLeft))):
			print("{0}".format(rightToLeft))
			return False
		
	return True
sum = 0
value = 0
incrementer =0
while True:
	value+= 3797
	if(isTruncatablePrime(value)):
		sum+= value
		incrementer+= 1
	if(value == 3797):
		break
	if(incrementer == 13):
		break
		
print("The sum is {0}".format(sum))
	
