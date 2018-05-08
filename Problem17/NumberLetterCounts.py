numberMapping={
	'1' : 'One',
	'2' : 'Two',
	'3' : 'Three',
	'4' : 'Four',
	'5' : 'Five',
	'6' : 'Six',
	'7' : 'Seven',
	'8' : 'Eight',
	'9' : 'Nine',
	'10' : 'Ten',
	'11' : 'Eleven',
	'12' : 'Tweleve',
	'13' : 'Thirteen',
	'14' : 'Fourteen',
	'15' : 'Fifteen',
	'20' : 'Twenty',
	'30' : 'Thirty',
	'40' : 'Fourty',
	'50' : 'Fifty',
	'60' : 'Sixty',
	'70' : 'Seventy',
	'80' : 'Eighty',
	'90' : 'Ninty',
	'100' : 'Hundred',
	'1000' : 'Thousand'
}

def TwodigitToWord(val):
	if val <= 15 and val >=1:
		return numberMapping[str(val)];
	
	elif val% 10 == 0 and val <= 100:
		return numberMapping[str(val)];
		
	elif val <= 19 and  val >=16:
		secondDigit = val%10
		return numberMapping[str(secondDigit)]+'teen'
	else:
		secondDigit = val%10
		return numberMapping[str(val-secondDigit)]+' ' + numberMapping[str(secondDigit)]
	

def ThreeDigitToWord(value):
	firstDigit = value/100
	returnWord = numberMapping[str(firstDigit)]+' '+ numberMapping['100']
	if value % 100 == 0:
		return returnWord
	
	tensDigit = value%100
	return returnWord +' '+ TwodigitToWord(tensDigit)

NumberLetterString = ""
for value in range(1,1001):
	if value < 100:
		NumberLetterString+=(TwodigitToWord(value)+' ')
	elif value>=100 and value < 1000 :
		NumberLetterString+=(ThreeDigitToWord(value)+' ')
	elif value == 1000:
		NumberLetterString+=numberMapping[str(value)]
		
count = len(NumberLetterString) - NumberLetterString.count(' ')
print("{0} letters from one to thousand".format(count))