def fibonacci():
	counter = 0;
	a,b = 0, 1;
	while True:
		if b % 2 == 0:
			counter += 1;
			print b;
		elif counter == 10:
			break;
		a,b = b, a+b;
		
fibonacci()