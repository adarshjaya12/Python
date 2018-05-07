def SmallestMultiple():
	incrementValue = 2520;
	flag = True;
	while True:
		rangeList = range(1,20);
		rangeList.reverse();
		for item in rangeList:
			if(incrementValue%item != 0):
				incrementValue+=20;
				flag = False;
				break;
		if(flag):
			print(incrementValue);
			break;

SmallestMultiple();
		
		