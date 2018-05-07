import sys
import math
def PrimeFactors(value):
	defRange = [sys.maxsize]
	defRange.extend(xrange(1,int(math.sqrt(value))+2))
	result = []
	for num in defRange:
		if(value%num == 0):
			while(value%num == 0):
				value /= num;
				result.append(num);
	
	if(result.len > 0):
		for r in result:
			print r;
			
PrimeFactors(600851475143);
	