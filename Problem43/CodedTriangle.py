# Copying some logic from Problem 22
import math
AlphaDict={
	"A" : 1,
	"B" : 2,
	"C" : 3,
	"D" : 4,
	"E" : 5,
	"F" : 6,
	"G" : 7,
	"H" : 8,
	"I" : 9,
	"J" : 10,
	"K" : 11,
	"L" : 12,
	"M" : 13,
	"N" : 14,
	"O" : 15,
	"P" : 16,
	"Q" : 17,
	"R" : 18,
	"S" : 19,
	"T" : 20,
	"U" : 21,
	"V" : 22,
	"W" : 23,
	"X" : 24,
	"Y"	: 25,
	"Z"	: 26
}

def getTriangleNumber(n):
	return n*(n+1)/2

def findTriange(val):
	maxVal = int(math.sqrt(val))+1
	
	for num in range(1,maxVal):
		triNumber = getTriangleNumber(num)
		#print("Tri Number are {0} and val is{1}".format(triNumber,val))
		if triNumber == val:
			return True
		elif triNumber > val:
			return False
	return False
	
def isTriangeWord(word):
	charList = list(word.upper())
	#print("The char are {0}".format(charList))
	wordCount = 0
	for c in charList:
		wordCount+=AlphaDict[c]
		#print("Count for word {0} are {1}".format(word,wordCount))
	return findTriange(wordCount)

f = open("words.txt","r")
fileRead = '';
for file in f:
	fileRead = file
NameList = fileRead.split("\"")
NameList = filter(lambda x: x !=",",NameList)
TestList = NameList[0:3]
triangleCountWord = 0
for word in TestList:
	if isTriangeWord(word):
		triangleCountWord+=1

print("Total count is {0}".format(triangleCountWord))
	
