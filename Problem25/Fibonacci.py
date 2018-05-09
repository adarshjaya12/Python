initial = 0
second = 1
flag = True;
termIncrementer = 0;
while flag:
	initial,second = second,initial+second;
	termIncrementer+=1;
	if(len(str(second)) == 4):
		print("The index is {0}".format(termIncrementer))
		break