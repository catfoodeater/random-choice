import random
import os

directory = "choices"
filePath = ""
printText = "options: "

def getFiles():
	if not os.path.exists(directory):
		os.mkdir(directory)

	return os.listdir(directory)

def getFileData():
	if os.path.exists(filePath):	
		with open(filePath, "r") as f:
			return f.read().splitlines(True)
			# return f.read().split(",")
	else:
		print(f"Failed to get file data '{filePath}'")

def printRandomItem(options):
	item = random.choice(options)

	print(item)

def promptFilePath():
	global filePath

	filePath = directory + "/" + input("> ")

	if not os.path.exists(filePath):
		promptFilePath()

for fileName in getFiles():
	printText += fileName + " "

print(printText)

promptFilePath()

printRandomItem(getFileData())

input("Press enter to exit")
