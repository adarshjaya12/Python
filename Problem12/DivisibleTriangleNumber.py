# Following Primality Test algorithm to check if a number is prime or not


def sumTillNth(n):
	res = sum(range(1,n))
	return res;

IncrementNumber = 2
flag = True

while flag:
	incrementCount = 0;	
	sumValue = sumTillNth(IncrementNumber);
	for val in range(1,IncrementNumber):
		if(sumValue% val == 0):
			incrementCount+= 1
	IncrementNumber+= 1
	print("The increment Number is {0} and the count is {1}".format(IncrementNumber,incrementCount))
	if(incrementCount == 500):
		print("The increment Number is {0} and the sum is {1}".format(IncrementNumber,sumValue))
		break

			

		