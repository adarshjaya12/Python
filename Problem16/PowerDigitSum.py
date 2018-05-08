from math import pow

valueList = list(str(pow(2,1000)))
valueList = map(lambda x: int(x),valueList)
totalSum = sum(valueList)

print("the sum is {0}".format(totalSum))