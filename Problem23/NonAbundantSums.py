# Create a list of all abundant numbers

abundant = {}
rangeStart = 0;
def setAbundant(val):
	valSum = 0;
	for ind in range(1,val+1):
		if(val % ind == 0 and ind != val):
			valSum += ind
	if( valSum > val):
		abundant.update({str(val): valSum})

def hasAbundant(val):
	for ind in len(abundant):
		if((ind+1) != len(abundant)):
			dict1 = abundant.keys.ElementAt(ind):
			dict2 = abundant.keys.ElementAt(ind+1):
			

for num in range(1,28124):
	
	
