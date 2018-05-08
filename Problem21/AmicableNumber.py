
def divisor(val):
	divisorTotal = 0
	for ran in range(1,val):
		if val%ran ==0:
			divisorTotal+=ran
			
	return divisorTotal

amicableTotal = 0
for val1 in range(1,10001):
	for val2 in range(1,10001):
		divisor1Val = divisor(val1)
		divisor2Val = divisor(val2)
		if divisor2Val == val1 and divisor1Val == val2:
			amicableTotal+= (divisor1Val + divisor2Val)

print("The sum of all the amicable number under 10000 is {0}".format(amicableTotal))