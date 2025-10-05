import random
import os

fileName = "items.txt"
items = []

def getFileData():
	global items

	if os.path.exists(fileName):
		with open(fileName, "r") as f:
			items = f.read().split(",")
	else:	
		with open(fileName, "w") as f:
			f.write("example 1,example 2")

def getRandomItem():
	item = random.choice(items)

	print(item)

getRandomItem()

input()
