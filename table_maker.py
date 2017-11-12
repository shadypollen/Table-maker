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
	wordList = []
	maxLength = findLongestWord(inputList)	
	maxRow = findLongestRow(inputList)
	print("Max length:", maxLength, "max row:", maxRow)
	for row in inputList:	
		for word in row:
			wordPadding = int((maxLength - len(word))/2)
			startBorder = "+" + ("-"*maxLength) + "+"
			endBorder = ("-"*(maxLength+2))
			evenStartWord = ("|" + (" "*wordPadding) + word + (" "*wordPadding) + "|") 
			oddStartWord = ("|" + (" "*wordPadding) + word + (" "*(wordPadding+1)) + "|")
			evenEndWord = (" " + (" "*wordPadding) + word + (" "*wordPadding) + "|") 
			oddEndWord = (" " + (" "*wordPadding) + word + (" "*(wordPadding+1)) + "|") 
			borderString = (startBorder + (endBorder)*len(row))
			if len(word) % 2 == 0 and row.index(word) == 0:
				wordList.append(evenStartWord)
			elif row.index(word) == 0:
				wordList.append(oddStartWord)
			elif len(word) % 2 == 0 and row.index(word) != 0:
				wordList.append(oddEndWord)
			else:
				wordList.append(evenEndWord)
		if inputList.index(row) == 0:
			print("+" + (("-"*maxLength) + "+")*maxRow)
		if len(row) < maxRow:
			print("".join(wordList) + (" "*maxLength) + "|")	
		else:
			print("".join(wordList))
		print("+" + (("-"*maxLength) + "+")*maxRow)
		wordList = []
 
		
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
