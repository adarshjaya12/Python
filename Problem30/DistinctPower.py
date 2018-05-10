#Yet to fix bugs
from math import pow

def SumOf5thPower(val):
	updatedValue = val
	while True:
		powerIncrement = 1;
		while updatedValue >=0:
			result = pow(powerIncrement,5)
			updatedValue -= result
			powerIncrement+=1
		if updatedValue == 0:
			return True
		return False

NumberList = []
for i in range(1,1000000):
	if(SumOf5thPower(i)):
		NumberList.append(i)

print("The sum is {0}".format(sum(NumberList)))
	