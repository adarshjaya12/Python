def isDecimalPalindrome(val):
	value1 = str(val)
	value2 = str(val)[::-1]
	if value1 == value2:
		return True
	
def isBinaryPalindrome(val):
	binaryValue1 = "{0:b}".format(val)
	binaryValue2 = "{0:b}".format(val)[::-1]
	return binaryValue1 == binaryValue2

palindromeSum = 0	
for val in range(1,1000000):
	if isDecimalPalindrome(val) and isBinaryPalindrome(val):
		palindromeSum+=val
		
print("The total sum of all numbers is {0} ".format(palindromeSum))