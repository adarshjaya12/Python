def SumOfSquare():
	result = 0;
	for val in range(1,100):
		result+= (val*val);
	
	return result;

def SquareOfSum():
	result =0;
	for val in range(1,100):
		result+= val;
	return result* result;

difference = SquareOfSum() - SumOfSquare() ;
print(difference)
		
		