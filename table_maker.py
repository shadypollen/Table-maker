masterList = []
miniList = []

def findLongestWord(inputList):
	maxLength = 0
	for row in inputList:
		for word in row:
			if len(word) > maxLength:
				maxLength = len(word)
	if maxLength % 2 == 0:
		return maxLength	
	else:
		return (maxLength+1)

def findLongestRow(inputList):
	maxLength = 0
	for row in inputList:
		if len(row) > maxLength:
			maxLength = len(row)
	return maxLength

def makeTable(inputList):
	rowList = []
	maxLength = findLongestWord(inputList)	
	maxRow = findLongestRow(inputList)
	print("Max length:", maxLength, "max row:", maxRow)
	for row in inputList: 
		if not inputList.index(row):
			print((("+" + "-"*maxLength) * maxRow) + "+")
		for word in row:
			rowList.append("|" + word.center(maxLength, " "))
		rowIndex = len(rowList)
		if rowIndex < maxRow:
			rowList.append("|" + ((" " * maxLength) + "|")*(maxRow - rowIndex))
		else:
			rowList.append("|")
		print("".join(rowList))
		print((("+" + "-"*maxLength) * maxRow) + "+")
		rowList = []
		
		
print("Input your word. Input !row for new row and !end to \
stop data input \n")

while True:
	inputWord = input("> ")
	if(inputWord == "!end"):
		if len(miniList):
			masterList.append(miniList)
		makeTable(masterList)
		break
	elif(inputWord == "!row"):
		masterList.append(miniList)
		miniList = []
	else:
		miniList.append(inputWord)	
