# Following Primality Test algorithm to check if a number is prime or not

rangeList = range(1,2000000)

def is_prime(n):
	if (val <= 3):
		return True;
	elif (val % 2 == 0 | val % 3 == 0):
		return False
	i = 5;
	while(i*i < val):
		if( val % i == 0 | val % (i +2) == 0):
			return False
		i = i+ 6;
		return True;
sum = 0
for val in rangeList:
	if(is_prime(val)):
		sum+= val;
		
print(sum)

			

		