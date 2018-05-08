# Values cannot be more than 500 as the total will be beyond 1000
rangeList = range(1,500)
rangeList.reverse()

flag = True;

for c in rangeList:
	for b in rangeList:
		for a in rangeList:
			if((a*a)+(b*b)== (c*c)):
				total = a + b + c;
				if(a+b+c == 1000):
					productSum = a*b*c;
					print(productSum);
					flag = False;
					break;
		if(not flag):
			break;
	if(not flag):
		break;

		