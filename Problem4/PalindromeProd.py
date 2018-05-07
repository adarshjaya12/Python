def DisplayLargestPali():
	print("Starting");
	numberList = range(100,1000);
	numberList.reverse();
	for first in numberList:
		for second in  numberList:
			result = int(first) * int(second);
			check1 = str(result)[:3];
			check2 = str(result)[3:];
			if(check1 == check2):
				print("The highest Palindrome Prod are",first,second);
				return;
	

DisplayLargestPali();
		
		