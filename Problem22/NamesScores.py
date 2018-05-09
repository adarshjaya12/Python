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

f = open("names.txt","r")
fileRead = '';
for file in f:
	fileRead = file
NameList = fileRead.split(",")
SortedList = sorted(NameList,key=str.lower)

def CalculateWord(word):
	SplitWord = list(word)
	FilteredWord = filter(lambda x: x !='"',SplitWord)
	TotalSum = 0
	for alpa in FilteredWord:
		TotalSum+= AlphaDict[alpa.upper()]
	return TotalSum
Result = 0;
for index, word in enumerate(SortedList):
	Result += ((index+1) * CalculateWord(word))

print("The total is {0}".format(Result))



