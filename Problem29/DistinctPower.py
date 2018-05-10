from math import pow

result = [];
for a in range(2,101):
	for b in range(2,101):
		pwr = pow(a,b)
		if(not pwr in result):
			result.append(pwr)

print("Distinct count is {0}".format(len(result)))