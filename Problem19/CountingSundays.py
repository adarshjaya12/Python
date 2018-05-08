
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

digitList = list(str(factorial(100)))
digitList = map(lambda x: int(x) , digitList)
print("The sum of digit is {0}".format(sum(digitList)))