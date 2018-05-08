
longestChain = 0;
rangeList = range(1,1000001)
rangeList.reverse()
for var in rangeList:
	chain = 0
	sequenceValue =var
	while(sequenceValue != 1):
		if(sequenceValue % 2 == 0):
			sequenceValue = sequenceValue/2
			chain+=1
		else:
			sequenceValue = (3* sequenceValue)+1
			chain+=1
	if(longestChain < chain):
		longestChain =  chain

print("The longest chain is {0}".format(longestChain))
		
	
