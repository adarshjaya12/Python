def DisplayMul(val):
	total = 0;
	for num in range(1,val):
		if(num%3 ==0 & num%5 ==0):
			total+=num;
		elif(num%3 == 0):
			total+=num;
		elif(num%5 == 0):
			total+=num;
	
	print total;
	

DisplayMul(1000);